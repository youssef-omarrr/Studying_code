from math import ceil
global i
i = 0

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        
        low_speed = 1
        high_speed = int( max(dist)*1e2 )
        print(high_speed)
        
        last_saved = -1
        
        while high_speed>=low_speed:
            # get the middle speed (we are adding low speed to prevent division by ZERO)
            mid_speed = low_speed + (high_speed-low_speed) // 2

            # if the answer is vaild, it can still be too fast (we want to find the smallest valid number)
            if self.check_speed_validation(dist, hour, mid_speed):
                # save it just in case it was the smallest
                last_saved = mid_speed
                
                # cut the high speeds
                high_speed = mid_speed - 1
            
            # if the speed is too low, cut the low speeds and continue
            else:
                low_speed = mid_speed + 1
        
        # no answer found
        return last_saved
        
        
    def check_speed_validation(self, dist: list[int], hour: float, speed: int):
        global i
        print(f"checked {i}, current speed = {speed}")
        i += 1
        total_hours = 0
        last_element = len(dist) - 1
        for index, km in enumerate(dist):
            # no need to round up the last train
            total_hours += km / speed if index == last_element else ceil(km/speed)
            # print(f"total hours = {total_hours}, actuall speed = {km/speed}, round up ={ceil(km/speed)}")
        
        return total_hours <= hour
    
if __name__ == "__main__":
    ans = Solution()
    
    questions = [ ([47,40,31,8,31,73,11,11,94,63,9,98,69,99,17,17,85,61,71,22,34,68,78,55,28,70,97,94,89,26,92,40,52,86,84,48,57,67,58,16,32,29,9,44,3,76,71,30,76,29,1,10,91,81,8,30,9], 73.58)]
    
    for q in questions:
        print(f"{q} -> {ans.minSpeedOnTime(*q)}")