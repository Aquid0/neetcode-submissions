import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True