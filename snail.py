def snail(snail_map):
    new_list = []
    list2 = snail_map
    for i in list2[0]:
        new_list.append(i)    
    for i in list2[1:]:
        new_list.append(i[-1])
    for i in list2[::-1]:
        counter = len(i) -2
        for e in range(len(i)):
            new_list.append(i[counter])
            counter = counter -1
        new_list.pop(-1)
        break
    for i in list2[-2::-1]:
        new_list.append(i[0])
    new_list.pop(-1)
    list3=list2[1]
    if len(snail_map) != 2:
        for i in list3[1:]:
            new_list.append(i)
        new_list.pop(-1)
        list4=list2[2]
        if len(snail_map) !=3:
            for i in list4[-2::-1]:
                new_list.append(i)
            new_list.pop(-1)


    print(new_list)  #[1, 2, 3, 1, 4, 7, 7]

array = [[1,2,3,1],[4,5,6,4],[7,8,9,7],[7,8,9,7]]
#array = [[1,2,3],[4,5,6],[3,8,9]]
#array = [[1,2,3],[4,5,6]]
snail(array)