class Solution(object):
    def search(self, nums, target):
         '''
         At least one section is sorted. We want to find this section and search it
         If target isn't possibly in the sorted section, we shrink our window to only look at the second, unsorted section. 
         If it's in (must be in) the sorted section, we shrink our window to only look at the sorted section.
         Once L > R we return -1, otherwise we'll have found target's index.
         '''

         l, r = 0, len(nums) - 1

         while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: #left is sorted
                if nums[l] <= target < nums[m]: #target in range
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
         return -1