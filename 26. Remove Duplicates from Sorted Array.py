class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == last_num:
                nums.pop(i)
            else: 
                last_num = nums[i]
        return len(nums)
        