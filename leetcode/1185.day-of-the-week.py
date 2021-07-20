from datetime import datetime

class Solution:
    """
    https://leetcode.com/problems/day-of-the-week/
    """
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = datetime.date(year, month, day)
        return d.strftime("%A")