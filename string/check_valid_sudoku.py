
import numpy as np



def define_tile_of_point(x,y):

    if x in range(3) and y in range(3):
        return 'Tile 1'
    if x in range(3) and y in range(3,6):
        return 'Tile 2'
    if x in range(3) and y in range(6,9):
        return 'Tile 3'
    
    if x in range(3,6) and y in range(3):
        return 'Tile 4'    
    if x in range(3,6) and y in range(3,6):
        return 'Tile 5'    
    if x in range(3,6) and y in range(6,9):
        return 'Tile 6'
    
    if x in range(6,9) and y in range(3):
        return 'Tile 7'
    if x in range(6,9) and y in range(3,6):
        return 'Tile 8'
    if x in range(6,9) and y in range(6,9):
        return 'Tile 9'


def check_sudoku(arr):
    for i in range(1, 10):
        indices = np.argwhere(arr == i)
        list_tile = []
        x_axis = []
        y_axis = []

        for idx in indices:
            x, y = idx
            result = define_tile_of_point(x, y)

            if x in x_axis: 
                return 'Not a valid Sudoku'
            if y in y_axis: 
                return 'Not a valid Sudoku'
            if result in list_tile: # 3x3 tile
                return 'Not a valid Sudoku' 
            
            list_tile.append(result)
            x_axis.append(x)
            y_axis.append(y)

    return 'A valid Sudoku'


if __name__ == "__main__": 
    line = [list(map(int, list(s))) for s in input().split()] ## stdin with each line including 9 digits with no space, and separator between lines can be space or tab, new line
    arr = np.reshape(line, (9,9))

    print(check_sudoku(arr))



    



    
    
    
