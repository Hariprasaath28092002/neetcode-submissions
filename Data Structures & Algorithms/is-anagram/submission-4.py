class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount_s = {}
        charCount_t = {}

        for i in range(len(s)):
            charCount_s[s[i]] = charCount_s.get(s[i], 0) + 1 #here s[i] is key if this key is present then we need to get value and append by 1. else not present return 0
            charCount_t[t[i]] = charCount_t.get(t[i], 0) + 1

        return charCount_s == charCount_t     



      