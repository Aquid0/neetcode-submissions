class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(left, right): 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
 
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            ans = max(odd, even, ans, key=len)

        return ans