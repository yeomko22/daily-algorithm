class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex = 0
        lee = 0
        piles = deque(piles)
        while piles:
            if piles[0] >= piles[-1]:
                alex += piles[0]
                lee += piles[-1]
            else:
                alex += piles[-1]
                lee += piles[0]
            piles.popleft()
            piles.pop()
        if alex > lee:
            return True
        return False