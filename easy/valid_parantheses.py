s = "()[]{}"
s = list(s)

stack = []
hash_map = {"(": ")", 
           "{": "}", 
           "[": "]"}


for count, i in enumerate(s):
    if i in hash_map:
        stack.append(i)

    elif i in hash_map.values():
        n = stack[-1]
        if hash_map[n] == i:
            stack.pop(-1)

        else:
            print("failed")

print(s)


    


              