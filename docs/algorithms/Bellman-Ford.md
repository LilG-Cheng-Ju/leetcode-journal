# Bellman-Ford

## 何時使用 Bellman-Ford?
- 尋找有向圖中單一源點到所有節點的**最短路徑**
- 支援**負權重邊**，並可偵測**負權重迴圈**

## 特點與技巧
- **動態規劃**：通過放鬆（relaxation）邊，反覆更新最短距離
- **負環檢測**：額外迭代檢查是否仍可更新距離，判斷負權重迴圈
- **兩種常見實作方式**：
  - **直接更新（原地放鬆）**：適用於標準最短路徑問題，不需臨時陣列
  - **使用臨時陣列**：用於需要「每一輪只使用上一輪資料」的題目（如：限制步數 / 傳播問題）
   [**787. Cheapest Flights Within K Stops**](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- **限制**：時間複雜度較高，適合中小型圖

## 程式碼範例

### 標準寫法(直接更新)

適用於：單源最短路徑，無特殊更新限制

```python
def bellman_ford(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0

    # 放鬆 V-1 次
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # 檢查負權重迴圈
    for u in range(n):
        for v, weight in graph[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None  # 有負環
    
    return distances
```

### 限制狀態傳播的寫法（使用臨時陣列）

適用於：不能用當前輪結果繼續更新（如「每次只能跳一步」的狀況）

```python
def bellman_ford(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0
    
    # 放鬆 V-1 次
    for _ in range(n - 1):
        temp_distances = distances.copy() # 臨時陣列
        for u in range(n):
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < temp_distances[v]:
                    temp_distances[v] = distances[u] + weight
        distances = temp_distances # 更新主陣列
    
    # 檢查負權重迴圈
    for u in range(n):
        for v, weight in graph[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None  # 如果放鬆 V-1 次後還能更新，表示有負環
    
    return distances
```

## 什麼時候一定要使用臨時陣列？

有些情況下，**不能直接更新距離陣列**，必須使用**上一輪的結果進行放鬆操作**，此時就需要使用臨時陣列。否則可能會提早用到當前輪才剛更新的值，導致結果錯誤

| 情境 | 是否需要臨時陣列 | 原因 |
|------|------------------|------|
| 標準單源最短路徑（無步數限制） | ❌ | 放鬆順序不影響正確性 |
| 限定只能經過 K 次跳躍的最短路徑 | ✅ | 不能提早用到同輪的更新結果（只能用前一輪） |
| 分層圖、多階段 DP 變形 | ✅ | 每一層只能使用上一層的資訊 |
| 傳染模擬、擴散問題（BFS/層級概念） | ✅ | 同樣需分層，每輪不能互相干擾 |

## 複雜度分析

- **時間複雜度**：`O(V * E)`
  - 迭代 `V-1` 次，每次遍歷所有邊 `E`，進行放鬆操作
  - 負環檢測需額外一次迭代，總計 `O(V * E)`
- **空間複雜度**：`O(V)`（距離陣列）

## 經典題目
- [**787. Cheapest Flights Within K Stops**](https://leetcode.com/problems/cheapest-flights-within-k-stops/)（有限站點的最便宜航班）
- [**1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance**](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)（閾值距離內鄰居最少的城市）
- [**743. Network Delay Time**](https://leetcode.com/problems/network-delay-time/)（訊號傳播時間）
- [**1514. Path with Maximum Probability**](https://leetcode.com/problems/path-with-maximum-probability/)（最大機率路徑）
- [**1162. As Far from Land as Possible**](https://leetcode.com/problems/as-far-from-land-as-possible/)（最遠離陸地的距離）