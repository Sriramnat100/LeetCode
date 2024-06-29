s = "MCMXCIV"
sum = 0
new_l1 = []
roman_dic = {"I": 1, "V": 5, "X": 10, 
                "L": 50, "C": 100, "D": 500, "M": 1000}

for i in s:
    new_l1.append(roman_dic[i])

for ind in range(1, len(new_l1) - 1):
    #the gay cases
    if (new_l1[ind] < new_l1[ind - 1]):
        sum -= abs(new_l1[ind] - new_l1[ind+1])

    else:
        sum +=

print(new_l1,sum)