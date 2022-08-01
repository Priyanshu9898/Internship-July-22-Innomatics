class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        
        bx = bin(x).replace('0b','')
        by = bin(y).replace('0b','')
        
        lx = len(bx)
        ly = len(by)
        
        if lx > ly:
            rem_len = lx-ly
            by = by.rjust(lx, '0')
            ly = len(by)
        else:
            rem_len = ly-lx
            bx = bx.rjust(ly, '0')
            lx = len(bx)
            
        i = 0
        j = 0
        diff = 0
        
        while i < lx and j < ly:
            if bx[i] != by[j]:
                diff+=1
            i+=1
            j+=1
        return diff