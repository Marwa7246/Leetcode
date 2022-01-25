class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")", 
            "{": "}", 
            "[": "]" 
        }
        arr=[]
        for x in s:
            if x in map:
                arr.append(map[x])
            else:
                if len(arr) == 0:
                    return False
                elif x == arr[-1]:
                    arr.pop()
                else:
                    return False                    
        return len(arr) == 0
print(Solution().isValid("[(])]"))
