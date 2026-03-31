class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        hand.sort()

        # [1 2 2 3 3 4 4 5]
        # [1, 2, 3, 4]
        # [2, 3, 4, 4]
        groups = [[] for _ in range(n//groupSize)]
        for num in hand:
            added = False
            for group in groups:
                if not group:
                    added = True
                    group.append(num)
                    break
                elif (group[-1]+1) == num and len(group) < groupSize:
                    added = True
                    group.append(num)
                    break
                else:
                    continue
            if not added:
                return False

        return True