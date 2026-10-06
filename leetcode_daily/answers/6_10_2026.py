'''
HOW ON EARTH IS THIS MEDIUM DIFFICULTY?!
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        closing = 0
        
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    closing += 1
                    
        return len(stack)+closing

if __name__ == "__main__":
    ans = Solution()
    
    questions = ["())", "((("]
    
    for q in questions:
        print(f"'{q} -> {ans.minAddToMakeValid(q)}")