class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        left = nums[0: n]
        right = nums[n: ]
        
        for i in range(n):
            ans.append(left[i])
            ans.append(right[i])
        
        return ans