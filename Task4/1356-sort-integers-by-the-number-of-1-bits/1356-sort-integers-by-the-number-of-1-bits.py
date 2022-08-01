class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        s=[[bin(arr[x]).replace("0b","").count('1'),arr[x]]  for x in range(0,len(arr))]
        
        s.sort()
        #print(s)
        return [ x[1] for x in s]