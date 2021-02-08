if __name__ == '__main__':
    num = int(input())
    cnt = 0
    for i in range(0, num + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(k) or '3' in str(j) or '3' in str(i):
                    cnt += 1

    print(cnt)