from collections import deque


def dfs(graph, start_node, visited):
    if visited[start_node] == False:
        visited[start_node] = True
        print(str(start_node) + ' ', end='')

        for i in graph[start_node]:
            # print(i, end=' ')
            dfs(graph, i, visited)

    else:
        return


if __name__ == '__main__':
    # num2 = 1
    # num2 = calling()
    # print('\n'+str(num2))
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
    start_node = 1

    dfs(graph, start_node, visited)
