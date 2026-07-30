class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)          # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()              # Undo (Backtrack)

        backtrack(1, [])
        return ans