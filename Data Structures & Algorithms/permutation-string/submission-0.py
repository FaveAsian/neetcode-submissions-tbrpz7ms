class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # count the number of characters in s1
        count = 0
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')] += 1
            s2_freq[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        # See how many matches
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # remove the left pointer
            old_letter = ord(s2[l])-ord('a')
            if s1_freq[old_letter] == s2_freq[old_letter]:
                matches -= 1
            s2_freq[old_letter] -= 1
            l += 1
            if s1_freq[old_letter] == s2_freq[old_letter]:
                matches += 1

            # add the current pointer
            new_letter = ord(s2[r])-ord('a')
            if s1_freq[new_letter] == s2_freq[new_letter]:
                matches -= 1
            s2_freq[new_letter] += 1
            
            if s1_freq[new_letter] == s2_freq[new_letter]:
                matches += 1
        if matches == 26:
            return True        

        return False