class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(left, right, searchVal):
            while left <= right:
                m = (left + right) // 2 
                if numbers[m] == searchVal:
                    return m
                elif numbers[m] < searchVal: # Our current number is less than the target, so target is in second half
                    left = m + 1
                else:
                    right = m - 1
            return False
        
        for i in range(len(numbers)):
            num = numbers[i]
            found = binarySearch(i+1, len(numbers)-1, target-num)
            if found:
                return [i+1, found+1]
        return [0, 0]
        
