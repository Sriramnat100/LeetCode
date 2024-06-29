# #just if anything fucks up

# nums = [-1,0,1,2,-1]
# l1 = []
# temp = []
# x = 0
# for i in nums:
#     #This one for positive
#     if (i > 0):
#         range1 = range(-1 * i, 1)
#         cond1 = (x in nums) & ((x + i) in nums)

#     elif (i < 0):
#         range1 = range(i * -1, -1, -1)
#         cond1 = (x in nums) & ((x - i) in nums)
    
#     else:
#         if (nums.count(0) == 3):
#             l1.append([0,0,0])
#             break

#     for x in (range1):
#         if (cond1):
#             temp = [i, x + i, x]
#             temp.sort()
#             l1.append(temp)
#             break
#         else:
#             continue

#     unique_l1 = list(map(list, set(map(tuple, l1))))


    
    
# print(unique_l1)

nums = [3,-2,1,0]
l1 = []
temp = []
sum = 0
if (len(nums) < 3):
    print([])
    
if (len(nums) == 3):
    for i in nums:
        sum = sum + i
    if (sum == 0):
        nums.sort()
        print(nums)
    else:
        print([])


for count, i in enumerate(nums):

    for x in range(count + 1, len(nums)-1):

        occurrences = sum(1 for y in nums[count+1:] if y == nums[x])
        
        if i >= 1:
            if ((-1 * ((i + nums[x])) in nums[count+1:] )):
                if (nums[x] == -1 * (i + nums[x]) and occurrences <= 1):
                    break
                else:
                    temp = [i, nums[x], -1 * (i + nums[x])]
                    temp.sort()
                    l1.append(temp)
                    break
            else:
                continue

        elif i <= -1:

            if ((-1 * ((i + nums[x])) in nums[count+1:])):
                if (nums[x] == -1 * (i + nums[x]) and occurrences <= 1):
                    break
                else:
                    temp = [i, nums[x], -1 * (i + nums[x])]
                    temp.sort()
                    l1.append(temp)
                    break
            else:
                continue
        else:
            if (nums.count(0) == 3):
                l1.append([0,0,0])
                break

unique_l1 = list(map(list, set(map(tuple, l1))))

print(unique_l1)