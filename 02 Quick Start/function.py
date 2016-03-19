#!/usr/bin/python3

def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False

    # This else statement does not look necessary. What happens if I remove it?
    #else:
    # Just as I thought... it works fine without it.

    print(n, "is a prime number")
    return True

for n in range(1, 20):
    isprime(n)

