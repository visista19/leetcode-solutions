class Solution(object):
    def finalString(self, s):
        s1=list(s)
        s2=[]
        for k in range(len(s1)):
            if s1[k]=="i":
                s2.reverse()
            else:
                s2.append(s1[k])
        return "".join(s2)
        