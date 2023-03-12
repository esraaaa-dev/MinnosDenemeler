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

#return eden fonksiyonlar
def ucgenAlaniHesapla(taban,yukseklik):
    return taban*yukseklik/2
alan=ucgenAlaniHesapla(9, 12)
print("alan= ",alan)

#lambda fonksiyonu
# fonksiyonun_adi =lambda x1,x2 : x1*x2/2
ucgenAlaniHesapla2=lambda taban,yukseklik : taban*yukseklik/2
print("lambda fonksiyonu ile alan :",ucgenAlaniHesapla2(9, 12))

#fibonacci
def fib(x):
    a=0
    b=1
    while a<x:
        print(a, end=' ')
        a,b=b,a+b
    print()
    
fib(20) 