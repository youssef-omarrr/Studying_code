from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # this is the straight forward solutoin, but surely there is a better more optimixed way to do it
        # apparently it was the most optimized answer lol
        for i in range(n):
            if n % (i+1) == 0:
                ans += nums[i]**2
                
        return ans
    
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,3,4],
                [2,7,1,19,18,3],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.sumOfSquares(q)}\n\n\n")