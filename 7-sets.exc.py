it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# lv1 1~5
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Blizzard", "Activision", "Epic"])
it_companies.pop()
print(it_companies)
# remove() procura pelo elemento e deleta, caso nao encontre retorna erro, já discard() apenas é skippado caso nao encontra o elemento

# lv2
ab_join = A.union(B)
print(ab_join)

A.intersection(B)
print(A)
A.issubset(B)
A.isdisjoint(B)
C = A.union(B)
A.symmetric_difference(B)
print(A, B)
del A, B

# lv 3
print("Length of list:", len(age))
age_set = set(age)
print("Length of set:", len(age_set))

if len(age) > len(age_set):
    print("The list is bigger.")
elif len(age) < len(age_set):
    print("The set is bigger.")
else:
    print("Both are the same size.")
# A string is text, a list is a mutable collection, a tuple is an immutable list, and a set is an unordered collection of unique items.

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()     
unique_words = set(words) 
print(unique_words)
print("Number of unique words:", len(unique_words))
