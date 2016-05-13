import sys
def test(num):
    flag=0
    reverse=0
    maxint=2147483647
    if num<0:
        flag=1
        num=-num
    while (num>0):
        reverse=reverse*10+num%10
        num=num/10
    if (flag==0):
        if reverse>maxint: #pay attention to the ovreflow case
            reverse=0
    else:
        reverse=-reverse
        if reverse<-maxint-1:
            reverse=0
    return reverse

if __name__=="__main__":
    num=1534236469
    ans=test(num)
    print ans
