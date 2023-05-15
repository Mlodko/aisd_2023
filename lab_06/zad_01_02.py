from math import floor
import random


class Color:
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


class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        if self.parent is None:
            self.depth = 1
        else:
            self.depth = self.parent.depth + 1

        self.left = left
        self.right = right

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        else:
            return False

    def __le__(self, other):
        if self.value <= other.value:
            return True
        else:
            return False

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def print(self, length=0):
        for _ in range(self.depth):
            length += 1
            print('-', end='')
        print("%.2f" % self.value, end='')
        length += len("%.2f" % self.value)

        if self.left is not None:
            self.left.print(length)
            return
        else:
            print()  # Newline f"Newline {Color.BLUE} #1 {Color.END} called by node {self.value}"

        if self.right is not None:
            for _ in range(length):
                print(' ', end='')
            self.right.print(length)
            return
        print()  # Newline f"Newline {Color.RED} #2 {Color.END} called by node {self.value}"

    def minimum(self):
        checked = self
        while checked.left is not None:
            checked = checked.left
        return checked

    def maximum(self):
        checked = self
        while checked.right is not None:
            checked = checked.right
        return checked

    def search(self, value):
        current = self
        if current.is_leaf() or current.value == value:
            return current
        if current.left is not None and value < current.value:
            return current.left.search(value)
        elif current.right is not None:
            return current.right.search(value)


def insert(root, val, prev=None):
    if root is None:
        return TreeNode(val, parent=prev)
    if val <= root.value:
        root.left = insert(root.left, val, root)
    else:
        root.right = insert(root.right, val, root)
    return root


def add_node(node_value, trunk_list):
    node_value = round(node_value, 2)
    # Trunk 0,5 zajmuje się liczbami z zakresu [0,1), trunk 1,5 - [1,2) itd
    trunk_value = floor(node_value) + 0.5
    if trunk_list:
        for existing_trunk in trunk_list:
            if existing_trunk is not None and existing_trunk.value == trunk_value:
                insert(existing_trunk, node_value)
                return
    trunk_element = TreeNode(trunk_value)
    trunk_list.append(trunk_element)
    sort_trunk_list(trunk_list)
    insert(trunk_element, node_value)


def sort_trunk_list(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    i, j = l, r
    pivot = arr[(l + r) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if l < j:
        sort_trunk_list(arr, l, j)
    if r > i:
        sort_trunk_list(arr, i, r)


def find_trunk(trunk_list, value):
    for trunk_element in trunk_list:
        if trunk_element.value == floor(value) + 0.5:
            return trunk_element
    return None


testing = False
if testing:
    element_count = 1000
    trunks = []
    elements = []
    for _ in range(element_count):
        while True:
            to_add = round(random.random() * 99.0, 2)
            if to_add not in elements:
                break
        elements.append(to_add)
        add_node(to_add, trunks)

    for trunk in trunks:
        trunk.print()
        print(Color.PURPLE + f"Minimum: {trunk.minimum().value}")
        print(Color.YELLOW + f"Maximum: {trunk.maximum().value}" + Color.END)
        print("\n")

    for num in sorted(elements):
        num = round(num, 2)
        error = False
        try:
            find_trunk(trunks, num).search(num)
            if error:
                print(Color.GREEN + f"Found element {num} in node" + Color.END, find_trunk(trunks, num).search(num))
        except AttributeError:
            print(Color.RED + f"☠ Element {num} not found" + Color.END)
            error = True

    if not error:
        print(Color.GREEN + "✓ All elements have successfully been found" + Color.END)