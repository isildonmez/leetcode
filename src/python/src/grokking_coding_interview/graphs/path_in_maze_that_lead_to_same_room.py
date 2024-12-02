from collections import defaultdict


def number_of_paths(n, corridors):
    score = 0
    room_connections = defaultdict(set)
    for r1, r2 in corridors:
        room_connections[r1].add(r2)
        room_connections[r2].add(r1)
        score += len(room_connections[r1] & room_connections[r2])
    return score
