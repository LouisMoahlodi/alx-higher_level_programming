#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = abs(number) % 10
if num2 > 5:
    print("Last digit of", number, "is", num2, "and is greater than 5")
elif num2 < 6:
    print("Last digit of", number, "is", num2, "and is less than 6 and not 0")
elif num2 == 0:
    print("Last digit of", number, "is", num2, "and is 0")
