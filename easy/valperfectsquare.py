class Solution(object):
    def isPerfectSquare(self, num):
        x = num
        left = 0
        right = x

        
        while (left <= right):
            middle = (left + right) // 2
          
            if middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1

            else:
                return True
        return False
        