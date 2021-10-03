class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def find_possible(gene):
            possible = []
            for candidate in bank:
                diff_cnt = 0
                for i in range(len(gene)):
                    if gene[i] != candidate[i]:
                        diff_cnt += 1
                if diff_cnt == 1:
                    possible.append(candidate)
            return possible
        candidates = find_possible(start)
        q = [(candidate, 1) for candidate in candidates]
        visited = set()
        while q:
            candidate, cnt = q.pop(0)
            visited.add(candidate)
            if candidate == end:
                return cnt
            candidates = find_possible(candidate)
            for candidate in candidates:
                if candidate not in visited:
                    q.append((candidate, cnt + 1))
        return -1