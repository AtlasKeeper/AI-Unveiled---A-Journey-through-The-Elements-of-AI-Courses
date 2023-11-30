"""
River Crossing Puzzle Solver

Overview:
This Python script solves a variation of the classic river crossing puzzle, known as the "robot in a rowboat" problem. In this puzzle, a robot needs to transport a fox, a chicken, and a sack of chicken-feed across a river, subject to certain constraints. The robot is the only one capable of operating the rowboat, and only two items can be on the rowboat at the same time. Crucially, the fox will eat the chicken if left alone, and the chicken will eat the chicken-feed if given the chance.

How It Works:
- The puzzle is modeled using the concept of states, representing the positions of the robot, fox, chicken, and chicken-feed.
- The script uses a depth-first search algorithm to explore possible moves from the initial state to the goal state while adhering to the puzzle constraints.
- The State class defines the current state, and the `generate_moves` function generates valid moves from a given state.
- The script systematically searches for a solution path, avoiding forbidden states, and prints the sequence of moves required to solve the puzzle.

Usage:
1. Set the initial and goal states.
2. Run the script to find the solution path.
3. The output displays the steps taken to move all items from the initial state to the goal state, ensuring the safety of the chicken and the chicken-feed.

Note: If no solution is found, the script will indicate that no valid sequence of moves exists to solve the puzzle.

"""


class State:
    def __init__(self, robot, fox, chicken, feed, boat):
        self.robot = robot
        self.fox = fox
        self.chicken = chicken
        self.feed = feed
        self.boat = boat

    def __eq__(self, other):
        return (
            self.robot == other.robot and
            self.fox == other.fox and
            self.chicken == other.chicken and
            self.feed == other.feed and
            self.boat == other.boat
        )

    def __hash__(self):
        return hash((self.robot, self.fox, self.chicken, self.feed, self.boat))

    def __str__(self):
        return f"Robot: {self.robot}, Fox: {self.fox}, Chicken: {self.chicken}, Feed: {self.feed}, Boat: {self.boat}"

def is_valid(state):
    # Check if the state violates any constraints
    if (state.fox == state.chicken and state.fox != state.robot) or \
       (state.chicken == state.feed and state.chicken != state.robot):
        return False
    return True

def generate_moves(state):
    # Generate possible moves from the current state
    moves = []
    if state.boat == 'near':
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'far'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'far'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'far'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'far'))
    else:
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'near'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'near'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'near'))
        moves.append(State(not state.robot, state.fox, state.chicken, state.feed, 'near'))

    return [move for move in moves if is_valid(move)]

def depth_first_search(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state == goal_state:
            return path + [current_state]

        if current_state not in visited:
            visited.add(current_state)
            stack.extend((neighbor, path + [current_state]) for neighbor in generate_moves(current_state))

    return None

# Initial and Goal States
initial_state = State(True, True, True, True, 'near')
goal_state = State(False, False, False, False, 'far')

# Solve the puzzle
solution_path = depth_first_search(initial_state, goal_state)

# Print the solution path
if solution_path:
    print("Solution Path:")
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}: {state}")
else:
    print("No solution found.")
