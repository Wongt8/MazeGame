from Maze import *
from Robot import *

from tkinter import *

def build_maze(grille:Canvas, maze:Maze, good_moves:list):
    tab = maze.get_maze()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == CellState.WALL:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="red")
            if (i,j) in good_moves:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="grey")
            elif tab[i][j] == CellState.EXIT:
                grille.create_rectangle(j*25,i*25,(j+1)*25,(i+1)*25,fill="orange")

                
def forward_robot(robot:Robot, grille:Canvas, direction:str, maze:Maze, fenetre:Tk, good_moves:list):
    grille.delete(ALL)
    build_maze(grille, maze, good_moves)
    robot.avancer(direction,maze.get_maze(),fenetre)
    robot.dessiner(direction,grille)


def on_key(event,robot:Robot,grille:Canvas,maze:Maze,fenetre:Tk,good_moves:list):
    key = event.keysym
    if key == 'Right' or key == 'd': direction = "E"
    elif key == 'Left' or key == 'q': direction = "W"
    elif key == 'Up' or key == 'z':  direction = "N"
    elif key == 'Down' or key == 's': direction = "S"
    forward_robot(robot, grille, direction, maze, fenetre, good_moves)


def get_oppisite(direction):
    if direction == "N":
        return "S"
    elif direction == "S":
        return "N"
    elif direction == "E":
        return "W"
    elif direction == "W":
        return "E"
