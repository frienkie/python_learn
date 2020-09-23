month=int(input())
if month==1 or month==2:  #没有规律，所以单拿出来
    print("1 1")
else:
    a=1   #第一个月
    b=1   #第二个月
    c=0   #一会求和用的变量，需要提前使其为0
    for i in range(3,month + 1):  
        c=a+b   
        a=b    
        b=c    
    print("{} {:.3f}".format(c,a/c) )
