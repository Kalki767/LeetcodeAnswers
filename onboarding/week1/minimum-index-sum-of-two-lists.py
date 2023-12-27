class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l = set(list1)
        a = {}
        ans = []
        for i in list2:
            if i in l:
                index1 = list1.index(i)
                index2 = list2.index(i)
                a[i] = index2+index1
        for i in a:
            if min(a.values())==a[i]:
                ans.append(i)
        return ans