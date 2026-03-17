from typing import List, Tuple, Dict
from mazegen.maze_generator import Cell


def draw_maze(grid: List[List[Cell]], entry: Tuple[int, int],
              exit: Tuple[int, int], width: int, height: int,
              c_color: Dict[str, str], point42: set[Tuple[int, int]]) -> None:
    """
    Print the maze in the terminal using colors,
    showing walls, paths, entry, exit, and special points.
    """
    print(f"{c_color['wall']}" * (2 * width) + c_color['wall'])
    for y in range(height):
        bottom_str = c_color['wall']
        mid_str = c_color['wall']
        for x in range(width):
            cell = grid[y][x]
            if cell.walls['South']:
                bottom_str += c_color['wall'] * 2
            else:
                if grid[y + 1][x].path and grid[y][x].path and y + 1 < height:
                    bottom_str += c_color['path'] + c_color['wall']
                else:
                    bottom_str += c_color['back'] + c_color['wall']
            if (cell.x, cell.y) == entry:
                mid_str += "\033[1;34m🔵\033[0m"
            elif (cell.x, cell.y) == exit:
                mid_str += "\033[31m🌀\033[0m"
            elif (cell.y, cell.x) in point42:
                mid_str += c_color['four2']
            elif cell.path:
                mid_str += c_color['path']
            else:
                mid_str += c_color['back']

            if cell.walls['East']:
                mid_str += c_color['wall']
            else:
                if grid[y][x + 1].path and grid[y][x].path and x + 1 < width:
                    mid_str += c_color['path']
                else:
                    mid_str += c_color['back']

        print(mid_str)
        print(bottom_str)
