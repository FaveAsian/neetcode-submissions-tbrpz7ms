class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        values = self.kv[key]
        l, r = 0, len(values)-1
        res = ""
        while l <= r:
            m = l + ((r-l)//2) # prevent overflow
            val, ts = values[m]

            if ts == timestamp:
                res = val
                break
            elif ts < timestamp:
                l = m + 1
                res = val
            else:
                r = m - 1
        
        return res