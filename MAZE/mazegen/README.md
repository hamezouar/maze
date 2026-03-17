## *This project has been created as part of the 42 curriculum by [hamezoua, mbidlal].*
## 🛠️ Usage as a Package (API)

If you want to integrate the maze generation engine into your own project, follow these technical guidelines.

### 📦 Import and Initialization
First, ensure you have `typing` and `random` available (though they are standard). Import the generator from your file:

```python
from mazegen import Mazegenerator, Cell # Replace 'mazegen' with your filename

# Parameters:
# width (int), height (int)
# entry (Tuple[int, int]), exit (Tuple[int, int])
# seed (Optional[int]) -> use a fixed int for reproducible mazes
generator = Mazegenerator(
    width=20, 
    height=15, 
    entry=(0, 5), 
    exit=(0, 12), 
    seed=42
)

```

### ⚙️ Step-by-Step Execution

To avoid issues, you must follow this specific order of execution:

1. **Grid Configuration**: This creates the 2D array of `Cell` objects.
```python
grid = generator.configue_grid() # Returns List[List[Cell]]

```


2. **Algorithm Execution**: Pass the `grid` and a `start_cell` (usually `grid[0][0]`).
```python
# For a Perfect Maze (DFS):
maze = generator.dfs_rec(grid, grid[0][0])

# For an Imperfect Maze (Loops):
# maze = generator.not_perfect(grid, grid[0][0])

```



### ⚠️ Important Requirements

To ensure the algorithm runs without crashing:

* **Start Cell**: The second argument of `dfs_rec` or `not_perfect` must be an actual `Cell` object from the grid, not just coordinates.
* **Coordinates**: Ensure `entry` and `exit` coordinates are within the range of `width` and `height`.
* **The "42" Zone**: Avoid placing your `entry` or `exit` inside the center of the grid where the "42" shape is protected, otherwise, the program will raise a `ValueError` and exit.

### 🔍 Data Structure Reference

When you iterate through the `maze` (List[List[Cell]]), you can access these attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| `cell.x` | `int` | Horizontal index. |
| `cell.y` | `int` | Vertical index. |
| `cell.walls` | `dict` | `{'North': bool, 'East': bool, 'South': bool, 'West': bool}`. `True` means the wall is still there. |
| `cell.visited` | `bool` | Used by the algorithm to track progress. |
