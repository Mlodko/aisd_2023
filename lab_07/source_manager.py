class Color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


def load_from_source(source_path):
    f = open(source_path, 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    f.close()
    return lines

def load_hashes(hash_file_path):
    with open(hash_file_path, 'r') as f:
        hash_string = f.read()
    return hash_string

# print(load_hashes('./hashes/'))