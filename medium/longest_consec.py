nums = [0,3,7,2,5,8,4,6,0,1]
nums = list(set(nums))
nums.sort()
count = 1
max = 1

for i in range(1,len(nums)):
    if (nums[i] == nums[i-1]+1):
        count +=1
    else:
        count = 1
    if count > max:
        max = count

print(max)