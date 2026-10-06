class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            # keys: values
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif stack and mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return False if len(stack) else True
                
if __name__ == "__main__":
    ans = Solution()
    
    questions = ["()", "()[]{}", "(]", "([])", "([)]", "]"]
    
    for q in questions:
        print(f"'{q}' -> {ans.isValid(q)}")