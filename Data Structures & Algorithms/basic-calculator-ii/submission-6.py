class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        last_seen = "+"
        operator = {"*", "/", "+", "-"}
        s = s.replace(" ", "")
        temp_num = ""
        for i, char in enumerate(s):
            if char not in operator:
                temp_num += char
            if char in operator or i == len(s)-1:
                print(temp_num, last_seen)
                if last_seen == "+":
                    nums.append(int(temp_num))
                elif last_seen == "-":
                    nums.append(-int(temp_num))
                elif last_seen == "*":
                    num = nums.pop()
                    nums.append(int(temp_num)*num)
                else:
                    num = nums.pop()
                    nums.append(int(num/int(temp_num)))
                last_seen = char
                temp_num = ""
        return sum(nums)