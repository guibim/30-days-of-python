#1 

list = []
print(list)

#2
list2 = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
print(list2)

#3
print(len(list2))

#4
print(list2[0])
print(list2[2])
print(list2[4])

#5
mixed_list = ['Guilherme', 26, True, 'Brazil']

#6 ~ #25
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies) #7
print(len(it_companies)) #8
print(it_companies[0])#9
print(it_companies[3])
print(it_companies[6])
it_companies[0] = 'Meta' #10 
print(it_companies) #10
it_companies.append('Twitter') #11
print(it_companies) #11
it_companies.insert(4, 'Blizzard') #12
it_companies[1] = it_companies[1].upper() #13
print(it_companies) #13

print(' - '.join(it_companies)) #14
does_exist = 'Twitter' in it_companies #15
print(does_exist) #15

it_companies.sort() 
print(it_companies) #16

it_companies.reverse()
print(it_companies) #17

print(it_companies[0:3]) #18
print(it_companies[-3:]) #19
print(it_companies[::2]) #20

#remove
it_companies.remove('Amazon')
print(it_companies) #21
it_companies.remove('Meta')
print(it_companies) #22
it_companies.remove('Twitter')
print(it_companies) #23

#clear
it_companies.clear()
print(it_companies, "Clear efetuado") #24

#destroy 
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
list_join = front_end + back_end
print(list_join)

#27
full_stack = list_join.copy()
full_stack.insert(front_end.index('Redux') + 1, 'Python')
full_stack.insert(front_end.index('Redux') + 2, 'SQL')
print(full_stack)


#excs 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Sorted ages:', ages)
min_age = ages[0]
max_age = ages[-1]
print('Min age:', min_age, 'Max age:', max_age)
ages.append(min_age)
ages.append(max_age)
ages_median = (ages[len(ages)//2] + ages[(len(ages)-1)//2]) / 2
print('Median age:', ages_median)
ages_avg = sum(ages) / len(ages)
print('Average age:', ages_avg)
age_range = max_age - min_age
print('Age range:', age_range)
print(abs(min_age - ages_avg), abs(max_age - ages_avg))
