
new = []
nums = [-1,-100,3,99]
k = 2


new_nums = nums[:]

for count, val in enumerate(new_nums):
    if count + k >= len(nums):
        nums[(count + k - len(nums)) % len(nums] = val
    else:
        nums[count + k] = val