class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        answer = 0
        visiteds = []
        for num in nums:
            flag = False
            for visited in visiteds:
                if num in visited:
                    flag = True
                    break
            if flag:
                continue
            curvisited = set()
            curnum = num
            while curnum not in curvisited:
                curvisited.add(curnum)
                curnum = nums[curnum]
            visiteds.append(curvisited)
            answer = max(answer, len(curvisited))
        return answer