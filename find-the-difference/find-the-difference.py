class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        answer = ''
        for key in counter_t:
            if counter_t[key] != counter_s[key]:
                answer = key
                break
        return answer