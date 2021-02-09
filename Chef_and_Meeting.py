try:
    def convert(num,dur):
        if dur=="AM" and num[:2]=="12":
            num="00"+num[2:]
        elif dur=="PM" and int(num[:2])<12:
            num=str(int(num[:2])+12)+num[2:]
        return num,dur
        
    for i in range(int(input())):
        time=list(map(str,input().split(" ")))
        num0,dur0=convert(time[0],time[1])
        minute=num0[3:5]
        minute=float(minute)/60
        time=int(num0[:2])+float(minute)
        member=int(input())
        for j in range(member):
            t=input()
            fro=t[:8]
            to=t[9:]
            num1,dur1=convert(fro[:5],fro[-2:])
            num2,dur2=convert(to[:5],to[-2:])
            minute1=num1[3:5]
            minute1=float(minute1)/60
            minute2=num2[3:5]
            minute2=float(minute2)/60
            time1=int(num1[:2])+float(minute1)
            time2=int(num2[:2])+float(minute2)
            if(time1<=time and time<=time2):
                print(1,end="")
            
            else:
                print(0,end="")
        print()
            
   
    
except:pass
