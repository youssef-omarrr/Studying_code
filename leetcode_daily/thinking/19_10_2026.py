from typing import List
import numpy as np

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        # 1. sort then get ans (slower)
        # # nums = np.array(nums) # no need to turn to np array before, sort does this by default
        # nums = np.sort(nums)
        # ans =[i for i, num in enumerate(nums) if num == target]
        
        # return ans
        
        
        # 2. without sorting (count less for traversing indexes, count the equal for the actual index)
        less = equal = 0
        
        for num in nums:
            if num < target: # instead of sorting we will count the number of smaller numbers
                less += 1
            elif num == target:
                equal += 1
            
        return list(range(less, less+equal)) # start with the number of smaller numbers -> index of first target
                                            # if there are many targts -> add the number of items equal to target
        
        
        
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                ([1,2,5,2,3], 2),
                ([1,2,5,2,3], 3),
                ([1,2,5,2,3], 5)
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.targetIndices(*q)}\n\n\n")