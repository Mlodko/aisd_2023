#Zad 2
class color:
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

import csv 
file = open('zadanie2.csv', newline='')
file_edit = open('zadanie2_edit.csv', 'w', newline='')
writer = csv.writer(file_edit)
reader = csv.reader(file)

data = [row for row in reader]
data = sorted(data, key=lambda x: int(x[0]) if x[0].isdigit() else 0)
file.close()

previous = None
for item in data:
    if previous and item[0].isdigit() and previous[0].isdigit() and int(item[0]) != int(previous[0]) + 1:
        item[0] = str(int(previous[0]) + 1)
    previous = item

for row in data:
    if(row[1] == ''):
        print(color.CYAN + 'Skipping row:', row)
        continue
    else:
        for item in row:
            item = item.lower()
            if(item.isdigit()):
                continue
            else:
                words = item.split()
                for word in words:
                    if(len(word) > 1 and abs(ord(word[0]) - ord(word[1])) == 1):
                        words.remove(word)
                        print(color.RED + 'Removing word:', word, "of 'id':", row[0])
                item = ' '.join(words)

        print(color.GREEN + 'Writing row:', row)
        writer.writerow(row)

file_edit.close()
