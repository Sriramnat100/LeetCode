# self = "121"
x = 3435343

if x>= 0:
    l1 = []
    intstring = str(x)
    string_list = []
    for char in intstring:
        string_list.append(char)


    for i in range(len(string_list)):
        if string_list[i] == string_list[((i+1)*-1)]:
            l1.append(string_list[i])
        else:
            print("not true")
            break
    
    if l1 == string_list:
        print("true")

else:
    print("not true")