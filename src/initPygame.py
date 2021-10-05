# import pygame
from numpy import zeros, loadtxt, int32, array
from numba import jit
from time import process_time
from src.functions import cell
width   = 500
height  = 500
n1      = 9
n2      = n1
# screen  = pygame.display.set_mode((width, height))


def updateWindow():
    pygame.display.update()

@jit(nopython=True)
def solved():
    global sudoku
    for i in range(n1):
        if 0 in sudoku[i]:
            return False
    return True

@jit(nopython=True)
def avaiable(sudoku, n, row, col):
    for j in range(9):
        if n==sudoku[row, j] and j!=col:
            # print("1")
            return False
    for i in range(9):
        if n==sudoku[i][col] and i != row:
            # print("2")
            return False

    iCell   = row//3
    jCell   = col//3
    i1      = iCell*3
    i2      = iCell*3+1
    i3      = iCell*3+2
    j       = jCell*3
    for k in range(3):
        if j != col:
            if i1 == row:
                if n==sudoku[i2,j]:
                    # print("4")
                    return False
                if n==sudoku[i3,j]:
                    # print("5")
                    return False
            elif i2 == row:
                if n==sudoku[i1,j]:
                    # print("3")
                    return False
                if n==sudoku[i3,j]:
                    # print("5")
                    return False
            elif i3 == row:
                if n==sudoku[i1,j]:
                    # print("4")
                    return False
                if n==sudoku[i2,j]:
                    # print("5")
                    return False
        j  += 1
    return True

def backTracing(depth, zero, k):
    global sudoku, done
    if not done:
        # Solved
        if k == len(zero):
            done = True
            return sudoku

        # algorithm
        i   = zero[k,0]
        j   = zero[k,1]
        for n in range(1, 10):
            sudoku[i,j]   = n
            if avaiable(sudoku, n, i, j):
                sudoku    = backTracing(depth+1, zero, k+1)
                if done:
                    break
            sudoku[i,j] = 0
        return sudoku
    else:
        return sudoku
    # if sudoku[row, col] == 0:
    #     for n in range(1, 10):
    #         sudoku[row, col] = n
    #         if avaiable(sudoku, n, row, col):
    #             sudoku = backTracing(depth+1, sudoku, zero, k+1)
    #     sudoku[row, col] = 0
    #     print("no 9")
    #     print(sudoku)
    #     return sudoku
    #
    # else:
    #     sudoku = backTracing(depth+1, sudoku, zero, k+1)


def start():
    global sudoku, sudoku, done
    arr     = zeros(81, dtype=int32)
    tic     = process_time()
    print("# Reading sudoku..   ")
    arr     = loadtxt("sudoku.txt", delimiter = ' ', dtype=int32)
    sudoku  = array([arr[i*n1:(i+1)*n1] for i in range(n2)])
    print("# Time exoploited:   ", process_time()-tic)
    # pygame.init()
    # pygame.display.set_caption("SudokuSolver")
    # running = True
    print("# Starting sudoku:   ")
    print(sudoku)
    done    = False
    tic     = process_time()
    print("# Generating zeros array..")
    zero    = array([[i,j] for i in range(9) for j in range(9) if sudoku[i, j] == 0 ])
    print("# Time exoploited:   ", process_time()-tic)
    tic =process_time()
    sudoku = backTracing(0, zero, 0)
    print("# Solving time:      ", process_time()-tic)
    print("# Ending sudoku:   ")
    print(sudoku)
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

        # updateWindow()
