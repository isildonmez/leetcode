# https://leetcode.com/problems/queue-reconstruction-by-height/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for height, idx in people:
            queue.insert(idx, [height, idx])
        return queue
