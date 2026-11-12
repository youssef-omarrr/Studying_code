class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        
        ans = []
        
        for i in range( min(n1, n2) ):
            ans.extend([word1[i], word2[i]])
        
        if n1 == n2:
            return "".join(ans)
        elif n1 > n2:
            print(f" word1 sub => {word1[n2:]}")
            ans.extend([word1[n2:]])
        else:
            print(f" word2 sub => {word2[n1:]}")
            ans.extend([word2[n1:]])

        return "".join(ans)
    
if __name__ == "__main__":
    magd = Solution()
    
    questions = [
        ("abc", "pqr"),
        ("ab", "pqrs"),
        ("abcd", "pq"),
        ("cdf", "a")
    ]
    
    for q in questions:
        print(f"'{q}' -> {magd.mergeAlternately(*q)}\n\n\n")