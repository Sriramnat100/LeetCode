s = "badc"
t = "baba"

new_dic = {}

new_dic[s[0]] = t[0]
for i in range(len(s)):
    reverse_dict = {value: key for key, value in new_dic.items()}
    if (s[i] in new_dic and new_dic[s[i]] != t[i]):
        print("false")
    elif (t[i] in reverse_dict and reverse_dict[t[i]] != s[i]):
        print("false")
    else:
        new_dic[s[i]] = t[i]
        


