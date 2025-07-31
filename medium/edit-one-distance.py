def isOneEditDistance(s, t):
    len_s = len(s)
    len_t = len(t)
    # Case 1: Replace (same length)
    if len_s == len_t:
        diff = 0
        for i in range(len_s):
            if s[i] != t[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1  # Must be exactly one replace
    # Case 2: Insert/Delete (length difference = 1)
    if abs(len_s - len_t) == 1:
        # Make sure s is always the shorter string
        if len_s > len_t:
            s, t = t, s  # swap
        i = j = diff = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                diff += 1
                j += 1  # Skip one char in longer string
                if diff > 1:
                    return False
        return True  # At most one skip was needed
    # Case 3: More than one edit needed
    return False
    # QUESTION:Given two strings s and t, determine if they are both one edit distance apart.
    # Note: 
    # There are 3 possiblities to satisify one edit distance apart:
    # Insert a character into s to get t
    # Delete a character from s to get t
    # Replace a character of s to get t
    # Example 1:
    # Input: s = "ab", t = "acb"
    # Output: true
    # Explanation: We can insert 'c' into s to get t.
    # Example 2:

    # Input: s = "cab", t = "ad"
    # Output: false
    # Explanation: We cannot get t from s by only one step.
    # Example 3:

    # Input: s = "1203", t = "1213"
    # Output: true
    # Explanation: We can replace '0' with '1' to get t.