from collections import deque
deq = deque()


def bfs(graph, start_node, visited):
    global deq
    visited[start_node] = True
    deq.append(start_node)

    while deq:
        pop_node = deq.popleft()
        print(pop_node, end=' ')

        for i in graph[pop_node]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)


    # global deq
    #
    # visited[start_node] = True
    # deq.append(start_node)
    #
    # while deq:
    #     pop_node = deq.popleft()
    #     print(str(pop_node), end=' ')
    #
    #     for i in graph[pop_node]:
    #         if not visited[i]:
    #             deq.append(i)
    #             visited[i] = True



if __name__ == '__main__':
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    visited = [False] * 9
    bfs(graph, 1, visited)