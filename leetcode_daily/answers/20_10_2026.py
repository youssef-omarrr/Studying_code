from typing import List
import math
from collections import deque

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = self.get_divisors_optimized(n)
        
        print(f"Divisors = {divisors}")
        
        sorted_nums = sorted(nums)
        
        if nums == sorted_nums:
            return sum(divisors)
        
        ans = 0
        
        for k in divisors:
            
            if k == 1:
                continue
            
            # final list to be checked
            final_ans = []
            
            for i in range(0, n, k):
                sub_array = nums[i: i+k]
                print(f"subarray {i+1} = {sub_array}")
                
                
                if sub_array == sorted(sub_array):
                    final_ans.extend(sub_array)
                    continue
                
                sorted_subarray = self.rotate_to_sorted(sub_array)
                if sorted_subarray:
                    final_ans.extend(sorted_subarray)
                    continue
                else:
                    break
            else:
                print(f"final ans = {final_ans}")
                if final_ans == sorted_nums:
                    ans += k
            
        return(ans)
    
    
    def get_divisors_optimized(self, n) -> List[int]:
        if n<= 0:
            return []
        
        divisors = []
        
        # Loop from 1 up to the square root of n (inclusive, hence the +1)
        for i in range (1, math.isqrt(n)+1):
            if n % i == 0:
                divisors.append(i)
                
                # avoid double counting perfect square roots (6*6=36)
                if i != n//i:
                    divisors.append(n//i)
                    
        return sorted(divisors)
    
    
    def rotate_to_sorted(self, nums) -> List[int] | None:
        if not nums:
            return nums
        
        n = len(nums)
        pivot = -1
        
        # find where the list sorting drops (the pivot point)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                if pivot != -1:
                    return None
                
                pivot = i
        # Slice and rotate the list: everything after the pivot comes to the front
        break_point = pivot + 1
        sorted_subarray = nums[break_point:] + nums[:break_point]
        
        print(f"sorted subarray= {sorted_subarray}") 
        
        return sorted_subarray


if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [3,1,2],
                [7,6,5],
                [5,8],
                [2,1,4,3],
                [3,4,1,2],
                [4,1,2,3]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.sortableIntegers(q)}\n\n\n")