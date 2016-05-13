def maxArea(height):
    start=0
    end=len(height)-1
    opt=0
    while(start<end):
        cur=min(height[start],height[end])*(end-start)
        if(cur>opt):
            opt=cur
        if(height[start]>height[end]):
            end=end-1
        else:
            start=start+1
    return opt

if __name__=="__main__":
    h=[4,7,3,5]
    ans=maxArea(h)
    print ans
    
