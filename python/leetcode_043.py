def multiply(s1,s2):    
    m=len(s1)
    n=len(s2)
    #table=[[0]*(m+n)]*n
    table=[[0]*(m+n)for row in range(n)]
    s=""
    for i in range(n):
        for j in range(m):
            table[i][i+j]=int(s1[m-1-j])*int(s2[n-1-i])
    carry=0
    for i in range(len(s1+s2)):
        temp=0
        for j in range(n):
            temp=temp+table[j][i]
        temp=temp+carry
        carry=temp/10
        temp=temp%10
        s=s+str(temp)
    s=s[::-1]
    while(s[0]=='0')and(len(s)>1):
        s=s[1:]
    return s
if __name__=="__main__":
    s1="323432"
    s2="298434"
    ans=multiply(s1,s2)
    print ans
