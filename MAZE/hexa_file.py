from mazegen.maze_generator import Cell
from typing import List, Tuple


def ft_converte_hexa(grid: List[List[Cell]], entry: Tuple[int, int],
                     exit: Tuple[int, int], path_direction: List[str]) -> str:
    """
    Convert the maze grid into a hexadecimal wall representation
    and include entry, exit, and path directions.
    """
    result = ""
    for row in grid:
        for cell in row:
            wall = 15
            if not cell.walls['North']:
                wall -= 1
            if not cell.walls['East']:
                wall -= 2
            if not cell.walls['South']:
                wall -= 4
            if not cell.walls['West']:
                wall -= 8
            result += format(wall, 'X')
        result += '\n'
    result += '\n'
    xe, ye = entry
    xo, yo = exit
    result += f"{xe}, {ye}\n"
    result += f"{xo}, {yo}\n"
    for d in path_direction:
        result += d
    return result
