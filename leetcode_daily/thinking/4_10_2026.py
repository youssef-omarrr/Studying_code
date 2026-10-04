class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # define a stack
        stack = []
        
        # define the mapping (we add the 'values' first -> then check the 'keys')
        # we do it like this as we can check the vlaue by the key not the other way around
        mapping = {
            # key:value
            ')':'(',  
        }
        
        # keep track of asterisk 
        asterisk_num = 0
        
        # keep track of closing parenthesis
        closing_num = 0
        
        for char in s:
            if char == '*':
                asterisk_num += 1
                print(f"{char}, *:{asterisk_num}, stack:{len(stack)}")
                
            # check for (
            elif char in mapping.values():
                stack.append(char)
                print(f"{char}, *:{asterisk_num}, stack:{len(stack)}")
                
            # check for )
            elif char in mapping.keys():
                # if the stack is empty (=0) 
                if not stack:
                    # AND there are no asterisks-> false
                    if not asterisk_num:
                        print(f"{char}, *:{asterisk_num}, stack:{len(stack)}")
                        return False
                
                    # stack empty and there is an asterisk -> continue
                    else:
                        closing_num += 1 # -> there is a closing parenthesis without an opening one
                        print(f"{char}, *:{asterisk_num}, stack:{len(stack)}")
                        continue
                    
                # if the stack is NOT empty, that means there is atleast one '(' -> pop the ')' and continue
                stack.pop()
                print(f"{char}, *:{asterisk_num}, stack:{len(stack)}")
                
        # if the whole loop is done AND the stack was empty (=0) at the end AND 
        # 1. there was no closing bracets -> true
        # 2. there were closing bracets but there number was less than or equal to the asterisks -> true
        # 
        # if the stack was NOT empty but the number of opening parenthesis less than or equal to the number of asterisks -> true
        #
        # if all fail -> false
        if not stack:
            if not closing_num:
                print(f"=={len(stack)}==")
                return True
            elif abs(closing_num - len(stack)) <= asterisk_num:
                print(f"=={len(stack)}==")
                return True
        elif len(stack) <= asterisk_num:
            print(f"=={len(stack)}==")
            return True
        
        print(f"=={len(stack)}==")
        return False



if __name__ == "__main__":
    sol = Solution()
    
    questions = ["()", "(*)", "(*))", "(", "(****())", 
                "(((((()*)(*)*))())())(()())())))((**)))))(()())()", 
                "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
                "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"]
    
    for i, question in enumerate(questions):
        print(f"{i}: {question}")
        ans = sol.checkValidString(question)
        print(f"ans {i}: {ans}\n")