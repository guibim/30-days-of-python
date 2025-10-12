#1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'

string_total = str1 + str2 + str3 + str4 
print(string_total)

#2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string1 = 'Coding'
string2 = 'For'
string3 = 'All'
string_total2 = string1 + string2 + string3
print(string_total2)

# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9 - Cut(slice) out the first word of Coding For All string.
print(company[0:6])

#10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company) # outra forma de fazer
print(company.startswith('Coding')) # outra forma de fazer
print(company.endswith('Coding')) # outra forma de fazer
# 11 - Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# 12 - Change Python for Everyone to Python for All using the replace method or other methods.
string_python = 'Python for Everyone'
print(string_python.replace('Everyone', 'All'))

# 13 - Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

#14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string_companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string_companies.split(','))

# 15 - What is the character at index 0 in the string Coding For All.
print(company[0])
# 16 - What is the last index of the string Coding For All.
print(len(company) - 1)
# 17 - What character is at index 10 in "Coding For All" string.
print(company[10])
# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
string_python = 'Python For Everyone'
acronym = string_python[0] + string_python[7] + string_python[11]
print(acronym)
# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = company[0] + company[7] + company[11]
print(acronym2)
# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))
# 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(sentence.rfind('because'))
# 25 - Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])
# 26 - Find the position of the first occurrence of the word 'because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))
# 27 - Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])
# 28 - Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
# 29 - Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())
# 31 - Which one of the following variables return True when we use the method isidentifier():
# thirty_days_of_python (porque identificadores nao podem começar com digito)

# 32 - The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon
# Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))
# 33 - Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# 34 - Use a tab escape sequence to write the following lines.
# Name      Age     Country     City
# Asabeneh  250     Finland     Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
# 35 - Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius **2
radius = 10
area = 3.14 * radius **2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

# 36 - Make the following using string formatting methods:
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # 2 decimal places
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
