#Lists #Tuples #Sets #Dictionaries

list = list()
empty_list = list() 
print(len(empty_list))

list = []
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
second_fruit = fruiits[2]
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
first_item, second_item, third_item = lst3
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