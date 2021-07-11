def validIPAddress(IP):
        """
        :type IP: str
        :rtype: str
        """
        ip4 = IP.split('.')
        ip6 = IP.split(':')
        ipl4 = len(ip4)
        ipl6 = len(ip6)

        if ipl4 == 4:
            for i in range(ipl4):
                if len(ip4[i]) > 1 and ip4[i].startswith('0'):
                    return "Neither"
                try:
                    num = int(ip4[i])
                    if num < 0 or num > 255:
                        return "Neither"
                except ValueError:
                    return "Neither"

            return 'IPv4'
        elif ipl6 == 8:
            for i in range(ipl6):
                if len(ip6[i]) > 4:
                    return "Neither"
                try:
                    num = int(ip6[i], 16)
                except ValueError:
                    return "Neither"
            return 'IPv6'
        else:
            return "Neither"


"""
OG solution
import re
class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 
"""