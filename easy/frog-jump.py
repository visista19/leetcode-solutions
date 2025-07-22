#User function Template for python3
class Solution:
    def minCost(self, height):
        n=len(height)-1
        dp=[0]*(len(height)+1)
        dp[0]=0
        for i in range(1,len(height)):
            if i==1:
                dp[i]=dp[i-1]+abs(height[i-1]-height[i])
                continue
            dp[i]=min(dp[i-1]+abs(height[i-1]-height[i]),
            dp[i-2]+abs(height[i-2]-height[i]))
        return dp[n]
            
#explaintion:
# eg: heights=[30,10,60,10,60,50]
# step 1:
# we create a dp list of length heights +1 --> dp[0]*len(heights)+1
# we get :[0,0,0,0,0,0,0]
# we keep dp[0] as 0 cuz the jump from index 0 to index 0 is zero itself
# we start the calucalation from 1
# step 2:
# i=1
# dp[1]=dp[1-1]+ abs(10-30)
# dp[1]=0+20=20
# dp=[0,20,0,0,0,0,0]
# i=2
# dp[2]=min(dp[2-1]+abs(60-10), dp[2-2]+abs(60-30))
# dp[2]=min(20+50,0+30)=30
# dp=[0,20,30,0,0,0,0]
# i=3
# dp[3]=min(dp[3-1]+abs(10-60), dp[3-2]+abs(10-10))= min(30+50,20+0)=20
# dp=[0,20,30,20,0,0,0]
# i=4
# dp[4]=min(dp[4-1]+abs(60-10), dp[4-2]+abs(60-60))=min(20+50,30+0)=30
# dp=[0,20,30,20,30,0,0]
# i=5
# dp[5]=min(dp[5-1]+abs(60-50), dp[5-2]+abs(10-50))=min(30+10,20+40)=40
# dp=[0,20,30,20,30,40]
# 40 is the answer.
