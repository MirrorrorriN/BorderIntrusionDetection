def romanToInt(s):
    romanmap=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    x=0
    index=0
    for i in range(13):
        t=len(romanmap[i])
        while (s[index:index+t]==romanmap[i]):
            x=x+num[i]
            index=index+t
    return x
if __name__=="__main__":
    s="MCMXCI"
    ans=romanToInt(s)
    print ans
    
