class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = [0] * len(positions)
        parent = {}
        count = 0

        for i in range(len(positions)):
            row, col = positions[i]
            if (row, col) in parent:
                res[i] = count
                continue
            parent[(row, col)] = (row, col)
            count += 1
            num_merge = self.merge(row, col, parent, m, n)
            count -= num_merge
            res[i] = count

        return res
    
    def find(self, index: tuple[int, int], parent):
        if parent[index] != index:
            parent[index] = self.find(parent[index], parent)
        
        return parent[index]
    
    def merge(self, row, col, parent, m, n):
        cardinals = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        parent_root = self.find((row, col), parent)
        num_merge = 0
        for rx, cx in cardinals:
            if not (0 <= row+rx < m and 0 <= col+cx < n):
                continue
            if (row+rx, col+cx) not in parent:
                continue
            neighbor_root = self.find((row+rx, col+cx), parent)
            if neighbor_root != parent_root:
                parent[parent_root] = neighbor_root
                num_merge += 1
                parent_root = self.find((row, col), parent)
        return num_merge
            
    