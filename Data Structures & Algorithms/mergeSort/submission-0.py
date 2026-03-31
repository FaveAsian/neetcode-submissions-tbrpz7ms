# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        # split  
        m = len(pairs)//2
        left = self.mergeSort(pairs[0:m])
        right = self.mergeSort(pairs[m:])
        # merge
        res = []
        l_idx, r_idx = 0, 0
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx].key <= right[r_idx].key:
                res.append(left[l_idx])
                l_idx += 1
            else:
                res.append(right[r_idx])
                r_idx += 1
        
        while l_idx < len(left):
            res.append(left[l_idx])
            l_idx += 1
        
        while r_idx < len(right):
            res.append(right[r_idx])
            r_idx += 1

        return res
