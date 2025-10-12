letter = 'P'
print(letter)
print(len(letter))  # Para ver o tamanho da string

greeting = 'Hello, World!'
print(greeting)
print(len(greeting))  # Para ver o tamanho da string

sentence = "This is a sentence."
print(sentence)

multiline_string = '''This is a string
that spans multiple lines.'''
print(multiline_string)

multiline_string2 = """This is another string
that spans multiple lines."""
print(multiline_string2)

# Concatenação de strings
first_name = 'Guilherme'
last_name = 'Bim'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(full_name))  # Para ver o tamanho da string
print(full_name.upper())  # Deixa todas as letras maiúsculas
print(full_name.lower())  # Deixa todas as letras minúsculas
print(full_name.title())  # Deixa a primeira letra de cada palavra maiúscula
print(len(first_name))
print(len(last_name))

print(len(first_name) > len(last_name))  # Verifica se o tamanho do primeiro nome é maior que o do sobrenome
print(len(first_name) < len(last_name))  # Verifica se o tamanho do primeiro nome é menor que o do sobrenome
print(len(full_name))

# \n - pular linha
print('Hello\nWorld')
print('Days\tTopics\tExercises')  # \t - tabulação
print('Day 1\t3\t5')
print('This is a backslash symbol (\\)')  # \\ - para imprimir uma barra invertida
print('In every programming language it starts with \"Hello, World!\"')

# Formatação de string

language = 'Python'

formated_string = 'I am %s %s. I teacch %s '%(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string2 = 'The area of a circle with radius %d is %.2f.'%(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn', 'TensorFlow', 'Keras']
formated_string3 = 'Some popular Python libraries are: %s.'%', '.join(python_libraries)
print(formated_string2)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# String interpolation (f-strings) (Python 3.6+)
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Accessing Characters in Strings by Index 
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# para fazer o contrário é so iniciar com -1 

#Substrings
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#Reverse
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#String Methods
#capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
#count()
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
#endswith()
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
#expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

#find()
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

#rfind()
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

#format()
age = 26
job = 'teacher'
country = 'Brazil'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) 


result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

#index()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
print(challenge.index(sub_string, 9)) #error

#rindex()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) 

#isalnum() checa se é alfanumérico
challenge = 'thirtydayspython'
print(challenge.isalnum()) # True
challenge = '30DaysOfPython'
print(challenge.isalnum()) # True
challenge = 'thirty days of python'
print(challenge.isalnum()) # False

#isalpha() checa se é alfabético
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

#isdecimal() checa se é decimal
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# isdigit() checa se é dígito
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

#isnumeric() checa se é numérico
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

#isidentifier() checa se é um identificador válido
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, identifiers cannot start with a digit
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

#islower() checa se está em minúsculo
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

#isupper() check if all characters are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

#join() junta uma lista de strings
challenge = ' '.join(['Thirty', 'days', 'of', 'Python'])
print(challenge) # Thirty days of Python
challenge = ' '.join(('Thirty', 'days', 'of', 'Python'))
print(challenge) # Thirty days of Python

#strip() remove espaços em branco no início e no fim
challenge = '  thirty days of python  '
print(challenge.strip('noth')) 
# 'irty days of py'

#replace() substitui uma substring por outra
challenge = 'thirty days of python'
print(challenge.replace('python', 'JavaScript'))
# 'thirty days of JavaScript'

#split() divide uma string em uma lista
challenge = 'thirty days of python'
print(challenge.split())
# ['thirty', 'days', 'of', 'python']

#title() coloca a primeira letra de cada palavra em maiúsculo
challenge = 'thirty days of python'
print(challenge.title())
# 'Thirty Days Of Python'

#swapcase() inverte maiúsculas e minúsculas
challenge = 'thirty DAYS of python'
print(challenge.swapcase())
# 'THIRTY days OF PYTHON'

#startswith() checa se a string começa com uma substring
challenge = 'thirty days of python'
print(challenge.startswith('th'))   # True
print(challenge.startswith('py'))   # False

