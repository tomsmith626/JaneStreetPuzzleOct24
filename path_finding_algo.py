# Define the 8 possible knight moves (row, col)
knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

board = [
        ['A', 'A', 'A', 'B', 'B', 'C'],
        ['A', 'A', 'A', 'B', 'B', 'C'],
        ['A', 'A', 'B', 'B', 'C', 'C'],
        ['A', 'B', 'B', 'B', 'C', 'C'],
        ['A', 'B', 'B', 'C', 'C', 'C'],
        ['A', 'B', 'B', 'C', 'C', 'C']
    ]

boardSize = 6

def knightPaths(start: list, end: list, maxPathLen):
    """ Find list of all routes available from start grid ref to end grid ref with max steps of maxPathLen """
    visited = [[False] * boardSize for _ in range(boardSize)]  # 6x6 board
    allPaths = []
    allRoutes = []
    allVisitedCells = []
    
    # set start as visited
    visited[start[0]][start[1]] = True
    path = (start[0],start[1])
    findKnightPaths(start[0], start[1], end[0], end[1], visited, [path], allPaths, allRoutes, allVisitedCells, maxPathLen)
    
    return allRoutes, allVisitedCells

def isValidMove(x, y, visited):
    """ Check if the knight's move is within the board and not yet visited """
    return 0 <= x < boardSize and 0 <= y < boardSize and not visited[x][y]

def findKnightPaths(x, y, target_x, target_y, visited, path, allPaths, allRoutes, allVisitedCells, maxPathLen):
    """ Recursively find all valid knight paths from (x, y) to (target_x, target_y) """
    # If the knight reaches the target cell, add the current path to all_paths
    if (x, y) == (target_x, target_y):
        allPaths.append(path.copy())  # Append a copy of the path
        # generate route in terms of letters
        route = []
        visitedCells = []
        for step in path:
            cell = board[step[0]][step[1]]
            route.append(cell)
            visitedCells.append(step)
        allRoutes.append(route)
        allVisitedCells.append(visitedCells)
        return
    
    if len(path) > maxPathLen:
        return

    # Try all possible knight moves
    for move in knightMoves:
        new_x, new_y = x + move[0], y + move[1]
        
        # If the move is valid, make the move
        if isValidMove(new_x, new_y, visited):
            visited[new_x][new_y] = True
            path.append((new_x, new_y))
            
            # Recur to explore the next move
            findKnightPaths(new_x, new_y, target_x, target_y, visited, path, allPaths, allRoutes, allVisitedCells, maxPathLen)
            
            # Backtrack: Unmark the square and remove the move from the path
            visited[new_x][new_y] = False
            path.pop()