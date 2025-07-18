class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target>x+y:
            return False
        stack=[(0,0)]
        visited=set()
        while stack:
            a,b=stack.pop()
            if a+b==target:
                return True
            if (a,b) in visited:
                continue
            visited.add((a,b))
            #append all possible states
            stack.append((x,b))   #Fill jug 1
            stack.append((a,y))   #Fill jug 2
            stack.append((0,b))     #Empty jug 1
            stack.append((a,0))     #Empty jug 2
            #Pour from A to B
            pour=min(a,y-b)
            stack.append((a-pour,b+pour))
            #Pour from B to A
            pour=min(b,x-a)
            stack.append((a+pour,b-pour))
        return False
