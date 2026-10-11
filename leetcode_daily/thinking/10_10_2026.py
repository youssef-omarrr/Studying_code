from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # print (nums1, nums2, k1, k2)
        n = len(nums1)
        ans = self.calc_sum_of_squares(nums1, nums2)
        
        if k1 == k2 == 0:
            return ans
        
        for i in range(n):
            temp1 = nums1.copy()
            temp2 = nums2.copy()
            
            # print (nums1)
            # print (nums2)
            print (temp1)
            print (temp2)
            print("====================")
        
            if nums1[i] < nums2[i]:
                temp1[i] = nums1[i] + k1 if nums1[i] + k1 < nums2[i] else nums2[i]
            else:
                temp2[i] = nums2[i] + k2 if nums2[i] + k2 < nums1[i] else nums1[i]
                
            print (temp1)
            print (temp2)
            
            temp = self.calc_sum_of_squares(nums1, nums2)
            print(temp)
            print('\n')
            
            if temp < ans:
                ans = temp
            
        return ans
    
    def calc_sum_of_squares(self, nums1: list[int], nums2: list[int]):
        n = len(nums1)
        ans = 0
        
        for i in range(n):
            ans += (nums1[i] - nums2[i])**2
        
        return ans
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [[1,2,3,4],  [2,10,20,19], 0,  0],
                [[1,4,10,12], [5,8,6,9],   1,  1],
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minSumSquareDiff(*q)}\n\n\n")