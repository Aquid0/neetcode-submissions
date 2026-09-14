from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = deque()
        ans = -1

        for i in range(len(s)):
            if s[i] not in x:
                x.append(s[i])
            else:
                ans = max(ans, len(x))
                while len(x) and x[0] != s[i]: # keep popping off x until we reach the duplicated character
                    x.popleft()
                x.popleft()
                x.append(s[i])
        
        # x might have elements in it
        ans = max(ans, len(x))

        return ans
