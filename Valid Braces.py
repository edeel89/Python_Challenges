txt = "(){}[]"
def valid_braces(string):
    x = ""
    if (len(string)) == 6:
        for i in string:
            x += (i + " ")
            p1 = string.count("(")
            p2 = string.count(")")
    else:
        print('false')
    print(p1)
    print(x)

valid_braces(txt)