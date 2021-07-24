class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        answer = []
        shortestlevel = 1001
        letters = [chr(x + 97) for x in range(26)]
        q = deque([([beginWord], 1)])
        wordset = set(wordList)
        visited = set()
        while q:
            words, level = q.popleft()
            if level > shortestlevel:
                break
            word = words[-1]
            if word == endWord:
                shortestlevel = level
                answer.append(words)
                continue
            visited.add(word)
            for i in range(len(word)):
                for j in range(len(letters)):
                    if word[i] == letters[j]:
                        continue
                    newword = word[:i] + letters[j] + word[i+1:]
                    if newword in visited or not newword in wordset:
                        continue
                    q.append((words + [newword], level + 1))
        return answer