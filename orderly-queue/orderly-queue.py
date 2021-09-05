class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        visited = set([s])
        answer = s
        cur_str = s
        while True:
            new_str = cur_str[1:] + cur_str[0]
            if new_str in visited:
                break
            answer = min(answer, new_str)
            cur_str = new_str
        return answer