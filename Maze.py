import random as r
from enum import Enum

class CellState(Enum):
    WALL = '#'
    EMPTY = ' '
    UNVISITED = 'u'
    EXIT = 'E'
    START = 'S'



class Maze:
    def __init__(self, height : int, width : int , level: int):
        self.height = height
        self.width = width
        self.level = level
        self.maze = []
        self.starting_height = int(r.random() * height) 
        self.starting_width = int(r.random() * width)


    def surroundingCells(self,rand_wall):
        s_cells = 0
        if (self.maze[rand_wall[0]-1][rand_wall[1]] == CellState.EMPTY):
            s_cells += 1
        if (self.maze[rand_wall[0]+1][rand_wall[1]] == CellState.EMPTY):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1]-1] == CellState.EMPTY):
            s_cells +=1
        if (self.maze[rand_wall[0]][rand_wall[1]+1] == CellState.EMPTY):
            s_cells += 1

        return s_cells



    def create_walls(self):
        for i in range(0, self.height):
            line = [CellState.UNVISITED for j in range(0, self.width)]
            self.maze.append(line)

        starting_height = int(r.random()*self.height)
        starting_width = int(r.random()*self.width)
        if (starting_height == 0): starting_height += 1
        if (starting_height == self.height-1): starting_height -= 1
        if (starting_width == 0): starting_width += 1
        if (starting_width == self.width-1): starting_width -= 1

        self.maze[starting_height][starting_width] = CellState.EMPTY

        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        self.maze[starting_height-1][starting_width] = CellState.WALL
        self.maze[starting_height][starting_width - 1] = CellState.WALL
        self.maze[starting_height][starting_width + 1] = CellState.WALL
        self.maze[starting_height + 1][starting_width] = CellState.WALL

        return walls

    def build_maze(self,walls):
        while (walls):

            rand_wall = walls[int(r.random()*len(walls))-1]


            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1]-1] == CellState.UNVISITED and self.maze[rand_wall[0]][rand_wall[1]+1] == CellState.EMPTY):

                    s_cells = self.surroundingCells(rand_wall)

                    if (s_cells < 2):

                        self.maze[rand_wall[0]][rand_wall[1]] = CellState.EMPTY

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])



                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])

                        if (rand_wall[1] != 0):	
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])
                    


                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0]-1][rand_wall[1]] == CellState.UNVISITED and self.maze[rand_wall[0]+1][rand_wall[1]] == CellState.EMPTY):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):

                        self.maze[rand_wall[0]][rand_wall[1]] = CellState.EMPTY

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])


                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])


                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])


                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue


            if (rand_wall[0] != self.height-1):
                if (self.maze[rand_wall[0]+1][rand_wall[1]] == CellState.UNVISITED and self.maze[rand_wall[0]-1][rand_wall[1]] == CellState.EMPTY):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):

                        self.maze[rand_wall[0]][rand_wall[1]] = CellState.EMPTY


                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])

                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])

                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])


                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)
                    continue

            if (rand_wall[1] != self.width-1):
                if (self.maze[rand_wall[0]][rand_wall[1]+1] == CellState.UNVISITED and self.maze[rand_wall[0]][rand_wall[1]-1] == CellState.EMPTY):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):

                        self.maze[rand_wall[0]][rand_wall[1]] = CellState.EMPTY


                        if (rand_wall[1] != self.width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != CellState.EMPTY):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = CellState.WALL
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])
                        if (rand_wall[0] != self.height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[0] != 0):	
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != CellState.EMPTY):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = CellState.WALL
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])


                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)
                    continue


            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == CellState.UNVISITED):
                    self.maze[i][j] = CellState.WALL


        for i in range(0, self.width):
            if (self.maze[1][i] == CellState.EMPTY):
                self.maze[0][i] = CellState.EMPTY
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == CellState.EMPTY):
                self.maze[self.height-1][i] = CellState.EMPTY
                break

    

    def add_ending_point_and_starting_point(self):
        index_of_start = self.maze[0].index(CellState.EMPTY)
        index_of_exit = self.maze[self.height-1].index(CellState.EMPTY)
        self.maze[0][index_of_start] = CellState.START
        self.maze[self.height-1][index_of_exit] = CellState.EXIT

    def generate_maze(self):
        self.build_maze(self.create_walls())
        self.add_ending_point_and_starting_point()
        
    
    def display_maze(self):
        print(f"Niveau {self.level}")
        for line in range(len(self.maze)):
            for i in range(len(self.maze[line])):
                print(self.maze[line][i].value, end=" ")
            print(" ")
    
    def get_maze(self):
        return self.maze

    def get_starting_point(self):
        return (0,self.maze[0].index(CellState.START))
    
    def get_exit_point(self):
        return (self.height,self.maze[self.height-1].index(CellState.EXIT))