from mazegen.maze_generator import Cell
from typing import List, Dict, Tuple


def get_neighbors_bfs(grid: List[List[Cell]], cell: Cell, width: int,
                      height: int) -> List[Tuple[str, Cell]]:
    """
    Return reachable neighbor cells (N, E, S, W)
    for BFS based on open walls.
    """
    x = cell.x
    y = cell.y
    neighbors: List[Tuple[str, Cell]] = []
    if not cell.walls['North'] and y - 1 >= 0:
        neighbors.append(('N', grid[y - 1][x]))
    if not cell.walls['East'] and x + 1 < width:
        neighbors.append(('E', grid[y][x + 1]))
    if not cell.walls['South'] and y + 1 < height:
        neighbors.append(('S', grid[y + 1][x]))
    if not cell.walls['West'] and x - 1 >= 0:
        neighbors.append(('W', grid[y][x - 1]))
    return neighbors


def bfs_reco(
        grid: List[List[Cell]], start_cell: Cell, end_cell: Cell, width: int,
        height: int) -> Dict[Tuple[int, int], Tuple[str, Tuple[int, int]]]:
    """
    Run Breadth-First Search to explore the maze
    and record parent cells for path reconstruction.
    """
    queue = []
    visited = []
    parent: Dict[Tuple[int, int], Tuple[str, Tuple[int, int]]] = {}

    queue.append(('Start', start_cell))
    visited.append((start_cell.x, start_cell.y))
    found = False

    while queue and not found:
        _, cell = queue.pop(0)
        neighbors = get_neighbors_bfs(grid, cell, width, height)

        for d, n in neighbors:
            coord = (n.x, n.y)
            if coord not in visited:
                visited.append(coord)
                parent[coord] = (d, (cell.x, cell.y))
                if coord == (end_cell.x, end_cell.y):
                    found = True
                    break
                queue.append((d, n))
    return parent


def short_way(parent: Dict[Tuple[int, int],
                           Tuple[str, Tuple[int, int]]], start_cell: Cell,
              end_cell: Cell) -> List[Tuple[str, Tuple[int, int]]]:
    """
    Reconstruct and return the shortest path
    from start to end using the parent map.
    """
    path: List[Tuple[str, Tuple[int, int]]] = []
    cell = (end_cell.x, end_cell.y)
    while cell != (start_cell.x, start_cell.y):
        d, parent_cell = parent[cell]
        path.append((d, cell))
        cell = parent_cell
    path.append(("Start", (start_cell.x, start_cell.y)))
    path.reverse()
    return path
