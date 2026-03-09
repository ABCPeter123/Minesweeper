
# Minesweeper

A desktop implementation of the classic **Minesweeper** game built with **Python** and **Pygame**.
This project recreates traditional Minesweeper gameplay while implementing custom graphics,
multiple difficulty levels, first-click-safe mine generation, recursive reveal logic,
and event-driven game interactions.

---

## Features

- Three difficulty levels
  - Easy: **12 × 9** board with **15 mines**
  - Medium: **20 × 15** board with **50 mines**
  - Hard: **28 × 21** board with **150 mines**
- Graphical interface built with **Pygame**
- **First-click-safe mine generation**
- Recursive reveal of empty regions
- Right-click flag placement and removal
- Shortcut reveal (chording)
- Win and loss screens
- Menu interface for difficulty selection and exiting the game

---

## Tech Stack

- **Python**
- **Pygame**

---

## Project Structure

```
Minesweeper/
│
├── Minesweeper.py
│
└── Sources/
    ├── title.png
    ├── title2.png
    ├── easy_button.png
    ├── medium_button.png
    ├── hard_button.png
    ├── exit.png
    ├── leave.png
    ├── win.png
    ├── lose.png
    ├── grid / number / mine / flag assets
```

The game loads graphical assets from the `Sources/` folder to render the board and interface elements.

---

## Installation

### 1. Install Python
Ensure Python 3 is installed on your system.

### 2. Install dependencies

```
pip install pygame
```

### 3. Run the game

```
python Minesweeper.py
```

Make sure the `Sources/` directory is located in the same folder as the main program.

---

## Controls

| Action | Input |
|------|------|
| Reveal tile | Left Click |
| Place/remove flag | Right Click |
| Shortcut reveal | Left + Right Click on opened number |
| Return to menu | Leave button |
| Quit game | Exit button |

---

## Gameplay Logic

### Mine Generation

Mines are generated **after the player's first click**.
This guarantees that the first move is always safe and prevents the player from losing immediately.

The clicked tile and its neighboring tiles are excluded from mine placement to ensure a playable starting area.

---

### Recursive Empty Expansion

When a tile with **zero adjacent mines** is revealed, the game automatically reveals all connected empty tiles until numbered boundary cells are reached.

This behavior is implemented using a **recursive flood-fill style algorithm** that explores neighboring cells while maintaining board-state invariants.

---

### Chord / Shortcut Reveal

If a numbered tile is already revealed and the correct number of flags are placed around it, the player can press **left + right click** simultaneously to reveal all remaining surrounding tiles.

This mirrors the behavior of classic Minesweeper implementations and improves gameplay speed.

---

## Difficulty Settings

| Difficulty | Grid Size | Mine Count |
|------------|-----------|-----------|
| Easy | 12 × 9 | 15 |
| Medium | 20 × 15 | 50 |
| Hard | 28 × 21 | 150 |

---

## What I Learned

This project helped strengthen skills in:

- Event-driven programming
- Algorithm design for grid traversal
- Game-state management
- Recursive algorithms
- Boundary checking and neighbor exploration
- Software modularity and maintainability
- Debugging complex state transitions
- Designing systems that maintain gameplay invariants

---

## Possible Improvements

Future improvements could include:

- Refactoring the codebase into multiple modules
- Replacing dynamic global variables with structured board objects
- Adding a timer and mine counter
- Implementing a restart button
- Adding animations and smoother UI feedback
- Adding keyboard shortcuts
- Creating automated tests for board generation logic
- Supporting additional board sizes or custom configurations

---

## Project Summary

This project implements a fully playable Minesweeper game using **Python and Pygame**, featuring multi-difficulty gameplay, first-click-safe mine generation, recursive region expansion, and event-driven user interaction.
The project emphasizes **algorithmic logic, state consistency, and interactive system design**.

---

## License

This project is open for educational and personal use.
