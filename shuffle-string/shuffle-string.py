class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = []
        for c, i in zip(s, indices):
            tmp.append((i, c))
        return "".join([x[1] for x in sorted(tmp)])
