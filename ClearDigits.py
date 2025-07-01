class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch.isdigit():
                if stack: #only remove if theres non-digit character to left
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.
"""