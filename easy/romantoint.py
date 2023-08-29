#convert roman numbers to list of numbers
class Solution(object):
    def romanToInt(self, s):

        uncint = []
        new_uncint = []
        l1 = []

        for i in s:
            uncint.append(i)

        for i in range(len(uncint)):
            if uncint[i] == "I":
                new_uncint.append(1)
            elif uncint[i] == "V":
                new_uncint.append(5)
            elif uncint[i] == "X":
                new_uncint.append(10)
            elif uncint[i] == "L":
                new_uncint.append(50)
            elif uncint[i] == "C":
                new_uncint.append(100)
            elif uncint[i] == "D":
                new_uncint.append(500)
            elif uncint[i] == "M":
                new_uncint.append(1000)

        l1 = new_uncint
        str2 = 0
        n = 0

        #Convert list of numbers to actual values
        for i in range(1,len(l1)): 
            #Removing all increasing terms and adding
            if len(l1) > i-n:
                if l1[i-n] > l1[i-1-n]:
                    #str2 is our current value and we add absolute value of difference between terms 1 and 2. 
                    str2 = str2 + abs(l1[i-n]-l1[i-1-n])

                    l1.pop(i-n)
                    l1.pop(i-1-n)
                    n = n + 1
                    
                    if len(l1) == 0 or len(l1) == 1:
                        break

        #adding rest of numbers in list
        str2 = str2 + sum(l1)
