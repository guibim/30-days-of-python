
#INTEGER OPERATORS
print('Addition: ', 3 + 3)
print('Subtraction: ', 3 - 3)
print('Multiplication: ', 3 * 3)
print('Division: ', 3 / 3) # Division in python gives floating number
print('Division: ', 7/ 2)
print('Division with the remainder: ', 7 // 2) # gives without the floating number or without the remaining
print('Modulus: ', 7 % 2) #Remainder of the division
print('Division without the remainder: ', 8 // 2)
print('Exponent: ', 3 ** 3) # 3 to the power of 3 means 3*3*

#Floating number operators
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

#Complex
print('Complex number: ', 1 + 2j)
print('Multiply complex number: ', (1 + 2j) * (1 - 2j))

#Var declarations always on the top
a = 3
b = 2 

#Operators and assignments
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponent = a ** b

print('a +  b = ', total)
print('a -  b = ', diff)
print('a *  b = ', product)
print('a /  b = ', division)
print('a %  b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponent)

num_one = 3
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two

print('Total: ', total)
print('Difference: ', diff)
print('Product: ', product)
print('Division: ', division)
print('Remainder: ', remainder)

#Area of a Circle
radius = 30
area_of_circle = 3.14 * radius ** 2
print('Area of a circle with radius 30m: ', area_of_circle, 'm2')

#Area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle, 'm2')

#Calcule a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print('Weight of an object:', weight, 'N')

print (3 > 2) #True
print (3 >= 2) #True
print (3 < 2) #False
print (2 < 3) #True
print (2 <= 3) #True
print (3 == 2) #False
print (3 != 2) #True
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

#Boolean comparison
print('True == True: ', True == True) 
print('False == False: ', False == False) 
print('True == False: ', True == False) 
print('True != False: ', True != False) 
print('True and True: ', True and True)

#Another way of comparing
print('1 is 1: ', 1 is 1)
print('1 is not 2: ', 1 is not 2)
print('A is Guilherme', 'A' in 'Guilherme')
print('B is not in Guilherme', 'B' not in 'Guilherme')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2', 4 is 2 ** 2)

print(3 > 2 and 4 > 3) #True
print(3 > 2 and 4 < 3) #False
print(3 < 2 and 4 < 3) #False
print(3 > 2 or 4 > 3) #True
print(3 > 2 or 4 < 3) #True
print(3 < 2 or 4 < 3) #False
print(not 3 > 2) #False
print(not 3 < 2) #True
print(not True) #False
print(not False) #True
print(not not True) #True
print(not not False)   #False

age = 26
height_float = 1.80
complex = 1 + 1j

print('Type Base and Height of a triangle:')
base = float(input('Base: '))
height_triangle = float(input('Height: '))
area_of_triangle = 0.5 * base * height_triangle
print('Area of triangle is: ' , area_of_triangle)

print('Type 3 sides of a triangle')
a_side = float(input('A_side: '))
b_side = float(input('B_side:  '))
c_side = float(input('C_side: '))
print('The perimeter of triangle is', a_side + b_side + c_side)

