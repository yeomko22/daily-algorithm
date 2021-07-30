class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {chr(x+65):x+1 for x in range(26)}
        answer = 0
        for i in range(len(columnTitle)):
            c = columnTitle[len(columnTitle) -1 -i]
            answer += pow(26, i) * d[c]
            # print(pow(26, i), d[c], pow(26, i) * d[c])
        return answer
