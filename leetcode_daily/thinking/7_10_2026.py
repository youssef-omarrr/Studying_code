from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        print(len(set(s)))
        print(set(s))
        
        temp = set(s)
        temp.discard('(')
        temp.discard(')')
        
        print(temp)
        print(len(temp))
        
        print(set(s) != {'(', ')'})
                
        if len(temp) and ')' not in s:
            
            s = s.replace("(", "").replace(")", "")
            print(s)
            
            ans = s if temp else ""
            return [ans]

        if '(' not in s:
            return [s.replace(')', '')]
        
        if s == "()":
            return [s]
        
        score = 0
        magd = []
        closing_i = []
        opening_i = []
        
        for i, c in enumerate(s):
            # print(f"\n{c} in {s}")
            # print(f"magd = {magd}")
            
            if c == '(':
                score += 1
                opening_i.append(i)
                
                        
            elif c == ')':
                score -= 1
                closing_i.append(i)
                
            if magd:
                magd = [item_in_magd + c for item_in_magd in magd]
            
            # print(f"Score= {score}, closing i= {closing_i}")
            
            if score < 0:
                # clear previous answers
                magd = []
                
                print(f"Score= {score}, closing i= {closing_i}")
                print(f"s[i-1] => {s[:i+1]}, {closing_i[:len(closing_i)-1]} \n")
                
                magd.extend(self.remove_closing_bracets(s[:i+1], closing_i[:len(closing_i)-1]) )
                score += 1
                
                print(f"    > magd = {magd}\n")
        
        if score > 0:
            if not magd:
                result = s

                for _ in range(score):
                    opening_index = result.rfind('(')
                    result = result[:opening_index] + result[opening_index + 1:]
                return [result]
            
            else:
                final_magd = set()
                
                for string in magd:
                    final_magd.add(string[:len(string)-1])
            
                return list(final_magd)

        return [""] if not list( set(magd) ) else list( set(magd) )
    
    def remove_closing_bracets(self, s:str, closing_i: List[int]):
        res = []
        
        for i in closing_i:
            res.append( s[:i] + s[i+1:] )
            print(f"result => {res}")
            
        return [""] if not res else res

if __name__ == "__main__":
    magd = Solution()
    
    questions = ["))", "()())()", "(a)())()", ")(", "()()()))((", "((", "n", "(x", "x)", "()", "(a)())()", "("]
    
    for q in questions:
        print(f"'{q}' -> {magd.removeInvalidParentheses(q)}\n\n\n")