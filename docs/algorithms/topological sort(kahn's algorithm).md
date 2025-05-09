# Topological Sort

Topological Sort 是一種圖論演算法，主要用於有向無環圖（DAG, Directed Acyclic Graph）。它的目的是將圖中的頂點排列成一個線性順序，使得對於每一條有向邊 `(u, v)`，頂點 `u` 在 `v` 之前。

## 特點
- 只適用於有向無環圖（DAG），因為如果圖中有環，則無法確定有效的線性順序。
- 常見於需要滿足依賴關係的問題，比如任務調度、編譯依賴、解決依賴的軟體包等。

## 實現方式

常見的 Topological Sort 實現方法有兩種：

### 1. Kahn's Algorithm（廣度優先）
- 初始化所有頂點的入度。
- 依次將入度為 0 的頂點加入隊列，並從圖中移除該頂點及其邊，更新其相鄰頂點的入度。
- 重複此過程直到所有頂點都被處理。

### 2. 深度優先搜索（DFS）
- 對圖中的每個頂點進行 DFS 訪問，當訪問完成後，將該頂點加入結果列表。
- 最後反轉結果列表，即為拓撲排序結果。

## 時間與空間複雜度
- **時間複雜度**：O(V + E)，其中 V 是圖中的頂點數，E 是邊的數量。
- **空間複雜度**：O(V + E)，主要用於存儲圖的結構和處理過程中的輔助資料結構。