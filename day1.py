file = open("input1.txt","r")
input = file.read()
                                

def p_1():
    result = 0
    i=0
    while i<len(input)-1:
        if input[i]==input[i+1]:
            result=result+int(input[i])
        i=i+1   

    
    if input[len(input)-1]==input[0]:
        result=result+int(input[0])
    print ("The result for Part 1 is  :  " ,result)

def p_2():
    result = 0
    i=0
    t=len(input)/2

    while i<len(input)-1:
        if input[i]==input[int((i+t)%len(input))]:
            result=result+int(input[i])
        i=i+1   

    print ("The result is for Part 2 is    :  " ,result)


p_1()
p_2()