class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            # If tank is empty, start from next station
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

sol = Solution()
print("Start station index:", sol.canCompleteCircuit(gas, cost))
#EXPLAINATION ---------->

# This code solves the Gas Station problem by simulating the journey around the circular route.

# It tracks two main things:

# total_tank: the overall gas left after traveling the full circle.

# curr_tank: the current gas in your tank while simulating the route.

# 🔁 How the loop works:
# At each station i, it calculates:

# gain = gas[i] - cost[i]
# This is how much gas you gain or lose after leaving that station.

# It adds gain to both total_tank and curr_tank.

# ❌ If curr_tank < 0:
# It means you can’t reach the next station from here, so the current starting point has failed.

# We reset the starting point to the next station:

# start_index = i + 1
# curr_tank = 0
# ✅ Final Check:
# After going through all stations, if total_tank >= 0, that means it’s possible to complete the circuit.

# Return the start_index which is the first station from where the full journey is possible.

# If total_tank < 0, return -1 — the journey is impossible.

# 🧪 Sample input walkthrough:
# For:

# python
# Copy
# Edit
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# Total gas = 15

# Total cost = 15 → ✅ possible

# The code finds that starting at index 3 lets you complete the entire circuit without running out of gas.

# So it prints:

# Start station index: 3
