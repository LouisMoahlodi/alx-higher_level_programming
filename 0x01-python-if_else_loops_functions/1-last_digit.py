#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number % 10

if number > 0 and num2 > 5:
        print("Last digit of", number, "is", num2, "and is greater than 5")

elif number < 0:
    num2 = abs(number)
    num3 = num2 % 10
    num4 = -abs(num3)
    if num4 < 6 and num4 != 0:
        print(f"Last digit of", number, "is", num4, "and is less than 6 and not 0")
    elif num4 == 0:
        print(f"Last digit of", number, "is", num4, "and is 0")

elif num2 == 0:
    print(f"Last digit of", number, "is", num2, "and is 0")


#if number > 0:
    #num2 = number % 10
    #f num2 > 5:
      #  print(f"Last digit of", number, "is", num2, "and is greater than 5")
#elif number < 0:
 #   num2 = number % 10
   # num3 = abs(number)
    #print(f"Last digit of", number, "is", num3, "and is less than 6 and not 0")
#elif num2 == 0:
    #print(f"Last digit of", number, "is", num2, "and is 0")

