class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_even = (nums[0] % 2) == 0

        for i in range(1, len(nums)):
            parity = nums[i]%2
            if is_even and parity == 1:
                is_even = False
            elif not is_even and parity == 0:
                is_even = True
            else:
                return False
        
        return True