from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 0
        
        # for num in nums:
        #     if num != mx:
        #         ans += (mx-num)
            
        # return ans
        
        # faster way
        return (len(nums)*max(nums) - sum(nums))


if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [2,1,3],
                [4,4,5],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minMoves(q)}\n\n\n")