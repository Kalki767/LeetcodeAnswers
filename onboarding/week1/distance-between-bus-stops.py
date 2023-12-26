class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination>=start:
            first_sum= sum(distance[start:destination])
            second_sum = sum(distance[0:start])+sum(distance[destination:])
        else:
            first_sum= sum(distance[destination:start])
            second_sum = sum(distance[0:destination])+sum(distance[start:])
        return min(first_sum,second_sum)