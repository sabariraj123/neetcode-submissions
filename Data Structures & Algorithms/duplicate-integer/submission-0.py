class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if(len(nums)==len(set(nums))):
          return False
        else:
          return True

          
        