import zad_01_02 as z1
from zad_01_02 import Color
from math import floor
import random
import time as t



class Times:
    def __init__(self):
        self.max = []
        self.min = []
        self.search = []
        self.insert = []


def add_node(node_value, trunk_list):
    global times
    trunk_value = floor(node_value) + 0.5
    if trunk_list:
        for existing_trunk in trunk_list:
            if existing_trunk is not None and existing_trunk.value == trunk_value:
                start = t.time()
                z1.insert(existing_trunk, node_value)
                end = t.time()
                times.insert.append(end - start)
                return
    trunk_element = z1.TreeNode(trunk_value)
    trunk_list.append(trunk_element)
    z1.sort_trunk_list(trunk_list)
    start = t.time()
    z1.insert(trunk_element, node_value)
    end = t.time()
    times.insert.append(end - start)


def avg(arr):
    return sum(arr) / len(arr)


node_counts = [25, 50, 100, 500, 1000]
trunks = []
values = []
times = Times()
times_list = []

for node_count in node_counts:
    for _ in range(node_count):
        while True:
            to_add = round(random.random() * 99.0, 2)
            if to_add not in values:
                break
        values.append(to_add)
        add_node(to_add, trunks)

    print(times.insert)
    print(avg(times.insert))

    for trunk in trunks:
        #print(trunk.value)

        start = t.time()
        max = trunk.maximum()
        end = t.time()
        times.max.append(end - start)

        start = t.time()
        min = trunk.minimum()
        end = t.time()
        times.min.append(end - start)

        print(Color.PURPLE + f"Minimum: {max.value}")
        print(Color.YELLOW + f"Maximum: {min.value}" + Color.END)

    print(times.max)
    print(avg(times.max))

    print(times.min)
    print(avg(times.min))

    for num in values:
        num = round(num, 2)
        error = False
        try:
            start = t.time()
            found = z1.find_trunk(trunks, num).search(num)
            end = t.time()
            times.search.append(end - start)
            if error:
                print(Color.GREEN + f"Found element {num} in node" + Color.END, found)
        except AttributeError:
            print(Color.RED + f"☠ Element {num} not found" + Color.END)
            error = True

    if not error:
        print(Color.GREEN + "✓ All elements have successfully been found" + Color.END)

    print(times.search)
    print(avg(times.search))
