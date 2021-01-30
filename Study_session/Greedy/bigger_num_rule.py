if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    # print('arr : '+str(arr))
    total = 0
    for i in range(m//k):
        for j in range(k):
            total += arr[0]

        total += arr[1]

    print('total : '+str(total))
'''
5 8 3
2 4 5 4 6
'''
