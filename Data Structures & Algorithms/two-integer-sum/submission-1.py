class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            if target-nums[i] in nums: 
                a=i
        for j in range(len(nums)):
            if target-nums[a]==nums[j] and a!=j:
                b=j
        return([b,a])
        

                