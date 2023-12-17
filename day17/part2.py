from aocd import get_data
from heapq import heappop, heappush

dataRaw = get_data(year=2023, day=17)
data = [[int(y) for y in x] for x in dataRaw.split("\n")]

start = (0, 0)
target = (len(data[0]) - 1, len(data) - 1)

# Down, Right, Up, Left.
# directions are rotated so we can determine easily which one is reverse direction
neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def inside_data_grid(pos, d):
    return 0 <= pos[0] < len(d) and 0 <= pos[1] < len(d[0])


def dijkstra(min_dist, max_dist):
    # cost, x, y, dont_go_direction
    # cost has to be first in order for heapq to work properly
    queue = [(0, 0, 0, -1)]
    seen = set()
    while len(queue) > 0:
        cost, x, y, dgd = heappop(queue)

        # Reached the end: return the cost.
        # prioritized queue makes sure its the least.
        if (x, y) == target:
            return cost

        # if the position and direction have been seen, then there is no need to search further.
        # Since heapq ensures that this queue is prioritized.
        # Cost will therefore always be higher.
        if (x, y, dgd) in seen:
            continue

        seen.add((x, y, dgd))
        for neighbor in range(4):
            # can't go in the direction or opposite of the direction. Can only turn.
            if neighbor == dgd or (neighbor + 2) % 4 == dgd:
                continue

            extra_cost = 0

            # 1, 2, ... max_dist times in the direction and add to queue if the distance is at least the min_dist.
            # Ensures that the next node always has to turn 90 degrees to not duplicate nodes.
            for distance in range(1, max_dist + 1):
                nx = x + neighbors[neighbor][0] * distance
                ny = y + neighbors[neighbor][1] * distance
                if inside_data_grid((nx, ny), data):
                    extra_cost += data[nx][ny]
                    new_cost = cost + extra_cost

                    if distance < min_dist:
                        continue

                    heappush(queue, (new_cost, nx, ny, neighbor))


print(dijkstra(4, 10))
