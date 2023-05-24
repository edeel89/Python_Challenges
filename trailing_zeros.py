def zeros(n):
    counter = 1
    zeroes = 0
    if n != 0:
        for i in range(1,n+1):
            counter = counter*i
        print(counter)
        counter = str(counter)
        for i in counter[::-1]:
            if int(i) <= 0:
                zeroes = zeroes + 1
            else:
                break
        print(zeroes)
    else: 
        return 0

zeros(30)