class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k = []
        dict_ran = Counter(ransomNote)
        dict_mag = Counter(magazine)
        for key in dict_ran:
            if key not in dict_mag:
                return False
            if dict_ran[key] <= dict_mag[key]:
                k.append(True)
            else:
                return False
        return bool(sum(k))