
# def multiplyer(list):
#     product = 1
#     for i in list:
#         product = product * i
#     return product

# nums = [-1,1,0,-3,3]
# new_nums = tuple(nums[:])

# #Created a duplicate list

# products = []
# for i in new_nums:
#     nums.remove(i)
#     products.append(multiplyer(nums))
#     nums = list(new_nums)
# print(products)
# def prefgen(lst):
#     empt = []
#     n = 0
#     for i in lst:
#         n = n+i
#         empt.append(n)
#     return empt


#vals is the array ur given
#qrys is a 2d array, representing each query
# so qrys[i][0] = l, qrys[i][1] = r

#vals: 5, 2, 1, 3, 4, 5, 6
#qrys: [[1, 2], [1, 5], [3, 6], [2, 4], [0, 3]]
#intended output: [3, 21, 18, 8, 11]

# def solve(vals, qrys):
#     l1 = []
#     for i in qrys:
#         #

nums = [1,2,3,4]
temp_pre = 1
temp_suf = 1
arr_pre = []
arr_suf = []
final_arr = []
#array of prefixes
for i in nums:
    temp_pre = temp_pre * i
    arr_pre.append(temp_pre)
#remove last term in list
arr_pre.pop()

#array of suffixes
for i in reversed(nums):
    temp_suf = temp_suf * i
    arr_suf.append(temp_suf)
#remove last term in list
arr_suf.pop()

for i in range(len(nums)):
    if i == 0:
        final_arr.append(arr_suf[len(arr_pre)-1])
    elif i == (len(nums)-1):
        final_arr.append(arr_pre[i-1])

    else:
        final_arr.append(arr_pre[i-1]*arr_suf[len(arr_pre)-i-1])

print(final_arr)



# def multiply_all(lst):
#     if len(lst) == 0:
#         return 1
#     else:
#         return lst[0] * multiply_all(lst[1:])

# new_nums = tuple(nums[:])
# products = []
# for i in new_nums:
#     nums.remove(i)
#     products.append(multiply_all(nums))
#     nums = list(new_nums)
# print(products)