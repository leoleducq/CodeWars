puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def sudoku(puzzle):
    # Fait des listes de lignes, de colonnes et de carrés
    lines = puzzle
    columns = [[puzzle[i][j] for i in range(9)] for j in range(9)]
    squares = [[puzzle[i][j] for i in range(3 * (k // 3), 3 * (k // 3) + 3) for j in range(3 * (k % 3), 3 * (k % 3) + 3)] for k in range(9)]
    
    #Récupère les informations sur les cases vides et chiffres manquants
    i = 0
    missing, empty, single, multiple = get_info(lines,columns,squares)
    while empty != [[], [], [], [], [], [], [], [], []]:
        missing, empty, single, multiple = get_info(lines,columns,squares)
        pos_number(missing,empty,single,multiple,puzzle)
        if i > 100:
            break
        i += 1
    return puzzle
    

def get_info(lines,columns,squares):
    # Fait une liste de listes de chiffres manquants
    missing = [[i for i in range(1, 10) if i not in lines[k] and i not in columns[k] and i not in squares[k]] for k in range(9)]
    
    # Fait une liste de listes de positions des cases vides
    empty = [[(k, i) for i in range(9) if puzzle[k][i] == 0] for k in range(9)]
    
    # Fait une liste de listes de positions des cases vides qui ont un seul chiffre manquant
    single = [[empty[k][i] for i in range(len(empty[k])) if len(missing[k]) == 1] for k in range(9)]

    # Fait une liste de listes de positions des cases vides qui ont plusieurs chiffres manquants
    multiple = [[empty[k][i] for i in range(len(empty[k])) if len(missing[k]) > 1] for k in range(9)]
    return missing, empty, single, multiple

def pos_number(missing,empty,single,multiple,puzzle):
    empty = [[(k, i) for i in range(9) if puzzle[k][i] == 0] for k in range(9)]
    # print(empty)
    # Remplit les cases vides qui ont un seul chiffre manquant
    # for k in range(9):
    #     for i in range(len(single[k])):
    #         puzzle[single[k][i][0]][single[k][i][1]] = missing[k][0]

    # Remplit les cases vides qui ont
    for k in range(9):
        for i in range(len(multiple[k])):
            for j in range(len(missing[k])):
                if missing[k][j] not in [puzzle[multiple[k][i][0]][j] for j in range(9)] and missing[k][j] not in [puzzle[j][multiple[k][i][1]] for j in range(9)]:
                    puzzle[multiple[k][i][0]][multiple[k][i][1]] = missing[k][j]
                    break
    return puzzle

# print(puzzle)
print(sudoku(puzzle))
# sudoku(puzzle)