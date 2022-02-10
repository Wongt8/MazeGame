from Maze import *
from Robot import *
from BreadthFirst import *


from tkinter import *

"""
Define maze size and level
"""
width = 8
height = 8
level = 1


def poseDecor(maze:Maze,good_moves:list):
    tab = maze.get_maze()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == CellState.WALL:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="red")
            if (i,j) in good_moves:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="grey")
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
    breadth_first = Breadth_First(maze) 
    good_moves = list(breadth_first.path_finding())
    poseDecor(maze,good_moves) # on construit le labyrinthe
    pers=Robot(maze.get_starting_point()[1],maze.get_starting_point()[0],"E",grille,maze.get_maze(),fenetre) # on construit le robot
    pers.dessiner("E",grille)
    fenetre.bind_all('<Key>',touche)
    fenetre.mainloop()
        # level += 1
        # width += 1
        # height += 1

    








