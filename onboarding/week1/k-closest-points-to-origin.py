class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ''' Approach: Sorting
        step1: create a default dictionary to store the distances along
        with their corresponding indices
        step2: sort the distances array
        step3: iterate k times through the sorted array and use the indices
        to append points to the answer list
        '''
        counter = defaultdict(list)
        dis =[]
        ans = []
        for index in range(len(points)):
            x,y = points[index][0],points[index][1]
            distance = x**2+y**2
            counter[distance]+=[index]
            dis.append(distance)
        dis.sort()
        i=0
        while i<k:
            index = counter[dis[i]]
            for j in index:
             ans.append(points[j])
             i+=1
        return ans
        #Time Complexity: O(n)
        #Space Complexity: O(n)