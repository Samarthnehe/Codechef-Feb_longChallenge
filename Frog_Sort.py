try:
    for i in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        val=list(map(int,input().split()))
        index=[]
        answer=0
        for j in range(1,len(l)+1):
            index.append(l.index(j)+1)
        for k in range(1,len(index)):
            max_num=max(index[:k])
            while index[k]<=max_num:
                index[k]+=val[l.index(k+1)]
                answer+=1
        print(answer)
            
            
except:pass
