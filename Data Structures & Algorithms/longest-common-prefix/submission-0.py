class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # The prefix of the first word is itself
        res = strs[0]

        for word in strs:
            # Build new prefix base on res
            new_pre = ""
            for i in range(min(len(res), len(word))):
                if res[i] == word[i]:
                    new_pre += word[i]
                else:
                    break
            res = new_pre
        
        return res
