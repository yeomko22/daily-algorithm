class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        answer = 0
        for word in text.split(' '):
            flag = True
            for c in brokenLetters:
                if c in word:
                    flag = False
                    break
            if flag:
                answer += 1
        return answer