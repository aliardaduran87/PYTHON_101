# ====================================================================
# == BAB 9: KOLEKSİYONLAR-2 (COLLECTIONS-2)(SÖZLÜKLER VE KÜMELER) : ==
# ====================================================================

#---------------------------
# SÖZLÜKLER (DICTIONARIES) :
#---------------------------
"""
-> Sözlük, verileri birbiriyle eşleşmiş çiftler halinde, yani Anahtar (Key) ve Değer (Value) ikilileri şeklinde saklayan bir veri yapısıdır.
-> Aynen gerçek hayattaki bir sözlük gibi; bir kelimeyi (Anahtar) ararsınız ve karşılığında o kelimenin tanımını/açıklamasını (Değer) bulursunuz.
-> Sözlükler süslü parantez {} kullanılarak tanımlanır. Her bir öğe anahtar: değer şeklinde yazılır.

Temel Özellikler:
-----------------
1-) Anahtar-Değer Çiftleri: Her eleman bir anahtar ve o anahtara karşılık gelen bir değerden oluşur.
-> Anahtar (Key): Benzersiz olmak zorundadır. Bir sözlükte aynı anahtardan iki tane bulunamaz. Bu, verilere hızlı erişimi sağlayan tanımlayıcıdır.
-> Değer (Value): Tekrarlanabilir. Birkaç anahtar aynı değeri gösterebilir.

2-) Sırasızlık (Genellikle): Çoğu programlama dilinde (Python'ın modern versiyonları hariç) sözlükler, elemanları ekleme sırasına göre saklamaz.
-> Erişim, konumlarına göre değil, anahtarlar aracılığıyla yapılır.

NOT: 
-> Python 3.6 öncesi: Tamamen sırasızdı.
-> Python 3.7 ve sonrası: Sözlükler artık ekleme sırasını (insertion order) koruyor. Yani elemanları hangi sırayla yazarsanız, ekrana bastığınızda veya döngüye soktuğunuzda o sırayla gelirler.
-> Sözlüklere erişim hâlâ konumla (0. indeks, 1. indeks gibi) değil, anahtar (key) ile yapılır. Bu yüzden "sırasızlık" kavramı, erişim mantığı açısından hâlâ geçerli bir öğretidir.

3-) Hızlı Erişim: Sözlüklerin en büyük avantajı, belirli bir anahtara karşılık gelen değere çok hızlı, genellikle sabit zamanda (Ortalama O(1) karmaşıklıkla) erişim imkanı sunmasıdır.
-> Bir sözlük genel olarak şöyle tanımlanır:

sozluk = {
    "anahtar1": "değer1",
    "anahtar2": "değer2",
    "anahtar3": "değer3"
}

sozluk={"anahtar1":"deger1","anahtar2":"deger2","anahtar3":"deger3"} #Yukarıdaki kod ile aynı sadece burada yan yana yazılmış.
"""
#-------------------------------
# SÖZLÜK OLUŞTURMANIN İKİ YOLU :
#-------------------------------

