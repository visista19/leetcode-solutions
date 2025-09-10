from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        q = defaultdict(int)
        maxlen = 0
        maxfreq = 0
        left = 0

        for right in range(len(s)):
            q[s[right]] += 1
            maxfreq = max(maxfreq, q[s[right]])  # track the max frequency

            # check if window is valid
            while (right - left + 1) - maxfreq > k:
                q[s[left]] -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen
# for better understanding :
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         q=defaultdict(int)
#         maxlen=0
#         maxfreq=0
#         left=0
#         for right in range(len(s)):
#             if s[right] not in q:
#                 q[s[right]]=1
#             else:
#                 q[s[right]]+=1
#             maxfreq=max(q.values())
#             if (right-left+1)-maxfreq<=k:
#                 maxlen=max(right-left+1, maxlen)
#             else:
#                 while (right-left+1)-maxfreq>k and left<right:
#                     q[s[left]]-=1
#                     left+=1
#         return maxlen


        