class TimeMap:

    def __init__(self):
        self.timeMap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append(( value, timestamp ))
        else:
            self.timeMap[key] = [( value, timestamp )]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        vals = self.timeMap[key]

        l = 0
        r = len(vals) - 1

        while l <= r:
            m = (l + r) // 2

            if vals[m][1] == timestamp:
                return vals[m][0]
            elif vals[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return "" if vals[r][1] > timestamp else vals[r][0]      
        
        

        
