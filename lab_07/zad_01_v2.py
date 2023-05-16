from source_manager import Color
import source_manager
import time as t

PATTERN = ['A', 'B', 'C', 'B', 'C']
FILES = ['./patterns/1000_pattern.txt', './patterns/2000_pattern.txt', './patterns/3000_pattern.txt',
         './patterns/4000_pattern.txt', './patterns/5000_pattern.txt', './patterns/8000_pattern.txt']

times = []
results = []
for file in FILES:
    result = []
    start = t.time()
    lines = source_manager.load_from_source(file)
    print(f'Checking file {file}')
    for y in range(len(lines) - 2):
        for x in range(len(lines[y]) - 2):
            if lines[y][x] == 'A' and lines[y][x+1] == 'B' and lines[y][x+2] == 'C' and lines[y+1][x] == 'B' and lines[y+2][x] == 'C':
                print(Color.GREEN, f"Found pattern at ({y}, {x})", Color.END)
                result.append((y,x))
    time = t.time() - start
    times.append(time)
    for r in result:
        print(f"  - {r}")
    print(Color.PURPLE, f"Found {len(result)} matches at coordinates in {time} s:", Color.END)
    results.append(len(result))
print(Color.YELLOW, f"Times: {times}", Color.END)
print(Color.YELLOW, f"Results: {results}", Color.END)