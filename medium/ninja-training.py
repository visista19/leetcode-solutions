#User function Template for python3

class Solution:
    def f(self,day, last, points, dp):
        if day==0:
            maxi=0
            for i in range(3):
                if i!=last:
                    maxi=max(maxi,points[0][i])
            return maxi
        if dp[day][last]!=-1:
            return dp[day][last]
        maxi=0
        for i in range(3):
            if i!=last:
                activity=points[day][i] + self.f(day-1, i, points,dp)
                maxi=max(maxi,activity)
        dp[day][last]=maxi
        return maxi
    def maximumPoints(self, arr):
        n=len(arr)
        dp=[[-1]*4 for _ in range(n)]
        return self.f(n-1, 3, arr, dp)
    
    
# Perfect 👌 This is a **Dynamic Programming (DP)** solution to the classic **Ninja Training** (or “Maximum Points” with activities) problem. Let me explain step by step:

# ---

# ## 🔹 Problem Idea (Ninja Training)

# * There are `n` days.
# * Each day you can do **one of 3 activities** (say `A`, `B`, `C`).
# * `points[day][i]` = points earned by doing activity `i` on day `day`.
# * You **cannot do the same activity on two consecutive days**.
# * Goal: Find the **maximum points** you can earn in `n` days.

# ---

# ## 🔹 Code Walkthrough

# ### Function `f(day, last, points, dp)`

# This is a **recursive function with memoization**.

# * **Parameters**:

#   * `day`: which day we are solving for (0-based index).
#   * `last`: which activity was done on the *next* day (so we cannot repeat it on this day).
#   * `points`: 2D array of size `n x 3`.
#   * `dp`: memoization table.

# ---

# ### Base Case

# ```python
# if day == 0:
#     maxi = 0
#     for i in range(3):
#         if i != last:
#             maxi = max(maxi, points[0][i])
#     return maxi
# ```

# 👉 If it’s the **first day (day = 0)**:

# * Choose the activity that is **not equal to `last`**.
# * Take the maximum points available.

# ---

# ### Memoization Check

# ```python
# if dp[day][last] != -1:
#     return dp[day][last]
# ```

# 👉 If we’ve already solved this state `(day, last)`, return the stored result.

# ---

# ### Transition (Recurrence)

# ```python
# maxi = 0
# for i in range(3):
#     if i != last:
#         activity = points[day][i] + self.f(day - 1, i, points, dp)
#         maxi = max(maxi, activity)
# ```

# 👉 For the current `day`:

# * Try all **3 activities** (`i = 0,1,2`).
# * Skip the one equal to `last`.
# * Add today’s points (`points[day][i]`) + best result from the previous day with activity `i` as the "last".
# * Take the **maximum** over all choices.

# ---

# ### Store in DP and Return

# ```python
# dp[day][last] = maxi
# return maxi
# ```

# 👉 Save result to avoid recalculating.

# ---

# ### Wrapper Function

# ```python
# def maximumPoints(self, arr):
#     n = len(arr)
#     dp = [[-1] * 4 for _ in range(n)]
#     return self.f(n - 1, 3, arr, dp)
# ```

# * `n = len(arr)` → number of days.
# * `dp[n][4]` → memo table (4 because `last` can be `0,1,2`, or `3`).
# * Start recursion from the **last day (`n-1`)**, with `last = 3` (dummy, meaning no restriction on the last activity).

# ---

# ## 🔹 Example

# Input:

# ```python
# arr = [
#   [10, 40, 70],  # Day 0
#   [20, 50, 80],  # Day 1
#   [30, 60, 90]   # Day 2
# ]
# print(Solution().maximumPoints(arr))
# ```

# Working:

# * Day 2: best = 90 (activity 2).
# * Day 1: can’t repeat activity 2 → best = 50 (activity 1).
# * Day 0: can’t repeat activity 1 → best = 70 (activity 2).

# Total = `70 + 50 + 90 = 210`.

# ---

# ✅ So this program finds the **maximum points** possible with the "no consecutive same activity" rule using **recursion + memoization (top-down DP)**.

# ---

# Do you want me to also show you the **bottom-up tabulation version** (iterative DP) of the same problem?
