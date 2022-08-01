class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        team_total = 0
        for p in range(1, len(rating) - 1):
            # increasing:
            left_less = 0
            right_great = 0
            
            # decreasing:
            left_great = 0
            right_less = 0
            
            pivot = rating[p]
            
            # lh: left half
            for lh in range(p):
                if rating[lh] < pivot:
                    left_less += 1
                elif rating[lh] > pivot:
                    left_great += 1
                    
            # rh: right half
            for rh in range(p+1, len(rating)):
                if rating[rh] > pivot:
                    right_great += 1
                elif rating[rh] < pivot:
                    right_less += 1
                    
            # all combinations of increasing and decreasing teams
            team_total += left_less*right_great + left_great*right_less
        return team_total
        