from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split())
    listing = list(map(int, input().split()))
    length = len(listing)
    weight = listing

    listing = [i for i in range(1, length + 1)]
    listing = list(combinations(listing, 2))

    # print(listing)
    listing_ = []
    for i in range(len(listing)):
        if weight[listing[i][0] - 1] != weight[listing[i][1] - 1]:
            listing_.append(listing[i])

    print(len(listing_))

'''
5 3
1 3 2 3 2
'''

'''
8 5
1 5 4 3 2 4 5 2
'''