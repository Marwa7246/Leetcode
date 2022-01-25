class Solution:
    def romanToInt(self, s: str) -> int:
            conv = {
                "I":             1,
                "V":             5,
                "X":             10,
                "L":             50,
                "C":             100,
                "D":             500,
                "M":             1000,
            }
            result =0
            print(len(s))
            for i in range(len(s)):
                if i == len(s)-1:
                    result += conv[s[i]] 
                    break
                print(i, conv[s[i+1]] , conv[s[i]])
                if (conv[s[i+1]] > conv[s[i]]):
                    result -= conv[s[i]]
                else:
                    result += conv[s[i]]
            return result

print(Solution().romanToInt("XIV"))