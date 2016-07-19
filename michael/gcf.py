#!/usr/bin/env python

#200 and 300
#200 and 100


# 36 and 81
# 36 and 45
# 36 and 9

def gcf(a, b):
    high, low = max(a, b), min(a, b)
    while low > 0:
        high -= low
        if low > high:
            high, low = low, high
    return high

if __name__ == "__main__":
    while True:
        a, b = map(int, input("give me two numbers: ").split(' '))
        if a == b:
            print("Exiting...")
            exit(0)
        print("the gcf is: ", gcf(a, b))
