if __name__ == '__main__':
    n, m = map(int, input().split())
    row, col, dir = map(int, input().split())
    turn = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    mapping = []
    for _ in range(n):
        mapping.append(list(map(int, input().split())))

    cnt = 1
    flag = 0
    while True:
        row_ = row + turn[dir][0]
        col_ = col + turn[dir][1]
        if (0 <= row_ < n) and (0 <= col_ < m):
            if mapping[row_][col_] == 0:
                mapping[row][col] = 1
                row = row_
                col = col_
                cnt += 1
                flag = 0
                # print(mapping)
            else:
                if flag == 3:
                    break
                if dir != 3:
                    dir += 1
                    flag += 1
                else:
                    dir = 0
                    flag += 1
        else:
            if flag == 3:
                break
            if dir != 3:
                dir += 1
                flag += 1
            else:
                dir = 0
                flag += 1
    print(cnt)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 0
1 1 0 0
'''

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 0 1
'''

'''
4 4
0 0 0
0 1 1 1
1 0 0 1
1 1 0 1
1 1 0 1
'''