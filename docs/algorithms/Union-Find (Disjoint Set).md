# Union-Find (Disjoint Set Union, DSU)

Union-Find（又稱`並查集`或`Disjoint Set Union`, DSU）是一種用於處理動態連通性問題的資料結構。它常用於圖論演算法中，特別是在需要合併集合或判斷是否屬於同一集合的情境，如連通圖判斷、最小生成樹（Kruskal's Algorithm）以及網路連通性問題等。 經典島嶼問題也可以使用 Union-Find 進行解題 (判斷周圍的區塊是否跟自己享有共同的 root)。

## 特點
- 能高效合併兩個集合(`union`操作)
- 能快速查找某個元素屬於哪個集合(`find`操作)
- 透過`路徑壓縮`及`Rank優化`提升效率，使每一次`union`或是`find`操作接近常數時間。

## 主要操作

### `find(x)`: 查找元素 `x` 的`根（root）`
- 如果 `x` 是集合的代表，則返回 `x` 本身。  
- 否則，遞迴查找 `x` 的父節點，並**壓縮路徑**（讓 `x` 直接連到 root），以加速未來的查找。  

一般會使用下方的 pattern
```python
def find(x):
    if parent[x] != x:
        # 路徑壓縮：
        # 將 x 直接指向其代表節點 root，以減少未來的查找步驟
        parent[x] = find(parent[x]) 
    return parent[x]
```

### `union(x, y)`: 合併 `x` 和 `y` 所在的集合
- 先透過 `find(x)` 和 `find(y)` 找到各自的`根節點`。
- 使用 `Rank 優化`：
    - 若 `rank[root_x]` > `rank[root_y]`，則 `root_y` 接到 `root_x`。
    - 反之則 `root_y` 接到 `root_x`。
    - 若兩邊 `Rank` 相等，則 `root_y` 接到 `root_x`，並增加 `root_x`的 `Rank`。

Union 操作也常見如下的pattern
```python
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        # Rank 優化：比較兩個集合的秩（樹的高度），將較小的樹合併到較大的樹
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
             # 如果 x 和 y 的樹高度相同，
             # 隨便將一個合併到另一個，並且增加合併後樹的高度
            parent[root_y] = root_x
            rank[root_x] += 1 # 增加根節點的 rank（樹的高度）
```

**💡路徑壓縮讓後續的 find 操作可以在常數時間 `O(1)`內完成**

**💡透過比較 `Rank` 來進行 `Union` 操作，可以保證合併時樹的深度不會過大，從而減少未來執行 Find 操作時需要遍歷(traversing) 的次數。**

## 應用場景
- 連通性問題 (判斷兩個節點是否在同一個group內)
- 群組合併問題
- 等式與不等式問題

## 複雜度分析
### 時間複雜度：
- `find` 與 `union` 操作接約略等於常數時間，亦即 `O(1)`。
    (實則為`O(α(n))`，其中α(n)為阿克曼函數的反函數)
- 在處理 m 次操作的情況下，可以視為 `O(m)`
### 空間複雜度
- `O(n)`：用於儲存 `root` 及 `rank`

## 經典題目
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection)
    - 如果發現某條邊在執行 union 操作前就已經有共同的root，表示圖內出現環了。
- [2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components)

