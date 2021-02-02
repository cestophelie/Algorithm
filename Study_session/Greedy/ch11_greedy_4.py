from itertools import permutations


if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    possible = []
    result = []

    for i in range(1, num + 1):  # 모든 가능한 숫자 조합을 뽑는다.
        permute = list(permutations(num_list, i))
        possible.append(permute)

    # print(possible)
    for i in range(len(possible)):  # 가능한 조합의 합을 구한다.
        for j in range(len(possible[i])):
            res = sum(list(possible[i][j]))
            result.append(res)

    result = list(dict.fromkeys(result))  # 딕셔너리를 이용해 duplicates 를 제거한다.

    result.sort()
    for i in range(0, len(result)):
        if result[i] != result[0] + i:  # 만들 수 없는 양의 정수 금액 중 최소값 구한다.
            print(result[0] + i)
            break


'''
5
3 2 1 1 9
'''
