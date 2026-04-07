COSC 4368 – Assignment 1, Task 1
Randomized Hill Climbing with Resampling (RHCR2)

Requirements

Python 3.8 or higher
NumPy

Install NumPy if you don't have it:
pip install numpy

How to Run
python task1_rhcr2.py
That's it. No arguments needed — all 32 experiments plus the 33rd preferred run will execute automatically and print to the terminal.

What the Program Does
The program minimizes the fFrog function:
fFrog(x, y) = x · sin(√|y+1−x|) · cos(√|x+y+1|)
            + (y+1) · cos(√|y+1−x|) · sin(√|x+y+1|)
with x, y ∈ [−512, 512].
It runs RHCR2 — Randomized Hill Climbing with Resampling — which chains three RHC calls with shrinking neighborhoods:
StageNeighborhood sizeStarting pointRun 1zsp (given)Run 2z / 20sol1Run 3z / 400sol2
Each RHC stage stops when no neighbor improves the current solution.

Experiments
The program runs 32 experiments over all combinations of:
ParameterValuesStarting points (sp)(-300,-400), (0,0), (-222,-222), (-510,400)p (neighbors per step)120, 400z (neighborhood size)9, 50Seeds1 (Run 1), 2 (Run 2)
It then runs a 33rd preferred run with:

sp = (-520, 40)
p = 400
z = 50
seed = 33


Output Format
For each of the 32 runs:
--------------------------------------------
p = 120, z = 9
starting point = (-300, -400)
run (seed) = 1

sol1 = (-278.9029, -437.9189),   f(sol1) = -436.282075
sol2 = (-279.7084, -438.2183),   f(sol2) = -436.353994
sol3 = (-279.7491, -438.2134),   f(sol3) = -436.354462

calls: r1 = 841, r2 = 361, r3 = 361, total = 1563
--------------------------------------------

sol1 / sol2 / sol3 — best (x, y) found after each RHC stage
f(sol1) / f(sol2) / f(sol3) — function value at each solution
r1 / r2 / r3 — number of times f was evaluated in each stage
total — total number of f evaluations for the full RHCR2 run


File Structure
task1_rhcr2.py   — main source code (frog, RHC, RHCR2, all experiments)
README.md        — this fileShare
