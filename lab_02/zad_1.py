# Zad 1.1
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
liczby = []
for i in range(500,3001):
    if i%7==0 and i%5!=0:
        liczby.append(i)

print(liczby)

#Zad 1.2
liczby_str = ''
for i in range(500,3001):
    if i%7==0 and i%5!=0:
        liczby_str += str(i)
print(liczby_str)

#Zad 1.3
liczby_xx = liczby_str.replace('21', color.RED + 'XX' + color.END)
print(liczby_xx)