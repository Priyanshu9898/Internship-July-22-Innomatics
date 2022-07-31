class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        mul = 1
        sum = 0
        
        while(n > 0):
            rem = int(n % 10)

            mul = mul * rem
            sum = sum + rem
            
            n = int(n / 10)
        
        

        return (mul - sum)