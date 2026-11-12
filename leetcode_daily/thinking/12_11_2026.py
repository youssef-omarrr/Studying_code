from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # inc_stack = [nums[0]]
        # dec_stack = [nums[0]]
        
        # n_inc_max = 1
        # n_dec_max = 1
        
        # print(nums)
        
        # for i in range(1, len(nums)):
        #     print( nums[i] )
            
        #     if nums[i] > inc_stack[-1]:
        #         inc_stack.append(nums[i])
        #         print (f"inc stack* ==> {inc_stack}")
        #         dec_stack = [ nums[i] ]
                
        #         n_inc_max = max( n_inc_max, len(inc_stack) )
                
        #     elif nums[i] < dec_stack[-1]:
        #         dec_stack.append(nums[i])
        #         inc_stack = [ nums[i] ]

        #         n_dec_max = max( n_dec_max, len(dec_stack) )
            
        #     else:
        #         inc_stack = dec_stack = [nums[i]]
            
        #     print (f"inc stack ==> {inc_stack}")
        #     print (f"dec stack ==> {dec_stack}")

        # return max(n_inc_max, n_dec_max)
    
        # instead of having 2 extra arrays we can just use the variable
        n_inc_max = 1
        n_dec_max = 1
        
        max_ans = 1
        print(nums)
        
        for i in range(len(nums) - 1):
            print( nums[i], nums[i+1])
            
            if nums[i+1] > nums[i]:
                n_inc_max += 1
                n_dec_max = 1
                
            elif nums[i+1] < nums[i]:
                n_dec_max += 1
                n_inc_max = 1
            
            else:
                n_inc_max = n_dec_max = 1
                
            max_ans = max(max_ans, n_inc_max, n_dec_max)

        return max_ans

if __name__ == "__main__":
    magd = Solution()
    
    questions = [
        [1,4,3,3,2],
        [3,3,3,3],
        [3,2,1],
        [1,1,5],
        [1,10,10]
    ]
    
    for q in questions:
        print(f"'{q}' -> {magd.longestMonotonicSubarray(q)}\n\n\n")