from Maze import *
from Robot import *
from breadth_first import *
from maze_gui import *

from tkinter import *


if __name__ == '__main__':

    width, height, level = 3, 3, 1

    while True:

        fenetre = Tk()
        fenetre.title(f'Labyrinthe Level {level}')
        maze = Maze(width, height, level)

        maze.generate_maze()
        maze.display_maze()

        grille = Canvas(fenetre,width=len(maze.get_maze()[0]*25), height=len(maze.get_maze())*25)
        grille.pack()

        breadth_first = Breadth_First(maze) 
        good_moves = list(breadth_first.path_finding())

        build_maze(grille, maze, good_moves)
        robot = Robot(maze.get_starting_point()[1],maze.get_starting_point()[0],"E",grille,maze.get_maze(),fenetre) # on construit le robot
        robot.dessiner("E",grille)

        fenetre.bind("<Key>", lambda event: on_key(event,robot,grille,maze,fenetre,good_moves))
        fenetre.mainloop()        
        fenetre.destroy()

        level += 1
        width += 1
        height += 1

    








