t=int(input())
for q in range(t):
    list=[]
    z=input()
    z=z.split(" ")
    a=int(z[0][::-1])
    b=int(z[1][::-1])
    k=a+b 
    while k%10==0:
        k=k/10
    w=str(int(k))
    w=w[::-1]
    print(w)
    