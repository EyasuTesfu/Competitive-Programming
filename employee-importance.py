"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee

        def dfs_sum(employee):
            if not employee.subordinates:
                return employee.importance
            res = employee.importance
            for sub in employee.subordinates:
                emp = employee_dict[sub]
                res += dfs_sum(emp)
            return res

        return dfs_sum(employee_dict[id])