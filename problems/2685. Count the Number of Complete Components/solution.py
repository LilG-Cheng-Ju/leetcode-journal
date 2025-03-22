from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.root = [i for i in range(n)]
        self.rank = defaultdict(int)

        adj_count = defaultdict(int)
        group = defaultdict(list)

        for s, e in edges:
            self.union(s, e)
            adj_count[s] += 1
            adj_count[e] += 1

        for i in range(n):
            self.root[i] = self.find(i)
            group[self.root[i]].append(i)
        

        ans = 0
        for members in group.values():
            num_node = len(members)
            if all(adj_count[m] == num_node - 1 for m in members):
                ans += 1
        return ans
        

    def find(self, x) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
    