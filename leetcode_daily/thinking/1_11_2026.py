from typing import List
import numpy as np

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # mx = np.max(nums) # it works with min not max!!!!! -> to get the min number of tries not the max
        
        # nums = np.array(nums)
        
        print(np.abs(nums - np.min(nums)))

        # return sum(np.abs(nums - np.min(nums))) # abs not needed as any number will be less than the 'min' of the array
        
        return sum(nums - np.min(nums)) 

        # to simplyfy it further, we just use basic math and properties of the 'sum' operator
        
        # we can split the sum to the 2 valuse like this
        # sum(nums) - sum(np.min(nums)))
        # sum(nums) - sum(min(nums))) # -> doing this we no longer need numpy!
        
        # as we will sum over num on the min only (only a constant number inside the sum operator), then that is the same as multiplying be len(nums)
        return sum(nums) - len(nums)*min(nums) # -> this is faster
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,3],
                [1,1,1],
                [1, 1, 1000000000]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minMoves(q)}\n\n\n")