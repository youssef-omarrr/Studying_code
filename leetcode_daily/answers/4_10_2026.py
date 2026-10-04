'''
Tabulation and memoization are two techniques used to implement dynamic programming. 
Both techniques are used when there are overlapping subproblems (the same subproblem is executed multiple times). 
Below is an overview of two approaches. (https://www.geeksforgeeks.org/dsa/tabulation-vs-memoization/)

Memoization:
    Top-down approach
    Stores the results of function calls in a table.
    Recursive implementation
    Entries are filled when needed.

Tabulation:
    Bottom-up approach
    Stores the results of subproblems in a table
    Iterative implementation
    Entries are filled in a bottom-up manner from the smallest size to the final size.
'''
from typing import List

# memoization approach
class Solution(object):
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        memo = [[-1]*n for _ in range(n)] # the cache table for dimension (n, n) all init at -1 where:
                                        # the rows are the indecies
                                        # the columns are the open bractes count
        
        # call the recursive function `is_valid_string` starting at index=0, open_bracets_count=0
        return self.is_valid_string(index = 0, 
                                    open_bracets_count = 0, 
                                    s = s, 
                                    memo = memo)
    
    def is_valid_string(self, 
                        index:int, 
                        open_bracets_count: int, 
                        s: str,
                        memo: List[List[int]]) -> bool:
        
        # if we reached the end of the string, check if the open bracets count equals zero (vaild) or not (invalid)
        if index == len(s):
            return open_bracets_count == 0
        
        # check if the answer to the current index and open bracets count is cached in memo
        if memo[index][open_bracets_count] != -1:
            return  memo[index][open_bracets_count] == 1 # return the memoized result
        
        # if none of the above -> init at 'not vaild' until proven otherwise
        is_vaild = False
        
        # if the current char is '*' -> try all possibilities
        if s[index] == '*': # we need to OR the answers to make sure that ATLEAST one solution is correct
            
            # 1. treat '*' as '(' 
            is_vaild |= self.is_valid_string(index+1,
                                            open_bracets_count+1, # <- +1 as '*' is now an open bracet
                                            s,
                                            memo)
            # 2. treat '*' as ')'
            if open_bracets_count > 0:
                is_vaild |= self.is_valid_string(index+1,
                                            open_bracets_count-1,  # <- -1 as '*' is now a closing bracet
                                            s,
                                            memo)
            
            # 3. treat '*' as empty space 
            is_vaild |= self.is_valid_string(index+1,
                                            open_bracets_count, # <- no change as '*' is now an empty space
                                            s,
                                            memo)
        
        # if the current char is not '*' then it is either '(' or ')'
        else:
            if s[index] == '(':
                is_vaild = self.is_valid_string(index+1,
                                                open_bracets_count+1, # <- +1 as the number of open bracets just increased
                                                s,
                                                memo)
                
            elif open_bracets_count > 0: # only handle ')' if there is an open bracet
                is_vaild = self.is_valid_string(index+1,
                                                open_bracets_count-1, # <- -1 as a closing bracet was just added
                                                s,
                                                memo)
        
        # cache/ memoize this result and return it for recursive loop
        memo [index][open_bracets_count] = 1 if is_vaild else 0
        
        return is_vaild


# another solution (like the one i was thinking of but didn't work)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # st = [] record left parenthesis
        # star = []
        # if *
        # if '(' -> st.append(i)
        # ')'-> st.pop() if not st-> star.pop()
        #O(n),O(n)
        left = []
        star = []
        n = len(s)
        for i in range(n):
            if s[i]=='(':
                left.append(i)
                
            elif s[i]=='*':
                star.append(i)
                
            elif s[i]==')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
                
        while left and star and left[-1]<star[-1]:
            left.pop()
            star.pop()
            
        if len(left)>0:
            return False
        
        return True


