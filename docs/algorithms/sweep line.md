# Sweep Line (掃描線演算法)

Sweep Line（掃描線演算法）是一種在處理區間、幾何圖形、事件排序等問題時常用的技術。它的核心概念是**將問題轉化為一系列「事件」的處理**，並且按照某個軸（通常是時間軸或座標軸）順序掃描、處理這些事件。

## **核心概念**
1. **事件排序**：  
   - 把問題拆解為「事件」，並按照某個順序排序（例如：左到右、時間先後）。
   - 譬如會議開始、會議結束可視為兩個事件，在事件開始時+1，事件結束(的隔天)-1，透過前綴和可快速查找無會議的時候(即前綴和為0的時候)。
2. **掃描過程**：  
   - 使用**一條掃描線**，逐步處理事件。
   - 可能需要維護一個動態數據結構（如**平衡樹、堆、哈希表**）來儲存當前的活躍區間或元素。
3. **處理事件**：  
   - 新的事件進入時，更新狀態。
   - 舊的事件結束時，從狀態中移除。
   - 根據問題需求執行相應的操作。

## **時間複雜度**
- 如果排序的事件數為 `N`，則 Sweep Line 通常需要 `O(N log N)` 的時間：
  - `O(N log N)`: 主要來自對事件的排序。
  - `O(N log N)`: 掃描線過程中（如平衡樹操作）可能帶來額外的 `log N` 負擔。

## **應用場景**
1. **區間問題**
   - 計算最大重疊區間數（類似會議室安排問題）。
   - 判斷區間是否有交集（航班時刻、時序分析）。
2. **幾何問題**
   - 計算矩形的總面積（需要排序邊界）。
   - 判斷多邊形是否相交。
3. **Skyline Problem（天際線問題）**
   - 用來計算城市天際線輪廓。

## **經典題目**
- [**218. The Skyline Problem**](https://leetcode.com/problems/the-skyline-problem/)（城市天際線問題）
- [**3169. Count Days Without Meetings**](https://leetcode.com/problems/count-days-without-meetings)（計算無事件區間）

## **程式碼範例**
**示例：計算最大重疊區間數**
```python
import heapq

def minMeetingRooms(intervals):
    events = []
    
    # 將會議的開始與結束當作事件
    for start, end in intervals:
        events.append((start, 1))  # 進入會議
        events.append((end, -1))   # 離開會議
    
    # 按照時間排序（如果時間相同，離開事件先處理）
    events.sort()
    
    max_rooms = 0
    current_rooms = 0

    for _, event in events:
        current_rooms += event
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms

# 測試
meetings = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(meetings))  # Output: 2
