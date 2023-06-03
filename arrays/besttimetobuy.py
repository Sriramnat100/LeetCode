##Part 1 
# prices = []
# subtracter = []
# subtracter = prices[:]
# sales = []
# for i in range(len(prices)):
#     for x in subtracter:
#         if x-prices[i] >= 0:
#             sales.append(x - prices[i])
#     subtracter.pop(0)

# if len(sales) == False:
#     print(0)
# else:
#     print(max(sales))







#Part 2
# Loop once, look for the max and split into two different o
# prices = [7,6,4,3,1]
# new_list = []

# if prices.index(max(prices)) == 0:
#     prices.pop(prices.index(max(prices)))

#     if prices.index(max(prices)) > prices.index(min(prices)):
#         print(max(prices)-min(prices))
        
#     else:
#         for i in range(0,(prices.index(max(prices))+1)):
#             new_list.append(prices[i])
#             prices.pop(i)

# if (max(prices)) - (min(prices)) >= 0:
#     print(max(prices)-min(prices))

# elif (max(new_list)-min(new_list)) >= 0:
#     print(max(new_list)-min(new_list))

# else:
#     print(0)
# print(max(prices)-min(prices))

##Part 3
prices = [7,1,5,3,6,4]
init_min = prices[0]
current_sale = 0
for i in prices:
    if i < init_min:
        init_min = i
    elif i - init_min > current_sale:
        current_sale = i - init_min

if current_sale <= 0:
    print(0)
else:
    print(current_sale)
    