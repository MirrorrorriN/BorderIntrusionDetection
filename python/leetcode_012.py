def intToRoman(x):
    table=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    times=[0]*13
    s=""
    for i in range(13):
        times[i]=x/num[i]
        x=x%num[i]
    for i in range(13):
        for j in range(times[i]):
            s=s+table[i]
    return s

if __name__=="__main__":
    x=671
    ans=intToRoman(x)
    print ans
