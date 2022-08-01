class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        lst = [start+2*i for i in range(n)] # create a list with the given start upto 'n'
        ans = lst[0] # take the first element as the ans
        for i in range(1,n):
            ans ^=lst[i] # BITWISE operater XOR
        return ans