nums = "3322251"
#sss = "01234567"

def rle(nums):
    res = ""
    length = 1
    temp = nums[0]
    for i in range(len(nums)):

        if (i == len(nums)-1):
            res = res + str(length) + nums[i]
            break

        elif (nums[i+1] == temp):
            length +=1

        else:
            res = res + str(length) + nums[i]
            length = 1
            temp = nums[i+1]
    
    return res

print(rle(nums))

# for i in range(1,1):
#     if i == 1:
#         check = rle(str(i))
#     else:
#         check = rle(check)
    
# print(check)