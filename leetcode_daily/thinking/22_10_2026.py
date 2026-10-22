from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # for it to have a soultion:
        # the array needs to be rotation on increasing/ decreasing order (regular or reversed)
        
        # to check for increasing/ decreasing order rotation 
        # we count the number of drops/ rises -> should equal exactly one
        
        nums_sorted = sorted(nums)
        if nums == nums_sorted:
            return 0 # already sorted no operations needed
        
        nums_sorted.reverse() # only inplace
        if nums == nums_sorted:
            return 1 # only reverse
        
        count_drops = 0
        count_rises = 0
        
        drop = 0
        rise = 0
        
        n = len(nums)
        
        for i in range(n):
            # print(nums[i], nums[(i+1)%n])
            if nums[i] > nums[(i+1)%n]: # # (i + 1) % n connects the last element back to the first element
                count_drops += 1
                drop = i
            else:
                count_rises += 1
                rise = i
            
        print(f"Count Drops: {count_drops}, Count Rises: {count_rises}")
        print(f"Drop = {drop}, Rise = {rise}")
        
        if count_drops != 1 and count_rises != 1:
            return -1 # not rotation increasing nor decreasing -> no solution
        
        elif count_drops == 1:
            return min(n-drop+1, drop+1) if drop != 0 else 1 # the smalles element IS first, then we rotate (ONLY ONE ROTATION IS NEEDED)
                    # number off operations is the number of rotations needed, (+1 as the smaller number is AFTER the drop index)
                    # n-drop -> 2 inverse operations, +1 as before
        else:
            # return the min between (rotating left only (n-rise) and rotating right and inversing (rise+1+1, +1 as the smaller number is BEFORE the indes and +1 for reversing))
            # if the smalles element IS first, then we rotate (ONLY ONE ROTATION IS NEEDED) then inverse
            return min(n-rise, rise+2) if rise!=0 else 2 # +1 for rotation, +1 for inverse
            
            

if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                [0,2,1],
                [1,0,2],
                # [2,0,1,3],
                # [1, 0],
                # [1, 2, 0],
                # [2, 0, 1],
                # [1,2,3,0],
                [2,1,0,3]
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minOperations(q)}\n\n\n")