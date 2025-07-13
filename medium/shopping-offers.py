from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n=len(price)
        @lru_cache(None)
        def dfs(current_needs):
            # Base cost: if no offer is used, buy all items at full price
            total=sum(current_needs[i]*price[i] for i in range(n))
            # Try each special offer
            for offer in special:
                new_needs=[] # Track what's left after using an offer
                # Check if the offer can be applied (doesn't exceed needs)
                for i in range(n):
                    if offer[i]>current_needs[i]:
                        break # Can't apply offer — skip it
                    new_needs.append(current_needs[i]-offer[i])
                else:
                    # If no break occurred, offer is valid
                    # If no break occurred, offer is valid
                    s_offer=offer[-1]
                    total=min(total,s_offer+dfs(tuple(new_needs)))
            return total  # Return minimum total cost for current_needs
         # Return minimum total cost for current_needs
        return dfs(tuple(needs))
    
#EXPLANATION:
#lru_cache:
#It's a tool that automatically remembers (caches) the results of function calls, so:
#If the function is called again with the same arguments, Python can return the result instantly, instead of recalculating it.
# Example input:
# price = [2, 5]           # Apple: $2, Banana: $5
# special = [[3, 0, 5],     # Offer 1: 3 apples for $5
#            [1, 2, 10]]    # Offer 2: 1 apple + 2 bananas for $10
# needs = [3, 2]           # We want 3 apples and 2 bananas

# Let's walk through:
# Initial call: dfs((3, 2))
# Base cost: 3*2 + 2*5 = 6 + 10 = 16

# Try offer [3, 0, 5] (3 apples for $5)
# It’s valid since 3 ≤ 3 and 0 ≤ 2
# New needs = [0, 2] → dfs((0, 2))
#     Base cost = 0*2 + 2*5 = 10
#     No valid offers apply → return 10
# Total = 5 (offer) + 10 = 15

# Try offer [1, 2, 10] (1 apple + 2 bananas)
# It’s valid since 1 ≤ 3 and 2 ≤ 2
# New needs = [2, 0] → dfs((2, 0))
#     Base cost = 2*2 + 0 = 4
#     No valid offers apply → return 4
# Total = 10 (offer) + 4 = 14
# Final answer: min(16, 15, 14) = 14 ✅
# The function will return 14 as the minimum cost to fulfill the needs
        
