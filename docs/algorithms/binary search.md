# Binary Search (二分搜尋)

Binary Search（二分搜尋）是一種在**有序資料結構**上，快速縮小搜尋範圍的經典方法。通常適用於單調性（答案滿足某種單調條件）明確的問題。

## 特點
- 適合處理 **有序** 或 **具有單調性** 的資料。
- 每次搜尋將搜尋區間減半，時間複雜度極低。
- 小心處理邊界 (`l`, `r`) 的變化，以及 `mid` 的選擇。

## 何時使用 Binary Search？

| 類型 | 說明 | 例題 |
|:---|:---|:---|
| 排序好的陣列 | 在排序陣列中找元素 | Ex: 搜尋目標元素 |
| 最小化最大值 / 最大化最小值 | 二分**答案空間**而不是資料本身 | Ex: 分配工作、最小化時間問題 |
| 滿足某個條件的最小值或最大值 | 有單調性，找臨界點 | Ex: 開始出現 True 的位置 |

## Mid 的選擇

| mid 寫法 | 適用情況 |
|:---|:---|
| `mid = (l + r) // 2` | 傳統 binary search，偏左，適合找「第一個符合條件」 |
| `mid = (l + r) // 2 + 1` | 當更新 `l = mid` 時需要偏右，避免無限循環 |

> 一般來說，如果更新左邊界 `l = mid` 而不是 `l = mid + 1`時，mid則需要偏右，否則可能會出現無限循環

##  l 和 r 的更新

| 情況 | 更新方式 |
|:---|:---|
| `mid` 符合條件 | 視需求，可能縮小右界 (`r = mid - 1`) |
| `mid` 不符合條件 | 縮小左界 (`l = mid + 1`) |

> 記得：當你「想保留 mid」時，不要直接捨棄它

## 複雜度分析

- **時間複雜度**：`O(log n)`  
  每次搜尋將搜尋範圍減半。
- **空間複雜度**：`O(1)`（如果是遞迴版本則是 `O(log n)` 的 stack space）

## **經典題目**

- [**704. Binary Search**](https://leetcode.com/problems/binary-search/)（經典基礎版）
- [**278. First Bad Version**](https://leetcode.com/problems/first-bad-version/)（找第一個錯誤版本）
- [**875. Koko Eating Bananas**](https://leetcode.com/problems/koko-eating-bananas/)（二分最小速度）
- [**1011. Capacity To Ship Packages Within D Days**](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)（二分最小運輸能力）
- [**153. Find Minimum in Rotated Sorted Array**](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)（旋轉排序陣列找最小值）
- [**162. Find Peak Element**](https://leetcode.com/problems/find-peak-element/)（找局部最大值）
- [**34. Find First and Last Position of Element in Sorted Array**](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)（找目標值的範圍）
- [**410. Split Array Largest Sum**](https://leetcode.com/problems/split-array-largest-sum/)（將陣列分割成子陣列並最小化最大和）
- [**4. Median of Two Sorted Arrays**](https://leetcode.com/problems/median-of-two-sorted-arrays/)（兩個排序陣列找中位數，Hard）


---

## 程式碼範例

### 搜尋目標數字在排序陣列的位置

```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2  # mid 偏左
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

### 搜尋「最小符合條件」的位置（例如找第一個大於等於 target 的位置）

```python
def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            ans = mid
            r = mid - 1  # 繼續往左找
        else:
            l = mid + 1
    return ans

