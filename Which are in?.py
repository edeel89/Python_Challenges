
def in_array(a1, a2):
    new = ""
    list = []
    for i in a1:
        for i2 in a2:
            if i in i2:
                if i[-1] == i2[-1]:
                    x = i
                    if x in new:
                        continue
                    else: 
                        new = i
                        list.append(i)
                        print(list)
                else:
                    continue
            else:
                #print("false")
                continue
    if new == "":
        print('false')

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1,a2)