class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost_step = float('inf')
        my_step = abs(target[0])+abs(target[1])
        for i in ghosts:
            ghost_step = min(ghost_step,abs(target[0]-i[0])+abs(target[1]-i[1]))
        return ghost_step>my_step