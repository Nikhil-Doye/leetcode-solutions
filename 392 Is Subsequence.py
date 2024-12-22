class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for both strings
        i, j = 0, 0
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move pointer in s
            if s[i] == t[j]:
                i += 1
            # Always move pointer in t
            j += 1
        
        # If we have traversed all characters in s, it's a subsequence
        return i == len(s)