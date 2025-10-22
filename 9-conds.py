#base do dia 9 no repo original
    #exc1
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)

if user_age >= 18:
    print("You are old enough to drive.")
else:
    dif_age = 18 - user_age
    print("You have to wait", dif_age, "more years to drive.")

#exc2
    
my_age = int(input('My age: '))
your_age = int(input('Your age: '))
difference = abs(my_age - your_age)  # valor da dif

if my_age > your_age:
    if difference == 1:
        print("I'm 1 year older than you.")
    else:
        print(f"I'm {difference} years older than you.")
elif your_age > my_age:
    if difference == 1:
        print("You're 1 year older than me.")
    else:
        print(f"You're {difference} years older than me.")
else:
    print("We are the same age!")
    
#exc3
a = int(input('Type A num: '))
b = int(input('Type B num: '))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#lv2

score = int(input("Type the student score: "))

if 80 <= score <= 100:
    print("A Student")
elif 70 <= score < 80:
    print("B Student")
elif 60 <= score < 70:
    print("C Student")
elif 50 <= score < 60:
    print("D Student")
elif 0 <= score < 50:
    print("F Student")
else:
    print("Invalid score")
    