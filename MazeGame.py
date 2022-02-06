from Maze import *
from Robot import *

from tkinter import *
import queue


level = 1
width = 10
height = 10



def poseDecor(maze:Maze,good_moves:list):
    tab = maze.get_maze()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == CellState.WALL:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="red")
            if (i,j) in good_moves:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="blue")
            elif tab[i][j] == CellState.EXIT:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="orange")
            

    
                
def avance(direction,maze,fenetre,good_moves:list):
    grille.delete(ALL)
    poseDecor(maze,good_moves)
    pers.avancer(direction,maze.get_maze(),fenetre)
    pers.dessiner(direction,grille)


def touche(event):
    key = event.keysym
    if key == 'Right' or key == 'd':
        direction = "E"
        avance(direction,maze,fenetre,good_moves)
    elif key == 'Left' or key == 'q': 
        direction = "W"
        avance(direction,maze,fenetre,good_moves)
    elif key == 'Up' or key == 'z': 
        direction = "N"
        avance(direction,maze,fenetre,good_moves)
    elif key == 'Down' or key == 's': 
        direction = "S"
        avance(direction,maze,fenetre,good_moves)

def get_oppisite(direction):
    if direction == "N":
        return "S"
    elif direction == "S":
        return "N"
    elif direction == "E":
        return "W"
    elif direction == "W":
        return "E"


def generate_coord_by_input(maze:Maze,input:list):
    start = maze.get_starting_point()
    coord = [start]
    for move in input:
        if move == "q":
            coord.append((coord[-1][0],coord[-1][1]-1))
        if move == "d":
            coord.append((coord[-1][0],coord[-1][1]+1))
        if move == "s":
            coord.append((coord[-1][0]+1,coord[-1][1]))
        if move == "z":
            coord.append((coord[-1][0]-1,coord[-1][1]))
    return coord


def valid(maze:Maze,moves:list):
    maze_ = maze.get_maze()
    col,row = maze.get_starting_point()
    for move in moves:
        if move == "q": row -= 1
        elif move == "d": row += 1
        elif move == "s": col += 1
        elif move == "z": col -= 1
        
        if not(0 <= row < len(maze_[0]) and 0 <= col < len(maze_)):
            return False
        elif maze_[col][row] == CellState.WALL:
            return False
    return True



def find_end(maze:Maze,moves:str):
    maze_ = maze.get_maze()
    col,row = maze.get_starting_point()
    for move in moves:
        if move == "q": row -= 1
        elif move == "d": row += 1
        elif move == "s": col += 1
        elif move == "z": col -= 1 
    if maze_[col][row] == CellState.EXIT:
        return True
    return False

def path_finding(maze:Maze):
    nums = queue.Queue()
    nums.put("")
    add = ""

    while not find_end(maze,add):
        add = nums.get()
        for move in ["q", "d", "s", "z"]:
            put = add + move
            if valid(maze,put):
                nums.put(put)
    return generate_coord_by_input(maze,add)



""" Programme principal"""
if __name__ == '__main__':
    global maze,good_moves
    # while True:
    fenetre=Tk()
    fenetre.title(f'Labyrinthe Level {level}')
    maze = Maze(width,height,level)
    maze.generate_maze()
    maze.afficher_maze()
    grille=Canvas(fenetre,width=len(maze.get_maze()[0]*25),height=len(maze.get_maze())*25)
    grille.pack()
    good_moves = list(path_finding(maze))
    poseDecor(maze,good_moves) # on construit le labyrinthe
    pers=Robot(maze.get_starting_point()[1],maze.get_starting_point()[0],"E",grille,maze.get_maze(),fenetre) # on construit le robot
    pers.dessiner("E",grille)
    fenetre.bind_all('<Key>',touche)
    fenetre.mainloop()
        # level += 1
        # width += 1
        # height += 1

    








