class TimeMap:
# IMPORTANT -> we only go to only direction which is right only.
# Need Timestamps either less then required or equal to.
    
    def __init__(self):
        # we will use 2 different dict.
        self.value_dict = collections.defaultdict(list) # Map key to all the values
        self.time_dict = collections.defaultdict(list) # Map key to all the timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 2 sets
        self.value_dict[key].append(value) # check example below how both sets are done
        self.time_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        #Initialize pointers
        l = 0
        r = len(self.time_dict[key]) - 1 
        while l <= r:
            mid = (l + r) // 2
            current_ts = self.time_dict[key][mid]  # get the current timestamps from the time_dict

            if current_ts == timestamp:   # check if curr ts == target ts
                return self.value_dict[key][mid]   # if yes, then use that midpoint to get the value from the value_dict and return that
            
            elif current_ts > timestamp: # too big compare to target_ts so move the right pointer left
                r = mid - 1
            else:                        # opposite
                l = mid + 1
        return self.value_dict[key][r] if r >= 0 else ""


# For Example , if we have the these operations:

set("foo", "bar", 1)
set("foo", "bar2", 4)

get("foo", 3) which should return "bar"
get("foo", 5) which should return "bar2"

Here’s the structures will look after each iterations:

```
After set("foo", "bar", 1): #1st operation
value_dict: {"foo": ["bar"]}
time_dict: {"foo": [1]}

After set("foo", "bar2", 4): # 2nd...
value_dict: {"foo": ["bar", "bar2"]}
time_dict: {"foo": [1, 4]}

and so on
```

```
After get("foo", 3):
l = 0, r = 1, mid = 0, curt_ts = 1 (curt_ts < tar_ts)
l = mid + 1 = 1
l = r + 1 = 2 (r is now out of bounds)
return value_dict["foo"][r] if r >= 0 else "" => return "bar"

After get("foo", 5):
l = 0, r = 1, mid = 0, curt_ts = 1 (curt_ts < tar_ts)
l = mid + 1 = 1
l = r + 1 = 2 (r is now out of bounds)
return value_dict["foo"][r] if r >= 0 else "" => return "bar2"
```
