from typing import List

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        
        # # brute force: time limit exceeded
        # for i in range(len(arr)+1):
        #     for j in range(i):
        #         print(j, i)
        #         print (arr[j:i])
        #         if sum(arr[j:i])%2 != 0:
        #             ans += 1
        
        
            
        return ans
                
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [1,3,5],
                [2,4,6],
                [1,2,3,4,5,6,7]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.numOfSubarrays(q)}\n\n\n")