# 테케 찾다 죽을뻔 함
# 20번 테케는 2 2 2 2\n 9
# 23,16 인가는 2 2 2 2\n 8
# 테케를 못 찾겠으면 문제를 다시 읽어보자
import heapq


def solution(food, interrupt):
    food1 = []  # 우선순위 큐
    if interrupt >= sum(food):  # 남은 음식이 없는 경우 처리
        return -1

    for i in range(len(food)):  # 음식이 적은 순으로 처리
        heapq.heappush(food1, (food[i], i))

    previous = 0

    while food1:
        amount, idx = heapq.heappop(food1)
        length = len(food1) + 1

        amount -= previous  # 매번 하나씩 consume 하도록 처리하지 말고 previous 변수에 총 consume 한 양 저장해서 빼주기
        previous += amount  # 기존에 consume 한 음식의 양
        total_subtract = amount * length  # 남은 음식 중 가장 양이 적은 element 기준으로 총 몇 바퀴 도는지 계산

        if interrupt > total_subtract:  # interrupt 까지 남은 초가 한 바퀴 도는 수보다 큰 경우, interrupt 만 없데이트 해줌
            interrupt -= total_subtract
        else:  # 한 바퀴 돌 만큼 초가 안 남아 있으면 뺏던 음식 다시 넣고 남은 애들 다시 인덱스 값으로 정렬해서 나머지 계산
            heapq.heappush(food1, (amount, idx))
            food1 = sorted(food1, key=lambda x: x[1])
            break

    if interrupt < len(food1):
        return food1[interrupt][1] + 1
    else:
        return food1[interrupt%len(food1)][1] + 1


if __name__ == '__main__':
    food = list(map(int, input().split()))
    interrupt = int(input())

    result = solution(food, interrupt)
    print(result)
'''
3 1 2
3
    
3 1 2
5

4 2 3 6 7 1 5 8
16

4 2 3 6 7 1 5 8
27

3 1 2
6
'''