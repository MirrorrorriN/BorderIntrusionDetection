def myAtoi(s):
    flag=0
    num=0
    sign=0
    for i in range(len(s)):
        if (s[i]==' '):
            if flag==0:
                continue
            else:
                break
        else:
            if(flag==0):
                flag=1
                if(s[i]=='+'):
                    sign=0
                elif(s[i]=='-'):
                    sign=1
                elif('0'<=s[i]<='9'):
                    num=ord(s[i])-48
                else:
                    return 0
            else:
                if('0'<=s[i]<='9'):
                    num=num*10+(ord(s[i])-48)
                else:
                    break
    if(flag==0):
        return 0
    if(sign==1):
        num=-num
    if (num>2147483647):
        num=2147483647
    elif (num<-2147483648):
        num=-2147483648
    return num
if __name__=="__main__":
    s=" +02147483649   "
    num=myAtoi(s)
    print num
