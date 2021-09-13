class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=lambda x: len(x))
        answer = ""
        for word in sentence.split(' '):
            add_word = word
            for root in dictionary:
                if word.startswith(root):
                    add_word = root
                    break
            answer += (add_word + " ")
        return answer.strip()