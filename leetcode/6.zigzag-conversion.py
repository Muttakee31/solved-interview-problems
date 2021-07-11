def convert(s, numRows):
    n = len(s)
    dic = dict()
    incr = 0
    flag = 1
    for i in range(n):
        if incr not in dic.keys():
            dic[incr] = ''
        dic[incr] += s[i]
        incr += flag
        if incr == 0 or incr == numRows-1:
            flag *= -1
    ans = ''
    for value in dic.values():
        ans += value
    
    return ans