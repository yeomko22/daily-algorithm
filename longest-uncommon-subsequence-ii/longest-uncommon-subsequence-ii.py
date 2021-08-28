class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        c = Counter()
        answer = -1
        for curstr in strs:
            for i in range(1, len(curstr) + 1):
                combs = itertools.combinations(curstr, i)
                for comb in combs:
                    c["".join(comb)] += 1
        for key in c:
            if c[key] != 1:
                continue
            answer = max(answer, len(key))
        return answer