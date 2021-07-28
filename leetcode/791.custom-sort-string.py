class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        https://leetcode.com/problems/custom-sort-string/
        """
        letter_weights = [26]*26
        w = 1
        for o in order:
            letter_weights[ord(o) - 97] = w
            w += 1

        li = list(s)
        li.sort(key=lambda x: letter_weights[ord(x)-97])
        # print(li)
        return "".join(li)
        