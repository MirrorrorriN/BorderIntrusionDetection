def longestCommonPrefix(str):
    n=len(str)
    s=""
    if (len(str)==0):
        return s
    if (len(str[0])==0):
        return s
    for i in range(len(str[0])):
        temp=str[0][i]
        for j in range(n):
            if(len(str[j])<=i):
                return s
            if(temp==str[j][i]):
                temp=str[j][i]
            else:
                return s
        s=s+temp
    return s
if __name__=="__main__":
    str=["abcd","abcde","abcde"]
    s=longestCommonPrefix(str)
    print s       
