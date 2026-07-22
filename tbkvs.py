#Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.timemap.get(key, 0) :
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timemap.get(key, 0):
            return ""
        l, r = 0, len(self.timemap[key]) - 1

        while l < r:
            m = l + (r - l) // 2
            
            if timestamp < self.timemap[key][m][1]:
                r = m - 1
            else:
                if m < r and timestamp >= self.timemap[key][m + 1][1]:
                    l = m + 1
                else:
                    return self.timemap[key][m][0]

        return "" if timestamp < self.timemap[key][l][1] else self.timemap[key][l][0]


