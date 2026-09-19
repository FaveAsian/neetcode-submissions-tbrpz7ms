class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char)%26] += 1
            tracker[tuple(freq)].append(word)
        
        return list(tracker.values())