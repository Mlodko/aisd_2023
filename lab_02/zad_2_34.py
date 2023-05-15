#Zad 2.3 i 2.4
import csv
file = open('zadanie2.csv', newline='')
file_edit = open('zadanie2_edit.csv', 'w', newline='')

reader = csv.reader(file)
writer = csv.writer(file_edit)

data = [row for row in reader]
data = sorted(data, key=lambda x: int(x[0]) if x[0].isdigit() else 0)

previous = None
for item in data:
    if previous and item[0].isdigit() and previous[0].isdigit() and int(item[0]) != int(previous[0]) + 1:
        item[0] = str(int(previous[0]) + 1)
    previous = item
    writer.writerow(item)
    
print("Done")
file.close()
file_edit.close()