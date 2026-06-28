class TimeMap:

    def __init__(self):
        self.store = {}
        self.last_time = -1   

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        self.last_time = timestamp
        

    def get(self, key: str, timestamp: int) -> str:
        if self.last_time == -1:
            return ""
        values = self.store.get(key,[])

        l = 0
        r = len(values) - 1
        prev_time = -1

        while l <= r:
            m = (l+r)//2

            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m -1
            else:
                l = m + 1
                prev_time = m
        if prev_time != -1:
            return values[prev_time][0]
        else:
            return ""
        
