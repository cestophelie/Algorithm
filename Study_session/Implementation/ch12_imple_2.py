if __name__ == '__main__':
    string = list(input())
    alphabets = []
    nums = []

    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90:
            alphabets.append(string[i])
        else:
            nums.append(int(string[i]))

    alphabets.sort()
    result = ''.join(alphabets) + str(sum(nums))
    print(result)

'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''