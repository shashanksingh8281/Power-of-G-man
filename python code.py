from collections import deque

# Function to calculate power consumption for a move
def calculate_power_consumption(prev_direction, new_direction):
    turns = abs(ord(prev_direction) - ord(new_direction))
    return 5 * turns + 10

# Function to check if a coordinate is valid within the grid
def is_valid(x, y):
    return 0 <= x < 6 and 0 <= y < 6

# Function to find the shortest path and remaining power
def find_shortest_path(source_x, source_y, source_direction, dest_x, dest_y):
    directions = ['N', 'E', 'S', 'W']
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([(source_x, source_y, source_direction, 200)])
    visited = set([(source_x, source_y, source_direction)])
    
    while queue:
        x, y, direction, power = queue.popleft()
        
        if x == dest_x and y == dest_y:
            return power
        
        for i in range(4):
            new_direction = directions[i]
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if is_valid(new_x, new_y) and (new_x, new_y, new_direction) not in visited:
                new_power = power - calculate_power_consumption(direction, new_direction)
                if new_power >= 0:
                    queue.append((new_x, new_y, new_direction, new_power))
                    visited.add((new_x, new_y, new_direction))
    
    return -1

# User Inputs
source_input = input("Enter source coordinates and direction (e.g., '2 1 E'): ")
dest_input = input("Enter destination coordinates (e.g., '4 3'): ")

# Parse Input
source_x, source_y, source_direction = source_input.split()
source_x = int(source_x)
source_y = int(source_y)
dest_x, dest_y = map(int, dest_input.split())

# Find shortest path
remaining_power = find_shortest_path(source_x, source_y, source_direction, dest_x, dest_y)

# Output
print("POWER", remaining_power)
