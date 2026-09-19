class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        last_seen = "+"
        operator = {"*", "/", "+", "-"}
        s = s.replace(" ", "")
        temp_num = ""
        for char in s:
            if char in operator:
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
            else:
                temp_num += char
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
        return sum(nums)