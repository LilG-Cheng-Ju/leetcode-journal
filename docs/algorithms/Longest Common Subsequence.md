# Longest Common Subsequence (LCS) 最長公共子序列

## 特性
- 尋找兩個序列（字串、陣列等）的**最長公共子序列**，即保持相對順序的公共子序列
- 子序列不同於子字串，在原序列中不用**相鄰**，但要保持**順序**

## 特點與技巧
- **動態規劃 (DP)**：用 DP 表格記錄子問題，比較兩個序列的字符
- **技巧**：
  - 構建 `dp[i][j]` 表示第一序列前 `i` 個字符與第二序列前 `j` 個字符的 LCS 長度。
  - 若字符相等，則包含該字符；否則，選擇較長的子序列
  - 可回溯 DP 表格重建 LCS
  - 空間優化：將二維 DP 壓縮為一維，降低空間複雜度

## 程式碼範例
### 1. 標準二維 DP

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 需要額外的一行 & 一列處理 text1 & text2 為空序列的情況

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### 1 維優化

```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    if m < n:
        text1, text2, m, n = text2, text1, n, m  
        # 確保使用較短序列
    dp = [0] * (n + 1)
    
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i-1] == text2[j-1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev = temp
    
    return dp[n]
```

### 編輯問題

[**72. Edit Distance**](https://leetcode.com/problems/edit-distance/)（最小編輯距離）  
[**583. Delete Operation for Two Strings**](https://leetcode.com/problems/delete-operation-for-two-strings/)（兩個字串的刪除操作）

```python
def minEditOperations(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1,  # 刪除
                              dp[i][j-1] + 1,  # 插入
                              dp[i-1][j-1] + 1) # 替換
    
    return dp[m][n]
```

## 複雜度分析
- **時間複雜度**：`O(m * n)`
  - 遍歷兩個序列的所有字符對，`m`, `n` 為序列長度。
- **空間複雜度**：
  - 二維 DP：`O(m * n)`（完整 DP 表格）。
  - 一維 DP：`O(min(m, n))`（壓縮為一維陣列）。

## 經典題目
- [**1143. Longest Common Subsequence**](https://leetcode.com/problems/longest-common-subsequence/)（標準 LCS）
- [**72. Edit Distance**](https://leetcode.com/problems/edit-distance/)（最小編輯距離）
- [**1092. Shortest Common Supersequence**](https://leetcode.com/problems/shortest-common-supersequence/)（最短公共超序列）
- [**583. Delete Operation for Two Strings**](https://leetcode.com/problems/delete-operation-for-two-strings/)（兩個字串的刪除操作）
- [**712. Minimum ASCII Delete Sum for Two Strings**](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)（最小 ASCII 刪除和）