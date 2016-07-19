#!/usr/bin/env python3

def fib_seq(n):
    prev, cur = 0, 1
    print(prev, end=' ')
    if n == 1:
        return
    print(cur, end=' ')
    count = 2
    while count < n:
        prev, cur = cur, cur + prev
        print(cur, end=' ')
        count += 1
    print()

if __name__ == "__main__":
    while True:
        amount = int(input("How many values of the fibonacci sequence do you want? "))
        if amount <= 0:
            print("Exiting...")
            exit(0)
        fib_seq(amount)
