from zad_02_precompute import hash
from zad_02_precompute import FILE_NUMBERS
from zad_02_precompute import FILES
import source_manager
from source_manager import Color
import os


PATTERN = 'ABCBC'
pattern_hash = hash(PATTERN)
print(f'Pattern hash: {pattern_hash}')

for i in range(len(FILE_NUMBERS)):
    result = []
    hashes = source_manager.load_from_source(f'./hashes/{FILE_NUMBERS[i]}_hashes.txt')
    for j in range(len(hashes)):
        h = hashes[j]
        h = h.split(',')
        hashes[j] = (int(h[0]), int(h[1]), int(h[2]))
    print(f'Loaded hashes from file {FILE_NUMBERS[i]}_hashes.txt')
    lines = source_manager.load_from_source(FILES[i])
    print(f'Loaded file {FILES[i]}')

    print(f'Checking file {FILES[i]}')
    for h in hashes:
        y = h[0]
        x = h[1]
        if h[2] == pattern_hash:
            print(Color.YELLOW, f"Hash match at ({y}, {x})", Color.END)
            if lines[y][x] == 'A' and lines[y][x+1] == 'B' and lines[y][x+2] == 'C' and lines[y+1][x] == 'B' and lines[y+2][x] == 'C':
                print(Color.GREEN, f"Found pattern at ({y}, {x})", Color.END)
                result.append((y,x))
    for r in result:
        print(f"  - {r}")


