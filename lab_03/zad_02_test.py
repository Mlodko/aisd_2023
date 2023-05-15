import zad_02_module as shapes 

circle = shapes.circle(4)
print(f'Area of circle of radius {circle.radius}: {circle.area()}')
print(f'Perimeter of circle of radius {circle.radius}: {circle.perimeter()}')

triangle = shapes.triangle(3, 4, 5, 4)
print(f'Area of triangle with sides {triangle.a}, {triangle.b}, {triangle.c} and height {triangle.height_a}: {triangle.area()}')
print(f'Perimeter of the triangle: {triangle.perimeter()}')

square = shapes.square(5)
print(f'Area of square with side length {square.side_len}: {square.area()}')
print(f'Perimeter of square with side length {square.side_len}: {square.perimeter()}')