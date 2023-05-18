import source_manager
import os
import glob

P = 17
M = 10**9 + 9
FILE_NUMBERS = [1000, 2000, 3000, 4000, 5000, 8000]
FILES = [f'./patterns/{FILE_NUMBERS[i]}_pattern.txt' for i in range(len(FILE_NUMBERS))]


'''
def hash(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value += ord(string[i]) * (P ** i)
    return hash_value % M
'''


def hash(string):
    # String postaci
    # 0 1 2
    # 3
    # 4
    if string[1] == string[3] and string[2] == string[4] and 'A' in string and 'B' in string and 'C' in string:
        return 1
    else:
        return 0


def precompute_hashes(lines):
    hashes = []
    for y in range(len(lines) - 2):
        for x in range(len(lines[y]) - 2):
            to_hash = lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y+1][x] + lines[y+2][x]
            #print(to_hash)
            hashes.append(hash(to_hash))
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
            hash_file.write(str(hashes[i]))
        hash_file.close()

hash_files()


