#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement to avoid infinite loop
    return result

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError
        print(factorial(num))
    except (IndexError, ValueError):
        sys.exit(1)

    f = factorial(num)
    print(f)
