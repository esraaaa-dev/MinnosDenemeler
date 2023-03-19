sayi=int(input("bir sayı giriniz: "))
def faktHesapla(sayi):
    sayac,fakt=1,1
    while sayac<=sayi:
        fakt=fakt*sayac
        sayac=sayac+1
    print("girilen sayının faktoriyeli: ",fakt)
faktHesapla(sayi)


#return eden
def faktoriyel(sayi):
    fakt = 1
    for i in range(1, sayi+1):
        fakt *= i
    return fakt
print(faktoriyel(6))

   
  
        

    
    
    