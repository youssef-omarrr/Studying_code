from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        
        # Approach 1: brute force
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1-num2) <= d:
                    break
            else:
                ans += 1
        
        return ans


if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                ([4,5,8], [10,9,1,8], 2),
                ([1,4,2,3], [-4,-3,6,10,20,30], 3),
                ([2,1,100,3], [-5,-2,10,-3,7], 6)
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.findTheDistanceValue(*q)}\n\n\n")