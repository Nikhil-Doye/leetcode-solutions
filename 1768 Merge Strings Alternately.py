class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op = []
        for i, j in zip(word1, word2):
            op.append(i+j)
        if len(word1)>len(word2):
            op.append(word1[-(len(word1) - len(word2)):])
        if len(word1) < len(word2):
            op.append(word2[-(len(word2) - len(word1)):])
        return "".join(op)