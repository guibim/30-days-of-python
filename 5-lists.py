#Lists #Tuples #Sets #Dictionaries

my_list = list()
empty_list = list() 
print(len(empty_list))

my_list = []
empty_list = []
print(len(empty_list))

fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'broccoli', 'spinach']
animals = ['dog', 'cat', 'mouse']
web_techs = ['HTML', 'CSS', 'JavaScript']
countries = ['USA', 'Canada', 'Mexico']


print('Fruits:', fruits)
print('Number of Fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animals:', animals)
print('Number of Animals:', len(animals))
print('Web Technologies:', web_techs)
print('Number of Web Technologies:', len(web_techs))
print('Countries:', countries)
print('Number of Countries:', len(countries))

#Lists can have items of different data types

lst2 = [1, 2.5, 'Hello', True, None]
print('Mixed List:', lst2)

#index use
first_fruit = fruits[1]
print('First fruit:', first_fruit)
second_fruit = fruits[2]
print('Second fruit:', second_fruit)

#Last index
last_index = len(fruits) - 1
last_fruit= fruits[last_index]

#negative index

first_fruit = fruits[-3]
print('First fruit using negative index:', first_fruit)
last_fruit = fruits[-1]
print('Last fruit using negative index:', last_fruit)

#unpacking list
lst3 = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
first_item, second_item, third_item, *rest = lst3
print('First Item:', first_item)
print('Second Item:', second_item)
print('Third Item:', third_item)
print(rest) 

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#Slicing 
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] 
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]

#negative indexing 
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

#Modifying Lists , List = mutable or modifiable 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'kiwi'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'apple'
print(fruits)

#Check and add
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

lst = list()
lst.append('item 1')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           
fruits.append('lime')   
print(fruits)

#Remove items from a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
fruits.remove('banana')
print(fruits)
fruits.remove('lime')
print(fruits)

#using pop()
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

#Remove using del
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)

#Clearing a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
fruits.clear()
print(fruits)

#copy list
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
fruits_copy = fruits.copy()
print(fruits_copy)


#joining lists
lst3 = list1 = lst2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-1, -2, -3, -4, -5]
integers = positive_numbers + zero + negative_numbers
print(integers)


#extend()
list1 = ['item 1', 'item 2', 'item 3']
list2 = ['item 4', 'item 5', 'item 6']
list1.extend(list2)

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-1, -2, -3, -4, -5]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('integers', negative_numbers)


#counting items

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#Find index of an item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

#reverse list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

#sorting list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

#sorted
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
#reversed
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse = True)
print(fruits)
