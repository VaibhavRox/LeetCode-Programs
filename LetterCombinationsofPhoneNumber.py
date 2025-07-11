class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_char={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wyxz'
        }
        res=['']
        for i in digits:
            temp=[]
            for c in res:
                for letter in digits_char[i]:
                    temp.append(c+letter)
            res=temp
        return res