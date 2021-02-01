# 문제 설명 : 주어진 한 자리수를 더하거나 곱해서 그 결과값이 최대가 되도록 하는 문제
result = 0


def calculate(idx):
    length = len(num)
    global result
    for i in range(idx, length):
        if num[i] >= 2:
            result *= num[i]

        else:
            result += num[i]
    print(result)


if __name__ == '__main__':
    # logic >> 0과 1은 더하는 게 최선의 옵션이고, 나머지 수는 더한다.
    global num
    num = list(map(int, input()))

    # 첫 번째 원소가 우선 0 인지 여부를 체크해서 두 케이스로 나눔
    if num[0] == 0:
        result += num[1]
        calculate(2)
    else:
        calculate(1)



'''
02984
'''