def strip_comments(strng, markers):
    
    for i in markers:
        #print(i)
        #z = strng
        if i in strng:
            strng = strng.replace(i, "")
    for i in strng:
        if strng.count(i) > 1:
            pass

    print(strng)


strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])