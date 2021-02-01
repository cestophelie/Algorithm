# 문제 :  문자열 최소로 뒤집어서 모두 같은 수로 만들기. 0과 1의 옵션이 있음
# 풀이 방법 : while룹 한 번 돌아서 청크의 개수를 세고 //2 연산을 진행하면 최소 뒤집는 수 구할 수 있음. 굳이 0과 1을 나눌 필요 x

if __name__ == '__main__':
    str = list(map(int, input()))
    cnt = 1

    length = len(str)
    i = 0

    while i < length - 1:
        if str[i] == str[i + 1]:
            i += 1
            continue
        else:
            cnt += 1
            i += 1

    print(cnt//2)
'''
0001100
'''

# 010101