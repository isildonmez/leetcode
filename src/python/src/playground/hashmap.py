from typing import Any


class Bucket:
    def __init__(self):
        self.bucket = []
        # [(k, v),...]

    # Assuming key exists for simplicity
    def get(self, key: Any) -> Any:
        for k, v in self.bucket:
            if k == key:
                return v

    def update(self, key: Any, value: Any) -> None:
        found = False
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key: Any) -> Any:
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]
                break


# For the simplicity I'm assuming both key and value as str
class HashMap:
    def __init__(self) -> None:
        self.mod = 2069
        self.buckets = [Bucket() for _ in range(self.mod)]

    # You may use hash() function in python instead
    def _simple_hashing(self, key: str) -> int:
        hash_val = 0
        for c in key:
            hash_val = hash_val * 31 + ord(c)
        return hash_val

    def put(self, key: str, value: str) -> None:
        k = self._simple_hashing(key)
        bucket = self.buckets[k % self.mod]
        bucket.update(k, value)

    def get(self, key: str) -> str:
        k = self._simple_hashing(key)
        bucket = self.buckets[k % self.mod]
        return bucket.get(k)

    def remove(self, key: str) -> None:
        k = self._simple_hashing(key)
        bucket = self.buckets[k % self.mod]
        bucket.remove(k)
