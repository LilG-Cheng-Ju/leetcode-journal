# Knapsack Problem（背包問題）

背包問題是一類經典的動態規劃問題，主要解決「在給定容量限制下，選擇物品使得價值最大化或成本最小化」的問題。它根據能否重複選取同一物品，可以分為 0/1 背包（每個物品只能用一次）與完全背包（每個物品可以用無限次）。

---

## 何時使用 Knapsack？

- 題目中有「選或不選」某些物品
- 有明確的「容量」限制（如金額、重量、時間）
- 需要 **最大化價值** 或 **最小化成本**

---

## 特點

- 經典動態規劃題型，狀態轉移清晰
- 有兩層迴圈：第一層遍歷物品，第二層遍歷容量（根據是否可重複使用，選擇正序或倒序）

---

## 兩層迴圈的意涵

- 外層迴圈：遍歷所有物品
- 內層迴圈：針對每種容量，根據是否能加入此物品來更新狀態

| 類型     | 內層迴圈方向 | 原因                             |
|----------|---------------|----------------------------------|
| 0/1 背包 | 倒序（W → 0） | 避免同一物品被重複使用             |
| 完全背包 | 正序（0 → W） | 允許重複使用，之前的狀態可再被使用 |

## 0/1 背包（01 Knapsack）

每個物品只能使用一次。常見於價值最大化問題。

```python
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):  # 遍歷物品
    for j in range(W + 1):  # 遍歷背包容量
        if j < weight[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j],
                           dp[i - 1][j - weight[i - 1]] + value[i - 1])
```

## 完全背包（Unbounded Knapsack）

每個物品可以使用無限多次。常見於「錢幣兌換」「組合方式」等問題。

```python
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        if j < weight[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j],
                           dp[i][j - weight[i - 1]] + value[i - 1])  # 注意是 dp[i][...]!
```

## 空間複雜度優化

- 0/1 背包 (倒序)

```python
dp = [0] * (W + 1)

for i in range(n):  # 遍歷物品
    for j in range(W, weight[i] - 1, -1):  # 倒序，避免重複使用
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
```

- 完全背包 (正序)

```python
dp = [0] * (W + 1)

for i in range(n):  # 遍歷物品
    for j in range(weight[i], W + 1):  # 正序，允許重複使用
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
```

## 複雜度分析

- **時間複雜度**：`O(n * W)`  
  其中 n 是物品數量，W 是容量限制
- **空間複雜度**：
    - `O(n * W)` 二維DP
    - `O(W)` 一維優化

## **經典題目**

- [**322. Coin Change**](https://leetcode.com/problems/coin-change/)（完全背包，最少硬幣數量，使用 `min`）
- [**518. Coin Change II**](https://leetcode.com/problems/coin-change-ii/)（完全背包，組合總數）
- [**416. Partition Equal Subset Sum**](https://leetcode.com/problems/partition-equal-subset-sum/)（0/1 背包，是否能分成兩個子集）
- [**139. Word Break**](https://leetcode.com/problems/word-break/)（背包變形，是否可用字典拼出字串）
- [**474. Ones and Zeroes**](https://leetcode.com/problems/ones-and-zeroes/)（多維 0/1 背包）
- [**1049. Last Stone Weight II**](https://leetcode.com/problems/last-stone-weight-ii/)（0/1 背包轉化，最小差值）