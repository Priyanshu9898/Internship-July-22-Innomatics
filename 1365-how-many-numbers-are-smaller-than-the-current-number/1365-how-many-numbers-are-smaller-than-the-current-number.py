class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        
        for i, value in enumerate(sorted(nums)):
            if value not in d:
                d[value] = i
            
        return [d[x] for x in nums]