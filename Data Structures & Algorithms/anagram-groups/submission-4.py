class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for word in strs:
            word_count = [0] * 26
            for char in word:
                word_count[ord(char)-ord('a')] += 1
            key = tuple(word_count)
            if key not in count:
                count[key] = []
            count[key].append(word)
        
        return [val for val in count.values()]