'''
DIVIDE AND CONQUER (https://leetcode.com/problems/score-of-parentheses/solutions/8556204/1-by-flerkeen-2mdi/)

Any balanced parentheses string can be broken down into one or more primitive balanced substrings 
(a primitive string is one that cannot be split into two smaller balanced strings).

For example, ()(()) can be split into two primitives: () and (()).

By keeping track of a balance counter (adding 1 for '(' and subtracting 1 for ')'), 
we know we've found a primitive substring the moment the balance reaches 0.

We can then compute the score of this primitive substring:
    If the primitive is exactly (), its score is 1.
    If it is longer, it must be of the form (A). Its score is 2 * score(A).
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def calc_balanced_substring(start:int,
                                    end:int):
            ans = balance = 0
            
            for i in range(start, end):
                balance += 1 if s[i] == '(' else -1 # add '1' ot the balance at '(' AND '-1' at ')'

                if balance == 0: # we isolated a primitive substring starting at 'start' and ending at 'i'
                            # if the string for example is ((())()()) it will take the whole string in the first loop
                    if i-start == 1: # -> ()
                        ans += 1
                    else: # -> (A)
                        ans += 2*calc_balanced_substring(start+1, i)
                    
                    start = i+1 # continue where we left off
            return ans
        
        return calc_balanced_substring(0, len(s))
        
    
if __name__ == "__main__":
    sol = Solution()
    questions = ["(()(()))"]
    
    for question in questions:
        print(f"ans '{question}' = {sol.scoreOfParentheses(question)}\n")


'''
ANOTHER SOLUTION

STACK OF SCORE BOXES
1. init stack = [0] -> score of the whole string
2. walk the string
    2.1. if '(' -> push 0 (a new empty box is init)
    2.2. if ')' -> pop the top of the box -> this is what's inside the box (bracets)
3. check the inside of the box (bracets):
    3.1. if inside == 0 -> empty box -> () -> add '1' to the box below
    3.2. if inside > 0 -> (A) -> add '2x inside' to the box below

4. at the end only one box is left -> final answer
'''

class Solution_2:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for i in range (len(s)):
            if s[i] == '(':
                stack.append(0)
            
            else:
                inside = stack.pop()
                
                if inside == 0: # -> ()
                    stack.append( stack.pop()+1 ) # add one to the last box -> stack[-1] +=1
                
                else: # (A)
                    stack.append (stack.pop() + 2*inside) # add 2xinside of the last closed box to the box before it

        return stack.pop() # final answer 