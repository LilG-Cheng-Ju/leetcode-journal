# Dijkstra

## 何時使用 Dijkstra?
- 尋找有向或無向圖中單一源點到其他節點的最短路徑
- 圖的邊權重必須**非負**

## 特點
- **貪心策略**：透過 **priority queue**，每次選擇當前距離最小的節點，確保局部最優逐步推向全局最優
- **限制**：無法處理負權邊，須改用 [**Bellman-Ford**](./Bellman-Ford.md) 算法

## 程式碼範例
```python
def dijkstra(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    
    while heap:
        curr_dist, curr = heappop(heap)
        if curr in visited:
            continue
        visited.add(curr)
        
        for neighbor, weight in graph[curr]:
            if neighbor not in visited:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heappush(heap, (new_dist, neighbor))
    
    return distances
```

## 複雜度分析

- **時間複雜度**：`O((V+E)log V)`  
V 為節點數，E 則為邊數
    - 每個節點最多出入 heap 一次，複雜度為 `O(V log V)`
    - 每條邊在更新鄰居距離時可能觸發堆更新，為 `O(E log V)`
    - 整體時間複雜度為 `O((V+E)log V)`  
- **空間複雜度**：`O(V)` 
用於 heap 及 distance array

## 最短路徑演算法比較

| 演算法 | 時間複雜度 | 空間複雜度 | 適用場景 | 支援負權邊 | 偵測負權環 | 限制 |
|--------|------------|------------|----------|------------|------------|------|
| Dijkstra | `O((V + E) log V)`（使用 Heap） | `O(V)` | 單源最短路徑（非負權圖） | ❌ | ❌ | 無法處理負權邊，無法偵測負環 |
| Bellman-Ford | `O(V * E)` | `O(V)` | 單源最短路徑（含負權） | ✅ | ✅ | 較慢，密集圖效率差 |
| Floyd-Warshall | `O(V^3)` | `O(V^2)` | 所有點對最短路徑 | ✅ | ✅ | 空間和時間需求高，不適合大圖 |

## 經典題目
- [**743. Network Delay Time**](https://leetcode.com/problems/network-delay-time/)（訊號傳播時間）
- [**787. Cheapest Flights Within K Stops**](https://leetcode.com/problems/cheapest-flights-within-k-stops/)（有限站點的最便宜航班）
- [**1514. Path with Maximum Probability**](https://leetcode.com/problems/path-with-maximum-probability/)（最大機率路徑）
- [**505. The Maze II**](https://leetcode.com/problems/the-maze-ii/)（迷宮中的最短路徑）
- [**1631. Path With Minimum Effort**](https://leetcode.com/problems/path-with-minimum-effort/)（最小努力路徑）