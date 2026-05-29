from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not (len(set(nums))==len(nums))

Solution=Solution()
print(Solution.hasDuplicate([1,2,3,1]))
print(Solution.hasDuplicate([1,2,3,4]))
