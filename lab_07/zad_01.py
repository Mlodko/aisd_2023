import source_manager
from source_manager import Color
import time as t


PATTERN = ['A', 'B', 'C',
           'B', '' , '' ,
           'C', '' , ''  ]

FILES = ['./patterns/1000_pattern.txt', './patterns/2000_pattern.txt', './patterns/3000_pattern.txt',
         './patterns/4000_pattern.txt', './patterns/5000_pattern.txt', './patterns/8000_pattern.txt']

def check_pattern(source, pattern):
    for i in range(len(pattern)):
        if pattern[i] == '':
            continue
        elif pattern[i] != source[i]:
            return False
    return True


def get_square(source, x_pos, y_pos):
    square = []
    for y in range(y_pos, y_pos + 3):
        for x in range(x_pos, x_pos + 3):
            square.append(source[y][x])
    return square


def naive_pattern_search(source, pattern):
    lines = source_manager.load_from_source(source)
    for y in range(len(lines) - 2):
        for x in range(len(lines[y]) - 2):
            square = get_square(lines, x, y)
            #print(f"Checking square at {x}, {y}")
            if check_pattern(square, pattern):
                yield y, x

times = []
for file_path in FILES:
    print(Color.YELLOW, f"Checking file {file_path}", Color.END)
    start = t.time()
    results = naive_pattern_search(file_path, PATTERN)
    for result in results:
        print(Color.GREEN, 'Found pattern at', result, Color.END)
    times.append(t.time() - start)
print(times)