class TimeMap(object):

    def __init__(self):
        self.hashmap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.hashmap:
            self.hashmap[key] = []

        self.hashmap[key].append([value,timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = -1

        if key not in self.hashmap:
            return ""

        l,r = 0,len(self.hashmap[key])-1

        while l <= r:

            mid = (l + r)/2

            if self.hashmap[key][mid][1] == timestamp:
                return self.hashmap[key][mid][0]

            elif self.hashmap[key][mid][1] > timestamp:
                r = mid - 1

            else:
                res = mid 
                l = mid + 1


        return self.hashmap[key][res][0] if res != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)