class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = []
        sum = 0;
        for i in nums:
            sum += i
            ls.append(sum)
            
        return ls 