class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        used=[False for _ in range(len(baskets))]
        unplaced=0
        for fruit in fruits:
            placed=False
            for i in range(len(baskets)):
                if not used[i] and baskets[i]>=fruit:
                    used[i]=True
                    placed=True
                    break
            if not placed:
                unplaced+=1
        return unplaced