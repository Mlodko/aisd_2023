import random
import math 
import numpy as np
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
    for x in np.linspace(start_x, finish_x, 100):
        values.append(function(x))
    return rectangle((start_x, min(values)), (finish_x, max(values)))

def monte_carlo(function, left_x, right_x, sample_size):
    rect = find_rectangle(left_x, right_x, function)
    hit_count = 0
    rand_hit_x = []
    rand_hit_y = []
    rand_miss_x = []
    rand_miss_y = []
    func_x = np.linspace(left_x, right_x, 100)
    func_y = []
    for x in func_x:
        func_y.append(function(x))
    for i in range(sample_size):
        check_pos = (random.random() * rect.width + rect.bl[0], random.random() * rect.height + rect.bl[1])
        func_value = function(check_pos[0])
        if(check_pos[1] <= func_value):
            rand_hit_x.append(check_pos[0])
            rand_hit_y.append(check_pos[1])
            hit_count += 1
        else:
            rand_miss_x.append(check_pos[0])
            rand_miss_y.append(check_pos[1])

    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.add_patch(Rectangle(rect.bl, rect.width, rect.height, edgecolor = 'purple', facecolor= 'none'))
    ax.scatter(rand_hit_x, rand_hit_y, s = 1, c = '#0000FF')
    ax.scatter(rand_miss_x, rand_miss_y, s = 1, c = '#FF0000')
    ax.plot(func_x,func_y, c = '#00FF00')
    plt.show()

    hit_ratio = hit_count/sample_size 
    return rect.area() * hit_ratio

print(monte_carlo(lambda x: math.log2(abs(x)), -5, 12, 20_000))