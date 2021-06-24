Started a project of creating Conway's Game of life in python using PyGame library.

The idea in the game is:
- There is a grid of cells, which can be colored Black(Alive) or White(Dead).

At each step in time, the following transitions occur:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

You can customize the game yourself!

What you'll need:
1. Python 3 installed
2. pyGame module installed
    - if not installed you can do it by this commands:
    1. Open cmd by pressing Windows + R or opening the start menu bar, and typing cmd and pressing Enter.
    2. type in cmd console one of the following (the pretty much all the same)
       - "pip install pygame"
       - "python pip install pygame"
       - "python3 pip intall pygame"

Customizable Variables:
- FPS of the Game 
- Cell Size
- Grid size according to cell size
- Starting patterns.
