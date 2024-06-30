
# MMMDCCXLIX

# 3000 -> MMM
# 700 -> DCC
# 40 -> XL
# 9 -> IX
# 900 -> CM

#First solution by me, second insporation/guidance from neetcode
def goman(num):
    new_dic = {"1": "I", "5": "V", 
               "10": "X", "50": "L", 
               "100": "C", "500": "D",
               "1000": "M", "5000": "N"}
     
    num = str(num)
    digits = len(num)
    y = ""
    for i in num:
        power = (10 ** (digits-1))
        fivex = new_dic[str(power * 5)]
        tenx = new_dic[str(power)]


        if int(i) < 4 and int(i) >=1:
            y = y + tenx * int(i)
        elif int(i) > 4 and int(i) < 9:
            y = y + fivex + tenx * (int(i) - 5)
        else:
            if int(i) == 4:
                y = y + tenx + fivex
            elif int(i) == 9:
                y = y + new_dic[str(power)] + new_dic[str(power*10)]

        digits -=1
    return y


num = 3749
def goman(num):
    roman_numerals_list = [
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M")
]

    x = len(roman_numerals_list) - 1
    y = ""
    while (num != 0):
        n = num // roman_numerals_list[x][0]
        y = y + roman_numerals_list[x][1] * n
        if ((num % roman_numerals_list[x][0] * n) != num) and (n!= 0):
            num = num % (roman_numerals_list[x][0] * n)
     
        x -=1

    return y
