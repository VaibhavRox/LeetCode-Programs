from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        visited = set()
        q = deque()
        q.append((0, 0))  # Start from empty jugs

        while q:
            a, b = q.popleft()
            if a == target or b == target or a + b == target:
                return True

            if (a, b) in visited:
                continue
            visited.add((a, b))

            # Possible states:
            q.append((x, b))             # Fill Jug A
            q.append((a, y))             # Fill Jug B
            q.append((0, b))             # Empty Jug A
            q.append((a, 0))             # Empty Jug B

            # Pour A → B
            pour = min(a, y - b)
            q.append((a - pour, b + pour))

            # Pour B → A
            pour = min(b, x - a)
            q.append((a + pour, b - pour))

        return False