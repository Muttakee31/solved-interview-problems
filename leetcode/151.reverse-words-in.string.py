def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    spl = s.split()
    l = len(spl)
    for i in range(l//2):
        spl[i], spl[l-1-i] = spl[l-i-1], spl[i]
    return "".join(spl)