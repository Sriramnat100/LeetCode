nums = [-4,-3,-2]
#sss = [0, 1,2,3, 4,5,6]

max_l1 = []
min_l2 = []

max_l1.append(nums[0])
min_l2.append(nums[0])

for i in range(1, len(nums)):

    if nums[i - 1] == 0:
        max_l1.append(nums[i])
        min_l2.append(nums[i])

    else:
        x = max_l1[-1]
        y = min_l2[-1]
        max_l1.append(max(nums[i], nums[i] * x, nums[i] * y))
        min_l2.append(min(nums[i], nums[i] * x, nums[i] * y))

