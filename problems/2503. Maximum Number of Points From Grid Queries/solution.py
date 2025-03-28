from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count, col_count = len(grid), len(grid[0])
        sort_queries = sorted(queries)
        visited = set([(0, 0)])

        heap = [[grid[0][0], 0, 0]]
        heapq.heapify(heap)

        points = 0
        res = {}

        for q in sort_queries:
            while heap and heap[0][0] < q:
                value, i, j = heapq.heappop(heap)
                points += 1

                for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_i = i + x
                    new_j = j + y
                    if  (new_i, new_j) not in visited and new_i >= 0 and new_j >= 0 and new_i < row_count and new_j < col_count:
                        visited.add((new_i, new_j)) 
                        heapq.heappush(heap, [grid[new_i][new_j], new_i, new_j])
                        
            res[q] = points

        return [res[q] for q in queries]