class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        last_seen = '('
        score = 0
        
        i=0
        
        print(s)
        while i < len(s):    
            print(f"index:{i}, stack:{stack}, s[i]: {s[i]}, score:{score}")
                    
            if s[i] == '(':
                stack.append(s[i])
                print(f"index:{i}, stack:{stack}, s[i+1]: {s[i+1]}, score:{score}")
                
                if s[i+1] == ')':
                    stack.pop()
                    score+=1
                    print(f"index:{i}, stack:{stack}, s[i+1]: {s[i+1]}, score:{score}")
                    
                    # skip the next iteration as we already know it's ')'
                    i+=2
                    
                else:
                    i+=1
                    
            else:
                mult = 2
                stack.pop()
                
                for j in range(len(stack)):
                    if s[i+1] ==')':
                        mult *= 2
                        stack.pop()
                        i+=1
                
                i+=1
                score *= mult
                
        return score

        
    
if __name__ == "__main__":
    sol = Solution()
    questions = ["(()(()))"]
    
    for question in questions:
        print(f"ans '{question}' = {sol.scoreOfParentheses(question)}\n")

# doesn't handle math operations order reliably