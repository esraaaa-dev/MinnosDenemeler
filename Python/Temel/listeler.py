#liste olusturma
lists=[1,3,5,7,9]
print(lists)
print(lists[3])
lists.append(45)  #append() fonksiyonu ile listenin sonuna eleman eklenir
print(lists)

letters=['a','b','c','d','e','f','g']
print("harf listesi: ",letters)
#replace some values
letters[2:5]=['C','D','E']
print("degistirildikten sonra harf listesi: ",letters)

#remove [2:5]
letters[2:5]=[]
print("2-5 arası kaldırıldıkta sonra harf listesi: ",letters)

#clear all 

letters[:]=[]
print("silindikten sonra harf listesi: ",letters)

#listeler stringlerden farklı olarak mutable yapılardır 
lists[2] =31
print("2. indise 31  atanınca lists listesi: ",lists)

#*** listelerin içinde farklı turden elemanlar bulunabilir. 

isim=['esra','zehra',5]
print(isim)

isim.append(True)
print(isim) #string integer ve boolean türünde degerler içerdi

#listeler diger listelerle birleştirilebiliz
birlesmisListe=isim+lists
print("isim ve lists listesi: ",birlesmisListe)

