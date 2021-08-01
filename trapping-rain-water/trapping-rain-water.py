class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        cur_l = height[l]
        cur_r = height[r]
        answer = 0
        while l < r:
            if height[l] > height[r]:
                r -= 1
                cur_r = max(cur_r, height[r])
                add_r = max(min(cur_l, cur_r) - height[r], 0)
                answer += add_r
            else:
                l += 1
                cur_l = max(cur_l, height[l])
                add_l = max(min(cur_l, cur_r) - height[l], 0)
                answer += add_l
        return answer