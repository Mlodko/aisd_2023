import glob
import os 

path = "./03-Modules-materials/zadanie1"
filename_list = os.listdir(path)
for filename in filename_list:
    starting_char = filename[0]
    file_path = os.path.join(path, filename)
    try:
        os.rename(file_path, os.path.join(path, starting_char, filename))
    except FileNotFoundError:
        os.mkdir(os.path.join(path, starting_char))
        os.rename(file_path, os.path.join(path, starting_char, filename))
