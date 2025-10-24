# ============================================
# 1. Declare a function add_two_numbers.
# It takes two parameters and it returns a sum.
# ============================================
def add_two_numbers(num1, num2):
    result = num1 + num2
    return result

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("A soma é:", add_two_numbers(num1, num2))

# ============================================
# 2. Write a function called add_all_nums which 
# takes arbitrary number of arguments and sums 
# all the arguments. Check if all the list items 
# are number types. If not, give a reasonable feedback.
# ============================================
def circle_area(r):
    pi = 3.14
    return pi * (r ** 2)

raio = float(input("Digite o raio do círculo: "))
print("A área é:", circle_area(raio))


# ============================================
# 3. Write a function which calculates area of a circle.
# Formula: area = π * r²
# The function takes radius as input parameter.
# ============================================
def add_all_nums(*args):
    total = 0
    for i in args:
        if not isinstance(i, (int, float)):
            return "Erro: todos os argumentos devem ser números."
        total += i
    return total

# ============================================
# 4. Temperature in °C can be converted to °F using this formula: 
# °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, called convert_celsius_to_fahrenheit.
# (Versão ampliada: o usuário escolhe se quer converter °C → °F ou °F → °C) 
# ============================================
def convert_temperature():
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    
    choice = input("Escolha uma opção (1 ou 2): ")

    if choice == "1":
        celsius = float(input("Digite a temperatura em °C: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Digite a temperatura em °F: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C")

    else:
        print("Opção inválida. Tente novamente.")

convert_temperature()

# ============================================
# 5. Write a function called check_season.
# It takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
# Adaptado para a localidade: Brasil (Hemisfério Sul)
# ============================================

def check_season(month):
    month = month.capitalize()  # padroniza a capitalização

    if month in ('Dezembro', 'Janeiro', 'Fevereiro'):
        return "Verão"
    elif month in ('Março', 'Abril', 'Maio'):
        return "Outono"
    elif month in ('Junho', 'Julho', 'Agosto'):
        return "Inverno"
    elif month in ('Setembro', 'Outubro', 'Novembro'):
        return "Primavera"
    else:
        return "Mês inválido."

mes = input("Digite o mês: ")
print("Estação:", check_season(mes))

    
#6
# ============================================
# 6. Write a function called calculate_slope
# which returns the slope of a linear equation.
# Formula: slope = (y2 - y1) / (x2 - x1)
# ============================================

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Erro: divisão por zero. A linha é vertical e não possui inclinação definida."
    slope = (y2 - y1) / (x2 - x1)
    return slope

x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

print("A inclinação (slope) é:", calculate_slope(x1, y1, x2, y2))


#7
# ============================================
# 7. Quadratic equation is calculated as follows:
# ax² + bx + c = 0
# Write a function which calculates the solution set 
# of a quadratic equation, called solve_quadratic_eqn.
# ============================================

import math

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Erro: o valor de 'a' deve ser diferente de zero."
    
    delta = b**2 - 4*a*c

    if delta < 0:
        return "Sem raízes reais (Δ < 0)"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: x = {x:.2f}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Duas raízes reais: x₁ = {x1:.2f}, x₂ = {x2:.2f}"

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(solve_quadratic_eqn(a, b, c))

#8
# ============================================
# 8. Write a function called print_list.
# It takes a list as a parameter and prints out
# each element of the list.
# ============================================

def print_list(items):
    for item in items:
        print(item)

minha_lista = ['Python', 'Cypress', 'Robot Framework', 'Postman']
print_list(minha_lista)

    
# ============================================
# 9. Write a function called reverse_list.
# It takes an array (list) as a parameter 
# and returns the reversed version of the list.
# ============================================

def reverse_list(lst):
    return lst[::-1]

minha_lista = [1, 2, 3, 4, 5]
print("Lista original:", minha_lista)
print("Lista invertida:", reverse_list(minha_lista))


# ============================================
# 10. Write a function called capitalize_list_items.
# It takes a list as a parameter and returns 
# a list of capitalized items.
# ============================================

def capitalize_list_items(items):
    return [item.capitalize() for item in items]

palavras = ['python', 'cypress', 'robot framework', 'postman']
print(capitalize_list_items(palavras))


#11
# ============================================
# 11. Write a function called add_item.
# It takes a list and an item parameter.
# It returns a list with the item added at the end.
# ============================================

def add_item(lst, item):
    lst.append(item)
    return lst

fruits = ['banana', 'mango', 'orange']
print(add_item(fruits, 'apple'))

# ============================================
# 12. Write a function called remove_item.
# It takes a list and an item parameter.
# It returns a list with the item removed.
# ============================================

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

fruits = ['banana', 'mango', 'orange', 'apple']
print(remove_item(fruits, 'mango'))

# ============================================
# 13. Write a function called sum_of_numbers.
# It takes a number parameter and adds all the numbers 
# in that range (from 1 to that number) and returns the sum.
# Example: sum_of_numbers(5) → 15 (1+2+3+4+5)
# ============================================

def sum_of_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

print(sum_of_numbers(5))
 
# ============================================
# 14. Write a function called sum_of_odds.
# It takes a number parameter and returns the sum 
# of all odd numbers in that range (from 1 to that number).
# ============================================

def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))
 
 
# ============================================
# 15. Write a function called sum_of_even.
# It takes a number parameter and returns the sum 
# of all even numbers in that range (from 1 to that number).
# ============================================

