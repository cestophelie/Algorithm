INF = int(1e9)

if __name__ == '__main__':
    listing = list(input())
    length = len(listing)
    min_cnt = INF
    cnt = 1
    backup = []
    result = ''

    for i in range(1, length // 2 + 1):  # 최대 반복 구간의 크기는 반  length // 2
        j = 0
        cnt = 1
        answer = []

        while j < length:
            if j < length - i + 1 and listing[j:j + i] == listing[j + i:j + 2*i]:  # 청크 범위가 같은 경우 카운트를 올리고 인덱스 j로 올림
                # print(listing[j:j + i])
                # print(listing[j + i:j + 2 * i])
                cnt += 1
                # print(cnt)
                j += i
                while listing[j:j + i] == listing[j + i:j + 2*i]:
                    cnt += 1
                    j += i
                # print('j : '+str(j))

            else:  # 단위당 스트링이 다른 경우
                if cnt == 1:  # 카운트가 1이면 숫자는 어펜드 안하고 문자만 그 청크 append - 나중에 단위 범위당 체크 해봐야 할 듯?
                    answer.append(listing[j])
                    j += 1
                else:  # 단위당 스트링이 있던 경우 더해준다.
                    answer.append(str(cnt))
                    print('append : '+str(''.join(listing[j-i:j])+str('\n')))
                    answer.append(''.join(listing[j-i:j]))

                    j += i
                    cnt = 1
                    continue

        answer = ''.join(answer)
        if len(answer) < min_cnt:
            min_cnt = len(answer)
            result = answer
        # print('here : '+answer)
        # print()
    print('result : '+str(result))
    print('min_cnt : '+str(min_cnt))

'''
aabbaccc  # 7
ababcdcdababcdcd  # 9
abcabcdede  # 8
abcabcabcabcdededededede  # 14
xababcdcdababcdcd  # 17
'''