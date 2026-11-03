from typing import List

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums)*min(nums)
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,3],
                [1,1,1],
                [1, 1, 1000000000]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minMoves(q)}\n\n\n")