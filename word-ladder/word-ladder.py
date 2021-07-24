class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        
        queue = [beginWord, None]
        count = 1
        n = len(beginWord)
        
        while queue[0]:
            while queue[0]:
                word = queue.pop(0)

                for i in range(n):
                    for j in range(26):
                        newword = word[:i] + chr(j+ord('a')) + word[i+1:]

                        if newword in word_set:
                            queue.append(newword)
                            word_set.remove(newword)
                            
                            if newword == endWord:
                                return count+1
            queue.pop(0)
            count+=1
            queue.append(None)
        
        return 0