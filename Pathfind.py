from Maze import *
import queue


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