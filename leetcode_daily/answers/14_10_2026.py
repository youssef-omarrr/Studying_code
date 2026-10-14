class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        ans = ""

        for i in range(num):
            if sum == 0:
                ans += '0'
            elif sum>=10:
                ans += '9'
                sum -= 9
            else:
                ans += str(sum)
                sum = 0
        
        return ans if sum ==0 else ""
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [2,3],
                [2,17],
                [1,10],
                [2, 10],
                [2, 19],
                [1, 9],
                [3, 28]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.maxSumOfSquares(*q)}\n\n\n")