class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        s = sorted(set(arr))
        ranks = {x: i+1 for i, x in enumerate(s)}
        return [ranks[x] for x in arr]
