#1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers_filter = [i for i in numbers if i <= 0 ]
print (numbers_filter)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = [x for sublist1 in list_of_lists for sublist2 in sublist1 for x in sublist2]

print(flat_list)

#Using list comprehension create the following list of tuples:
result = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(result)


#4 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [[country.upper(), country[:3].upper(), city.upper()] 
             for [[country, city]] in countries]

print(flattened)


#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_list = [{'country': country.upper(), 'city': city.upper()} 
             for [[country, city]] in countries]

print(dict_list)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f"{first} {last}" for [[first, last]] in names]

print(full_names)

#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
m = slope(2, 3, 5, 11)
b = intercept(2, 3, 5, 11)
print(f"Slope: {m}, Intercept: {b}")
