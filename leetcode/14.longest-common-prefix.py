def longestCommonPrefix(self, strs):
        """
        https://leetcode.com/problems/longest-common-prefix
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        template = strs[0]
        count = float('inf')
        for i in range(1, len(strs)):
            j = 0
            min_len = min(len(template), len(strs[i]))
            while(j < min_len and template[j] == strs[i][j]):
                j+=1
            if j < count:
                count = j
                
        return template[:count]

        """
        def rotate(self, A):
            A[:] = zip(*A[::-1])
        """