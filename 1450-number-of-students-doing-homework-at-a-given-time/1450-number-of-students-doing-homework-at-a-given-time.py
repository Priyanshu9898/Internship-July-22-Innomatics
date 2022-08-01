class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        n = len(startTime)
        ans = 0
        i = 0
        while(i < n):
           
            
            if((startTime[i] <= queryTime) &  (endTime[i] >= queryTime)):
                ans+=1
                
            i+=1
            
        return ans