try:
    from collections import defaultdict
    for m in range(int(input())):
        num=int(input())
        
        l=list(map(str,input().split()))
        d=defaultdict(set)
        for i in l:
            d[i[1:]].add(i[0])
        answer=0
        first=list(d.keys())
        for i in range(len(first)-1):
            for j in range(i+1,len(first)):
                answer+=(len(d[first[i]].difference(d[first[j]]))*len(d[first[j]].difference(d[first[i]])))
        print(2*answer)
        
   
except:pass