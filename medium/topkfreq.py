nums = [1,1,1,2,2,3]

k = 2

new_dic = {}

for i in nums:
    if i in new_dic:
        new_dic[i] +=1
    else:
        new_dic[i] = 1

sorted_dic = sorted(new_dic.items(), key=lambda x:x[1], reverse = True)

l1 = []
for i in range(k):
    l1.append(sorted_dic[i][0])