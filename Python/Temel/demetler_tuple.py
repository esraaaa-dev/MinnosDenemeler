#tuple listelere benzer fakat listeden farklı olarak tuple elemanları degistirilemez

tup1=(34,2,5,"eee",(3,4))
print(tup1)
#tup1[0]=2 #elemanların yerine farklı bir eleman atanmaz
print(tup1) #output:TypeError: 'tuple' object does not support item assignment
print(len(tup1)) #output:5 ,tuple içindeki tuple tek bir elemandır
#tuple içine farklı turler tanımlanabilir list,tuple,int,str ..

#tek elemanlı bir tuple varsa elimizde virgül kullanmamız gerekir 
#aksi halde sistem degisken tipini tuple olarsk algılayamaz

#örn
tekElemanliTuple=(4)
print(type(tekElemanliTuple)) #output:<class 'int'>
tekElemanliTuple2=(5,)
print(type(tekElemanliTuple2)) #output:<class 'tuple'>

print(tup1[1:3]) #indexli bir yapısı vardır bu nedenle substring kullanılabilir.