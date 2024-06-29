all_pos = []
maxes = []
strs = ["ab", "a"]

#Finding all substrings 
def string_checker(strings):
    temp = []
    for index in range(len(strings)):
        string_new = ""
        for test in range(index + 1):
            string_new = string_new + strings[test]
            temp.append(string_new)
    #Removing duplicates
    temp = list(set(temp))


    return temp

#Made a list of the possible strings
for i in strs:
    all_pos.append(string_checker(i))
all_pos = [item for sublist in all_pos for item in sublist]



#Check how many times each sub appears

for sub in all_pos:
    if all_pos.count(sub) == len(strs):
        maxes.append(sub)

print(max(maxes))



