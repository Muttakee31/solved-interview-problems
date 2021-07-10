# solved partially, missed one corner case.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = list()
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        i = 0
        while(i < len(s)):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                st.append(s[i])
            elif (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                if len(st) > 0:
                    tp = st[-1]
                    if s[i] == bracket_dict[tp]:
                        st.pop()
                    else:
                        return False
                else:
                    return False
            i += 1
        return True if len(st) == 0 else False
