row, col = map(int, input().split())
plate = []
for i in range(row):
    lists = list(map(int, input()))
    plate.append(lists)


def dfs(r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
        return False

    elif plate[r][c] == 0:
        plate[r][c] = 1
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        return True
    return False


if __name__ == '__main__':
    result = 0
    for i in range(row):
        for j in range(col):
            if dfs(i, j):
                result += 1

    print('result : '+str(result))
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
