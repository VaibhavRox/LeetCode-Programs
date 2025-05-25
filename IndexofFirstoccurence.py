class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen=len(haystack)
        needlelen=len(needle)
        if needlelen>haylen:
            return -1
        for i in range(haylen-needlelen+1):
            if haystack[i:i+needlelen]==needle:
                return i
        return -1