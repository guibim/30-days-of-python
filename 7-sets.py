st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(st)
len(fruits)

print("Does set st contain item 3?",'item3' in st)
print('mango' in fruits)

# add set 
fruits.add('lime')

#or update 
st.update(['item5', 'item6', 'item7'])
fruits.update(st)

#remove 
st.remove('item2')

#pop() remove a random item 
fruits.pop()
removed_item = fruits.pop()
print(removed_item)
#clear func
st.clear()

del st

#converting list to set 
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) 

# joining
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) 


#intersection
whole_numbers = {0, 1, 2, 3, 4, 5, 6 }
even_numbers = {2, 4, 6}
whole_numbers.intersection(even_numbers)
print(whole_numbers)