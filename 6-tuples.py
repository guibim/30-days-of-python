tpl = ('item 1', 'item 2', 'item 3','Item 4')
print(tpl)
print(len(tpl))

#Accessing
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

#Negative index
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

#slicing
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]   
all_fruits= fruits[0:]      
orange_mango = fruits[1:3]  
orange_to_the_rest = fruits[1:]

#Negative
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    
orange_mango = fruits[-3:-1]  
orange_to_the_rest = fruits[-3:]

#tuples to list
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     
fruits = tuple(fruits)
print(fruits)     

#Check a item
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits) 
#fruits[0] = 'apple' #error

#Joining tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#deleting
del tpl
del fruits
print(tpl, fruits) #check delete
