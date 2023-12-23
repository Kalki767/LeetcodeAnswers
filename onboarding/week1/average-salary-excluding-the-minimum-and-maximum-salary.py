class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        average = (total-min(salary)-max(salary))/(len(salary)-2)
        return average