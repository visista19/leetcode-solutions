class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        light = 0
        heavy = len(people) - 1
        boats = 0

        while light <= heavy:
            # Try to pair the lightest and heaviest
            if people[light] + people[heavy] <= limit:
                light += 1
            heavy -= 1
            boats += 1

        return boats
    
#EXPLANATION--->
# Problem Restatement
# You have people with weights in people[], and each boat can carry at most two people subject to a limit.

# Goal: Minimize the number of boats needed.

# 🧠 Why use this approach: greedy + two pointers
# 1. Sort the people by weight

# people.sort()
# This gives you an ordered list from lightest to heaviest, which helps in pairing strategically. 


# 2. Use two pointers

# light = 0              # lightest
# heavy = len(people)-1  # heaviest
# We always try to pair the heaviest person with the lightest person if it fits. 

# 3. Greedy pairing logic

# while light <= heavy:
#     if people[light] + people[heavy] <= limit:
#         light += 1  # they share a boat
#     heavy -= 1
#     boats += 1
# If the heaviest can go with the lightest, great — we use one boat for both.

# If not, the heaviest must go alone, and we still count a boat.

# In both cases, the heaviest person is always taken care of in each iteration. 


# 4. Why it's optimal
# This approach is proven to be optimal using a greedy-choice argument:

# In any optimal solution, the heaviest person (hi) must either go alone or with someone.

# If pairing them with the lightest (lo) is possible, that’s always a valid or even better choice—never worse.

# If not possible with the lightest, then pairing hi with anyone will fail. So hi must go alone.

# Essentially, pairing the heaviest with the lightest possible is never a bad move and often saves space.

# ✅ Time & Space Complexity:
# Sorting: O(n log n)

# Two-pointer pass: O(n)

# Overall: O(n log n) time, O(1) extra space

# 🎯 Summary:
# Sort the array

# Use light and heavy pointers

# Always take care of the heaviest person:

# Pair with lightest if you can

# Or send alone otherwise

# Count a boat each step