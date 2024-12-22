class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        min_length = 100000000
        for s in strs:
            min_length = min(min_length, len(s))

        for i in range(min_length):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res