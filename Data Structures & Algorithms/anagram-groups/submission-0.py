class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            tracker[tuple(sorted(word))].append(word)
        
        res = []
        for word_list in tracker.values():
            res.append(word_list)
        
        return res