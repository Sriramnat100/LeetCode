class Solution(object):
    def mySqrt(self, x):
        
        left = 0
        right = x 
        l1 = []
        if x == 1 or x == 0:
            return x
        while (left <= right):
            middle = (left + right) // 2
          
            if middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1
                l1.append(middle)
            else:
                return middle
        return l1[-1]
