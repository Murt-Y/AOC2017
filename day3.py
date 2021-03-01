def retn(x, y):
    e=max(abs(x), abs(y))
    t=(e-1)*2+1
    t=t*t
    if(y==-e):
        return t+(6*e)+(x+e)
    if(x==e):
        return t+y+e
    if(y==e):
        return t+(2*e)+(e-x)
    if(x==-e):
        return t+(4*e)+(e-y)

def retc(t):
    edge=1
    total=edge*edge
    i=0
    while total<t:
        edge=edge+2
        total=edge*edge
        i+=1
    x=i
    y=(i-1)*-1
    total=(edge-2)*(edge-2)+1
    while(x!=y):
        if(total==t):
            return(x,y)
        total+=1
        y+=1
    while(x!=-y):
        if(total==t):
            return(x,y)
        total+=1
        x-=1
    while(x!=y):
        if(total==t):
            return(x,y)
        total+=1
        y-=1
    while(x!=-y):
        if(total==t):
            return(x,y)
        total+=1
        x+=1
    return(x,y)

def checkn(m):
    sum=0
    l=len(num)
    a=[0,0]
    a=retc(m)
    xm=a[0]
    ym=a[1]

    x=retn(xm-1, ym)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm+1, ym)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm, ym-1)
    if(x<l):
        sum=sum+num[x]    
    x=retn(xm, ym+1)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm-1, ym-1)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm-1, ym+1)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm+1, ym-1)
    if(x<l):
        sum=sum+num[x]
    x=retn(xm+1, ym+1)
    if(x<l):
        sum=sum+num[x]
    return sum




num =[0,1]
i=2
xc=2
yc=0
goon=True
while(goon):

    p=checkn(i)
    num.append(p)
    if(p>265149):
        goon=False
        print(p)
    i+=1