class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtracking(start, split: list):
            # Using an array so len of exactly 4 is a valid IP
            if len(split) == 4 and start >= len(s):
                res.append(".".join(split))
                return
            if start >= len(s):
                return
            # Need to check validity of what is being added
            # No leading zeros. Only zero by itself
            for end in range(1, 4):
                if start+end > len(s):
                    break
                value = s[start:start+end]
                if is_valid(value):
                    split.append(value)
                    backtracking(start+end, split)
                    split.pop()

        def is_valid(ip_num):
            if len(ip_num) == 1 and ip_num[0] == "0":
                return True
            elif len(ip_num) > 1 and ip_num[0] == "0":
                return False
            elif 0 <= int(ip_num) <= 255:
                return True
                
            return False

        backtracking(0, [])
        return res