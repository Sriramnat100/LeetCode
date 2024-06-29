head = [1,2,3,4,5,6,7,8]
temp = -1
clone = [item for item in head]

#1,2,3,4,5,6,7,8
#0,1,2,3,4,5,6,7

#1,2,3,4,5,6,7,8
#0,2,4,6,7,5,3,1

#1,8,2,7,3,6,4,5
#0,1,2,3,4,5,6,7

x = int(len(head) / 2)

for index, value in enumerate(head):
    if (index < x):
        clone[index] = "y"
        clone[index * 2] = value
clone[-1] = "y"

g = 1
for i in range(len(clone) - 1, 0, -1 ):
    if (clone[i] == "y"):
        clone[g] = clone[i]
        g = g + 2
        


    else:
        continue



print(clone)
print([0,1,2,3,4,5,6,7])
    
