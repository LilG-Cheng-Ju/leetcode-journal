# 3169. Count Days Without Meetings 🟡

[🔗 3169. Count Days Without Meetings](https://leetcode.com/problems/count-days-without-meetings)

## Description
Given an positive integer `days`, representing the total number of days an employee is available for work (starting from day `1`), and a 2D array `meeting`, where `meeting[i] = [start_i, end_i]` represents the starting and ending days of meeting i.

Find the count of days when the employee **has no meetings.**

## Approach - sweep line & sort
💡 Using a `difference array` efficiently compute prefix sums and determine free days.

### 🔹 Steps:
1. **Maintain a hashmap `schedule`** 
 - Record events using a difference array technique.
 - When a meeting starts on day `s`, increment `schedule[s]` by 1.
 - When a meeting ends on day `e`, decrement `schedule[e + 1]` by 1.
 - The `e + 1` ensures that day `e` is still **within the meeting**, but `e + 1` **is the first free day after the meeting.**
2. **Sort the key in `schedule`** to iterate through all events in order.
3. **Maintain a `prefix sum`**
 - If `prefix_sum == 0`, the employee has no meeting that day.
4. **Compute free days (`ans`)**
 - Accumulate the count of free days using `current_day - prev_day`.

### ⏳ Complexity Analysis 
- **Time Complexity**: `O(n log n)`
    - Sorting the events takes `O(n log n)`, where `n` is the number of unique days in `meetings`.
- **Space Complexity**: `O(n)`
    - The hashmap `schedule` stores at most `2n` entries, where `n` is the number of meetings.

