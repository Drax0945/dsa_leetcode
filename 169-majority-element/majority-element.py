class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rep_map = {} #value:frequency
        max_rep = len(nums)//2
        
        for i in nums:
            rep_map[i] = 1 + rep_map.get(i, 0)
            if rep_map[i]>max_rep:
                return i

        