# Iterative vs Recurssion 
def iterative_fun(i):           #call function    
    fact = 1                       # assigned variable
    for i in range (2,i+1):         # i = 0 => range starts from 2 to all the way before  n+1 or (5)
        fact *= i                   # 1 * 1 (fact = 1 and i = 2) , type print here to see each iterative happening
        print(i)                       #  fact * i => 1 * 2 => 2*3 => 6*4 => then 24*5 = 120
    return fact

print (iterative_fun(5))            #VS Recurssion


def recurrsion_fun(i):    # call funtion starts opposite side    ----(1)
    if i ==1:               # function will stop once we reached to 1
        return i                
    else:                           # start from here
        fact = recurrsion_fun(i-1)      # turns fun(5) to fun(4) then pushes to go back to --- (1), 
        print(i)
        return fact  * i                       # keep going until we hit recurrsion_fun(1), the return n or (1), then second part starts. Calculations
                                                     # then in second part return fact * i => 1 * 2, return 2, 2 (fact) * 3 (i) = 6, 6 * 4 = 24, 24 * 5 = 120 Walaah. 
                                                            #if still confuse about last part check my youtube channel or see what happen in itertive side but try to do it from bottom to top. Same thing. 

print(recurrsion_fun(5))                            