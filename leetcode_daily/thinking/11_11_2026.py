from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        dp = [0]
        i=0
        
        while i < n:
            
            if i+3 <= n:
                temp3 = costs[i+3]+(3-i)**2
            elif i+2 <= n:
                temp2 = costs[i+2]+(2-i)**2
            else:
                temp1 = costs[i+1]+(1-i)**2
            
    
        pass
    
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                (4, [1,2,3,4]),
                (4, [5,1,6,2]),
                (3, [9,8,3]),
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.climbStairs(*q)}\n\n\n")