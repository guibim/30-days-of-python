#while normal
count = 0
while count < 5:
    print(count)
    count = count + 1

#while with else
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
    
#break 
    count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#continue
   
    count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
    
 #for   
    numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    print(number)       
    
# for loop string
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
    
#for loop with tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    
    
#for loop with dictionary

person = {
    'first_name':'Guilherme',
    'last_name':'Bim',
    'age':26,
    'country':'Brazil',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) 
    
#for loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    

#breaks
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
    
#range() func
lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst) 
st = set(range(0,11,2))
print(st) 

#for else
for number in range(11):
    print(number) 
else:
    print('The loop stops at', number)
    
#pass 

for number in range(6):
    pass

#exc 1
for i in range(11):
    print(i)
#while 
i = 0
while i <= 10:
    print (i)
    i += 1
    
#exc 2
for i in range(10, -1, -1):
    print (i)
#while
i = 10
while i >= 0:
    print (i)
i -= 1

#exc 3
for i in range(1, 8):  # de 1 até 7
    print('#' * i)

#exc 4
for i in range(8):              # loop das linhas
    for j in range(8):          # loop das colunas
        print('#', end=' ')    
    print()                     

#exc 5
for i in range(11):  
    print(f"{i} x {i} = {i * i}")

#exc 6-7-8
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in languages:
    print(item)

for i in range(101):   
    if i % 2 == 0:    #par
        print(i)

for i in range(101):
    if i % 2 != 0:    #impar
        print(i)

#lv2 
total = 0
for i in range(101):  
    total += i
print("The sum of all numbers is", total)

even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)

#lv3 exc 2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)
