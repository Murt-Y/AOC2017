file = open("input2.txt","r")
input = file.readlines()

sum=0
divsum=0                           

def min_max(i):
    max=0
    min=1000000
    x = i.split()
    for t in x:
        if(int(t)>max):
            max=int(t)
        if(int(t)<min):
            min=int(t)
    global sum
    sum=sum+max-min

def div(i):
    global divsum
    x = i.split()
    found = False
    for t in x:
        if (found==False):
            for z in x:
                if(t!=z and int(t)%int(z)==0):
                    divsum=divsum+(int(t)/int(z))
                    found = True
                    break



for j in input:
    min_max(j)
    div(j)
print(sum)
print(divsum)
