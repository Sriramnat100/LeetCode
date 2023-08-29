l1 = [3,2,6,5,11,3]
target = 6
i = 0
for i in range(len(l1)):
    for x in range(len(l1)):
        if l1[i] + l1[x] == target and i!= x:
            print(i,x)
            
    