
#break
for i in range(2,10):
    for x in range(2,i):
        if(i%x==0):
            print(i," equals",x,"*",i//x)
            break
           
    else:
        print(i," is prime number")
print("\n\n")

#continue
for num in range(2,10):
    if(num%2==0):
        print(num," is even number")
        continue # skip to next iteration if num is even
        
    print(num," is odd number")