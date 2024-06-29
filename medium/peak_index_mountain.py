arr = [0,1,0]

l = 0
r = len(arr) - 1
temp = 0
new_dic = {}
while l != r:
    if arr[l + 1] > arr[l]:
        if arr[l + 1] > temp:
            new_dic[0] = l + 1
            temp = arr[l + 1]
        l +=1
    if arr[r - 1] > arr[r]:
        if arr[r - 1] > temp:
            new_dic[0] = r - 1
            temp = arr[r - 1]
        r -= 1


print(new_dic[0])