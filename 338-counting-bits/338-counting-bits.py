class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(n + 1):
            curr = self.count_one_bits(i)
            result.append(curr)
        
        return result
    
    def count_one_bits(self, num):
        result = 0
        while num:
            result += num & 1
            num >>= 1
        
        return result