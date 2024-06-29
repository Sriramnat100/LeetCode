nums = [1,1]
n = len(nums)
#nss = [1,2,2,3,3,4,7,8]
#nss = [1,2,3,4,5,6,7,8]
#nss = [1,2,3,4,7,8]
nums.sort()
nums = list(set(nums))
l1 = []
for i in range(n):
    if i >= len(nums):
        l1.append(i + 1)
    elif (i+1) != nums[i]:
        l1.append(i+1)
        nums.insert(i, i + 1)
# n = len(nums)
# new_dic = {}
# for i in range(n):
#     new_dic[i] = nums[i]

# #removing duplicates 

# # my_set = set(nums)
# # nums = list(my_set)

# l2 = []

# for i in range(len(nums)):
#     if 