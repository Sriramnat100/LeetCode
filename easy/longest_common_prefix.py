strings = "dog"
stringtwo = "racecar"
stringthree = "car"

["dog","racecar","car"]

#Finding all substrings 
def string_checker(strings):
    temp = []
    for index in range(len(strings)):
        string_new = ""
        for test in range(index):
            string_new = string_new + strings[test]
            temp.append(string_new)
    #Removing duplicates
    temp = list(set(temp))


    return temp


max1 = string_checker(strings)
max2 = string_checker(stringtwo)
max3 = string_checker(stringthree)



def val_in_list(l1,l2,l3):
    counter = []
    for i in l1:
        if i in l2 and i in l3:
            counter.append(i)
    for i in l2:
        if i in l1 and i in l3:
            counter.append(i)
    for i in l3:
        if i in l1 and i in l2:
            counter.append(i)
    return max(counter)



print(val_in_list(max1, max2, max3))