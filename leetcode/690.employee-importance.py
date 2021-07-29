class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    
    def findEmployee(self, employees: List['Employee'], id: int) -> Employee:
        e = list(filter(lambda x: x.id == id, employees))[0]
        return e
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        https://leetcode.com/problems/employee-importance/
        should have used a dictionary to reduce search cost.
        """
        emp = self.findEmployee(employees, id)
        q = list()
        q.append(emp)
        importance = emp.importance
        while len(q) != 0:
            first = q.pop(0)
            for id in first.subordinates:
                temp = self.findEmployee(employees, id)
                q.append(temp)
                importance += temp.importance
    
        return importance