*This project has been created as part of the 42 curriculum by [hamezoua, mbidlal].*

# 🧩 A-Maze-ing: The Labyrinth Generator

## 📝 Description
**A-Maze-ing** is a Python-based interactive tool designed to generate, solve, and visualize mazes. The project features two main generation modes: **Perfect Mazes** (using Depth-First Search) and **Imperfect Mazes** (using a custom randomized algorithm). 

The goal of this project was to implement a robust system that handles complex grid logic, provides an interactive CLI experience, and allows users to find the shortest path between any two points using graph traversal techniques (BFS).

---

## ⚙️ Instructions

### 🛠️ Installation & Setup
We have simplified the setup process using a `Makefile`. You can install all necessary dependencies (including `readchar`, `flake8`, and `mypy`) with:

```bash
make install

```

### 🚀 Execution

The project is driven by a `config.txt` file and can be launched easily:

* **To run the generator:**
```bash
cd MAZE/
make run

```


* **For debugging (using pdb):**
```bash
make debug

```



### 🧹 Maintenance & Quality Control

To maintain code quality and keep the repository clean:

* **Linting (Standard):** `make lint` (Runs flake8 and mypy to check for errors and type consistency).
* **Linting (Strict):** `make lint-strict` (For more rigorous type checking).
* **Clean caches:** `make clean` (Removes `__pycache__`, `.mypy_cache`, and other temporary files).

---

## 📄 Configuration File Structure (`config.txt`)

The generator expects a `.txt` file at the root with the following format:

```text
WIDTH = 20
HEIGHT = 15
ENTRY = 0,5
EXIT = 0,12
OUTPUT_FILE = outpute.txt
PERFECT = false
SEED = 11

```

---

# 🎮 Interactive CLI Features

Using the `readchar` library, we implemented a real-time menu where you don't need to press "Enter" to trigger actions:

| Key | Action |
| --- | --- |
| **1** | **Re-generate**: Create a brand new maze based on the config. |
| **2** | **Show/Hide Path**: Toggle the BFS-calculated shortest path from entry to exit. |
| **3** | **Rotate Colors**: Change the visual color scheme of the maze. |
| **4** | **Animation Mode**: Toggle the step-by-step generation visualization. |
| **5** | **Quit**: Safely exit the application. |

---

## 🧠 Technical Choices: Algorithms

### 1. The Chosen Algorithm: "Not Perfect" Maze

While we initially considered a standard Prim's algorithm, we decided to implement a custom **Randomized Growth Algorithm**.

* **How it works:** It picks random cells from a growth queue. If no unvisited neighbors are found, it has a **20% probability** of breaking a wall to an already-visited neighbor.
* **Why this choice?** Unlike standard DFS or Prim's, this creates **Loops** (cycles). We chose this because it offers a more "open" and less predictable maze layout, providing a unique challenge compared to standard perfect mazes.

### 2. Solving Algorithm (BFS)

We chose **Breadth-First Search (BFS)** for finding the path because it guarantees finding the **shortest path** in an unweighted grid, which is essential for our "Show Path" feature.

### 3. The "Sacred 42"

We implemented a `protect_42` method that marks a specific set of coordinates in the center of the grid as "visited" before generation starts. This ensures the maze always respects and preserves the shape of the number "42".

---

## ♻️ Reusable Code

The project is built with **Object-Oriented Programming (OOP)**, making several parts reusable:

* **`Cell` Class:** A standalone class that manages wall states and visit status, easily portable to other grid-based projects.
* **Algorithm Decoupling:** The `Mazegenerator` logic is separated from the rendering. You can feed the generated grid into a GUI (like PyGame) or a web interface with minimal changes.

---

## 👥 Team & Management

### Roles:

* **hamezoua**: Algorithm implementation (DFS/BFS), core maze logic, and generation flow.
* **mbidlal**: Configuration parsing, interactive CLI (readchar), and Makefile architecture.

### Planning & Evolution:

* **Anticipated Planning:** 1 week.
* **Actual Duration:** 10 days.
* **Evolution:** We spent more time than expected learning **Git** workflows (branching and merging). This initial friction eventually led to a much more organized collaboration.

### Reflection:

* **What worked well:** Modularizing the project into classes allowed us to work on different features (like the menu and the algorithm) simultaneously.
* **Areas for improvement:** We could further optimize the rendering engine for very large mazes (e.g., 100x100).

---

## 🤖 AI Usage & Resources

### AI Task Description:

We used AI as a peer-coding tool for:

* **Conceptual Clarity:** Understanding the mathematical differences between maze algorithms.
* **Best Practices:** Helping us structure the `Makefile` and linting configurations.
* **Documentation:** Assisting in the clear phrasing of technical sections in this README.

### Resources:

* [Maze Generation Algorithms - Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
* [Python `readchar` Library](https://pypi.org/project/readchar/)
* [Mypy Documentation](https://mypy.readthedocs.io/)
