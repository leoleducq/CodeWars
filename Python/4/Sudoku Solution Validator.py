def valid_solution(board):
    for i in range(9):
        if not (set(board[i]) == set(range(1, 10)) and set([board[j][i] for j in range(9)]) == set(range(1, 10))):
            return False
    for i in range(3):
        for j in range(3):
            if not set([board[3 * i + k][3 * j + l] for k in range(3) for l in range(3)]) == set(range(1, 10)):
                return False
    return True