import time as t
from copy import deepcopy
MATRIX_SIZES = [20] #, 100, 500, 1000]

def load_data(matrix_size):
    path = f"./packages/packages{matrix_size}.txt"
    data = []
    try:
        with open(path, 'r') as f:
            for line_enum in enumerate(f):
                if line_enum[0] < 2:
                    continue
                edited_line = [int(i) for i in line_enum[1].strip().split(",")]
                edited_line.append(round(edited_line[-2] / (edited_line[1] * edited_line[2]), 5))
                data.append(tuple(edited_line))                
    except FileExistsError:
        print("Couldn't find file with path {path}")
    return data

def top_n(to_sort, sort_key, if_reverse, n):
    return sorted(deepcopy(to_sort), key=sort_key, reverse=if_reverse)[:n]

def if_area_free(matrix, anchor, width, height):
    # Check if area exists
    if anchor[0] + width >= len(matrix) or anchor[1] + height >= len(matrix):
        return False
    # Check if area is free
    for x in range(1, width):
        for y in range(1, height):
            if matrix[anchor[1] + y][anchor[0] + x] != 0:
                return False
    return True

def find_empty(matrix, matrix_size):
    for x in range(matrix_size):
                for y in range(matrix_size):
                    if matrix[y][x] == 0:
                        return [x, y]


def main():
    for matrix_size in MATRIX_SIZES:
        matrix_area = matrix_size ** 2
        matrix = []
        for _ in range(matrix_size):
            matrix_line = []
            for __ in range(matrix_size):
                matrix_line.append(0)
            matrix.append(matrix_line)
        data = top_n(load_data(matrix_size), n=matrix_size, if_reverse=True, sort_key=lambda x: x[-1]) # Sorted by value/area ratio
        occupied_space = 0
        for thing in data:
            if occupied_space + (thing[1] * thing[2]) > matrix_area:
                print(f"Mathematically can't fit thing of id {thing[0]} due to lack of space")
                break

            # Find an empty space
            checked_anchor = find_empty(matrix, matrix_size)

            
            # Check horizontal
            if thing[1] >= thing[2] and if_area_free(matrix, checked_anchor, thing[1], thing[2]):  # If width > height
                print(f"Placing thing of id {thing[0]} in position {checked_anchor}")
                # Change the area into ids
                for x in range(thing[1]):
                    for y in range(thing[2]):
                        matrix[y][x] = thing[0]
            elif if_area_free(matrix, checked_anchor, thing[2], thing[1]):
                print(f"Placing thing of id {thing[0]} in position {checked_anchor}")
                # Change the area into ids
                for x in range(thing[2]):
                    for y in range(thing[1]):
                        matrix[y][x] = thing[0]
            else:
                print(f"Can't find place for thing of id {thing[0]}")

                
                            


        
        for matrix_line in matrix:
            print(matrix_line)
            



if __name__ == '__main__':
    main()