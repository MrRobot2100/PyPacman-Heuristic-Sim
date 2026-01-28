# Pacman Game Simulation ᗧ•••

## Overview

This project is a modular implementation of the classic arcade game **Pacman**, developed in **Python** using the `turtle` graphics library. It demonstrates fundamental concepts of game development, including coordinate systems, state management, basic Artificial Intelligence (AI) for enemies, and file I/O for persistence.

The system separates the graphical engine (`pacman.py`) from the game logic and heuristics (`principal_alunos.py`), simulating a real-time grid-based movement system with collision detection and ghost behavior.

## ⚙️ Key Features

### Game Logic & Architecture
* **Modular Design:** Separation of concerns between the rendering engine (drawing the world, handling sprites) and the controller logic (movement, rules).
* **Grid-Based Movement:** Custom algorithm to translate pixel coordinates into grid tiles for precise collision detection and wall interactions.
* **State Management:** Robust system to track the game state (`estado_jogo`), including score, player position, and ghost statuses.

### Artificial Intelligence (Ghosts)
* **Distinct Behaviors:** Implementation of different movement heuristics for the ghosts:
    * **Clyde (Orange):** Features a "Scatter/Chase" logic based on distance calculation. If Pacman is far, he chases; if too close, he scatters to corners.
    * **Pinky (Pink):** Uses target anticipation logic to intercept the player.
    * **Randomized Movement:** Other ghosts utilize randomized pathfinding to create unpredictability.

### Persistence & Customization
* **Save/Load System:** Capability to serialize the game state to a text file (`save.txt`) and restore it later, preserving the score and positions.
* **Dynamic Map Loading:** The game reads the level layout from external text files (`mapa_inicial.txt`), allowing for custom level designs without changing the code.

## 🛠️ Tech Stack

* **Language:** Python 3
* **Graphics:** Turtle (Standard Library) & Tkinter
* **Logic:** `functools` for event binding, `math` for vector/distance calculations.
* **Concepts:** Cartesian Coordinate Systems, Game Loops, File I/O, Heuristic Algorithms.

## 🚀 How to Run

### Prerequisites
* Python 3.x installed.
* An `images` folder containing the sprites (`pacman.gif`, `3.gif`, `4.gif`, `5.gif`, `6.gif`) in the root directory.

### Execution
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/teu-usuario/pacman-python.git](https://github.com/teu-usuario/pacman-python.git)
    cd pacman-python
    ```

2.  **Run the Game:**
    ```bash
    python principal_alunos.py
    ```

3.  **Controls:**
    * **Arrow Keys:** Move Pacman (Up, Down, Left, Right).
    * **`S` Key:** Save current game state.
    * **`L` Key:** Load saved game.
    * **`ESC`:** Exit the game.

---
*Developed for [Nome da Cadeira/Disciplina] at [Nome da Universidade].*
