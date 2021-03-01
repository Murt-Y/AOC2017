file = open("input4.txt","r")
input = file.readlines()
valid=0
                 
def val(i):                 #her satir icin bu fonksiyon cagiriliyor
    plist = []                 
    x = i.split()
    s = False
    for t in x:             #satirdaki her kelime icin
        if s==True:
            break
        for k in plist:     #plist daha once okunanlarin listesi
            if t==k:
                s=True     #ayni kelimeden varsa ayni var diyor
                break
            l =len(t)
            if(l==len(k)):
                tlist = []  
                klist = []    
                for i in range(0,l):
                    tlist.append(t[i])
                    klist.append(k[i])
                    tlist.sort()
                    klist.sort()
                if tlist==klist:
                    s=True
                    break

        if s == False:      #aynisi yoksa pliste ekliyor
            plist.append(t)
    if s==False:
        global valid
        valid +=1

for j in input:
    val(j)

print (valid)