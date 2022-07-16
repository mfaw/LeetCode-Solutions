class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hash = set(candyType)
        if len(candyType)//2 <= len(hash):
            return len(candyType)//2
        else:
            return len(hash)
        