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
                edited_line.append(round(edited_line[-2] / (edited_line[1] * edited_line[2]), 5))  # Add value/area ratio
                data.append(tuple(edited_line))                
    except FileExistsError:
        print("Couldn't find file with path {path}")
    return data 


def if_area_free(matrix, anchor, width, height):
    # Check if area exists
    if anchor[0] + width >= len(matrix) or anchor[1] + height >= len(matrix):
        return False
    # Check if area is free
    for x in range(width):
        for y in range(height):
            if matrix[anchor[1] + y][anchor[0] + x] != 0:
                return False
    return True


def find_empty(matrix, matrix_size):
    for y in range(matrix_size):
        for x in range(matrix_size):
            if matrix[y][x] == 0:
                return [x, y]
                

def print_matrix(matrix):
    #for matrix_line in matrix:
    #    for thing_id in matrix_line:
    #        print(f"{thing_id}\t", end='')
    #    print()
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def split_matrix(matrix, top_left_pos, bottom_right_pos):
    (x_min, y_max) = top_left_pos
    (x_max, y_min) = bottom_right_pos
    important_xes = [0, x_min, x_max, len(matrix[0])]
    important_ys = [0, y_min, y_max, len(matrix)]

    # Split matrix into 8 parts (9-1 because don't include the thingamagick)
    matrices = []
    for i in range(1, len(important_xes)):
        for j in range(1, len(important_ys)):
            if i != 2 or j != 2:
                submatrix = []
                for y in range(important_ys[j - 1], important_ys[j]):
                    matrix_line = []
                    for x in range(important_xes[i - 1], important_xes[i]):
                        matrix_line.append(matrix[y][x])
                    submatrix.append(matrix_line)
                matrices.append(submatrix)
    return matrices


def main():
    left_top = (13, 6)
    right_bottom = (16, 9)

    matrix = []
    # Generate empty matrix
    for y in range(20):
        matrix_line = []
        for x in range(20):
            matrix_line.append((x, y))
        matrix.append(matrix_line)
    print_matrix(matrix)
    print()
    for m in enumerate(split_matrix(matrix, left_top, right_bottom)):
        print(f"Matrix {m[0]}:")
        print(m[1])
        print()

def mainn():
    for matrix_size in MATRIX_SIZES:
        matrix_area = matrix_size ** 2
        matrix = []
        # Generate empty matrix
        for _ in range(matrix_size):
            matrix_line = []
            for __ in range(matrix_size):
                matrix_line.append(0)
            matrix.append(matrix_line)

        # Load and sort data
        data = sorted(load_data(matrix_size), reverse = True, key = lambda x: x[-1]) # Sorted by value/area ratio
        occupied_space = 0
        for thing in data:
            # Check if there is enough space to place the thing
            if occupied_space + (thing[1] * thing[2]) > matrix_area:
                print(f"Mathematically can't fit thing of id {thing[0]} due to lack of space")
                break

            # Find an empty space
            anchor = find_empty(matrix, matrix_size)

            # Check horizontal
            if thing[1] >= thing[2] and if_area_free(matrix, anchor, thing[1], thing[2]):  # If width > height
                print(f"Placing thing of id {thing[0]} in position {anchor}")
                # Change the area into ids
                for x in range(thing[1]):
                    for y in range(thing[2]):
                        matrix[anchor[1] + y][anchor[0] + x] = thing[0]
            elif if_area_free(matrix, anchor, thing[2], thing[1]):
                print(f"Placing thing of id {thing[0]} in position {anchor}")
                # Change the area into ids
                for x in range(thing[2]):
                    for y in range(thing[1]):
                        matrix[anchor[1] + y][anchor[0] + x] = thing[0]
            else:
                print(f"Can't find place for thing of id {thing[0]}")
            print_matrix(matrix)
            input()

        for matrix_line in matrix:
            print(matrix_line)
            



if __name__ == '__main__':
    main()