class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        repeated = set() #creating empty set
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                repeated.add(fronts[i]) #adding elements into the created set in which flipping them would result in no change
        front_unique = set(fronts)-repeated #elements in the front where flipping results in change
        back_unique = set(backs)-repeated #elements in the back where flipping results in change
        if len(front_unique)==0 and len(back_unique)==0: # if both the sets are empty return 0
            return 0
        elif len(front_unique)==0: #if one of them is empty return the minimum of the other set
            return min(back_unique)
        elif len(back_unique)==0:
            return min(front_unique)
        return min(min(front_unique),min(back_unique)) #returning the minimum value of the two sets
        