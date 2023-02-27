#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = -((-1 * number) % 10)
else:
    last = number % 10
s = f"Last digit of {number} is {last}"
if last > 5:
    s = s + " and is greater than 5"
elif last == 0:
    s = s + " and is 0"
else:
    s = s + " and is less than 6 and not 0"
print(s)
