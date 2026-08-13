class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        result = []
        i = len(s)
        while i > 0:
            start = max(0, i - k)
            result.append(s[start:i])
            i = start
        result.reverse()
        return "-".join(result)