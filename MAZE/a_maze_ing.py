from mazegen.maze_generator import Mazegenerator
from mazegen.maze_generator import Cell
from configuration import open_file_read
from draw import draw_maze
from found_path import bfs_reco, short_way
from hexa_file import ft_converte_hexa
from typing import Optional, Tuple, List
import os
import time
import sys
import random
from colors import color_list, RESET, GREEN, RED
import readchar

c_color = color_list[0]

args = sys.argv
argc = len(args)
try:
    if argc == 1:
        raise IndexError("No arguments provided!")
except Exception as e:
    print(f"⚠️  Error: {e} ,Please add config.txt")
    sys.exit(1)
file_path = sys.argv[1]
output = open_file_read(file_path)
width: int = output['WIDTH']
height: int = output['HEIGHT']
entry: Tuple[int, int] = output['ENTRY']
exit: Tuple[int, int] = output['EXIT']
output_file: str = output['OUTPUT_FILE']
perfect: bool = output['PERFECT']
seed: Optional[int] = output['SEED']
maze = Mazegenerator(width, height, entry, exit, seed)
ox, oy = exit
ex, ey = entry
grid = maze.configue_grid()
start_cell = grid[0][0]
end_cell = grid[oy][ox]
point42 = maze.protect_42(grid)


def reset_grid(grid: List[List[Cell]]) -> None:
    """
    Reset all cells in the grid to the initial state
    """
    for row in grid:
        for cell in row:
            cell.visited = False
            cell.walls = {
                "North": True,
                "East": True,
                "South": True,
                "West": True
            }


def generation_maze(perfect: bool) -> None:
    """
    Generate a maze (perfect or imperfect)
    and display it in the terminal.
    """
    if perfect:
        maze.dfs_rec(grid, start_cell)
    else:
        maze.not_perfect(grid, start_cell)
    draw_maze(grid, entry, exit, width, height, c_color, point42)


def animation_generation(perfect: bool) -> None:
    """
    Generate the maze step-by-step with animation
    and display each step.
    """
    if perfect:
        res = maze.dfs_rec(grid, start_cell)
        reset_grid(res)
    else:
        res = maze.not_perfect(grid, start_cell)
        reset_grid(res)
    for current, neighbor, direction in maze.animation:
        print("\033[H", end="")
        maze.remove_walls(current, neighbor, direction)
        draw_maze(grid, entry, exit, width, height, c_color, point42)
        time.sleep(0.1)


def hexa_output(path: List[Tuple[str, Tuple[int, int]]]) -> None:
    """
    Save the maze in hexadecimal format
    with the solution path to an output file.
    """
    os.makedirs("maze_output", exist_ok=True)
    maze_path_out = "maze_output" + "/" + output_file
    path_direction = [d for d, _ in path if not d == 'Start']
    with open(maze_path_out, 'w') as file:
        hex_maze = ft_converte_hexa(grid, entry, exit, path_direction)
        file.write(hex_maze)


def hide_path(path_coords: List[Tuple[int, int]]) -> None:
    """
    Hide the solution path in the maze
    by disabling path markers.
    """
    for (x, y) in path_coords:
        if grid[y][x].path:
            grid[y][x].path = False


def show_path(path_coords: List[Tuple[int, int]]) -> None:
    """
    Show the solution path in the maze
    by enabling path markers.
    """
    for (x, y) in path_coords:
        grid[y][x].path = True


# -----------------------check the input started----------------------------
turn_on = False
current_color = RESET
animation = False
output_file = output['OUTPUT_FILE']
print("\033[?25l", end="")
os.system('clear')
print("\033[H", end="")
generation_maze(perfect)
try:
    while True:

        parent = bfs_reco(grid, start_cell, end_cell, width, height)
        path = short_way(parent, start_cell, end_cell)
        path_coords = [cell for _, cell in path]
        hexa_output(path)
        print("\n")
        print("████████████████████████ A-Maze-ing ████████████████████████")
        print(
            "\033[1;99m██  1. Re-generate a new maze                             ██\033[0m"
        )
        if turn_on:
            print(f"\033[1;99m██  2. Show/Hide Path [{GREEN}ON{RESET}]"
                  "from entry to exit              ██\033[0m")
        elif not turn_on:
            print(f"\033[1;99m██  2. Show/Hide Path Path [{RED}OFF{RESET}]"
                  "from entry to exit        ██\033[0m")
        print(
            "\033[1;99m██  3. Rotate maze colors                                 ██\033[0m"
        )
        if animation:
            print(f"\033[1;99m██  4. Mode Animation  [{GREEN}ON{RESET}\033[0m]"
                  "                               ██")
        elif not animation:
            print(f"\033[1;99m██  4. Mode Animation  [{RED}OFF{RESET}]"
                  "                              ██\033[0m")
        print(
            "\033[1;99m██  5. Quit                                               ██\033[0m"
        )
        print(f"\033[1;99m██  1337. future is loading"
              "                               ██\033[0m")
        print("██                                                        ██")
        print("\033[1;99m██  by hamezoua and mbidlal                "
              "               ██\033[0m")
        print("██                                                        ██")
        print("█" * 60)
        x = readchar.readchar()
        2
        if x == "1":
            os.system('clear')
            turn_on = False
            hide_path(path_coords)
            if not animation:
                reset_grid(grid)
                generation_maze(perfect)
            elif animation:
                reset_grid(grid)
                animation_generation(perfect)
        if x == '2':
            os.system('clear')
            draw_maze(grid, entry, exit, width, height, c_color, point42)
            if not turn_on and not animation:
                show_path(path_coords)
                turn_on = True
            elif not turn_on and animation:
                entry_current = entry
                for (ax, ay) in path_coords:
                    grid[ay][ax].path = True
                    print("\033[H", end="")
                    draw_maze(grid, entry, exit, width, height, c_color,
                              point42)
                    time.sleep(0.1)
                turn_on = True
            else:
                hide_path(path_coords)
                turn_on = False

        if x == "3":
            os.system('clear')
            old_color = c_color
            while c_color == old_color:
                c_color = random.choice(color_list)
            draw_maze(grid, entry, exit, width, height, c_color, point42)
        if x == "4":
            # os.system('clear')
            print("\033[H", end="")
            draw_maze(grid, entry, exit, width, height, c_color, point42)
            if not animation:
                animation = True
            else:
                animation = False
        if x == "5":
            print("\033[?25h", end="")
            os.system('clear')
            break
        else:
            os.system('clear')
            print("\033[H", end="")
            draw_maze(grid, entry, exit, width, height, c_color, point42)
except BaseException:
    print("\033[?25h", end="")
    os.system('clear')
    print("\n⚠️  Program interrupted by error")
    sys.exit(1)
except Exception as e:
    print("\033[?25h", end="")
    print(f"Error: {e}")
    sys.exit(1)
# -----------------------check the input ended----------------------------
