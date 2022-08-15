import numpy as np


def rotate(matrix):
    return list(reversed(list(zip(*matrix))))


def snail(snail_map):
    path = []

    def trace(submatrix):
        if not submatrix:
            return
        path.extend(submatrix[0])
        print(path)
        trace(rotate(submatrix[1:]))
    
    trace(snail_map)
    return path


def snail_2(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


def snail_3(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []