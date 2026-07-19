class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # index we aim to reach

        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] + i) >= goal:
                goal = i # if we can reach the goal from index i, our new goal is to reach index i

        return goal == 0