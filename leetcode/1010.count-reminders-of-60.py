class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
        """
        duration = dict()
        
        for t in time:
            p = t % 60
            if p not in duration.keys():
                duration[p] = 0
            duration[p] += 1
        
        count = 0
        if duration.get(30, 0) and duration[30] > 0:
            count += (duration[30]*(duration[30]-1))//2
            del duration[30]
            
        if duration.get(0, 0) and duration[0] > 0:
            count += (duration[0]*(duration[0]-1))//2
            del duration[0]

            
        for k,v in duration.items():
            _k = 60 - k
            if _k in duration.keys() and duration[k]>0:
                count += duration[k]*duration[_k]
                duration[_k] = duration[_k]*-1
        return count
        