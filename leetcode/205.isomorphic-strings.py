class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_letters = dict()
        t_letters = dict()
        for i in range(len(s)):
            if s[i] not in s_letters.keys():
                s_letters[s[i]] = [0, '']
            s_letters[s[i]][0] += 1
            s_letters[s[i]][1] += str(i)
        
        for i in range(len(t)):
            if t[i] not in t_letters.keys():
                t_letters[t[i]] = [0, '']
            t_letters[t[i]][0] += 1
            t_letters[t[i]][1] += str(i)
        
        csl = list(zip(s_letters.values()))
        ctl = list(zip(t_letters.values()))
        csl.sort()
        ctl.sort()
        if len(csl) != len(ctl):
            return False
        # print(csl)
        # print(ctl)
        for i in range(len(csl)):
            if csl[i] != ctl[i]:
                return False
        
        return True

    """
    better solution. just make a pattern from the string and check if the patterns match     
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
    """