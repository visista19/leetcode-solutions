import math
class Solution:
    def isPrime(self, n):
        count=0
        for i in range(1,int(math.sqrt(n)+1)):
            if n%i==0:
                count+=1
                if(i!=n/i):
                    count+=1
        return count==2
# 1. Purpose
# This function checks if a number n is prime by counting how many divisors it has.

# 2. Variables
# count → tracks how many divisors have been found so far.

# i → loop variable, starts from 1 and goes up to √n (since any factor greater than √n will have a corresponding smaller factor that’s already checked).

# 3. Loop logic

# for i in range(1, int(math.sqrt(n) + 1)):
# The loop runs from 1 to √n (inclusive).

# Why stop at √n? Because divisors come in pairs: if i divides n, then n/i is also a divisor.

# 4. Divisor check
# if n % i == 0:
# If n is divisible by i, then:

# Increase count by 1 (for i itself).

# If i is not equal to n/i (to avoid counting perfect squares twice), also increase count for the other divisor.

# Example for n = 6:

# i = 1 → divisors: 1 and 6 → count += 2

# i = 2 → divisors: 2 and 3 → count += 2
# Total = 4 divisors.

# 5. Prime check

# return count == 2
# A prime number has exactly 2 divisors: 1 and itself.

# So, if count == 2, return True (prime), otherwise False.

# ✅ Example runs

# n = 7 → divisors: 1, 7 → count = 2 → prime ✅

# n = 9 → divisors: 1, 3, 9 → count = 3 → not prime ❌

# 💡 Small note: Your range() ends at int(math.sqrt(n) + 1), but the standard prime check loop starts at 2 (not 1) and directly returns False if divisible, so your method is slightly slower for large n because it counts divisors rather than stopping early.
