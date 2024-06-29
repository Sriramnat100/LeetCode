haystack = "leetcode"
needle = "leeto"
l1 = []
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

l1 = string_checker(haystack)

print(l1)

if needle in l1:
    #Create a new function that breaks up 
    continue