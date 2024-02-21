"""

Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width
and height, using a cost entered by the user.

"""

WIDTH = 1
HEIGHT = 2

surface_area = WIDTH * HEIGHT
price = float(input("Enter the price per square meter here: "))

total_cost = round(surface_area * price, 2)
print("The cost to cover a surface of width ", WIDTH, " and height ", HEIGHT, " is $", total_cost)