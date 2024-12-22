class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1}
        op = 0
        for i in range(len(s)):
            if i == len(s)-1:
                op = op + dict[s[i]]
            elif dict[s[i]]>=dict[s[i+1]]:
                op = op + dict[s[i]]
            else:
                op = op - dict[s[i]]
        return op