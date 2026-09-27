class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        while len(s) > 0:
            # Find the number
            pointer = 0
            while s[pointer] != "#":
                pointer += 1

            length = s[:pointer]
            word_start = pointer+1
            word_end = word_start + int(length) 
            res.append(s[word_start:word_end])
            s = s[word_end:]

        return res