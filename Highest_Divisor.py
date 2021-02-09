try:
    num=int(input())
    for i in range(10,0,-1):
        if(num%i==0):
            print(i)
            break
except:pass