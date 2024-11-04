from collections import defaultdict
import heapq


def network_delay_time(times: list[int], n: int, k: int):
    adjacency = defaultdict(list)
    for start, end, time in times:
        adjacency[start].append((end, time))

    visited = set()
    delay = 0
    nodes_heap = []
    heapq.heappush(nodes_heap, (delay, k))

    while len(nodes_heap) > 0:
        time, current = heapq.heappop(nodes_heap)
        if current in visited:
            continue
        visited.add(current)
        delay = max(delay, time)
        neighbours = adjacency[current]

        for neighbour, neighbour_time in neighbours:
            if neighbour in visited:
                continue
            new_time = time + neighbour_time
            heapq.heappush(nodes_heap, (new_time, neighbour))
    if len(visited) == n:
        return delay
    return -1
