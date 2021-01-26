# 양방향
# 모든 거리는 1
INF = int(1e9)


def dijkstra():
    n, m = map(int, input().split())  # n 은 노드 개수, m은 간선 개수
    distance = [[INF] * (n + 1) for _ in range(n + 1)]  # 최단 경로 테이블

    for i in range(1, n + 1):  # 자기 자신으로 가는 노드들 초기화
        distance[i][i] = 0

    for _ in range(m):  # 그래프 연결 정보
        a, b = map(int, input().split())
        distance[a][b] = 1
        distance[b][a] = 1

    des, stop_by = map(int, input().split())

    for layover in range(1, n + 1):
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                distance[row][col] = min(distance[row][col], distance[row][layover] + distance[layover][col])

    # print(distance)

    final = distance[1][stop_by] + distance[stop_by][des]
    if final >= INF:
        return -1
    else:
        return final


if __name__ == '__main__':
    result = dijkstra()
    print('result : '+str(result))

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

'''
4 2
1 3
2 4
3 4
'''
