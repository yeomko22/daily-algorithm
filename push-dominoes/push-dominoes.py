class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = [0] * len(dominoes)
        r = [0] * len(dominoes)
        answer = ['.'] * len(dominoes)
        l_tmp = 0
        found_l = False
        for i in range(len(dominoes)):
            j = len(dominoes) - 1 -i
            if dominoes[j] == '.':
                if found_l:
                    l_tmp += 1
                l[j] = l_tmp
            elif dominoes[j] == 'L':
                l_tmp = 1
                l[j] = l_tmp
                found_l = True
            else:
                l_tmp = 0
                found_l = False
        
        r_tmp = 0
        found_r = False
        for i in range(len(dominoes)):
            if dominoes[i] == '.':
                if found_r:
                    r_tmp += 1
                r[i] = r_tmp
            elif dominoes[i] == 'R':
                r_tmp = 1
                r[i] = r_tmp
                found_r = True
            else:
                r_tmp = 0
                found_r = False
        
        answer = ''
        for i in range(len(l)):
            if l[i] == r[i]:
                answer += '.'
            elif l[i] != 0 and r[i] != 0:
                if l[i] < r[i]:
                    answer += 'L'
                else:
                    answer += 'R'
            elif l[i] != 0:
                answer += 'L'
            else:
                answer += 'R'
        return answer