from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        q=defaultdict(int)
        left=0
        maxlen=-1
        for right in range(len(s)):
            q[s[right]]+=1
            while len(q)>k:
                q[s[left]]-=1
                if q[s[left]]==0:
                    del q[s[left]]
                left+=1
            if len(q)==k:
                maxlen=max(maxlen,right-left+1)
        return maxlen
            
            
        
        