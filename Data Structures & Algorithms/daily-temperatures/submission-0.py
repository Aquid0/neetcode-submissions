class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = list(enumerate(temperatures))
        res = [0 for _ in range(len(temperatures))]
        
        while temps:
            curr = temps.pop(0)
            
            while len(stack) > 0 and stack[-1][1] < curr[1]:
                setDay = stack.pop()
                res[setDay[0]] = curr[0] - setDay[0]
            
            stack.append(curr)
        
        return res

            

