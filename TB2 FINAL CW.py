# Grids 1-4 are 2x2
grid1 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [0, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 2, 3, 4],
    [2, 1, 4, 3],
    [3, 4, 2, 1],
    [4, 3, 1, 2]]
grid4 = [
    [1, 3, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]



# Grids 4-7 are 3x3
grid5 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, ],
    [2, 3, 4, 5, 6, 7, 8, 9, 1, ],
    [3, 4, 5, 6, 7, 8, 9, 1, 2, ],
    [4, 5, 6, 7, 8, 9, 1, 2, 3, ],
    [5, 6, 7, 8, 9, 1, 2, 3, 4, ],
    [6, 7, 8, 9, 1, 2, 3, 4, 5, ],
    [7, 8, 9, 1, 2, 3, 4, 5, 6, ],
    [8, 9, 1, 2, 3, 4, 5, 6, 7, ],
    [9, 1, 2, 3, 4, 5, 6, 7, 8, ]]

grid6 = [
    [6, 1, 7, 8, 4, 2, 5, 3, 9, ],
    [7, 4, 5, 3, 6, 9, 1, 8, 2, ],
    [8, 3, 2, 1, 7, 5, 4, 6, 9, ],
    [1, 5, 8, 6, 9, 7, 3, 2, 4, ],
    [9, 6, 4, 2, 3, 1, 8, 7, 5, ],
    [2, 7, 3, 5, 8, 4, 6, 9, 1, ],
    [4, 8, 7, 9, 5, 6, 2, 1, 3, ],
    [3, 9, 1, 4, 2, 8, 7, 5, 6, ],
    [5, 2, 6, 7, 1, 3, 9, 4, 8, ]]

grid7 = [
    [6, 1, 9, 8, 4, 2, 5, 3, 7, ],
    [7, 4, 5, 3, 6, 9, 1, 8, 2, ],
    [8, 3, 2, 1, 7, 5, 4, 6, 9, ],
    [1, 5, 8, 6, 9, 7, 3, 2, 4, ],
    [9, 6, 4, 2, 3, 1, 8, 7, 5, ],
    [2, 7, 3, 5, 8, 4, 6, 9, 1, ],
    [4, 8, 7, 9, 5, 6, 2, 1, 3, ],
    [3, 9, 1, 4, 2, 8, 7, 5, 6, ],
    [5, 2, 6, 7, 1, 3, 9, 4, 8, ]]

# grids 8-10 are 2x3
grid8 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grid9 = [
    [1, 2, 6, 5, 4, 3],
    [5, 3, 4, 6, 2, 1],
    [6, 1, 3, 4, 5, 2],
    [2, 5, 5, 3, 1, 6],
    [4, 6, 1, 2, 3, 5],
    [3, 5, 2, 1, 6, 4]]

grid10 = [
    [1, 2, 6, 5, 4, 3],
    [5, 3, 4, 6, 2, 1],
    [6, 1, 3, 4, 5, 2],
    [2, 4, 5, 3, 1, 6],
    [4, 6, 1, 2, 3, 5],
    [3, 5, 2, 1, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2),
         (grid5, 3, 3), (grid6, 3, 3), (grid7, 3, 3),
         (grid8, 2, 3), (grid9, 2, 3), (grid10, 2, 3)]

expected_outputs = [False, False, False, True, False, False, True, False, False, True]

'''The is_correct functions for each respective grids, firstly checks whether all the values in each grid
 are unique and agree with the rules of sudoku for each size of each grid, then each respective is_correct 
 function checks whether each column, row and subgrid contains all unique values.'''

'''The check_sudoku fucntion uses all respective is_correct fucntions to check all grids and output 10 boolean
values inidcating whether each grid is correct or not'''

def check_solution(grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10):
    def is_correct_9x9(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
        for i in range(9):
            row = set(grid[i])
            col = set([grid[j][i] for j in range(9)])
            if len(row) != 9 or len(col) != 9:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = set([grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)])
                if len(sub_grid) != 9:
                    return False
        return True

    def is_correct_4x4(grid):
        for i in range(4):
            for j in range(4):
                if grid[i][j] not in [1, 2, 3, 4]:
                    return False
        for i in range(4):
            row = set(grid[i])
            col = set([grid[j][i] for j in range(4)])
            if len(row) != 4 or len(col) != 4:
                return False
        for i in [0, 2]:
            for j in [0, 2]:
                sub_grid = [(grid)[x][y] for x in range(i, i+ 2) for y in range(j, j + 2)]
                if len(set(sub_grid)) != 4:
                    return False
        return True
    def is_correct_6x6(grid):
        for i in range(6):
            for j in range(6):
                if grid[i][j] not in [1, 2, 3, 4, 5, 6]:
                    return False
        for i in range(6):
            row = set(grid[i])
            col = set([grid[j][i] for j in range(6)])
            if len(row) != 6 or len(col) != 6:
                return False
        for i in range(0, 6, 2):
            for j in range(0, 6, 3):
                sub_grid = set([grid[x][y] for x in range(i, i+2) for y in range(j, j+3)])
                if len(sub_grid) != 6:
                    return False
        return True




    return [is_correct_4x4(grid1), is_correct_4x4(grid2), is_correct_4x4(grid3), is_correct_4x4(grid4),
            is_correct_9x9(grid5), is_correct_9x9(grid6), is_correct_9x9(grid7), is_correct_6x6(grid8),
            is_correct_6x6(grid9), is_correct_6x6(grid10)]
print(check_solution(grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10))