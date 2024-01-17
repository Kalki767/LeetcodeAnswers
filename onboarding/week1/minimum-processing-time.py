class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        k = len(tasks)-1
        minimum = 0
        for i in processorTime:
            minimum = max(minimum,i+tasks[k])
            k-=4
        return minimum
        