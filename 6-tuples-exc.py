tuple_char = ('A', 'B', 'C')
tuple_num = ('1', '2', '3')
tuple_merge = tuple_char + tuple_num

print(len(tuple_merge))


# 2
tuple_fruits = ('Banana', 'Mango', 'Apple')
tuple_veg = ('Broccoli', 'Lettuce')
tuple_animal_prod = ('Milk', 'Eggs', 'Meat')

food_stuff = tuple_fruits + tuple_veg + tuple_animal_prod
print(food_stuff)

food_list = list(food_stuff)
print(food_list)
print(type(food_list))

# Slice
food_list = food_list[3:4]         
print(food_list)


food_list = [food_stuff[i] for i in (2, 5, 6)]  
print(food_list)

tuple_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in tuple_countries)
print('Iceland' in tuple_countries)