def fibonacci_sequence(number):
    if number == 1:
        print("0")
    elif number == 2:
        print("0,1")
    else:
        first = 0
        second = 1
        print("0,1", end = ",")
        for x in range(2, number):
            new_val = first + second
            if x == number - 1:
                print(new_val)
            else:
                print(new_val , end = ",")
            first = second
            second = new_val
        return

if __name__ == "__main__":
    while True:
        print("")
        number = input("Enter the number for the Fibonacci sequence: ").strip()
        if number != "":
            number = int(number)
            if number == 0:
                break
            fibonacci_sequence(number)
