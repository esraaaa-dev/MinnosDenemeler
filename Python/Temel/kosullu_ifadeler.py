#if ifadesi

# x=int(input("please enter an integer: "))
# if x<0:
#     x=0
#     print("negative changed to zero")
# elif x==0:
#     print("zero")
# elif x==1:
#     print("single")
# else:
#     print("more")
    
#for döngüsü

words= ['cat','car','computer']
for i in words:
    print(i,len(i))
    
#collection olusturmak

users={'hans:' 'active','esra:' 'inactive','joe:' 'active'}
print(users)

#range() fonksiyonu

for i in range(5):
    print(i)
    
print(list(range(-10, -100, -30))) # -10  ile -100 arasında 30 cıkararak ilerle 
    
    