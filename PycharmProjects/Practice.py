print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

character_name = "john"
character_age = "85"
print("There once was a man named " + character_name.upper() + ".")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name.capitalize() + ".")
print(f"But didn't like to be {character_age}.")
print("hello\nhow are you")
print('x' in character_name)
print(len(character_name) + len(character_age))
print(character_name[2])
print(character_name.index('n'))
print(character_name.replace("john", "tom"))
print("---------------------------------------------------")

my_age = -75
print("He was " + str(my_age) + " years old.")
print(abs(my_age))
print(pow(2, 3))
print(max(4, 6, 9))
print(min(4, 6, 9))
print(round(5.49))
print(10 ** 3)
print(10 // 3)
from math import *

# or import math and use prefix "math."
print(floor(4.9))
print(ceil(4.1))
print(sqrt(100))
print("---------------------------------------------------")

try:
    # name = input("enter your name: ")
    # age = input("enter your age: ")
    print("my name is " + name + " and I'm " + age)

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + float(num2)
    print(result)
except NameError as err:
    print(err)

print("---------------------------------------------------")
numbers = [40, 8, 8, 8, 50, 23, 42]
friends = ["Kevin", "Tom", "Alyssa", "Oscar", "Toby"]
friends.sort()
print(friends)
numbers.reverse()
print(numbers)
print(friends[0])
print(friends[-1])
print(friends[2:])
print(friends[1:3])
friends.extend(numbers)
print(friends)
friends.append("Martha")
print(friends)
friends.insert(1, "Jax")
print(friends)
friends.remove("Jax")
print(friends)
friends.pop(11)
print(friends)
print(friends.index('Alyssa'))
print(friends[2])
print(friends.count(8))
friends2 = friends.copy()
print(friends2)
print("---------------------------------------------------")


def say_hi(yourname, yourage):
    print("Hello " + yourname + " you are " + str(yourage))


say_hi("Arian", 32)


def cube(num):
    return pow(num, 3)


print(cube(4))

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are tall but not a male")
else:
    print("You are neither male or tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2, 5, 9))
print("---------------------------------------------------")

try:
    # num1 = float(input("Enter first number: "))
    # op = input("Enter operator: ")
    # num2 = float(input("Enter second number: "))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("Invalid operator!")
except NameError as err:
    print(err)
print("---------------------------------------------------")

monthconversion = {
    "Jan": "January",
    2: "February"
}
print(monthconversion.get("Jan"))
print(monthconversion[2])
print(monthconversion.get("Feb", "Invalid Key"))
monthconversion[2] = "March"
print(monthconversion[2])
print("---------------------------------------------------")
try:
    code = {"1": "One", "2": "Two", "3": "Three", "4": "Four"}
    # entered_code = input("Phone: ")
    new_code = ""
    for digit in entered_code:
        new_code = new_code + code.get(digit) + " "
    print(new_code)
except NameError as err:
    print(err)
print("---------------------------------------------------")

i = 1
while i < 3:
    print(i)
    i += 1
print("Done with loop")
print("---------------------------------------------------")

for letter in "Arian":
    print(letter)

friends = ["John", "Tony", "Chris"]
for friend in friends:
    print(friend)
for index in range(len(friends)):
    print(friends[index])

print("---------------------------------------------------")


def raise_to_power(base_num, pow_num):
    return base_num ** pow_num


print(raise_to_power(5, 3))


def raise_to_power2(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power2(5, 3))
print("---------------------------------------------------")

number_grid = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10]]
print(number_grid[3][0])
for element in number_grid:
    for sub_element in element:
        print(sub_element)
print("---------------------------------------------------")

try:
    10 / 1
    # number = int(input("Enter a number: "))
    # print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
print("---------------------------------------------------")

# r: reads only, r+: reads and writes, w: overwrites  only, w+: writes and reads, a: appends only, a+: appends and reads

employee_file = open("employee file.txt", "r")
print(employee_file.writable())
print(employee_file.readlines()[1])
employee_file.close()
print("---------------------------------------------------")

