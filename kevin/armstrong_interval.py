def armstrong_interval(beginning, ending):
    for x in range(beginning, ending + 1):
        num = x
        tsum = 0
        while num > 0:
            dig = num % 10
            tsum = tsum + (dig ** 3) 
            num = num // 10
        if tsum == x:
            print(x, end = " ")

    print("")

if __name__ == "__main__":
    while True:
        beginning = input("Enter beginning of interval: ").strip()
        ending = input("Enter ending of interval: ").strip()
        if beginning != "" and ending != "":
            beginning = int(beginning)
            ending = int(ending)
            if ending - beginning <= 0:
                break
            else:
                armstrong_interval(beginning, ending)
