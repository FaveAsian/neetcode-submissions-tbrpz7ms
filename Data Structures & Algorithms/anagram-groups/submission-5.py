class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            word_count = [0] * 26
            for char in word:
                word_count[ord(char)-ord('a')] += 1
            count[tuple(word_count)].append(word)
        
        return list(count.values())