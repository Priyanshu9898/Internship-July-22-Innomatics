class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in range(0, len(nums)):
            
            for j in range(i , len(nums)):
                
                
                if ((i < j) & (nums[i] == nums[j])):
                
                    count = count + 1
                    
        return count