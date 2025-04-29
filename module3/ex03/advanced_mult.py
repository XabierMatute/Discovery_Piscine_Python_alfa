table = 0
while table <= 10:
    print("table of", table, end=" ")
    num = 0
    while num < 10:
        print(num * table, end=" ")
        num += 1
    print(num * table)
    table += 1