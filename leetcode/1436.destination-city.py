class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        di = dict()
        for p in paths:
            if p[0] not in di.keys():
                di[p[0]] = ""
            if p[1] not in di.keys():
                di[p[1]] = ""
            
            di[p[0]] = p[1]
        
        for k,v in di.items():
            if v == "":
                return k