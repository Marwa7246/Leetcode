class Solution:
    def longestCommonPrefix(self, strs):
        lengths = map(lambda str: len(str), strs)
        minLength = min(lengths)
        ref = strs[0]
        result = ""
        for i in range(minLength):
            for str in strs:
                if str[i] != strs[0][i]:
                    return result
            result += str[i]
        return result


print(Solution().longestCommonPrefix(["dog","racecar","car"]))