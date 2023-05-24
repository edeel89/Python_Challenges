def increment_string(strng):
    if strng.isalpha():
        print(strng + "1")
    else:
        for i in strng[::-1]:
            x = i 
            x = int(x) +1
            x = str(x)
            x = strng.replace(i, x)
            print(x)
            break
        

increment_string("foox")