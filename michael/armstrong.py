#!/usr/bin/env python3


# a_n * 10^n + ... + a_0 = a_n**3 + ... + a_0**3

def armstrong(low, high):
    for i in range(low, high + 1):
        cubed =sum(map(lambda x: (int(x))**3, str(i)))
        if cubed == i:
            print(i, end=' ')
    print()


if __name__ == "__main__":
    while True:
        low, high = map(int, input("Find Armstrong numbers within bound: ").split(" "))
        if high < low:
            print("Need better bounds")
            continue
        elif high == low:
            print("Exiting...")
            exit(0)
        armstrong(low, high)
