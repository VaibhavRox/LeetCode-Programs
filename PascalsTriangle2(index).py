class Solution:
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        res=[[1]]
        for i in range(1,rowIndex+1):
            prev_row=res[-1]
            new_row=[1]     #first element always 1
            for j in range(1,i):
                new_row.append(prev_row[j-1]+prev_row[j])
            new_row.append(1)       #last element of new arrangement always 1
            res.append(new_row)
        return res[rowIndex]