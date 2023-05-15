import math 

def pierwiastek(n):
    try:
        return math.sqrt(n)
    except ValueError:
        return 'brak'
    
print(math.sqrt('abc'))