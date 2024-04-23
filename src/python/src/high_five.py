from collections import defaultdict
import heapq as hq

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores_by_ids = defaultdict(default_scores)
        for id, score in items:
            hq.heappushpop(scores_by_ids[id], score)
        sorted_ids = sorted(scores_by_ids.keys())
        for i, id in enumerate(sorted_ids):
            sorted_ids[i] = [id, sum(scores_by_ids[id]) // 5]
        return sorted_ids
    
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        mapper = defaultdict(list)
        for sid, score in items:
            hq.heappush(mapper[sid], score)
            if len(mapper[sid]) > 5:
                hq.heappop(mapper[sid])
        return sorted((map(lambda x: [x[0] , sum(x[1])//5], mapper.items())))


def default_scores():
    return [0] * 5


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]) == [[1,87],[2,88]]
    assert s.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]) == [[1,100],[7,100]]
    print("Done!")

