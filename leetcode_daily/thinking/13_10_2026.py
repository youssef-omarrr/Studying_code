from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        print(nums)
        
        n = len(nums)
        nums = [nums[i]**2 for i in range(n)]
        
        if n == 1:
            return nums[0]
        
        print(nums)

        min_nums = sorted(nums)
        
        print(min_nums)
        
        score = 0
        
        for i in range(n//2):
            
            # max numbers
            score += min_nums[-(i+1)]
            # min numbers
            score -= min_nums[i]
            
            print(score)
        
        if n%2 != 0:
            score = score+min_nums[n//2]
            print(score)
            
        print(f"score = {score}")

        return score
    
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,3],
                [1,-1,2,-2,3,-3],
                [-6],
                [12,3,16,-1,7]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.maxAlternatingSum(q)}\n\n\n")