class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0): return False
        y = [int(i) for i in str(x)]
        for j in range(len(y)):
            print(j,y[j] , y[len(y)-1-j])
            if (y[j] !=y[len(y)-1-j]):
                return False
        return True
print (Solution().isPalindrome(121))