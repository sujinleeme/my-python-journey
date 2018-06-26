'''
Lession 1 : BinaryGap
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

'''
def solution(N):
    # write your code in Python 3.6
    bi_num = bin(N)[2:]
    s = ''
    result = []
    for i in range(len(bi_num)):
        
        if bi_num[i] == '0':
            s = s+bi_num[i]
        else:
            result.append(len(s))
            s = ''
    return max(result)
            



solution(123)