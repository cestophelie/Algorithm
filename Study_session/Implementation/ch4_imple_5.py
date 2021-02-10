if __name__ == '__main__':
    listing = list(map(int, input()))
    idx = len(listing) // 2
    list1 = sum(listing[:idx])
    list2 = sum(listing[idx:])

    if list1 == list2:
        print('LUCKY')
    else:
        print('READY')
'''
123402

7755
'''