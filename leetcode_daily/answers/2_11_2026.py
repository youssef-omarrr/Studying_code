from typing import List
import numpy as np

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # use median not mean
        median = np.median(nums)
        
        print(f"diff ==> {np.abs(nums - median)}")
        
        pivot = nums[ np.argmin( np.abs(nums - median) ) ]
        
        print(f"median = {median} -> pivot = {pivot}")
        
        return int(sum( np.abs(pivot - np.array(nums)) ))
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [2,1,3],
                [1,10,2,9],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minMoves2(q)}\n\n\n")