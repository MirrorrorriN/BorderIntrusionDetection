def test(s):
   
    n = len(s)
    s='0'+s
    opt= [0]*(n+1)
    changed =1
    for i in xrange(1,n+1):
        if opt[i] == 0 and s[i] == ')':
            ind = i-opt[i-1]-1
            if ind > 0 and s[ind] == '(':
                opt[i] = opt[i-1] +2
        if opt[i] != 0:
            opt[i] += opt[i-opt[i]]
    return max(opt)

if __name__=="__main__":
    s='(()()((()((())))()((())()(()))('
    match=test(s)
    print match
    
