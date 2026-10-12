class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # new = set(nums)
        # if(len(n)==len(set(nums))):
        #   return False
        # else:
        #   return True
        return not (len(nums)==len(set(nums)))
          
        