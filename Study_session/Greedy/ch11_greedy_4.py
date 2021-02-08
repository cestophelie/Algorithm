from itertools import combinations

if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split()))
    possible = []
    result = []

    for i in range(1, num + 1):  # 모든 가능한 숫자 조합을 뽑는다.
        permute = list(combinations(num_list, i))
        possible.append(permute)

    # print(possible)
    for i in range(len(possible)):  # 가능한 조합의 합을 구한다.
        for j in range(len(possible[i])):
            res = sum(list(possible[i][j]))
            result.append(res)

    result = list(dict.fromkeys(result))  # 딕셔너리를 이용해 duplicates 를 제거한다.

    result.sort()  # 전체 가능한 수
    print(result)
    flag = 0
    for i in range(0, len(result)):
        if result[i] != i + 1:  # 만들 수 없는 양의 정수 금액 중 최소값 구한다.
            print('here')
            print(i + 1)
            flag = 1
            break

    if flag == 0:
        print(result[-1] + 1)
'''
5
3 2 1 1 9
'''

'''
3
3 5 7
'''

'''
5
1 1 1 1 1
'''
