#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif number % 3 == 0:
            print(f"Fizz", end=" ")
        elif number % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print(number, end=" ")
