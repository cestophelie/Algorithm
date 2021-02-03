if __name__ == '__main__':
    num = int(input())
    num_list = list(input().split())
    global row
    global col
    row = 1
    col = 1

    for i in range(len(num_list)):
        comp = num_list[i]
        if comp == 'R' and col < num:
            col += 1
        if comp == 'L' and col != 1:
            col -= 1
        if comp == 'U' and row != 1:
            row -= 1
        if comp == 'D' and row < num:
            row += 1

    # print(str(row)+' '+str(col))
    print(row, end=' ')
    print(col)

'''
5
R R R U D D
'''

'''
3
L L L
'''

'''
5
R D R D R D R D U R
'''