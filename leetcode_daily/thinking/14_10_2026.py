import numpy as np

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        print (f'num = {num}, sum = {sum}')
        # print(num, len(str(sum)), str(sum)[-1])
        # print(num == len(str(sum)) and str(sum)[-1] == '9')
        
        # number of digits less than the sum's number of digits or in genral no 'num' numbers can add up to 'sum'
        if num < len(str(sum)) or ( num == len(str(sum)) and str(sum)[-1] == '9' and num != 1):
            return ""
        
        ans = np.array([], dtype=int)

        for i in range(num):
            if sum == 0:
                ans = np.append(ans, 0)
                print(ans)
            elif sum>=10:
                ans = np.append(ans, 9)
                sum -= 9
                print(ans)
            else:
                ans = np.append(ans, sum)
                sum = 0
                print(ans)
                
        if sum != 0:
            return ""

        # return str(np.sum(np.square(ans)))
        result = "".join(ans.astype(str))
        
        return result
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [2,3],
                [2,17],
                [1,10],
                [2, 10],
                [2, 19],
                [1, 9]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.maxSumOfSquares(*q)}\n\n\n")