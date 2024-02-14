class Solution(object):
    def isValid(self, s):
        s = list(s)
        x = []
        for i in s:
            x.append(i)
        
        count = 0

        stack = []
        hash_map = {"(": ")", 
                "{": "}", 
                "[": "]"}

        if len(s) <= 1:
            return False

        for counter, i in enumerate(s):
            if i in hash_map:
                stack.append(i)
                x.pop(counter - count)
                count = count + 1

            elif i in hash_map.values():
                
                if len(stack) > 0:
                    n = stack[-1]
                    if hash_map[n] == i:
                        stack.pop(-1)
                        x.pop(counter - count)
                        count = count + 1
                        

                    else:
                        return False
            

        if len(stack) != 0:
            return False
        elif len(x) != 0:
            return False
        else:
            return True
