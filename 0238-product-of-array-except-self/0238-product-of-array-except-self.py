class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LENGTH = len(nums)
        res = [1] * LENGTH

        # prefix array; nums[i] after this loop will be the product of all elements before index i
        factor = 1 # multiplying factor based on product of elements before index i
        for i in range(LENGTH):
            res[i] *= factor
            factor *= nums[i]
        
        # multiplying by postfix array; nums[i] after this loop will be the product of all elements in the array except self
        factor = 1 # multiplying factor based on product of elements after index i
        for i in range(LENGTH - 1, -1, -1):
            res[i] *= factor
            factor *= nums[i]
        
        return res
        
        