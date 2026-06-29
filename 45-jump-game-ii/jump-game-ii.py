class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        steps = 0
        while r < len(nums) - 1:
            max_step = 0
            for i in range (l, r+1):
                max_step = max(max_step, nums[i]+i)
            l = r+1
            r = max_step
            steps += 1
        return steps

        