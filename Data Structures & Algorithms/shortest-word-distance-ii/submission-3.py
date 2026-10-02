class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_pos = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_pos[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1_pos = self.word_pos[word1]
        word2_pos = self.word_pos[word2]
        n, m = len(word1_pos), len(word2_pos)
        i, j = 0, 0
        res = float('inf')

        while i < n and j < m:
            pos1 = word1_pos[i]
            pos2 = word2_pos[j]
            res = min(res, abs(pos1-pos2))
            if res == 1:
                return 1
            if pos1 < pos2:
                i += 1
            else:
                j += 1

        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
