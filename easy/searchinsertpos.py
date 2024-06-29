nums = [1,3,5,6,7,8,9,10]

#sss = [0,1,2,3,4,5,6, 7, 8, 9]

target = 4


def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    middle = int((left + right) / 2)

    while (nums[middle] != target):
        middle = int((left + right) / 2)

        if left > right:
            return left

        if target > nums[middle]:
            left = middle + 1
        
        
        elif target < nums[middle]:
            right = middle - 1
            
   
print(binary_search(nums, target))