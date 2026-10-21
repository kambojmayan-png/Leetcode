
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            time, value = values[mid]

            if time <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1

        return res
