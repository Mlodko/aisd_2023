from zad_1 import move


def possible_move(src, dest):
    if len(src) == 0:
        possible_move(dest, src)
        return
    if len(dest) > 0:
        if src[-1] < dest[-1]:
            move(src, dest)
        else:
            move(dest, src)
    else:
        move(src, dest)


def hanoi_iter(src, dest, buff):
    steps = []
    i = 1
    while len(src) != 0 or len(buff) != 0:
        if i % 3 == 1:
            possible_move(src, dest)
        elif i % 3 == 2:
            possible_move(src, buff)
        else:
            possible_move(buff, dest)
        print(f"""Iteracyjnie (i = {i}:
    Source: {src}
    Buffer: {buff}
    Destination: {dest}""")
        i += 1
