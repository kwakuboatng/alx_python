#!/usr/bin/python3
import random
number = str(random.randint(-10000, 10000))
last_digit = int(number[-1])
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5\n".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0\n".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and is not 0\n".format(number, last_digit))