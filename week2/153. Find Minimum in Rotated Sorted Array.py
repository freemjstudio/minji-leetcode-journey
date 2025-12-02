# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = n-1
        answer = min(nums[left], nums[right])
        while left <= right: 
            mid = (left+right)//2
            print(mid)
            if nums[left] > nums[right]: 
                answer = min(answer, nums[mid])
                left = mid + 1
            elif nums[right] < nums[left]: 
                answer = min(answer, nums[mid])
                right = mid -1
            else: 
                answer = min(answer, nums[mid])
                break 

        return answer
    

    class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left, right = 0, n-1
        answer = min(nums[left], nums[right])
        
        while left < right: 
            mid = (left+right)//2
            
            if nums[mid] > nums[right]: 
                answer = min(answer, nums[mid])
                left = mid + 1
            else :
                answer = min(answer, nums[mid])
                right = mid


        return answer