class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        anss=[]
        def solve(ans,arr,i):
            
            if i==len(arr):
                anss.append(ans)
                return
            solve(ans,arr,i+1)
            solve(ans+[arr[i]],arr,i+1)            
        solve([],nums,0)
        return anss