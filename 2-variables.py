import keyword
first_name = 'Guilherme'
last_name = 'Bim'
country = 'Brazil'
city = 'Campinas'
age = 26
is_married = True
skills = ['Javascript', 'Python', 'Cypress', 'Docker', 'SQL']
person_info = {
    'first_name': 'Guilherme',
    'last_name': 'Bim',
    'country': 'Brazil',
    'city': 'Campinas'
    }

print('First Name:', first_name)
print('First name length:', len(first_name))
print('Last Name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is Married:', is_married)
print('Skills:', skills)
print('Person Info:', person_info)

first_name, last_name, country, age, is_married = 'Guilherme', 'Bim', 'Brazil', 26, True

print (first_name, last_name, country, age, is_married)
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)  
print('Age:', age)
print('Is Married:', is_married)

print(type(first_name)) 
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))

num_one = 5
num_two = 4

total = num_one + num_two
print('Total:', total)
diff = num_one - num_two
print('Difference:', diff)
product = num_one * num_two
print('Product:', product)
division = num_one / num_two
print('Division:', division)
remainder = num_one % num_two
print('Remainder:', remainder)
power = num_one ** num_two
print('Power:', power)
floor_division = num_one // num_two
print('Floor Division:', floor_division)
# Area of a triangle
radius = float(input('Enter the radius: '))
area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * 3.14159 * radius
print('Area:', area_of_circle)
print('Circumference:', circum_of_circle)


first_name2 = input('Enter your name: ')
last_name2 = input('Enter your last name: ')
age2 = input('Enter your age: ')
country2 = input('Enter your country: ')

print(keyword.kwlist)