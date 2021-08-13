class Solution:
    def maximum69Number (self, num: int) -> int:
        answer = num
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == '6':
                answer = int(str_num[:i] + '9' + str_num[i+1:])
                break
        return answer
            