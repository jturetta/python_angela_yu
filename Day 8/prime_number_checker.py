import math


def paintCalculator(wall_height, wall_width, coverage):
    result = (wall_height * wall_width) / coverage
    return math.ceil(result)


def primeNumberChecker(number):
    isPrime = True
    for item in range(2, number):
        if number % item == 0:
            isPrime = False
    return isPrime
