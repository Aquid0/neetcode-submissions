class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                brackets.append(s[i])
            else:
                if len(brackets) <= 0:
                    return False

                if brackets[-1] == "[" and s[i] == "]":
                    brackets.pop()
                elif brackets[-1] == "{" and s[i] == "}":
                    brackets.pop()
                elif brackets[-1] == "(" and s[i] == ")":
                    brackets.pop()
                else: 
                    return False

        return len(brackets) <= 0