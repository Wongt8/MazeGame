from Maze import *
from Robot import *

from tkinter import *
import math


global maze

level = 1
width = 20
height = 30


################################################################################################

def poseDecor(maze:Maze):
    tab = maze.get_maze()
    start = maze.get_starting_point()
    exit = maze.get_exit_point()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == CellState.WALL:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="red")
            # FOR THE PATH FINDIND
            # if tab[i][j] == CellState.EMPTY:
            #     pts = distance(exit,(i,j)) - distance(start,(i,j))
            #     grille.create_text(j*25+12,i*25+12,text=pts,fill="blue")
            elif tab[i][j] == CellState.EXIT:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="orange")
                
def avance(direction,maze,fenetre):
    grille.delete(ALL)
    poseDecor(maze)
    pers.avancer(direction,maze.get_maze(),fenetre)
    pers.dessiner(direction,grille)


def touche(event):
    t=event.keysym
    if t == 'Right' or t == 'd':
        direction = "E"
        avance(direction,maze,fenetre)
    elif t == 'Left' or t == 'q': 
        direction = "W"
        avance(direction,maze,fenetre)
    elif t == 'Up' or t == 'z': 
        direction = "N"
        avance(direction,maze,fenetre)
    elif t == 'Down' or t == 's': 
        direction = "S"
        avance(direction,maze,fenetre)


def distance(p0, p1):
    # P0 = exit point
    return round(math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2),2)


def get_oppisite(direction):
    if direction == "N":
        return "S"
    elif direction == "S":
        return "N"
    elif direction == "E":
        return "W"
    elif direction == "W":
        return "E"


def create_value(maze):
    maze_ = maze.get_maze()
    value = [distance(maze.get_exit_point(),(i,j)) - distance(maze.get_starting_point(),(i,j)) if maze_[i][j] == CellState.EMPTY else None for i in range(len(maze_)) for j in range(len(maze_[i]))]
    return value

def pathfinding(maze:Maze, value:list):
    #TODO
    pass






""" Programme principal"""

# while True:
fenetre=Tk()
fenetre.title(f'Labyrinthe Level {level}')
maze = Maze(width,height,level)
maze.generate_maze()
maze.afficher_maze()
grille=Canvas(fenetre,width=len(maze.get_maze()[0]*25),height=len(maze.get_maze())*25)
grille.pack()
poseDecor(maze) # on construit le labyrinthe
# pathfinding(maze)

pers=Robot(maze.get_starting_point()[1],maze.get_starting_point()[0],"E",grille,maze.get_maze(),fenetre) # on construit le robot
pers.dessiner("E",grille)
fenetre.bind_all('<Key>',touche)
fenetre.mainloop()
    # level += 1
    # width += 1
    # height += 1

    