from Tools_Package import useful_tools

# from Tools_Package.useful_tools import roll_dice
print(useful_tools.roll_dice(5))

result = useful_tools.Dice(1, 1)
print(result.roll_both_dice())

members = ["John Lenon", "Paul McCartney", "George Harrison", "Ringo Star"]
print(useful_tools.rand_name_pick(members))
print("---------------------------------------------------")

from Class import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.gpa)
print(student2.is_on_probation)
print(student1.is_on_honor_roll())
print("---------------------------------------------------")

from Class import Chef
from Class import PersianChef

my_chef = Chef()
my_persian_chef = PersianChef()

my_chef.make_chicken()
my_persian_chef.make_salad()
my_persian_chef.make_stew()
print("---------------------------------------------------")

# Print F using x
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ""
    for element in range(number):
        output = output + 'x'
    print(output)
print("---------------------------------------------------")

# find a max number in a list
numbers = [8, 2, 3, 4, 5]
print(max(numbers))


# Alternative Solution
def max_num(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


print(max_num(numbers))
print("---------------------------------------------------")

# Remove duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1, 2, 2]


def dup_remover(numbers):
    non_dup_list = []
    for number in numbers:
        if number not in non_dup_list:
            non_dup_list.append(number)
    return non_dup_list


print(dup_remover(numbers))
print("---------------------------------------------------")

coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)
print("---------------------------------------------------")


# emoji convertor using dictionary
def emoji_converter():
    message = input(">")
    words = message.split()
    print(words)
    emojis = {
        ":)": "☺",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


# print(emoji_converter())
print("---------------------------------------------------")

from pathlib import Path

path = Path("Tools_Package")
print(path.exists())

path2 = Path()
for file in path2.glob('*.py'):
    print(file)
print("---------------------------------------------------")

age = 36
weight = 75
txt = "My name is John, and I am {} and weigh {}"
print(txt.format(age, weight))


age = 36
txt = f"      My name is John, and I am {age} years old"
print(txt)
print(type(txt))
print(txt.strip())
print("---------------------------------------------------")

# Write a function to get the first n odd numbers from a list
list1 = [10, 21, 4, 45, 66, 93, 67, 93, 74, 100, 33, 49]
list2 = []
for num in list1:
    if num % 2 != 0 and len(list2) < 4:
        list2.append(num)
print(list2)
print("---------------------------------------------------")

# Stack
list1 = [10, 21, 4, 45, 66, 93, 67, 93, 74, 100, 33, 49]
list2 = []
i = 0
while i < len(list1):
    list2.append(list1.pop(-1))
print(list2)
print("---------------------------------------------------")

# Queue
list1 = [10, 21, 4, 45, 66, 93, 67, 93, 74, 100, 33, 49]
list2 = []
i = 0
while i < len(list1):
    list2.append(list1.pop(0))
print(list2)
print("---------------------------------------------------")


# Palindrome
def palindrome():
    while True:
        string = input(("Enter a string:"))
        if string == string[::-1]:
            print("The string is a palindrome")
        else:
            print("Not a palindrome")

# palindrome()
print("---------------------------------------------------")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits)
print("---------------------------------------------------")

# Fizz Buzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print("\n---------------------------------------------------")

# Fibonacci Sequence
a = 0
b = 1
print(a, b, end=" ")
for num in range(0, 20):
    sum = a + b
    print(sum, end=" ")
    a = b
    b = sum
print("\n---------------------------------------------------")

# Fibonacci Sequence
def fib_loop(n):
    a = 0
    b = 1
    if n <= 1:
        return 0
    else:
        print(a, b, end=" ")
        for num in range(2, n):
            sum = a + b
            print(sum, end=" ")
            a = b
            b = sum


print(fib_loop(5))
print("---------------------------------------------------")

# Fibonacci Sequence
def FibRecursion(n):
    if n <= 1:
        return n
    else:
        return (FibRecursion(n - 1) + FibRecursion(n - 2))


for i in range(5):
    print(FibRecursion(i), end=" ")


