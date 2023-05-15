import time
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
text = input("Podaj tekst: ")

start_time = time.time()
file = open('SJP.txt', 'r')
sjp = file.read().splitlines()
print(color.PURPLE + "Otwieranie SJP.txt:", time.time() - start_time)


start_time = time.time()
if ' ' in text:
    print(color.RED + "Nie jeden wyraz")
else:
    print(color.GREEN + "Jeden wyraz")
print(color.PURPLE + "Sprawdzanie czy jeden wyraz:", time.time() - start_time)

start_time = time.time()
text = text.lower()
print(color.PURPLE + "Zmiana na małe litery:", time.time() - start_time)

start_time = time.time()
if text in sjp:
    print(color.GREEN + "Wyraz jest słowem z SJP")
else:
    print(color.RED + "Wyraz nie jest słowem z SJP")
print(color.PURPLE + "Sprawdzanie czy słowo jest w SJP:", time.time() - start_time)

# Wniosek:  SJP.txt jest bardzo duże i otwieranie go zajmuje dużo czasu.
#           Aby zmniejszyć czas przetwarzania można podzielić SJP.txt 
#           na mniejsze pliki (Np jeden plik na jedną literę rozpoczynającą wyraz)
#           i sprawdzać czy wyraz jest w danym pliku.