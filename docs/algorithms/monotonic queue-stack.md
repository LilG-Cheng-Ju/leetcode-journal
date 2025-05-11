# Monotonic Stack / Queue（單調堆疊／佇列）

## 何時使用 Monotonic Stack / Queue？

- 要在**線性時間內**找**左/右邊第一個比自己大/小的元素**
- 處理**區間最大值／最小值**並保持更新（滑動視窗）
- 維護一個「單調遞增／遞減序列」以快速查詢當前極值

## 特點

- 維持單調性：元素從頭到尾遞增或遞減。
- 常搭配**掃描一次 array**解決：
    - Next Greater / Smaller Element
    - 最大矩形、滑動視窗最大值
- 時間複雜度多為 O(n)，因為每個元素最多被加入與彈出一次。

## Monotonic Stack vs Monotonic Queue

| 特性             | Monotonic Stack 🧱            | Monotonic Queue 📏            |
|------------------|-------------------------------|-------------------------------|
| 結構             | 後進先出（LIFO）              | 先進先出（FIFO）              |
| 單調性           | 通常維持單調「遞增」或「遞減」 | 同上，但維護的是滑動視窗中的最大或最小值 |
| 常見場景         | 找 **下一個／前一個較大或較小元素** | 處理 **固定區間（如滑動視窗）的最大／最小值** |
| 對時間的敏感性   | 不考慮區間長度／時間順序        | 明確限制一個固定長度的區間（視窗） |

### 什麼時後用？

#### Monotonic Stack

- 要求找出：
  - **下一個更大元素（Next Greater Element）**
  - **上一個更小元素（Previous Smaller Element）**
  - **每個元素對應的最近較大/小值的位置**
- 題目有「**相對位置**」或「**單調性**」的描述
- 題目明示需要「**鄰近比較或紀錄**」

📌 常見題目關鍵字：
- Next Greater/Smaller Element
- Histogram / Rectangle 面積
- Temperature / Stock span

---

#### Monotonic Queue

- 題目給你一個**滑動視窗大小 k**
- 要你找出每個視窗的：
  - 最大值 / 最小值
- 要求區間內的最大最小 / 單調性 / 效率

📌 常見題目關鍵字：
- Sliding Window
- Minimum / Maximum in Subarray
- Fixed-length window + Optimization

## 模板

### Monotonic Stack

📌 找每個元素的 下一個較大元素（Next Greater Element）

```python
def nextGreater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)

    return res
```
> 單調遞減 stack：維持從頂到底 遞減，遇到更大的元素時把小的彈出。

### Monotonic Queue

📌 處理滑動視窗最大值（Sliding Window Maximum）

```python
def maxSlidingWindow(nums, k):
    dq = deque()
    res = []

    for i in range(len(nums)):
        # 移除超出視窗範圍的元素
        if dq and dq[0] <= i - k:
            dq.popleft()

        # 維持遞減性（從大到小），移除比現在小的
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            res.append(nums[dq[0]])

    return res
```
> 單調遞減 queue：維持最大值在最前端

## 複雜度分析

- **時間複雜度**：`O(n)`  
- **空間複雜度**：`O(n)` 
> n 為給定陣列的長度，由於每個元素多半只會進入/彈出一次，而最壞情況下 monotonic stack / queue 將會跟給定陣列一樣長，因此複雜度皆為 `O(n)`

## 經典題目

### Monotonic Stack

- [**739. Daily Temperature**](https://leetcode.com/problems/daily-temperatures/)（找出下個更大的溫度）
- [**496. Next Greater Element I**](https://leetcode.com/problems/next-greater-element-i/)（找下一個更大的元素）
- [**84. Largest Rectangle in Histogram**](https://leetcode.com/problems/largest-rectangle-in-histogram/)（柱狀圖中的最大矩形）
- [**1019. Next Greater Node In Linked List**](https://leetcode.com/problems/next-greater-node-in-linked-list/)（鏈表中找下一個更大的節點）
- [**1004. Max Consecutive Ones III**](https://leetcode.com/problems/max-consecutive-ones-iii/)（滑動窗口 + 區間最大值）

---

### Monotonic Queue

- [**239. Sliding Window Maximum**](https://leetcode.com/problems/sliding-window-maximum/)（滑動視窗中找最大值）
- [**862. Shortest Subarray with Sum at Least K**](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)（最短子陣列和大於等於K）
- [**1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)（最長連續子陣列絕對差小於等於限制）
- [**239. Sliding Window Maximum**](https://leetcode.com/problems/sliding-window-maximum/)（滑動視窗最大值）