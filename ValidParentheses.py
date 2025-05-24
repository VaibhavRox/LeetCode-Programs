class Solution:
    def isValid(self, s: str) -> bool:
        count1,count2,count3=0,0,0
        stack=[]
        for i in s:
            if i == '(':
                count1+=1
                stack.append(i)
            elif i==')':
                count1-=1
                if count1<0 or stack.pop()!='(':
                    return False
            elif i=='[':
                count2+=1
                stack.append(i)
            elif i==']':
                count2-=1
                if count2<0 or stack.pop()!='[':
                    return False
            elif i=='{':
                count3+=1
                stack.append(i)
            elif i=='}':
                count3-=1
                if count3<0 or stack.pop()!='{':
                    return False
        return count1==0 and count2==0 and count3==0
               
        

        