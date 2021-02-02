from itertools import permutations


if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    possible = []  # 모든 가능한 숫자 조합을 뽑는다.
    result = []

    for i in range(1, num + 1):
        permute = list(permutations(num_list, i))
        possible.append(permute)

    # print(possible)
    for i in range(len(possible)):
        for j in range(len(possible[i])):
            res = sum(list(possible[i][j]))
            result.append(res)

    result = list(dict.fromkeys(result))

    result.sort()
    for i in range(0, len(result)):
        if result[i] != result[0] + i:

            print(result[0] + i)
            break


'''
5
3 2 1 1 9
'''