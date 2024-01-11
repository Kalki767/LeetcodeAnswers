class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 0,len(skill)-1
        product = skill[left]*skill[right]
        Sum = skill[left]+skill[right]
        left+=1
        right-=1
        while left<right:
            if skill[left]+skill[right]!=Sum:
                return -1
            product+=(skill[left]*skill[right])
            left+=1
            right-=1
        return product