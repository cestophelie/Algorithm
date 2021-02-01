if __name__ == '__main__':
    num = input()
    degree = list(map(int, input().split()))
    degree.sort(reverse=True)
    print(degree)

    cnt = 0
    length = len(degree)

    i = 0
    while i < length:
        if degree[i] <= length - i:
            cnt += 1
            i += degree[i]

    print('result : ' + str(cnt))


'''
5
2 3 1 2 2
'''