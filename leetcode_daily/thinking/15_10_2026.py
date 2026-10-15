from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # each item alone is a subarray with 1 distinct value, so init ans with len of list (1^2 = 1)
        ans = n   
        
        # easy solution: 2 pointers
        for i in range (n-1):
            for j in range(i+2, n+1):
                print (i, j)
                ans += len(set(nums[i:j])) ** 2
                print(f"subarray: {nums[i:j]} -> set: {set(nums[i:j])}")
                print(ans)
                
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,2,1],
                [1,1],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.sumCounts(q)}\n\n\n")