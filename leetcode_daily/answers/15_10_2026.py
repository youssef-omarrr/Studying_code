from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            distinct_set = set()
            for j in range(i, n):
                distinct_set.add(nums[j])
                total_sum += len(distinct_set) ** 2
                
        return total_sum
                
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,1],
                [1,1],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.sumCounts(q)}\n\n\n")