class BorderIntrusion():
    def __init__(self,x,L,r):
        self.x=x
        self.d=[0]*len(x)
        self.L=L
        self.r=r
        self.xx=[]
        self.minsum=0
        for i in range(len(x)):
            self.xx.append(x[i])
        n=len(self.x)
        self.o=[]
        self.g=[]
        if (x[0]>0):
            self.g.append([-1,0,0,x[i],x[i]])
        for i in range (n-1):
            if (x[i]<=-2*self.r) or (x[i]>=L+2*self.r):
                self.o.append(2*self.r)
                continue            
            if x[i]+2*self.r<x[i+1]:
                self.g.append([i,i+1,x[i]+2*self.r,x[i+1],x[i+1]-x[i]-2*self.r])
#            else:
#                t=i+1
#                while (t<n)and(x[i]+2*self.r>x[t]):
#                    self.o.append([i,t,x[t],x[i]+2*self.r,x[i]+2*self.r-x[t]])
#                    t=t+1
            elif x[i]+2*self.r>x[i+1]:
                self.o.append([i, i+1, x[i+1], x[i]+2*self.r, x[i]+2*self.r-x[i+1]])
        if (x[n-1]+2*self.r<L):
            self.g.append([n-1,n,x[n-1]+2*self.r,L,L-x[n-1]-2*self.r])
    def minSum(self):
        n=len(self.x)
        m=len(self.g)
        for i in range(m):
            while (self.g[i][4]>0):
                
                ll,c1,o1,s1,e1=self.leftOverlap(i)
                rr,c2,o2,s2,e2=self.rightOverlap(i)
                if(ll<=rr):
                    #print("l",s1,e1)
                    self.g[i][4]=self.g[i][4]-c1
                    self.o[o1][4]=self.o[o1][4]-c1
                    if self.o[o1][4]==0:
                        del self.o[o1]
                    for j in range(s1,e1+1):
                        self.d[j]=self.d[j]+c1
                        self.xx[j]=self.xx[j]+c1
                else:
                    #print("r",s2,e2)
                    self.g[i][4]=self.g[i][4]-c2
                    self.o[o2][4]=self.o[o2][4]-c2
                    if self.o[o2][4]==0:
                        del self.o[o2]
                    for j in range(s2,e2+1):
                        self.d[j]=self.d[j]-c2
                        self.xx[j]=self.xx[j]-c2
        for i in range(n):
            self.minsum=self.minsum+abs(self.d[i])
        return self.xx,self.minsum
    def leftOverlap(self,t):
        if len(self.o)==0:
            return 2**38,-1,-1,-1,-1
        if self.o[0][3]>self.g[t][2]:
            return 2**38,-1,-1,-1,-1
        i=0        
        while (i<len(self.o))and(self.o[i][3]<=self.g[t][2]):
            i=i+1
        i=i-1
        c=min(self.o[i][4],self.g[t][4])
        j=self.o[i][1]
        cost=c*(j-self.o[i][1])
        return cost,c,i,self.o[i][1],self.g[t][0]   
    def rightOverlap(self,t):
        if len(self.o)==0:
            return 2**38,-1,-1,-1,-1
        if self.o[len(self.o)-1][2]<self.g[t][3]:
            return 2**38,-1,-1,-1,-1
        i=len(self.o)-1
        while (i>=0)and(self.o[i][2]>=self.g[t][3]):
            i=i-1
        i=i+1
        c=min(self.o[i][4],self.g[t][4])
        j=self.o[i][0]
        cost=c*(self.o[i][0]-j)
        return cost,c,i,self.g[t][1],self.o[i][0]
if __name__=="__main__":
    L=20
    c=[1, 1,5,5,9,9, 9,15,17,17]
    x=[]
    cc=[]
    r=1
    #c=(-2,3,4,7,8
    for i in range(len(c)):
        x.append(c[i]-r)    
    weak=BorderIntrusion(x,L,r)
    xx,minsum=weak.minSum()
    for i in range(len(c)):
        cc.append(xx[i]+r)
    print cc,minsum
    
