# https://leetcode.com/problems/lru-cache/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.data) == self.capacity:
                self.data.popitem(last=False)
            self.data[key] = value
        else:
            self.data[key] = value
            self.data.move_to_end(key)
