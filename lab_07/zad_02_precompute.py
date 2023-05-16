import source_manager
import os
import glob

P = 17
M = 10**9 + 9
FILE_NUMBERS = [1000]
FILES = [f'./patterns/{FILE_NUMBERS[i]}_pattern.txt' for i in range(len(FILE_NUMBERS))]


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    print ("\033[A                             \033[A")
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def hash(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value += ord(string[i]) * (P ** i)
    return hash_value % M


def precompute_hashes(lines):
    hashes = []
    total_hashes = (len(lines) - 2) ** 2
    iteration = 0
    for y in range(len(lines) - 2):
        iteration += 1
        if iteration % 1000 == 0:
            print(f'{iteration}/{total_hashes} done')
        #printProgressBar(y, total_hashes)
        for x in range(len(lines[y]) - 2):
            to_hash = lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y+1][x] + lines[y+2][x]
            #print(to_hash)
            hashes.append(f'{y}, {x}, {hash(to_hash)}')
    return hashes

# To precompute manually run this function
def hash_files():
    # Create directory for hashes
    if not os.path.exists('./hashes'):
        os.makedirs('./hashes')
    else:
        print("Hash directory exists, clearing it's contents")
        for f in glob.glob('./hashes/*'):
            print('Deleting file ' + f)
            os.remove(f)

    print(FILES)
    # Load patterns
    for i in range(len(FILES)):
        print(f'Precomputing hashes for file {FILES[i]}')
        lines = source_manager.load_from_source(FILES[i])
        print(f'Loaded file {FILES[i]}')
        hashes = precompute_hashes(lines)
        print(f'Precomputing hashes complete')
        hash_file = open(f'./hashes/{FILE_NUMBERS[i]}_hashes.txt', 'w')
        for i in range(len(hashes)):
            #printProgressBar(i, len(hashes))
            hash_file.write(str(hashes[i]) + '\n')
        hash_file.close()

#hash_files()


