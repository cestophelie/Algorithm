if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    minimum = []

    for i in range(n):
        minimum = list(map(int, input().split()))
        arr.append(min(minimum))

    print(max(arr))
    
'''
3 3
3 1 2
4 1 4
2 2 2
'''

'''
2 4
7 3 1 8
3 3 3 4
'''
