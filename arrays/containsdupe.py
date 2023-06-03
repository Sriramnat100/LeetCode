nums = [1,2,3,4]
nums = sorted(nums)
if len(nums) <= 1:
    print(False)
else:
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            print(True)
        else:
            continue
    print(False)