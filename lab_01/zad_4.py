l = [1,2,3]
try:
    print(l[1000])
except IndexError:
    print("IndexError caught")

try:
    print(1//0)
except ZeroDivisionError:
    print("ZeroDivisionError caught")

try:
    print(a[2000])
except NameError:
    print("NameError caught")
