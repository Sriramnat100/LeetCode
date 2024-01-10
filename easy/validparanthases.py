s = "()[]{}"

n = 0
g = 1


def finder(startn, sub_str, acc_string):
    pos = acc_string.find(sub_str, startn)

    if pos != -1:
        str_list = list(acc_string)

        str_list.pop(startn)
        str_list.pop(pos - 1)

        return str_list
    else:
        str_list = []
        return str_list
        
val = finder(0, ")", s)
while(val):
    val = finder(0, ")", s)
    s = "".join(val) 
    val = finder(0, "]", s)
    s = "".join(val) 
    val = finder(0, "}", s)
    s = "".join(val)   

        

    


              
