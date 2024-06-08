class TimeMap:

    def __init__(self):
        # we will use 2 different dict.
        self.value_dict = collections.defaultdict(list) # Map key to all the values
        self.time_dict = collections.defaultdict(list) # Map key to all the timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time_dict[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            current_ts = self.time_dict[key][mid]

            if current_ts == timestamp:
                return self.value_dict[key][mid]
            elif current_ts > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return self.value_dict[key][r] if r >= 0 else ""