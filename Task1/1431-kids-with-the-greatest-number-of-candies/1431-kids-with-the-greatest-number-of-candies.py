class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxNum = max(candies)
        
        ans = []
        
        for i in candies:
            if(i + extraCandies >= maxNum):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans