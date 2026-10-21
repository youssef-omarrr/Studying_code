class Solution:
    def minOperations(self, s: str) -> int:
        
        sorted_s = "".join(sorted(s))
        n = len(s)
        
        if s == sorted_s:
            return 0
        elif n == 2:
            return -1
        
        mn = sorted_s[0]
        mx = sorted_s[-1]
        
        
        if mn in s[0:n-1] and mx in s[1:n]:
            
            block_1 = "".join([sorted_s[0:n-1]]+[s[-1]])
            block_2 = "".join([s[0]]+[sorted_s[1:n]])
            
            if block_1 == sorted_s or block_2 == sorted_s:
                return 1
                
            else:
                return 2
                
        elif mn in s[0:n-1]:
            block = "".join(sorted(s[0:n-1])+[s[-1]])
            
            if mx in block[1:n]:
                return 2
            
        elif mx in s[1:n]:
            block = "".join([s[0]]+sorted(s[1:n]))
            
            if mn in block[0:n-1]:
                return 2
            
        else:
            return 3
        

if __name__ == "__main__":
    magd = Solution()
    
    questions = [
                "dog",
                "card",
                "gf",
                "cab"
                # "abcdfeg"
                ]
    
    for q in questions:
        print(f"'{q}' -> {magd.minOperations(q)}\n\n\n")