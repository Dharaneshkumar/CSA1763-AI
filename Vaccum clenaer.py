environment = [
    [1, 0],  
    [1, 1]   
]
vacuum_position = [0, 0]  
def print_environment(environment):
    print("Current environment:")
    for row in environment:
        print(row)
    print()
def is_goal_state(environment):
    for row in environment:
        if 1 in row:
            return False
    return True
def move_vacuum(vacuum_position, direction):
    x, y = vacuum_position
    if direction == "UP" and x > 0:
        return [x - 1, y]
    elif direction == "DOWN" and x < 1:
        return [x + 1, y]
    elif direction == "LEFT" and y > 0:
        return [x, y - 1]
    elif direction == "RIGHT" and y < 1:
        return [x, y + 1]
    return vacuum_position  
def vacuum_cleaner_agent(environment, vacuum_position):
    moves = 0
    while not is_goal_state(environment):
        x, y = vacuum_position
        if environment[x][y] == 1:
            print(f"Cleaning position ({x}, {y})")
            environment[x][y] = 0
            moves += 1
            print_environment(environment)
        if y < 1:
            vacuum_position = move_vacuum(vacuum_position, "RIGHT")
        elif x < 1:
            vacuum_position = move_vacuum(vacuum_position, "DOWN")
        else:
            break  
    print(f"All cells are clean! Total moves: {moves}")
def main():
    print("Initial environment:")
    print_environment(environment)
    vacuum_cleaner_agent(environment, vacuum_position)
main()
