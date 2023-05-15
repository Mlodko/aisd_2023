def move(src, dest):
    try:
        dest.append(src[-1])
        src.pop(-1)
    except IndexError:
        return


def hanoi_rek(n, src, dest, buff):
    if n > 0 and (len(src) != 0 or len(buff) != 0):
        if n == 1:
            move(src, dest)
        hanoi_rek(n - 1, src, buff, dest)
        move(src, dest)
        hanoi_rek(n - 1, buff, dest, src)
    print(f"""Rekurencyjnie:
    Source: {src}
    Buffer: {buff}
    Destination: {dest}""")
