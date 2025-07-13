class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result=[]
        def backtrack(index,path):
            if index==len(digits):
                result.append(path)
                return
            letters=phone[digits[index]]
            for letter in letters:
                backtrack(index+1,path+letter)
        backtrack(0,"")
        return result
    # ---------------------- EXPLANATION ----------------------
# This function generates all possible letter combinations that the input digits could represent,
# based on a standard mobile phone keypad mapping.

# 🔁 It uses a recursive backtracking technique:
# - At each digit, it loops through all letters mapped to that digit.
# - It adds one letter at a time to a temporary string (called 'path').
# - When the path length equals the number of digits, it adds the complete combination to the result list.

# ✅ Base Case:
# - When index == len(digits), a complete combination has been formed → append to result.

# 🔄 Recursive Step:
# - For each letter mapped to the current digit, call backtrack on the next digit,
#   building up the combination character by character.

# 🎯 Example:
# Input: "23"
# Mappings: 2 → "abc", 3 → "def"
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# 🧠 Time Complexity: O(3^N * 4^M), where:
# - N = number of digits that map to 3 letters (like 2, 3, 4, 5, 6, 8)
# - M = number of digits that map to 4 letters (like 7, 9)
# ---------------------------------------------------------