from Maze import *
import queue

class Breadth_First():
    def __init__(self,maze:Maze) :
        self.maze = maze

    
    def generate_coord_by_input(self, input:list):
        start = self.maze.get_starting_point()
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

    def valid(self, moves:list):
        maze_ = self.maze.get_maze()
        col,row = self.maze.get_starting_point()
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

    def find_end(self, moves:str):
        maze_ = self.maze.get_maze()
        col,row = self.maze.get_starting_point()
        for move in moves:
            if move == "q": row -= 1
            elif move == "d": row += 1
            elif move == "s": col += 1
            elif move == "z": col -= 1 
        if maze_[col][row] == CellState.EXIT:
            return True
        return False

    def path_finding(self):
        nums = queue.Queue()
        nums.put("")
        add = ""

        while not self.find_end(add):
            add = nums.get()
            for move in ["q", "d", "s", "z"]:
                put = add + move
                if self.valid(put):
                    nums.put(put)
        return self.generate_coord_by_input(add)