flag=-1
head,foot=map(int,input().split())
for i in range(head):
    for j in range(head):
        if(i+j==head):
            if((4*i+2*j)==foot):
                flag=1
                print("{} {}".format(j,i))

if(flag<0):
    print("Data Error!")
