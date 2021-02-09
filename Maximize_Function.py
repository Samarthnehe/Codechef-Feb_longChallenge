try:
    for i in range(int(input())):
        num=int(input())
        max_val=0
        l=list(map(int,input().split()))
        l.sort()
        a=l[0]
        b=l[-1]
        for i in range(len(l)-2,0,-1):
            num=abs(a-b)+abs(a-l[i])+abs(l[i]-b)
            if num>max_val:
                max_val=num
                
        print(max_val)
                    
    
except:pass