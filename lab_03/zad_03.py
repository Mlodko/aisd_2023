import random
import math 
from numpy import linspace
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class rectangle:
    def __init__(self, bottom_left, top_right):
        self.bl = bottom_left
        self.br = (top_right[0], bottom_left[1])
        self.tl = (bottom_left[0], top_right[1])
        self.tr = top_right
        self.height = self.tl[1] - self.bl[1] 
        self.width = self.br[0] - self.bl[0]

    def area(self):
        return self.height * self.width

def find_rectangle(start_x, finish_x, function):
    if(start_x > finish_x):
        raise Exception('Bad integral limits, start>finish')
    values = []
    for x in linspace(start_x, finish_x, 100):
        values.append(function(x))
    return rectangle((start_x, min(values)), (finish_x, max(values)))

def monte_carlo(function, left_x, right_x, sample_size):
    rect = find_rectangle(left_x, right_x, function)
    hit_count = 0
    rand_hit_x = []
    rand_hit_y = []
    rand_miss_x = []
    rand_miss_y = []
    func_x = linspace(left_x, right_x, 100)
    func_y = [function(x) for x in func_x]
    for i in range(sample_size):
        check_pos = (random.random() * rect.width + rect.bl[0], random.random() * rect.height + rect.bl[1])
        func_value = function(check_pos[0])

        if func_value >= 0:
            if check_pos[1] <= func_value and check_pos[1] >= 0:
                rand_hit_x.append(check_pos[0])
                rand_hit_y.append(check_pos[1])
                hit_count += 1
            else: 
                rand_miss_x.append(check_pos[0])
                rand_miss_y.append(check_pos[1])
        else:
            if check_pos[1] >= func_value and check_pos[1] <= 0:
                rand_hit_x.append(check_pos[0])
                rand_hit_y.append(check_pos[1])
                hit_count += 1
            else: 
                rand_miss_x.append(check_pos[0])
                rand_miss_y.append(check_pos[1])


        #if(check_pos[1] <= func_value):
        #    rand_hit_x.append(check_pos[0])
        #    rand_hit_y.append(check_pos[1])
        #    hit_count += 1
        #else:
        #    rand_miss_x.append(check_pos[0])
        #    rand_miss_y.append(check_pos[1])

    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.add_patch(Rectangle(rect.bl, rect.width, rect.height, edgecolor = 'purple', facecolor= 'none', lw = 2))
    ax.scatter(rand_hit_x, rand_hit_y, s = 1, c = '#0000FF')
    ax.scatter(rand_miss_x, rand_miss_y, s = 1, c = '#FF0000')
    ax.plot(func_x,func_y, c = '#00FF00', linewidth=2)
    plt.show()

    hit_ratio = hit_count/sample_size 
    print(f"Stosunek punktów pod wykresem do wszystkich: {hit_ratio}")
    return rect.area() * hit_ratio

integral_sin = monte_carlo(lambda x: math.log(abs(x)), 1, 10, 1_000_000)
print(integral_sin)

# x^2 + y^2 = r^2
# y = +/-sqrt(r^2 - x^2)
r = float(input('Radius of the circle: '))
integral_circ = 2 * monte_carlo(lambda x: math.sqrt(r**2 - x**2),-r , r, 10_000)
print(integral_circ)
print(f'Theoretical area of circle: {math.pi * r**2}')