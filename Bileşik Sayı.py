print("""****************************************************************************
BİLEŞİK SAYI BULMA SİHİRBAZI

"Kullanıcıdan alınan input'a kadar olan tüm bileşik sayılar ekrana yazdırılır.
"Bileşik sayı, en az iki asal sayının çarpımı olarak yazılabilen pozitif tam sayıdır.
Tanım olarak, 1'den büyük her tam sayı ya asal ya da bileşik sayıdır.
0 ve 1 ne bileşik, ne de asal sayılardır.
Örnek olarak, 14 bir bileşik sayıdır çünkü:
14 = 1 x 14 = 2 x 7 ."   
****************************************************************************""")
import math   #matematik kütüphanesi çağırılır


def asalsayı(sayi): #asalsayı fonksiyonu tanımlanır
    sqrt = math.ceil(math.sqrt(sayi))  #sayının karekökünü alıyoruz, verilen ondalıklı sayıyı bir üst sayıya çevirmek için ".ceil" fonksiyonu kullanılır
    for i in range(2, sqrt+1): #for döngüsü kullanılır, range fonksiyonunu 2 ile sqrt değişkeninin bir fazlası arasında alırız
        if sayi % i == 0: #if bloğu açarız ve sayı ile i değişkeninin modunun sıfıra (0) eşit olduğu değerler olarak belirlenir
            return False #öyleyse False döndürürüz
    return True #değilse True döner



def tumbolenler(sayi): #tumbolenler isimli bir fonksiyon oluşturulur
    bolenler = []  #bolenler isimli bir liste açılır, şimdilik boş bırakılır
    while(sayi > 1):  #while döngüsü kurulur ve sayi değişkeninin 1'den büyük olduğu değerler koşul olarak yazılır
        for i in range(2, sayi+1):  #for döngüsü kurulur ve range fonksiyonu kullanılır, 2 ile sayi değişkeninin bir fazlası olarak kullanılır. 2 almamızın nedeni en küçük asal sayının 2 olmasıdır
            if(sayi % i == 0):  #if bloğu açılır ve sayi değişkeni ile i değişkeninin modunun sıfıra (0) eşit olması koşul olarak belirlenir
                sayi = int(sayi/i)  #sayi değişkeni bu girintide atanır
                bolenler.append(i) #bolenler listesine i ".append" ile eklenir
                break
    return bolenler #return edilir


sözlük = {} #sözlük oluşturulur


def isbilesik(liste: dict):
    sonuc = [] #sonuc isimli liste oluşturdum
    for sayi in liste.keys(): #".keys" fonksiyonu kullanılır
        sayac = 0 #sayaç oluşturulur ve 0 atanır
        if(sayi % 2 == 0): #if bloğu açılır ve koşulu sayi değişkeninin 2 ile modunun 0 a eşit olduğu değerler olarak belirlenir
            sonuc.append(sayi) #sonuça append ile sayi değişkeni eklenir
            continue #devam
        for bolenler in liste[sayi]: #for döngüsü oluşturulur
            if(asalsayı(bolenler)):
                sayac = sayac+1 #sayaçı bir artır
        if(sayac >= 2): #eğer sayaç ikiden büyük eşitse:
            sonuc.append(sayi) #sonuç listesine append ile sayi değişkeni eklenir
    return sonuc


def baslat(): #fonksiyonu oluşturuyoruz
    sayi = int(input("Lütfen bir sayı giriniz:"))  # sayi değişkeni alınır
    if(sayi < 4): #eğer sayı 4den küçükse
        print("En küçük bileşik sayı 4 olmalı, 4'ten küçük sayı girmeyiniz!") #4den küçük bileşik sayı olmayacağı için (2*2=4 min) 4den küçük olmaması yönünde uyarı koyuyoruz
        return
    if(sayi == 4): #sayı eğer 4e eşitse
        print("En küçük bileşik sayı 4'tür, 4'ten küçük sayı girmeyiniz!") #uyarı
        return
    for i in range(4, sayi+1): #for döngüsü kullanılır ve range fonksiyonu 4den alınır sayi değişkeni + 1 arasında yapılır, 4den alıyoruz çünkü min4
        sözlük[i] = tumbolenler(i) #sözlüğün birinci indexine tumbolenlerin i değişkeninin değeri atanır



baslat() #başlat
print(isbilesik(sözlük)) #yazdır
print("-_-") #imzam