#-------------------------------
# 1.LİTERAL YÖNTEM (EN YAYGIN) :
#-------------------------------
sozluk = {} # Boş bir sözlük tanımlaması yapıldı.
"""
-> Daha kısa ve hızlıdır.
-> Genellikle boş bir sözlük başlatırken tercih edilir.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
nfs_blacklist = {
    "Razor": "BMW M3 GTR",
    "Bull": "Dodge Viper",
    "Ronnie": "Aston Martin DB9",
    "Ming": "Lamborghini Murcielago"
}
# Bu sözlük içerisinde kelimenin ingilizcesi anahtar(key),Türkçesi değerdir(value).


#----------------------
# 2.dict() FONKSİYONU :
#----------------------
sozluk = dict()     # Boş bir sözlük tanımlaması yapıldı.
"""
-> Daha açık (explicit) bir yazımdır.
-> Farklı veri türlerini (örneğin liste içindeki demetleri) sözlüğe dönüştürmek için de kullanılır.
-> sozluk = dict(anahtar1="deger1", anahtar2="deger2") (Dikkat: Burada anahtarların başına tırnak koymanıza gerek kalmaz, Python onları otomatik string'e çevirir.)
"""
sozluk = dict(Izmir="35", Istanbul="34", Ankara="06", Burdur="15")   
# Fonksiyon parantezleri () içinde anahtar ve değerleri bağlamak için : (iki nokta) kullanamazsınız. İki nokta sadece süslü parantez {} içinde geçerlidir.
# Eğer dict() içinde eşittir = kullanacaksanız,

#-----------------------------                                               
# SÖZLÜK ELEMANLARINA ERİŞİM :
#-----------------------------
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
kelime = sozluk["book"]
print(kelime)    #Çıktı: kitap 

araba = nfs_blacklist["Razor"]
print(araba)     #Çıktı: BMW M3 GTR

# Burada köşeli parantez kullanımı, sözlüklerde bir anahtara(key) karşılık gelen değeri (value) almak için standart ve en yaygın yöntemdir.
# Aslında burada listelerdeki elemanı çağırmak için kullandığımız sayıyı değil anahtar kelimeyi giriyoruz.
"""
sozluk={"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
kelime=sozluk["orange"]
print(kelime)

#KeyError: 'orange' hatası alıyoruz.
"""

#------------------
# get(key) KOMUTU :
#------------------
"""
-> get()komutu parantez içerisine yazılan anahtara ait değeri bulmamızı sağlar. Ancak anahtar yoksa KeyError üretmez.
-> Python'da .get() metodu, sözlüklerden veri çekmenin en güvenli ve profesyonel yoludur.
-> Köşeli parantez [] kullanımına kıyasla en büyük farkı, programınızın hata verip durmasını engellemesidir.
-> .get() metodu iki parametre alabilir: sozluk.get(anahtar, varsayılan_değer)
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
kelime = sozluk.get("orange")
print(kelime)
# get komutu ile belirtilen anahtarı bulunmazsa "None" sonucu üretir.
# Anahtarın varlığından şüpheli olduğunuz her durumda .get() metodunu kullanmak en iyi uygulama (best practice) olarak kabul edilir.

sozluk = {
        "101":"Algoritma ve Programlamaya Giriş-1 (Python_101)",
        "201":"Algoritma ve Programlamaya Giriş-2 (Python_201)",
        "301":"Python ile Veri Analizi ve Bilimsel Hesaplama",
        "401":"Python ile Makine Öğrenmesine Giriş"
}
sec = sozluk.get("501")
print(sec)

sozluk = dict(ders_101="Algoritma ve Programlamaya Giriş-1", ders_201="Algoritma Ve Programlamaya Giriş-2")


#------------------------
# SÖZLÜĞE ELEMAN EKLEME :
#------------------------
"""
-> Var olan sözlüğe yeni eleman ekleme işlemi oldukça basittir.
-> Yeni bir anahtar-değer çifti eklemek için, sözlük adını yazar, ardından köşeli parantez içine yeni anahtarı koyar ve = işareti ile yeni değerini atarsınız.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}

# Doğru Söz Dizimi: sozluk'e yeni bir Anahtar-Değer çifti ekle
sozluk["rose"] = "gül" 
sozluk["pencilcase"]="kalemkutusu"

print(sozluk)
#Çıktı: {'apple': 'elma', 'computer': 'bilgisayar', 'book': 'kitap', 'pen': 'kalem', 'rose': 'gül', 'pencilcase': 'kalemkutusu'}


#--------------------------------
# SÖZLÜK ELEMANLARINI DÜZENLEME :
#--------------------------------
sozluk= {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
sozluk["pen"] = "dolma kalem"  #Çıktı: {'apple': 'elma', 'computer': 'bilgisayar', 'book': 'kitap', 'pen': 'dolma kalem'} 
print(sozluk) 


#-------------------------
# SÖZLÜKTEN ELEMAN SİLME :
#-------------------------
"""
-> Sözlükten eleman silmek için del komutu kullanılır.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
del sozluk["pen"] # sozluk içindeki pen anahtarı ve buna ait değeri sil.
print(sozluk)
#Çıktı: {'apple': 'elma', 'computer': 'bilgisayar', 'book': 'kitap'}


#--------------------
# SÖZLÜĞÜ TEMİZLEME :
#--------------------
"""
-> Sözlüğün tüm elemanlarını silmek için clear() komutu kullanılır.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
sozluk.clear()
print(sozluk)
#Çıktı: {} 


#--------------------------------
# SÖZLÜK ELEMANLARINI LİSTELEME : 
#--------------------------------
"""
-> Python'da sözlük elemanlarını listelemek (görüntülemek) için 3 temel yöntem vardır.
-> Sözlük elemanları listelenirken tanımlama alanındaki sıralamaya göre değil, rastgele listelenir.
-> Aynı listeleme komutu tekrar çalıştırılırsa sıralamanın farklı olması mümkündür.
"""
#-----------------------------------------
# 1. Sadece Anahtarları (Keys) Listeleme :
#-----------------------------------------
sozluk = {"apple": "elma", "book": "kitap", "pen": "kalem"}
print(sozluk.keys())  # Çıktı : dict_keys(['apple', 'book', 'pen'])

sozluk = {
        "101":"Algoritma ve Programlamaya Giriş-1 (Python_101)",
        "201":"Algoritma ve Programlamaya Giriş-2 (Python_201)",
        "301":"Python ile Veri Analizi ve Bilimsel Hesaplama",
        "401":"Python ile Makine Öğrenmesine Giriş"
}
print(sozluk.keys())
#Çıktı: dict_keys(['101', '201', '301', '401'])


sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for k in sozluk.keys():
    print(k)   # Bu şekilde de yazılabilir.

#Çıktı:
#apple
#computer
#book
#pen

nfs_blacklist = {
    "Razor": "BMW M3 GTR",
    "Bull": "Dodge Viper",
    "Ronnie": "Aston Martin DB9",
    "Ming": "Lamborghini Murcielago"
}
print(nfs_blacklist.keys())   #Çıktı : dict_keys(['Razor', 'Bull', 'Ronnie', 'Ming'])


#-----------------------------------------
# 2. Sadece Değerleri (Values) Listeleme :
#-----------------------------------------
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print(sozluk.values())  #Çıktı: dict_values(['elma', 'bilgisayar', 'kitap', 'kalem'])


sozluk = {
        "101":"Algoritma ve Programlamaya Giriş-1 (Python_101)",
        "201":"Algoritma ve Programlamaya Giriş-2 (Python_201)",
        "301":"Python ile Veri Analizi ve Bilimsel Hesaplama",
        "401":"Python ile Makine Öğrenmesine Giriş"
}
print(sozluk.values())
#Çıktı: dict_values(['Algoritma ve Programlamaya Giriş-1 (Python_101)', 'Algoritma ve Programlamaya Giriş-2 (Python_201)', 'Python ile Veri Analizi ve Bilimsel Hesaplama', 'Python ile Makine Öğrenmesine Giriş'])

sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for k in sozluk.values():
    print(k)    #Çıktı: Bu şekilde de yazılabilir.

#Çıktı:
#elma
#bilgisayar
#kitap
#kalem   

nfs_blacklist = {
    "Razor": "BMW M3 GTR",
    "Bull": "Dodge Viper",
    "Ronnie": "Aston Martin DB9",
    "Ming": "Lamborghini Murcielago"
}
print(nfs_blacklist.values())  #Çıktı: dict_values(['BMW M3 GTR', 'Dodge Viper', 'Aston Martin DB9', 'Lamborghini Murcielago'])


#-------------------------------------------------
# 3. Hem Anahtar Hem Değerleri (Items) Listeleme :
#-------------------------------------------------
"""
-> En profesyonel yöntem budur. Çiftler halinde (kelime: anlam) listeleme yapar. Özellikle for döngüsü ile birlikte çok sık kullanılır.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for k in sozluk:
    print("İngilizcesi:",k,"Türkçesi:",sozluk[k])

#Çıktı:
#İngilizcesi: apple Türkçesi: elma
#İngilizcesi: computer Türkçesi: bilgisayar
#ingilizcesi: book Türkçesi: kitap
#İngilizcesi: pen Türkçesi: kalem

nfs_blacklist = {
    "Razor": "BMW M3 GTR",
    "Bull": "Dodge Viper",
    "Ronnie": "Aston Martin DB9",
    "Ming": "Lamborghini Murcielago"
}
for k in nfs_blacklist:
    print("Rakip:",k,"Arabası:",nfs_blacklist[k])

#Çıktı:
#Rakip: Razor Arabası: BMW M3 GTR
#Rakip: Bull Arabası: Dodge Viper
#Rakip: Ronnie Arabası: Aston Martin DB9
#Rakip: Ming Arabası: Lamborghini Murcielago


#---------------------------------------------------------
# .items() METODU: ANAHTAR VE DEĞER ÇİFTLERİNİ LİSTELEME :
#---------------------------------------------------------
"""
-> items() komutu, bir sözlüğün içerisinde 'hem anahtar hem de değerlere aynı anda ulaşmamızı' sağlar.
-> items()komutu, for döngüsü ile birlikte şu şekilde kullanabiliriz.
"""

sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print(sozluk.items())
#Çıktı: dict_items([('apple', 'elma'), ('computer', 'bilgisayar'), ('book', 'kitap'), ('pen', 'kalem')])

nfs_blacklist = {
    "Razor": "BMW M3 GTR",
    "Bull": "Dodge Viper",
    "Ronnie": "Aston Martin DB9",
    "Ming": "Lamborghini Murcielago"
}
print(nfs_blacklist.items())
#Çıktı: dict_items([('Razor', 'BMW M3 GTR'), ('Bull', 'Dodge Viper'), ('Ronnie', 'Aston Martin DB9'), ('Ming', 'Lamborghini Murcielago')])


sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
for anahtar,deger in sozluk.items():
    print("Anahtar:",anahtar,"Değer:",deger)

#Çıktı:
#Anahtar: apple Değer: elma
#Anahtar: computer Değer: bilgisayar
#Anahtar: book Değer: kitap
#Anahtar: pen Değer: kalem


#-------------------------------
# SÖZLÜK ELEMAN SAYISINI BULMA :
#-------------------------------
"""
-> Sözlük elemanlarını bulmak için len() komutu kullanılır. Aslında eleman sayısından kasıt anahtar sayısıdır.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print(len(sozluk))
#Çıktı: 4 -> Her bir anahtar ikilisi tek bir eleman sayılır.


#------------------------------------------
# SÖZLÜKTE ANAHTAR VARLIĞINI KONTROL ETME :
#------------------------------------------
"""
-> Herhangi bir anahtarın sözlük içinde var olup olmadığını kontrol etmek için in ve not in komutları kullanılır.
-> Burada dikkat edilmesi gereken nokta sözlük içinde sadece bir anahtarın varlığı kontrol edilebiliyorken, değerin varlığı kontrol edilmez.
-> Lakin bunun bir çözümü var. .values() kullanınca sorun çözülüyor.
"""
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pen":"kalem"}
print("apple" in sozluk)           #True 
print("elma " in sozluk)           #False 
print("elma" in sozluk.values())   #True 

sozluk = {"Aydın":"Emre","İzmir":"Ali","Konya":"Ümit","Ordu":"Baran","Ahmet Barış":"Isparta"}
print ("Aydın" in sozluk)          #True
print ("İzmir" in sozluk)          #True
print("Burdur" in sozluk)          #False


#--------------------------------------
# SÖZLÜKLERİN EŞİTLİĞİNİ KONTROL ETME : 
#-------------------------------------- 
stok1 = {"kitap":5,"kalem":10}
stok2 = {"kalem":10,"kitap":5}
durum = stok1==stok2
print(durum)
# Her ne kadar anahtar-değer ikililerinin sırası farklı olsa bile her iki sözlük de aynı anahtar-değer çiftlerini barındırdığı için iki sözlük birbirine eşittir.


# Öncelikle stok1 == stok2 kısmı çalışır.

# == operatörü, matematikteki eşitlik kontrolü gibidir. 
# İki değerin eşit olup olmadığını kontrol eder 
# Ve sonuç olarak ya True (Doğru) ya da False (Yanlış) mantıksal bir değer (Boolean) döndürür.
# Anahtar-değer çiftlerinin liste içindeki sıralamalarının eşitlikte herhangi bir etkisi yoktur.


#--------------------
# SÖZLÜK GÜNCELLEME :
#--------------------
"""
-> Bir sözlük  içerisinde yer alan ve değerlerinin güncellenmesi için update() komutu kullanılır. 
-> "update()" metodu kalıcıdır; yani 'urun' sözlüğünü doğrudan değiştirir (In-place).
"""
urun = {"kalem":2,"defter":5,"makas":4}
yeni = {"kalem":3,"defter":7,"makas":6,"boya":10}
urun.update(yeni)
print(urun)
#Çıktı:{'kalem': 3, 'defter': 7, 'makas': 6, 'boya': 10}


#------------------
# SÖZLÜK KOPYALAMA:
#------------------
"""
-> Sözlükler, daha önce listeler konusunda bahsettiğimiz gibi, birer referans tipidir.
-> Yani sözlük türü değişkenlerinin içerisinde verilerin bellekte tutulduğu adres bilgisi yer alır.
-> Bundan dolayı iki sözlük değişkenini  birbirine eşitlemek aslında arka planda her iki değişkenin de aynı bellek bölgesini (nesneyi) referans göstermesini sağlar.
-> Yani her iki değişken de bellekte aynı bölgeye işaret eder.
-> Bunun doğal sonucu olarak tahmin ya da hava durumu değişkenlerinin herhangi biri üzerinde yapılacak değişiklik diğerini etkiler.
-> Burada yapılan işlemin bir sözlüğün içeriğini kopyalamadığını görüyoruz.
-> Sadece değişkenlerin değerleri eşitleniyor.
-> Bellekte yine tek bir sözlük veri kümesi vardır.
-> Bir sözlüğün içindeki elemanların kopyasını oluşturmak için ise copy() komutu kullanılır.
"""
havadurumu = {"ankara":"bulutlu","istanbul":"yağmurlu","antalya":"güneşli"}
tahmin = havadurumu
print(id(tahmin))
print(id(havadurumu))
#2403238991040
#2403238991040

havadurumu["izmir"]="güneşli"
print(havadurumu)

tahmin = havadurumu.copy()
print(tahmin)
#Çıktı:{'ankara': 'bulutlu', 'istanbul': 'yağmurlu', 'antalya': 'güneşli', 'izmir': 'güneşli'}
"""
-> Bu durumda iki değişkenin bellek adresleri eşitlenmez. Değerlerin ikinci bir kopyası oluşturulur.
-> Bu durumda herhangi bir değişken üzerinde yapılacak değişiklik diğerini etkilemez.

"""
havadurumu = {"ankara":"bulutlu","istanbul":"yağmurlu","antalya":"güneşli"}
tahmin = havadurumu.copy()
havadurumu["izmir"]="güneşli"
print(tahmin)
#Çıktı:{'ankara': 'bulutlu', 'istanbul': 'yağmurlu', 'antalya': 'güneşli'}
# Burada görüldüğü üzere "izmir":"güneşli" yazmıyor çünkü bellek adresleri eşitlenmedi sadece kopyası çıkarıldı.

# -----------------------------------------------------
#  ANALİZ: REFERANS ATAMA (=) VS. KOPYALAMA (.copy()) :                                  
# -----------------------------------------------------
# -------------------------------------------------------------------------------------------
#  İŞLEM            | MANTIK (NE OLUYOR?)                  | BELLEK (ID) DURUMU             |
# -------------------------------------------------------------------------------------------
#  tahmin = hava    | Aynı eve iki farklı anahtar çıkarmak.| id'ler AYNI. (Referans)        |
#  tahmin = .copy() | Yan eve evin aynısından inşa etmek.  | id'ler FARKLI. (Yeni Nesne)    |
# -------------------------------------------------------------------------------------------

# 1. DURUM: REFERANS ATAMA (tahmin = havadurumu)
# Burada yeni bir sözlük oluşmaz. Sadece "havadurumu" sözlüğüne "tahmin" diye ikinci bir isim takarsın.
# Eğer havadurumu'na İzmir'i eklersen, tahmin'e baktığında onu da orada görürsün.
# Çünkü ikisi de bellekteki AYNI kutuya bakıyor.

# 2. DURUM: KOPYALAMA (tahmin = havadurumu.copy())
# Burada Python gider, bellekte tamamen yeni bir alan açar ve içini doldurur.
# Artık havadurumu'na ne yaparsan yap, tahmin bundan etkilenmez. Çünkü bağlar koptu.

"""
 Gerçek Hayat Benzetmesi (Mühendis Gözüyle):
--------------------------------------------
Referans (=): Bir Google Dokümanı düşün. Linki arkadaşına gönderdin. Arkadaşın bir cümle silerse, sen dokümanı açtığında o cümleyi silinmiş görürsün. Çünkü doküman tek, kullanıcı iki.
Kopyalama (.copy()): O Google Dokümanının bir kopyasını bilgisayarına .docx olarak indirdin. Artık sen bilgisayarındaki dosyayı değiştirsen de internetteki asıl doküman değişmez.
"""


#-----------------
# KÜMELER (SETS) :
#-----------------

"""
-> Kümeler de listeler ve demetler gibi birden çok elemanı organize eden koleksiyonlardır.
-> Demetlerden farklı olarak kümeler değiştirilebilir yapıdadır.
-> Farklı türde elemanlar barındırabilirler.
-> Matematiksel kümelerin taşıdığı bütün özellikleri taşırlar.

# ------------------------------------------------------------------------------------------------
#  ÖZELLİK            | AÇIKLAMA VE MANTIK                                                       |
# ------------------------------------------------------------------------------------------------
#  Benzersizlik       | Aynı elemandan sadece BİR tane barındırır. (Unique elements)             |
#  Sırasızlık         | Elemanların belli bir sırası yoktur (İndeksleme yapılamaz).              |
#  Değiştirilebilirlik| Kümenin kendisi değiştirilebilir ama içindeki elemanlar sabit olmalı.    |
#  Temel Görevi       | Veri setindeki tekrarları temizlemek ve küme işlemleri yapmak.           |
# ------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------
#  NEDEN SET() KULLANIRIZ? (MÜHENDİSLİK KULLANIMI)                                        |
# -----------------------------------------------------------------------------------------
#  1. Tekrar Silme  : Bir listedeki mükerrer kayıtları tek satırda temizler.              |
#  2. Hızlı Sorgu   : Bir elemanın kümede olup olmadığını kontrol etmek çok hızlıdır.     |
#  3. Matematik     : Kesişim (&), Birleşim (|) ve Fark (-) gibi işlemleri sağlar.        |
# -----------------------------------------------------------------------------------------
"""

#-----------------
# KÜME TANIMLAMA :
#-----------------
"""
-> Python'da küme tanımlamak için set() komutu kullanılır. 
-> set(), Python'da kümeler oluşturmamızı sağlayan yerleşik (built-in) bir fonksiyondur.
-> Elemanları ile birlikte küme tanımlamak için {} simgesi kullanılır.
-> Bu simgeyi daha önce sözlük oluşturmak için de kullanmıştık .
-> Ancak buradaki fark sözlüklerde anahtar,değer ikilileri halinde elemanlar tanımlarken kümelerde tekli olarak tanımlanır.
-> Daha önce tanımlanmış olan listeler ya da demetler de kümeye dönüştürülebilir.
"""
kume = set()      # Boş bir küme oluşturma işlemi.
kume = {1,2,3,4}
print(type(kume))
#Çıktı:<class 'set'>

print(kume)
#Çıktı: {1, 2, 3, 4}

liste = ["yeşil","beyaz","mavi"]
renkler = set(liste)  # Burada listeyi kümeye dönüştürüyoruz.
print(renkler)
#Çıktı: {'yeşil', 'mavi', 'beyaz'}


#-----------------------
# KÜMEYE ELEMAN EKLEME :
#-----------------------
"""
-> Mevcut kümeye eleman eklemek için add() komutu kullanılır.
"""
kume = {1,2,3}
kume.add(4)
print(kume)
#Çıktı: {1, 2, 3, 4}

kume2 = {"Ali","Mehmet","Veli"}
kume2.add("Ahmet")
print(kume2)
#Çıktı: {"Ali","Mehmet","Veli","Ahmet"}


#-------------------------
# KÜMEDEN ELEMAN ÇIKARMA :
#-------------------------
"""
-> Mevcut kümeden eleman çıkarmak için remove() ve discard() isminde 2 ayrı komut kullanılır.
-> Bu 2 komut benzer işleri yerine getirse de aralarında küçük bir fark vardır.
-> discard()komutu remove ile aynı işi yapmakla beraber tek farkı kümede olmayan bir elemanı silinmek isterse hata meydana gelmez.

.discard() -> Hata vermiyor.
.remove()  -> Hata veriyor.
"""
kume = {1,2,3}
kume.remove(3)
kume.discard(2)
print(kume)
#Çıktı: {1}
#kume.remove(5) -> Bunda KeyError: 5 hatası veriyor.
kume.discard(5)
print(kume)

#-----------------
# İKİ KÜME FARKI :
#-----------------
"""
-> Bir kümede olup diğer kümede olmayan elemanları bulma işlemine 'fark alma' denir.
-> İki küme arasındaki fark almak için 'difference() komutu' kullanılır.
"""
kume1 = {1,2,3,4}
kume2 = {1,2,3,4,5,6,7}
fark = kume2.difference(kume1) # Bunun türkçesi şu : Küme 2 de olup Küme 1 de olmayan elemanlar neler :
print(fark)
#Çıktı: {5, 6, 7}
# Şu şekil de yazılabilir.
fark = kume2-kume1
print(fark)
#Çıktı: {5, 6, 7}


#-----------------------------------------
# KESİŞİM KÜMESİNİ BULMA: (INTERSECTION) : 
#-----------------------------------------
"""
-> Kesişim, iki veya daha fazla kümede ortak olarak bulunan elemanlardan oluşan yeni bir küme oluşturma işlemidir.
-> Kesişim için Python'da intersection() komutu kullanılır.
-> Kesişim işleminde (Intersection), kümelerin sırası önemli değildir.
"""
kume1 = {1,2,3,4,5,6}
kume2 = {1,3,5,7,9}
kesisim = kume1.intersection(kume2)
kesisim_ters = kume2.intersection(kume1)
print(kesisim)
print(kesisim_ters)
#Çıktı:{1, 3, 5}
#Çıktı:{1, 3, 5}

# Kesişimde sıranın önemi yok ikisinde de aynı sonuç çıkıyor.
# Bu & (Ampersant) işaretini yapmak için alt-38 tuşlarına basılmalı. 

karakter = "çğıöşüÇĞIÖŞÜ"
isim = input("Lütfen isminizi giriniz:")
if set(karakter) & set(isim):
    print("Girdiğiniz isim Türkçe karakter barındırıyor.")
# & işareti (Ampersant), iki veya daha fazla kümenin Kesişimini (Intersection) bulmak için kullanılan operatördür.

sayi = {1,2,3,4,5}
tahmin = {5}
if not set(sayi) & set(tahmin):
    print("Sayıyı tahmin edemediniz.")
else:
    print("Sayıyı doğru tahmin ettiniz.")


#--------------------------
# BİRLEŞİM KÜMESİ:(UNION) :
#--------------------------
"""
-> İki veya daha fazla kümenin tüm elemanlarını bir araya getirerek, her elemanın sadece bir kez yer aldığı yeni bir küme oluşturma işlemidir.
-> Python'da Kullanımı: .union() metodu veya | (dikey çizgi/pipe) operatörü.
-> Birleşim Kümesinde, kümelerin sırası önemli değildir.
"""
kume1 = {1,2,3}
kume2 = {3,4,5}
birlesim = kume1.union(kume2)
print(birlesim)
#Çıktı: {1, 2, 3, 4, 5}


#------------------------------------------
# AYRIK KÜME TESPİTİ (DISJOINT SET UNION) :
#------------------------------------------
"""
-> Ortak hiçbir elemanı bulunmayan kümelere 'Ayrık Küme' denir. 
-> Yani iki kümenin kesişimi boş bir küme ise bu kümeler birbirine göre ayrıktır.
-> Pythonda ayrık küme tespiti için isdisjoint() komutu kullanılır.
-> Bu komut ayrık ise True, değilse False sonuç üretir. (Yani Boolean mantığı ile çalışır)
"""
kume1 = {1,2,3}
kume2 = {3,4,5}
ayrik_küme_mi = kume1.isdisjoint(kume2)
print(ayrik_küme_mi)
#Çıktı: False -> Çünkü 3 ortak oldu.


#--------------------
# ALT KÜME (SUBSET) :
#--------------------
"""
-> Bir kümenin tüm elemanlarının bir başka küme içerisinde var olup olmadığının tespitinde kullanılır.
-> Yani bir kümenin bir başka kümenin alt kümesi olup olmadığının kontrolünde issubset() komutu kullanılır.
"""
kume1 = {1,2,3}
kume2 = {1,2,3,4,5}
altKume = kume1.issubset(kume2) # Küme 1 Küme 2'nin alt kümesi midir ?
print(altKume)
#Çıktı: True


#---------------------------
# KAPSAYAN KÜME (SUPERSET) :
#---------------------------
"""
-> Alt küme sorgulamasının tam tersi olark "küme2,küme1'i kapsar mı ?" sorusuna cevap bulmak için issuperset()komutu kullanılır.
"""
kume1 = {1,2,3}
kume2 = {1,2,3,4,5}
kapsar = kume2.issuperset(kume1) 
print(kapsar)
#Çıktı: True -> Küme 2 küme 1'i kapsar.


#---------------------------------------
# İÇ İÇE SÖZLÜK (NESTED DICT) KAVRAMI :
#---------------------------------------
"""
-> Bir sözlüğün değer (value) kısmında, başka bir sözlüğün yer alması durumudur.
-> Gerçek hayatta bir apartman (ana sözlük), içindeki daireler (alt sözlükler) ve dairelerin içindeki bilgiler (isim, oda sayısı) gibi düşünülebilir.
-> Karmaşık verileri (Müşteri kayıtları, oyun karakterleri, ders detayları) tek bir çatı altında toplamak için kullanılır.
"""
sirket_personelleri = {
    "emp101": {
        "ad": "Ahmet Yılmaz",
        "departman": "Yazılım",
        "maas": 75000,
        "yetenekler": ["Python", "SQL", "Docker"]
    },
    "emp102": {
        "ad": "Ayşe Demir",
        "departman": "Tasarım",
        "maas": 68000,
        "yetenekler": ["Figma", "Photoshop"]
    },
    "emp103": {
        "ad": "Mehmet Can",
        "departman": "Pazarlama",
        "maas": 55000,
        "yetenekler": ["Google Ads", "Analiz"]
    }
}
"""
Neden Bu Yapı Mühendislik İçin Hayati?
--------------------------------------
1-Veri Gruplama: 
-> Eğer iç içe sözlük kullanmasaydın; isimler için ayrı bir liste, maaşlar için ayrı bir liste tutman gerekecekti. Bir personeli sildiğinde her listeden ayrı ayrı silmek zorunda kalacaktın.
-> Bu yapı sayesinde tek bir ID'yi silerek o kişiye ait tüm dünyayı silebilirsin.

2-API ve Web Dünyası:
-> İnternetten bir hava durumu verisi çektiğinde veya bir e-ticaret sitesinden ürün listesi istediğinde sana veri tam olarak bu formatta gelir.

3-Esneklik:
-> Dikkat edersen her personelin yetenek sayısı farklı (biri 3, biri 2). Sözlükler ve içindeki listeler sana bu esnekliği sağlar; sabit bir sütun sayısına mahkum kalmazsın.
"""

# ===============================================================================================================
# == BAB 9: KOLEKSİYONLAR-2 (SÖZLÜKLER VE KÜMELER) PROJELERİ (COLLECTIONS-2 (DICTIONARIES AND SETS) PROJECTS : ==
# ===============================================================================================================

#-------------------------------------------------------------------------------
# ÖRNEK 1 : Koleksiyonlar(1-2) Üzerinde Veri Analizi ve Koşullu Transformasyon :
#-------------------------------------------------------------------------------

sayilar = [1,3,5,7,9,12,19,21]

# 1-Sayılar listesinde hangi sayılar 3'ün katıdır ?
for sayi in sayilar:
    if (sayi % 3 == 0):
        print(sayi)

# 2-Sayılar listesinde sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam = toplam+sayi
print("Toplam:", toplam)

# 3-Sayılar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(sayi**2)


sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4-Şehirlerden hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if len(sehir)<=5:
        print(sehir)

urunler=[
    {"name":"samsung s6","price":"3000"} ,
    {"name":"samsung s7","price":"4000"} ,
    {"name":"samsung s8","price":"5000"} ,
    {"name":"samsung s9","price":"6000"} ,
    {"name":"samsung s10","price":"7000"} ,
]
# 5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam = toplam+fiyat
print("Toplam ürün fiyatı:",toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz .
for urun in urunler:
    if (int(urun["price"]) <= 5000) :
        print(urun)


#----------------------------------------
# ÖRNEK 2: Sözlükler Üzerinde  Gezinmek :
#----------------------------------------
sozluk = {"bir":1, "iki":2, "üç":3, "dört":4, "beş":5}
sozluk.keys()
sozluk.values()
sozluk.items()
print(sozluk)


sozluk = {"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
for eleman in sozluk:
    print(eleman,sozluk[eleman])

#-------------------------------------------------------------------
# ÖRNEK 3 : Sözlükler Üzerinde Temel Gezinti (Keys, Values, Items) :
#-------------------------------------------------------------------

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5}

# A-) SADECE ANAHTARLAR (KEYS) ÜZERİNDE GEZİNME : Bu yöntem, sadece etiketler (anahtarlar) üzerinden işlem yapacağınızda kullanılır.
print("\n--- A-) Sadece Anahtarlar Üzerinde Gezinti ---")
for anahtar in sozluk.keys():
    print(f"Sayı İsmi (Key): {anahtar}")


# B-) SADECE DEĞERLER (VALUES) ÜZERİNDE GEZİNME : Anahtarlarla işiniz yoksa, sadece sayısal verileri toplamak veya analiz etmek için idealdir.
print("\n--- B-) Sadece Değerler Üzerinde Gezinti ---")
toplam_deger = 0
for deger in sozluk.values():
    print(f"Sayısal Değer (Value): {deger}")
    toplam_deger += deger
print(f"Sözlükteki Tüm Değerlerin Toplamı: {toplam_deger}")


# C-) HEM ANAHTAR HEM DEĞER (ITEMS) ÜZERİNDE GEZİNME (Tavsiye Edilen) : En profesyonel ve 'Pythonic' yöntem budur.
# ->  'Unpacking' (Paket Açma) yaparak  her iki veriye de aynı anda, en hızlı şekilde erişiriz.
print("\n--- C-) Hem Anahtar Hem Değer (Items) Üzerinde Gezinti ---")
for anahtar_ismi, sayisal_deger in sozluk.items():
    # :6 ifadesi çıktıların nizami durması için 6 karakterlik boşluk bırakır.
    print(f"Sayı: {anahtar_ismi:6} | Değeri: {sayisal_deger}")


# D-) SÖZLÜK ÜZERİNDE DOĞRUDAN DÖNGÜ (Varsayılan Davranış) : Eğer sözlüğü doğrudan döngüye sokarsanız, Python varsayılan olarak anahtarları getirir.
print("\n--- D-) Doğrudan Döngü (Varsayılan: Anahtarlar) ---")
for eleman in sozluk:
    # Bu yöntem sozluk.keys() ile aynı sonucu verir.
    print(f"Eleman (Anahtar): {eleman} -> Değeri: {sozluk[eleman]}")

"""
ÇIKTI ANALİZİ:
- Items() kullanımı en temiz görüntüyü ve en güvenli erişimi sağlar.
- Programlamada veriyi (Data) sadece saklamak yetmez; onu nasıl 'iterate' (tekrar ederek işleme) edeceğinizi bilmek asıl maharettir.
"""

#-------------------------------------------------------------------
# ÖRNEK 4 : Sözlükler Üzerinde Temel Gezinti (Keys, Values, Items) :
#-------------------------------------------------------------------
turkce_karakterler = set("çğıöşüÇĞIÖŞÜ")
tahmin = input("\nBir harf söyleyiniz: ")

if not set(tahmin).isdisjoint(turkce_karakterler):
    print("İngilizce karakter düzenini bozan harfler tespit edildi.")


#-----------------------------------------------------------------------
# ÖRNEK 5: Dinamik Dijital Kütüphane ve İlim Dalları Sorgulama Sistemi :
#-----------------------------------------------------------------------

print("-------- Dijital Kütüphane Sistemine Hoşgeldiniz --------")

# 1. BÖLÜM: Kimlik Yapılandırması (Configuration)
isim = input("Lütfen isminizi giriniz: ").strip()  
cinsiyet = input("Cinsiyetinizi seçiniz (E/K): ").upper()

# Hitap ve Sistem Verileri
if cinsiyet == "E":
    hitap, kullanici_sistem, sifre_sistem = "Bey", "Ali_Arda87", "arda123"
elif cinsiyet == "K":
    hitap, kullanici_sistem, sifre_sistem = "Hanımefendi", "Zeynep10", "zeynep123"
else:
    hitap, kullanici_sistem, sifre_sistem = "Misafir", "misafir", "123"

# 2. BÖLÜM: Kütüphane Veri Tabanı (Veri Yapısı)
kutuphane = {
    "Edebiyat": [
        {"ad": "Divan-ı Hikmet", "yazar": "Ahmet Yesevi"},
        {"ad": "Mesnevi", "yazar": "Mevlana"}
    ],
    "Matematik": [
        {"ad": "Cebir", "yazar": "Harezmi"}
    ],
    "Fen_Bilimleri": [
        {"ad": "Kanun fi’t-Tıp", "yazar": "İbn Sina"}
    ],
    "Sosyal_Bilimler": [
        {"ad": "Mukaddime", "yazar": "İbn Haldun"}
    ],
    "Din_ve_Inanc": [
        {"ad": "İhya-u Ulumiddin", "yazar": "İmam Gazali"}
    ],
    "Teknoloji ve Yazılım": [
        {"ad": "Python-3","yazar":"Onur Sevli"},
        {"ad": "PYTHON_101","yazar":"Ali Arda"}
    ]
}

# 3. BÖLÜM: Giriş Kontrolü
print(f"\nMerhaba {isim} {hitap}, lütfen kimlik doğrulaması yapınız.")
girilen_user = input("Kullanıcı Adı: ")
girilen_pass = input("Şifre: ")

if girilen_user == kullanici_sistem and girilen_pass == sifre_sistem:
    print(f"\n>>> Hoşgeldin {isim} {hitap}. Raflar yükleniyor...\n")
    
    # Kategori listesini bir kez oluştur (Performans için döngü dışı)
    kategori_listesi = list(kutuphane.keys())

    while True:
        print("-" * 50)
        print("MEVCUT İLİM RAFLARI:")
        for i, kategori in enumerate(kategori_listesi, 1):
            print(f"{i}- {kategori}")
        print("q- Güvenli Çıkış")
        print("-" * 50)
        
        secim = input("Seçiminiz: ").strip()
        
        if secim.lower() == 'q':
            print("İlim yolculuğunuzda başarılar dileriz. Allah'a emanet...")
            break
            
        hedef_kategori = None
        
        # Akıllı Seçim Kontrolü
        if secim.isdigit(): 
            indeks = int(secim) - 1
            if 0 <= indeks < len(kategori_listesi):
                hedef_kategori = kategori_listesi[indeks]
        else:
            # Kullanıcı ismini yazarsa (Büyük/Küçük harf duyarlılığını kaldırdık)
            for k in kategori_listesi:
                if k.lower() == secim.lower():
                    hedef_kategori = k
                    break
            
        # 4. BÖLÜM: Veriyi Sunma (Amel)
        if hedef_kategori:
            print(f"\n✅ {hedef_kategori.upper()} RAFINDAKİ ESERLER:")
            for eser in kutuphane[hedef_kategori]:
                # Formatlı yazdırma (Göz hitabı)
                print(f"📖 {eser['ad']:<25} | Yazar: {eser['yazar']}")
            print("\n")
        else:
            print(f"\n Hata: '{secim}' adında bir raf bulunamadı.\n")

else:
    print("\n Yetkisiz Giriş! Sistem güvenliği için oturum kapatıldı.")


#NOT:
"""
.strip(): Kullanıcı ismini yazarken yanlışlıkla başına veya sonuna boşluk koyarsa (" Ali " gibi), Python bu boşlukları atar. Temiz veri (Data Cleaning) için hayati bir kuraldır.
.upper(): Kullanıcı küçük "e" veya "k" girse bile sistem bunu büyük harfe çevirir. Kodun geri kalanındaki if kontrollerinde işimizi kolaylaştırır.
enumerate(..., 1): Bu fonksiyon, listenin elemanlarını tek tek çıkarırken yanlarına 1'den başlayarak numara verir. Kullanıcı "Sosyal_Bilimler" yazmakla uğraşmasın, sadece "4" yazabilsin diye bu numaralandırmayı yapıyoruz.
"""

# ===============================================================================================================================================
""" 
 Elhamdülillah, 9. Bab nihayete erdi; Sözlüklerin 'Anahtar-Değer' nizamı ve Kümelerin 'Benzersizlik' sırrı ile koleksiyonlar ilmini tamamladık. 
 Dağınık veriyi Sözlüklerle anlamlandırdık, mükerrer veriyi Kümelerle arındırdık.                                                               
 Bu iki güçlü yapı ile programlarımızın hafızasını hem daha güvenli hem de daha hızlı (O(1)) kıldık.                                            
 Bu 9.Babımızı 5 örnekle pekiştirdik.                                                                                                           
"""                                                                                                                                                    
# ===============================================================================================================================================
# ÖRNEK 1: Koleksiyonlar Üzerinde Veri Analizi ve Koşullu Transformasyon (Listeler ve Sözlüklerin İç İçe Kullanımı)                             |
# ÖRNEK 2: Sözlükler Üzerinde Temel Gezinti (Implicit Loop Yöntemi)                                                                             |
# ÖRNEK 3: Sözlük Metotları ile Profesyonel Veri İşleme (Keys, Values, Items ve Unpacking Teknikleri)                                           |
# ÖRNEK 4: Kümeler (Sets) ile Karakter Denetimi ve Ayrık Küme Analizi (isdisjoint Metodu Uygulaması)                                            |   
# ÖRNEK 5: Dinamik Dijital Kütüphane ve İlim Dalları Sorgulama Sistemi (Kapsamlı Veri Tasnifi ve Güvenli Erişim Uygulaması)                     |
# ===============================================================================================================================================
