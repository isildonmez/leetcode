# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/


import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        direct_flights = [[] for _ in range(n)]
        for flight in flights:
            start, end, price = flight
            direct_flights[start].append((end, price))
        stops = [float(inf) for _ in range(n)]
        stops[src] = 0
        min_heap = []
        # dist_from_source_node, node, num_of_stops_from_src_node = 0, src, 0
        heapq.heappush(min_heap, (0, src, 0))

        while len(min_heap) > 0:
            dist, node, steps = heapq.heappop(min_heap)
            if steps > stops[node] or steps > k:
                continue
            stops[node] = steps
            if node == dst:
                return dist
            for neighbour, price in direct_flights[node]:
                heapq.heappush(min_heap, (dist + price, neighbour, steps + 1))
        return -1
