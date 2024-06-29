nums = [2,2,1,1,1,2,2]
majority_num = nums[0]
count = 0

for i in nums:
    if i == majority_num:
        count +=1
    else:
        count -=1

    if count == 0:
        majority_num = i
        count+=1
print(majority_num)