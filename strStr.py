class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            firstOccur = haystack.index(needle)
            return firstOccur 
        except:
            return -1