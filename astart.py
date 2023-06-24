from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class AStar:
    def __init__(self, grid):
        self.grid = Grid(matrix=grid)

    def findPath(self, start, end):
        start_p = self.grid.node(start[1], start[0])
        end_p = self.grid.node(end[1], end[0] - 1)
        finder = AStarFinder()
        path, _ = finder.find_path(start_p, end_p, self.grid)

        for i, p in enumerate(path):
            path[i] = p[::-1]

        return path
