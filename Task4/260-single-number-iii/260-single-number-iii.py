class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if(n == 1):
            return nums
        
        ans = []
        nums = sorted(nums)
        
        
        
        for i in range(0 , n):

            if( i == 0):
                if(nums[i] != nums[i+1]):
                    ans.append(nums[i])
                
            elif(i == n-1):
                if(nums[i-1] != nums[i]):
                    ans.append(nums[i])
            
            elif( (i != 0) & (i != n-1) & (nums[i] != nums[i-1]) & (nums[i] != nums[i+1]) ):
                ans.append(nums[i])
        
        return ans