def next_bigger(n):
    string = str(n)
    out = -1
    for i in string[::-1]:
        out = out - 1
        one = 0
        print(i)
        next_1 = int(string[out])
        if int(i) > next_1:
            output = string[:out] + i + str(next_1)
            print(output)
            break



next_bigger(144)