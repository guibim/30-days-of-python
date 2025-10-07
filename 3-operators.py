import math
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

#exc 1-2-3
age = 26
height_float = 1.80
complex = 1 + 1j

#exc 4
print('Type Base and Height of a triangle:')
base = float(input('Base: '))
height_triangle = float(input('Height: '))
area_of_triangle = 0.5 * base * height_triangle
print('Area of triangle is: ' , area_of_triangle)

#exc 5
print('Type 3 sides of a triangle')
a_side = float(input('A_side: '))
b_side = float(input('B_side:  '))
c_side = float(input('C_side: '))
print('The perimeter of triangle is', a_side + b_side + c_side)

#exc 6
print('Type a length and width of a rectangle')
type_rect_length = float(input('Rect_Length: '))
type_rect_width = float(input('Rect_Width: '))
print('Rectangle Length is', type_rect_length, 'Width is', type_rect_width)
rect_area =  type_rect_length * type_rect_width
print('Rectangle area is: ', rect_area)
rect_perimeter = 2 * (type_rect_length + type_rect_width) 
print('Rectangle perimeter is', rect_perimeter)

#exc 7
print('Type a radius of circle')
radius_circle = float(input('Circle Radius: '))
area_circle = 3.14 * radius_circle * radius_circle
circ_circle =  2 * 3.14 * radius_circle

#exc 8
slope = 2 #coeficiente angular
y_intercept = -2
x_intercept = -y_intercept / slope
print(f"Slope (m): {slope}")
print(f"Y-intercept (b): {y_intercept}")
print(f"X-intercept: {x_intercept}")

#exc 9
x1, y1 = 2, 2
x2, y2 = 6, 10

slope2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Slope: {slope2}")
print(f"Euclidean distance: {distance}")

#exc 10
if slope == slope2:
    print("The slopes in exc 8 and exc 9 are equal.")
elif slope > slope2:
    print("The slope in exc 8 is greater than the slope in exc 9.")
else:
    print("The slope in exc 9 is greater than the slope in exc 8.")

#exc 11 
for x in range(-10, 5):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}") 

#exc 12
word1 = "Python"
length1 = len(word1)
print(length1)

word2 = "dragon"
length2 = len(word2)
print(length2)

print(len({word1}) != len({word2})) 

#exc 13
print('"ON in python and dragon', 'on' in {word1} and 'on' in {word2})

#exc 14
jargon = 'I hope this course is not full of jargon'
print('jargon in sentence' 'jargon' in  {jargon.lower()})

#exc 15
print('There is no ON in both:', 'on' not in {word1} and  'on' not in {word2})

#exc 16
print("Length of Python and convert to float", len((word1)))
length_float = float(len(word1))
length_string = str(len(word1))
print(length_float, length_string)

#exc 17
print('Type the number: ')
number1 = int(input())

if number1 % 2 == 0:
    print('Numero Par/Even Number')
else:
    print('Numero Impar/Odd number')

#exc 18
print('Check floor division //')
check_floor = 7 // 3
check_floor_converted = int(2.7)
if check_floor == check_floor_converted:
    print('Exercise ok')
else:
    print('It\'s not')

#exc 19
if type('10') == type(10):
    print('Equal')
else:
    print('Not equal')

#exc 20
int1 = int(float('9.8'))
if int1 == 10:
    print(' 9.8 is equal to 10')
else:
    print ('Not Equal')

#exc 21
print('Calculate weekly earnings')
hours = int(input('Hours: '))
rate = float(input('Rate: '))
weekly_earnings = hours * rate
print('Your weekly earnings is: ', weekly_earnings)

#exc 22
print('Calculate time lived (Max 100)')
years = int(input('Years: '))

if years > 100:
    years = 100
    print('Maximum allowed age is 100 years.')

seconds_year = 31536000
total_year = years * seconds_year
print('Time Lived in seconds is:', total_year)

#exc 23 table
print('n 1 n n^2 n^3')

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)