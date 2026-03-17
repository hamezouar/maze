#!/usr/bin/env python3
import random
import sys
from typing import List, Tuple, Set, Optional


class Cell:
    """
    Represents a single cell in the maze,
    with walls and visit/path status.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a maze cell.
        Args:
        x (int): Column index of the cell.
        y (int): Row index of the cell.
        """
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"North": True, "East": True, "South": True, "West": True}
        self.path = False

    def remove_wall(self, direction: str) -> None:
        """
        Remove the wall in the specified direction
        for this cell.
        """
        self.walls[direction] = False


class Mazegenerator:
    """
    Generates a maze with optional
    perfect/non-perfect paths and animation.
    """

    def __init__(self,
                 width: int,
                 height: int,
                 entry: Tuple[int, int],
                 exit: Tuple[int, int],
                 seed: Optional[int] = None) -> None:
        """
        Initialize the maze generator.
        Args:
        width : Number of columns in the maze.
        height : Number of rows in the maze.
        entry : Coordinates (x, y) of the maze entry.
        exit : Coordinates (x, y) of the maze exit.
        seed : Optional random seed for reproducible mazes.
        """
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.animation: List[Tuple[Cell, Cell, str]] = []
        self.seed = seed

        if seed is not None:
            random.seed(seed)

    def configue_grid(self) -> List[List[Cell]]:
        """
        Create and return a grid of unvisited cells
        with all walls intact.
        """
        grid = []
        for a in range(self.height):
            row = []
            for b in range(self.width):
                new_cell = Cell(b, a)
                row.append(new_cell)
            grid.append(row)
        return grid

    def protect_42(self, grid: List[List[Cell]]) -> Set[Tuple[int, int]]:
        """
        Mark a fixed  area in the maze
        as visited and protect entry/exit.
        """
        mx, my = self.width // 2, self.height // 2
        point1 = [(my, mx - 6), (my - 1, mx - 6), (my - 2, mx - 6),
                  (my + 1, mx - 6), (my + 2, mx - 6), (my - 2, mx - 7),
                  (my - 2, mx - 8), (my - 1, mx - 8), (my + 2, mx - 5),
                  (my + 2, mx - 7)]
        point3 = [(my, mx - 1), (my - 1, mx - 1), (my - 2, mx - 1),
                  (my - 2, mx - 2), (my - 2, mx - 3), (my, mx - 2),
                  (my, mx - 3), (my + 1, mx - 1), (my + 2, mx - 1),
                  (my + 2, mx - 2), (my + 2, mx - 3)]
        point3_p1 = [(my, mx + 3), (my - 1, mx + 3), (my - 2, mx + 3),
                     (my - 2, mx + 2), (my - 2, mx + 1), (my, mx + 3),
                     (my, mx + 3), (my + 1, mx + +3), (my + 2, mx + 3),
                     (my, mx + 2), (my, mx + 1), (my + 2, mx + 2),
                     (my + 2, mx + 1)]
        point7 = [(my, mx + 7), (my - 1, mx + 7), (my - 2, mx + 7),
                  (my - 2, mx + 6), (my - 2, mx + 5), (my + 1, mx + 7),
                  (my + 2, mx + 7)]
        point42 = set(point1 + point3 + point3_p1 + point7)

        for y, x in point1:
            if 0 <= y < self.height and 0 <= x < self.width:
                grid[y][x].visited = True
        for y, x in point3:
            if 0 <= y < self.height and 0 <= x < self.width:
                grid[y][x].visited = True

        for y, x in point3_p1:
            if 0 <= y < self.height and 0 <= x < self.width:
                grid[y][x].visited = True

        for y, x in point7:
            if 0 <= y < self.height and 0 <= x < self.width:
                grid[y][x].visited = True

        try:
            ex, ey = self.entry
            ox, oy = self.exit
            if (ey, ex) in point42:
                raise ValueError(
                    f"🚨 Alert the Entry {ex,ey} in the sacred 42 coordinates\n"
                    "     ! Please choose another place.")
            if (oy, ox) in point42:
                raise ValueError(
                    f"🚨 Alert! the Exit {ox,oy} in the sacred 42 coordinates\n"
                    "     ! Please choose another place.")

        except ValueError as e:
            print(e)
            print("      🛠️   Please fix your configuration file")
            sys.exit(0)
        return point42

    def get_neighbors(self, grid: List[List[Cell]],
                      cell: Cell) -> List[Tuple[str, Cell]]:
        """
        Return all neighbors of a cell
        in the grid regardless of walls.
        """
        x = cell.x
        y = cell.y
        neighbors = []
        if y - 1 >= 0:
            neighbors.append(("North", grid[y - 1][x]))
        if x + 1 < self.width:
            neighbors.append(("East", grid[y][x + 1]))
        if y + 1 < self.height:
            neighbors.append(("South", grid[y + 1][x]))
        if x - 1 >= 0:
            neighbors.append(("West", grid[y][x - 1]))
        return neighbors

    def remove_walls(self, cell: Cell, neighbor: Cell, direction: str) -> None:
        """
        Remove the wall between two adjacent cells in the given direction.
        """
        opposite = {
            "North": "South",
            "South": "North",
            "East": "West",
            "West": "East"
        }
        cell.remove_wall(direction)
        neighbor.remove_wall(opposite[direction])

    def dfs_rec(self, grid: List[List[Cell]],
                start_cell: Cell) -> List[List[Cell]]:
        """
        Generate a perfect maze using depth-first search,
        optionally recording animation.
        """
        self.animation = []
        self.protect_42(grid)
        stack = []
        start_cell.visited = True
        stack.append(start_cell)

        while stack:
            current = stack[-1]
            neighbors = self.get_neighbors(grid, current)
            unvisited = [(d, n) for d, n in neighbors if not n.visited]
            if unvisited:
                direction, neighbor = random.choice(unvisited)
                self.animation.append((current, neighbor, direction))
                self.remove_walls(current, neighbor, direction)
                neighbor.visited = True
                stack.append(neighbor)
            else:
                stack.pop()
        return grid

    def not_perfect(self, grid: List[List[Cell]],
                    start_cell: Cell) -> List[List[Cell]]:
        """
        Generate an imperfect maze with loops,
        optionally recording animation steps.
        """
        self.animation = []
        point42 = self.protect_42(grid)
        queue = []
        start_cell.visited = True
        queue.append(start_cell)
        while queue:
            current = random.choice(queue)
            neighbors = self.get_neighbors(grid, current)
            unvisited = [(d, n) for d, n in neighbors if not n.visited]
            if unvisited:
                direction, neighbor = random.choice(unvisited)
                self.animation.append((current, neighbor, direction))
                self.remove_walls(current, neighbor, direction)
                neighbor.visited = True
                queue.append(neighbor)
            else:
                if random.random() < 0.2:
                    all_neighbors = self.get_neighbors(grid, current)
                    if all_neighbors:
                        d, n = random.choice(all_neighbors)
                        if (n.y, n.x) not in point42 and (
                                current.y, current.x) not in point42:
                            self.remove_walls(current, n, d)

                queue.remove(current)
        return grid
