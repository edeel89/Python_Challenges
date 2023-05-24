
def pig_it(text):
    string = text.split(" ")
    new_list = []
    for i in string:
        if i.isalpha():
            x = i[1:] + i[0] + "ay"
            new_list.append(x)
        else:
            new_list.append(i)
    x = " ".join(new_list)
    print(x)

pig_it("Hello world !")

