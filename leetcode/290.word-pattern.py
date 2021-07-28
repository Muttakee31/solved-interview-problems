class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = dict()
        
        x = s.split()
        i = j = 0
        pen = sen = ""
        di = dict()
        ic = dict()
        if len(x) != len(pattern):
            return False
        for p in pattern:
            if p not in di.keys():
                di[p] = i
                i += 1
            pen += str(di[p]) +" "
        
        for t in x:
            if t not in ic.keys():
                ic[t] = j
                j += 1
            sen += str(ic[t]) +" "
        

        return True if pen == sen else False