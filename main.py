with open ("data.txt", "r") as file:

    # nr.1

    read = file.readlines()
    # print()
    # print (read[0:2])
    list = []
    for x in read:
        each = x.rstrip("\n").split(",")
        # print(each)
        if each[4] == "Oman":
            # print (each[6])
            list.append(each[6])
    min = min(list)
    print(min)

    # nr.2

    list1 = []
    for x1 in read:
        each1 = x1.rstrip("\n").split(",")
        # print(each)
        if each1[4] == "Latvia":
            # print (each1[8])
            list1.append(int(each1[8]))

    print (type(list1[0]))
    print (sum(list1))

    # nr.3

    list2 = []
    for x2 in read:
        each2 = x2.rstrip("\n").split(",")
        # print(each)
        if each2[4] == "Latvia":
            if each2[7] == "Telecommunications":
                print (each2[8])
                list2.append(int(each2[8]))

    print (len(list2))
    print(sum(list2))

    # nr.4 

    list3 = []
    for x3 in read:
        each3 = x3.rstrip("\n").split(",")
        # print(each)
        if each3[4] == "Latvia":
            # print (each3[3])
            list3.append(each3[3])
    
    print (len(list3))

    new_list = []
    for i in list3:
        # print(i[0:8])
        if i[0:8] == "https://":
            new_list.append(i)
                        
    print (len(new_list))

    # nr.5
        
    list4 = []
    for x4 in read:
        each4 = x4.rstrip("\n").split(",")
        # print(each)
        if each4[4] == "Latvia":
            # print (each3[3])
            list4.append(each4[3])
    
    print (len(list4))

    new_list1 = []
    for i in list4:
        # print(i[0:8])
        if ".org" in i:
            new_list1.append(i)
            # print (i)
                        
    print (len(new_list1))

