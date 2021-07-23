class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum % 2:
            return False
        dp = set([0])
        for num in nums:
            tmp = copy.deepcopy(dp)
            for dp_num in dp:
                cursum = dp_num + num
                if cursum in dp:
                    continue
                if cursum == totalsum // 2:
                    return True
                tmp.add(cursum)
            # print('tmp', tmp)
            dp = tmp
        return False