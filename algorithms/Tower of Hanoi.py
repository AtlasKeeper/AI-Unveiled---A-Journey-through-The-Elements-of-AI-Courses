""" 
Tower of Hanoi Solver

Overview:
This Python script solves the Tower of Hanoi problem, a classic puzzle involving three rods and a number of disks of different sizes. The objectve is to move the entire stack of disks from one rod to another,
obeying specific rules: only one disk can be moved at a time, and no disk may be placed on top of a smaller disk.

How It Works:
- The script implements a recursive algorithm to solve the Tower of Hanoi problem.
- The `tower_of_hanoi` function moves disks from the source rod to the target rod, using the auxiliary rod when necessary.
- The algorithm follows the principles of recursion, breaking the problem into subproblems and solving them step by step.

Usage:
1. Set the number of disks and the initial and target rods in the `tower_of_hanoi` function.
2. Run the script to see the sequence of moves required to solve the Tower of Hanoi problem.

"""

def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n-1, source, target, auxiliary)

        # Move the nth disk from the source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary peg to target peg
        tower_of_hanoi(n-1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')