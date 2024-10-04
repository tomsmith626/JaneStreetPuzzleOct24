
board = [
    ['A', 'A', 'A', 'B', 'B', 'C'],
    ['A', 'A', 'A', 'B', 'B', 'C'],
    ['A', 'A', 'B', 'B', 'C', 'C'],
    ['A', 'B', 'B', 'B', 'C', 'C'],
    ['A', 'B', 'B', 'C', 'C', 'C'],
    ['A', 'B', 'B', 'C', 'C', 'C']
]

board_size = 6

# Define the 8 possible knight moves (row, col)
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def is_valid_move(x, y, visited):
    """ Check if the knight's move is within the board and not yet visited """
    return 0 <= x < board_size and 0 <= y < board_size and not visited[x][y]

def find_knight_paths(x, y, target_x, target_y, visited, path, all_paths):
    """ Recursively find all valid knight paths from (x, y) to (target_x, target_y) """
    # If the knight reaches the target cell, add the current path to all_paths
    if (x, y) == (target_x, target_y):
        all_paths.append(path.copy())  # Append a copy of the path
        return
    
    if len(path) > 6:
        return

    # Try all possible knight moves
    for move in knight_moves:
        new_x, new_y = x + move[0], y + move[1]
        
        # If the move is valid, make the move
        if is_valid_move(new_x, new_y, visited):
            visited[new_x][new_y] = True
            path.append((new_x, new_y))
            
            # Recur to explore the next move
            find_knight_paths(new_x, new_y, target_x, target_y, visited, path, all_paths)
            
            # Backtrack: Unmark the square and remove the move from the path
            visited[new_x][new_y] = False
            path.pop()

def knight_paths_from_corner_to_corner():
    """ Find all knight paths from (0,0) to (5,5) on a 6x6 board """
    visited = [[False] * board_size for _ in range(board_size)]  # 6x6 board
    all_paths = []
    
    # Start from the top-left corner (0, 0)
    visited[0][0] = True
    find_knight_paths(0, 0, 5, 5, visited, [(0, 0)], all_paths)
    
    return all_paths

# Generate all paths
paths = knight_paths_from_corner_to_corner()

# Output the paths
print(f"Total paths: {len(paths)}")
for path in paths:
    print(path)