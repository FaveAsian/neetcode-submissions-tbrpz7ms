class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = ""
        res = 0
        count = 0
        i = 0
        input_idx = 0

        while i < len(chars):
            if chars[i] == prev:
                count += 1
            else:
                if prev != "":
                    chars[input_idx] = prev
                    input_idx += 1
                    res += 1
                if count > 1:
                    for num in str(count):
                        chars[input_idx] = num
                        input_idx += 1
                        res += 1
                prev = chars[i]
                count = 1
            i += 1
        
        chars[input_idx] = prev
        input_idx += 1
        res += 1
        if count > 1:
            for num in str(count):
                chars[input_idx] = num
                input_idx += 1
                res += 1

        return res