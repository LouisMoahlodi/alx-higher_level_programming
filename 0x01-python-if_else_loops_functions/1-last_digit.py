#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number % 10
num3 = num2 % 10
n = -abs(num3)

if number > 0 and num2 > 5:
    print("Last digit of", number, "is", num2, "and is greater than 5")

elif num2 == 0:
    print(f"Last digit of", number, "is", num2, "and is 0")

elif number < 0:
    num2 = abs(number)
    if n < 6 and n != 0:
        print("Last digit of", number, "is", n, "and is less than 6 and not 0")
    elif n == 0:
        print(f"Last digit of", number, "is", n, "and is 0")
