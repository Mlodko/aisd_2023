from zad_02_precompute import hash
from zad_02_precompute import FILE_NUMBERS
from zad_02_precompute import FILES
import source_manager
from source_manager import Color
import time as t


PATTERN = 'ABCBC'
#pattern_hash = hash(PATTERN)
#print(f'Pattern hash: {pattern_hash}')
TIMES = []
RESULTS = []


for i in range(len(FILE_NUMBERS)):
    result = []
    hashes = source_manager.load_hashes(f'./hashes/{FILE_NUMBERS[i]}_hashes.txt')
    print(f'Loaded hashes from file {FILE_NUMBERS[i]}_hashes.txt')
    lines = source_manager.load_from_source(FILES[i])
    print(f'Loaded file {FILES[i]}')
    print(f'Checking file {FILES[i]}')
    start = t.time()
    for k in range(len(hashes)):
        y = k // (FILE_NUMBERS[i] - 2)
        x = k % (FILE_NUMBERS[i] - 2)
        if int(hashes[k]) == 1:
            print(Color.YELLOW, f"Hash match at ({y}, {x})", Color.END)
            if lines[y][x] == 'A' and lines[y][x+1] == 'B' and lines[y][x+2] == 'C' and lines[y+1][x] == 'B' and lines[y+2][x] == 'C':
                print(Color.GREEN, f"Found pattern at ({y}, {x})", Color.END)
                result.append((y,x))
    TIMES.append(t.time() - start)
    RESULTS.append(len(result))
    for r in result:
        print(f"  - {r}")


print(TIMES)