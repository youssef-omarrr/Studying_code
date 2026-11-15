from typing import List

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        cost = k
        ans = 0
        mx = k # worst case scenario is all zeros and we flip thme k times
        
        temp = nums.copy()
        
        for n, i in enumerate(nums):
            
            if i == 1:
                ans += 1 
                
            elif cost>0: # we can afford to flip a bit
                ans += 1
                cost -= 1
                temp[n] = 1
                print(f"replacing {n} ==> {temp}, ans = {ans}")
                
            else:
                ans = 1
                cost = k-1
                
                temp = nums
                temp[n] = 1
                print(f"reset at {n} ===> {temp}, ans = {ans}")

            mx = max(mx, ans)
            
        return mx
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
        ([1,1,1,0,0,0,1,1,1,1,0], 2),
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),
    ]
    
    for q in questions:
        print(f"'{q}' -> {magd.longestOnes(*q)}\n\n\n")