def sum_of_even(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))

# ============================================
# LEVEL 2 - EXTRA EXERCISES
# ============================================

# ============================================
# 1. Declare a function named evens_and_odds.
# It takes a positive integer and counts evens and odds from 0..n.
# ============================================

def evens_and_odds(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    evens = n // 2 + 1           # includes 0
    odds = (n + 1) // 2
    return {"evens": evens, "odds": odds}

result = evens_and_odds(100)
print(f"The number of odds are {result['odds']}.")
print(f"The number of evens are {result['evens']}.")



# ============================================
# 2. factorial(n): returns n! for whole numbers n >= 0
# ============================================

def factorial(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be an integer >= 0")
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out

print(factorial(5))



# ============================================
# 3. is_empty(x): checks if a value is empty (falsy)
# ============================================

def is_empty(value):
    return not bool(value)

print(is_empty([]))
print(is_empty("text"))



# ============================================
# 4. Stats helpers: mean, median, mode, range, variance, std (population)
# ============================================

from collections import Counter
import math

def calculate_mean(data):
    if len(data) == 0:
        raise ValueError("Empty data")
    return sum(data) / len(data)

def calculate_median(data):
    if len(data) == 0:
        raise ValueError("Empty data")
    s = sorted(data)
    m = len(s) // 2
    if len(s) % 2 == 1:
        return s[m]
    return (s[m - 1] + s[m]) / 2

def calculate_mode(data):
    if len(data) == 0:
        raise ValueError("Empty data")
    counts = Counter(data)
    max_freq = max(counts.values())
    modes = [v for v, c in counts.items() if c == max_freq]
    return {"modes": modes, "frequency": max_freq}

def calculate_range(data):
    if len(data) == 0:
        raise ValueError("Empty data")
    return max(data) - min(data)

def calculate_variance(data):
    if len(data) == 0:
        raise ValueError("Empty data")
    mu = calculate_mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)  # população

def calculate_std(data):
    return math.sqrt(calculate_variance(data))

nums = [2, 4, 4, 4, 5, 5, 7, 9]
print(calculate_mean(nums))
print(calculate_median(nums))
print(calculate_mode(nums))
print(calculate_range(nums))
print(calculate_variance(nums))
print(calculate_std(nums))

# ============================================
# LEVEL 3 - FUNCTIONS
# ============================================

# ============================================
# 1. Write a function called is_prime,
# which checks if a number is prime.
# ============================================

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(12))



# ============================================
# 2. Write a function which checks 
# if all items are unique in the list.
# ============================================

def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 3]))



# ============================================
# 3. Write a function which checks 
# if all the items of the list are of the same data type.
# ============================================

def same_data_type(lst):
    if not lst:
        return True
    tipo = type(lst[0])
    return all(isinstance(i, tipo) for i in lst)

print(same_data_type([1, 2, 3]))
print(same_data_type([1, '2', 3]))



# ============================================
# 4. Write a function which checks if 
# provided variable is a valid python variable.
# ============================================

def is_valid_variable(name):
    return isinstance(name, str) and name.isidentifier()

print(is_valid_variable("variavel_1"))
print(is_valid_variable("1variavel"))
