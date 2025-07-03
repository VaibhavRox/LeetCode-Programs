class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        if rows==0:
            return -1
        cols=len(grid[0])
        #fresh oranges counter
        fresh_cnt=0
        #queue with rotten oranges
        rotten=deque()
        #visit each cell in grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    #update fresh count
                    fresh_cnt+=1
        minutes=0
        while rotten and fresh_cnt>0:
            minutes+=1
            for i in range(len(rotten)):
                x,y=rotten.popleft()
                #visit all adjacent cells
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    #adjacent cell
                    xx,yy=x+dx,y+dy
                    #ignore if out of bounds
                    if xx<0 or xx==rows or yy<0 or yy==cols:
                        continue
                    #ignore if already rotten(2) or empty(0)
                    if grid[xx][yy]==0 or grid[xx][yy]==2:
                        continue
                    #reduce the fresh count and mark and grid as rotten
                    fresh_cnt-=1
                    grid[xx][yy]=2
                    rotten.append((xx,yy))
        return minutes if fresh_cnt==0 else -1