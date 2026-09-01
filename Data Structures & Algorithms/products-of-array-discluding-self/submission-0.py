class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardPrefSum = list(nums)
        backwardPrefSum = list(nums)

        output = list(nums)

        for i in range(1, len(nums)):
            forwardPrefSum[i] = forwardPrefSum[i-1] * forwardPrefSum[i]

        
        for i in range(len(nums)-2, -1, -1):
            backwardPrefSum[i] = backwardPrefSum[i+1] * backwardPrefSum[i]

        for i in range(len(nums)):
            if i == 0:
                output[i] = backwardPrefSum[i+1]
            elif i == len(nums)-1:
                output[i] = forwardPrefSum[i-1]
            else:
                output[i] = backwardPrefSum[i+1] * forwardPrefSum[i-1]
                
        return output
