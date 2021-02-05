import heapq

INF = int(1e9)


def dijkstra():
    num_city, routes, start = map(int, input().split())
    graph = [[] for i in range(num_city + 1)]  # 여기 문법
    distance = [INF] * (num_city + 1)
    queue = []

    for _ in range(routes):
        x, y, time_taken = map(int, input().split())
        graph[x].append((time_taken, y))

    # 첫 번째 노드 초기화
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    print(graph)
    print()

    while queue:
        # 파이썬 이터레이터 종류
        time, node_num = heapq.heappop(queue)

        if time > distance[node_num]:
            continue

        for i in graph[node_num]:
            if distance[node_num] + i[0] < distance[i[1]]:
                distance[i[1]] = distance[node_num] + i[0]
                heapq.heappush(queue, (distance[i[1]], i[1]))

    return distance


if __name__ == '__main__':
    final_distance = dijkstra()
    # 방문 가능 도시 => Inf 값이 아닌 곳 | 최대 걸리는 시간
    cities = len(final_distance) - final_distance.count(INF) - 1
    max_time = max(final_distance[1:])

    print(cities, end=' ')
    print(max_time)

'''
3 2 1
1 2 4
1 3 2
'''
