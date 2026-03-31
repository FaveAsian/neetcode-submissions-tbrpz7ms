class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = pos + speed*time
        # (target-pos)/speed = time

        stack = []
        comb = [pos_speed for pos_speed in zip(position, speed)]
        comb.sort(reverse=True)
        
        for pos, speed in comb:
            t = (target-pos)/speed

            if stack and t <= stack[-1]:
                continue
            stack.append(t)

        return len(stack)