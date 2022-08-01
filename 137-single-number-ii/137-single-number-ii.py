class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        
        n = len(nums)
        
        if(n == 1):
            return nums[0]
        
        for i in range(0 , n):

            if( i == 0):
                if(nums[i] != nums[i+1]):
                    return nums[i]
                
            elif(i == n-1):
                if(nums[i-1] != nums[i]):
                    return nums[i]
            
            elif( (i != 0) & (i != n-1) & (nums[i] != nums[i-1]) & (nums[i] != nums[i+1]) ):
                return nums[i]
        
        return 0