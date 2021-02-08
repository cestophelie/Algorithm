if __name__ == '__main__':
    recv = list(input())

    num = int(recv[1]) - 1
    to_num = ord(recv[0]) - 97

    location = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    count = 0

    for i in range(len(location)):
        if num + location[i][0] >= 0 and num + location[i][1] >= 0:
            count += 1

    print(count)