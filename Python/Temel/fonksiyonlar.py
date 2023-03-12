#parametre almayan fonksiyonlar
def selamla():
    print("Merhabalar Aq!!")
selamla()

#parametre alan fonksiyonlar

def selamla(isim="yoldaş"):
    print("Merhaba ",isim)
    
selamla("esra")
selamla() #parametre verilmezse default parametreyi kullanır
#her iki fonksiyonun da isimleri aynı fakat birisi parametre alıyor diğeri almıyor 
#bkz. metotoverloading benzeri


def fib(x):
    a=0
    b=1
    while a<x:
        print(a, end=' ')
        a,b=b,a+b
    print()
    
fib(20) 