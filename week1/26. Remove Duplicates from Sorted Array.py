from types import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == last_num:
                nums.pop(i)
            else: 
                last_num = nums[i]
        return len(nums)

# "My approach is to iterate through the array backwards, 
# comparing each element with the last unique element I've seen. 
# If I find a duplicate, I remove it using pop()."

# "The time complexity is O(N²) because pop(i) is O(N), 
# and we potentially do this N times.
# Space complexity is O(1) since we modify in-place."