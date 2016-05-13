def isPalindomric(x):
    if x<0:
        return False
    if x==0:
        return True
    if x%10==0:
        return False
    temp=x
    r=0
    while (temp>0):    
        r=r*10+temp%10
        temp=temp/10
    if (r==x):
        return True
    else:
        return False
if __name__=="__main__":
    x=124321
    ans=isPalindomric(x)
    print ans
    
