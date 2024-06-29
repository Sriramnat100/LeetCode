nums = [9,-15,6,6,10,-2,8,8,0,-6,-4,-2,14,-6,-14,-2,12,5,-2,-8,13,13,-10,4,-6,8,6,-15,-5,11,-15,11,3,-2,-6,-10,11,-12,13,-12,-11,-5,2,10,-4,-5,-15,-7,7,-2,0,5,-11,-3,-13,-10,-9,0,-10,-7,-12,12,-11,7,-5,-1,12,-8,-6,3,-13,-10,5,-4,-14,-14,6,8,-14,-9,-8,-7,3,-4,6,5,1,12,-9,6,-10,-6,-5,-14,-14,5,-8,6,4,1]


l1 = []
temp = []
sum = 0
# if (len(nums) < 3):
#     return []
    
# if (len(nums) == 3):
#     for i in nums:
#         sum = sum + i
#     if (sum == 0):
#         nums.sort()
#         return [nums]
#     else:
#         return []


for counta, a in enumerate(nums):
    for countb, b in enumerate(nums[counta+1:]):
        new_nums = nums[counta+1:]
       
        new_nums.remove(b)
        if (-1 * (a + b) in new_nums):
            temp = [a,b,-1 * (a + b)]
            temp.sort()
            l1.append(temp)
            if (len(temp) == 3):
                temp = []
            else:
                continue
            

        elif (a == 0 and nums.count(0) >= 3):
            l1.append([0,0,0])
            break
            
        else:
                continue
 
unique_l1 = list(map(list, set(map(tuple, l1))))
sorted_list = [sorted(sublist) for sublist in unique_l1]
print(sorted_list)