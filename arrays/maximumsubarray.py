nums = [1,-1,1]
sum_nums = []
inds = []
final = []
#Creating a list of sums of all numbers
for i in range(1, len(nums)):
    sum_nums.append(nums[i]+nums[i-1])

#Going through the positive numbers
for i in range(len(sum_nums)):
    if sum_nums[i] <= 0:
        continue
    else:
        inds.append(i)

#adding the last, uncounted value into inds
inds.append((inds[-1])+1)

#Creating a new list w/ inds
for i in inds:
    final.append(nums[i])

#checking outputs
if final[0] <= 0:
    final.pop(0)
elif final[-1] <= 0:
    final.pop(-1)
elif final[-1] <= 0 and final[0] <= 0:
    final.pop(-1) and final.pop(0)

print(sum(final))

