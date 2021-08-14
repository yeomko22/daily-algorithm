class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        c_chars = Counter(chars)
        for word in words:
            flag = True
            c_word = Counter(word)
            for c in c_word:
                if c_chars[c] < c_word[c]:
                    flag = False
                    break
            if flag:
                answer += len(word)
        return answer