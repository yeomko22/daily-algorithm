class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ''
        i = len(a) - 1
        j = len(b) - 1
        flag = False
        while i != -1 or j != -1:
            if i == -1:
                tmp = int(b[j])
                j -= 1
            elif j == -1:
                tmp = int(a[i])
                i -= 1
            else:
                tmp = int(b[j]) + int(a[i])
                i -= 1
                j -= 1
            # print('i', i, 'j', j, 'flag', flag, 'tmp', tmp, 'answer', answer)
            if flag:
                tmp += 1
            answer = str(tmp % 2) + answer
            if tmp >= 2:
                flag = True
            else:
                flag = False
        if flag:
            answer = '1' + answer
        return answer