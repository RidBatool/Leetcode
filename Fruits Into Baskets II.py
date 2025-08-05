class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n  # Track if a basket is already used
        unplaced = 0

        for i in range(n):  # For each fruit
            placed = False
            for j in range(n):  # Try to find leftmost available basket
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True  # Mark this basket as used
                    placed = True
                    break
            if not placed:
                unplaced += 1  # Could not place this fruit

        return unplaced
