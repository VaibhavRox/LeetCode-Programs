class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors={}
        color_count={} #Stores the balls having given color
        result=[]
        for x,y in queries:
            if x in ball_colors:
                prev_color=ball_colors[x]
                if prev_color!=y:  #only change if the color is different
                    color_count[prev_color]-=1
                    if color_count[prev_color]==0:
                        del color_count[prev_color]
                    ball_colors[x]=y
                    color_count[y]=color_count.get(y,0)+1
            else:
                ball_colors[x]=y
                color_count[y]=color_count.get(y,0)+1
            result.append(len(color_count))
        return result
