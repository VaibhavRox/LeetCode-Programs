class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        top,bottom,left,right=0,m-1,0,n-1
        res=[]
        while left<=right and top<=bottom:
            #Traverse the first row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            #Traverse the last column from top to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            #Traverse the last row from right to left
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            #Traverse the column from bottom to top
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res