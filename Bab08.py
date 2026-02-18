# ===================================================================
# == BAB 8: KOLEKSİYONLAR-1(COLLECTIONS-1)(LİSTELER VE DEMETLER) : ==
# ===================================================================

# Koleksiyon: Birden fazla veri öğesini bir araya getirip tek bir mantıksal birim altında saklayan, organize eden ve yöneten veri yapısıdır.
"""
Koleksiyonların Temel Amacı:
----------------------------
1.Gruplandırma: Birbirleriyle ilişkili verileri (Örn: Bir öğrencinin notları, bir ülkenin şehirleri) bir arada tutmak.
2.Toplu İşlem: Öğrendiğiniz for döngüleri ile koleksiyondaki her bir öğeyi tek tek gezerek işlem yapmayı sağlamak.
3.Organizasyon: Verilerin belirli bir düzende (sıralı veya anahtar-değer ilişkisiyle) saklanmasını sağlamak.

-> Pythonda 4 ana yerleşik koleksiyon türü (veri yapısı) vardır. Bu türler, verileri farklı kurallarla organize eder.
-> 1.Liste
-> 2.Demet
-> 3.Sözlük
-> 4.Küme
"""

#--------------------
# 1.LİSTELER(LISTS) :
#--------------------
"""
-> Aynı ya da farklı türde, birden çok elemanı bir arada tutan ve bu elemanlar üzerinde ekleme, silme, güncelleme işlemlerine olanak sağlayan koleksiyonlardır.
"""
liste = list()                          # Boş bir liste tanımlar. list() yapıcı fonksiyonu, bir listeyi açıkça oluşturmak için kullanılır.
liste = []                              # Boş bir liste tanımlamanın başka bir yolu
liste = list([1, 2, 3])                 # İçerisinde 1,2,3 değerleri olan bir liste tanımlar.
liste = [1, 2, 3]                       # İçerisinde 1,2,3 değerleri olan listeyi tanımlamanın bir başka yolu.
liste = ["elma", "kiraz", "erik"]       # String listesi
liste = [1, 2, "elma", "erik", 2.34]    # Farklı türdeki elemanlardan oluşan bir liste

# Not: Yani aynı türde olma zorunluluğu yok farklı türde de olabilir. 


#-----------------------------------------
# LİSTELERİN YAPISI VE ESNEKLİK ÖZELLİĞİ :
#-----------------------------------------
"""
-> Python listeleri 'Heterojen' (Çok Türlü) bir yapıya sahiptir.
-> Bir liste içerisinde int, float, string, boolean ve hatta nesneler bir arada bulunabilir.
-> Teknik olarak her liste elemanı, aslında bellekteki başka bir nesneye işaret eden bir 'pointer' (işaretçi) tutar.
"""

# Farklı türde verilerin bir arada kullanımı:
personel_verisi = ["Ahmet Yılmaz", 34, 45500.50, True]

#--------------------------------------------------
# Neden Bu Yapıyı Kullanırız? (Teknik Avantajlar) :
#--------------------------------------------------

# 1. Veri Paketleme (Data Packaging):
#------------------------------------
# Gerçek dünyadaki bir varlığı temsil etmek için farklı tipte değişkenler oluşturmak yerine ilgili tüm bilgileri tek bir yapıda toplamanızı sağlar.
# Örn: Bir sensörden gelen veriler: [Zaman_Damgası, Sıcaklık, Cihaz_Adı, Aktif_mi]
sensor = ["2026-02-08 21:00", 22.5, "Salon_Termostat", True]

# 2. Tip Bağımsızlık (Type Agnosticism):
#---------------------------------------
# Python listeleri, içine ne koyacağınızı önceden bilmenize gerek duymaz.
# Bu durum, özellikle dış kaynaklardan (API, Veritabanı) gelen ve tipi değişebilen verilerle çalışırken kodun kırılmasını engeller.

# 3. Dinamik Bellek Yönetimi:
#----------------------------
# Listenin her elemanı farklı boyutta yer kaplayabilir. Python bunu arka planda otomatik yönettiği için geliştirici bellek hesabı yapmak zorunda kalmaz.


#--------------------------------
# ÖZET VE KARŞILAŞTIRMA TABLOSU :
#--------------------------------

# ----------------------------------------------------------------------------------------------------------
#  Özellik       : Açıklama                                                                                |
#  --------------:------------------------------------------------------------------------------------------
#  Heterojenlik  : Farklı veri tiplerini (str, int, bool) aynı kutuda saklayabilme yeteneğidir.            |
#  Mutability    : Listeler değiştirilebilirdir; elemanlar güncellenebilir veya silinebilir.               |
#  Indeksleme    : Elemanlara 0'dan başlayan tam sayılarla hızlıca erişim imkanı sağlar.                   |
#  Esneklik      : Veri setlerini gruplandırırken katı kurallara takılmadan işlem yapmayı sağlar.          |
# ----------------------------------------------------------------------------------------------------------

"""
BİLGİ: C veya Java gibi dillerde diziler genellikle 'Homojen'dir (tek tip veri kabul eder). 
Python'ın bu kadar popüler olmasının nedenlerinden biri, listelerin sunduğu bu 'hoşgörülü' ve esnek yapıdır.
"""

"""
SONUÇ: 
Python listeleri, katı veri tiplemesi kurallarını yıkarak geliştiriciye hız kazandırır. 
Farklı türleri bir arada tutabilmesi sayesinde, karmaşık veri yapılarını (JSON benzeri yapılar) oluşturmak çok daha basit hale gelir.
"""

"""
-> Bir liste tanımlarken elemanları köşeli parantez[] içerisinde,her birinin arasına virgül koyarak yazılır.
-> Liste içerisindeki tüm elemanlar aynı türde olabileceği gibi(hepsi sayı ya da hepsi string) , farklı türde elemanlar da bir arada bulunabilir.
-> Liste içerisindeki her bir eleman bellekte ayrı ayrı bölgelerde sıralı vaziyette yer alır.
-> Adresler (referanslar) ardışıktır, ama verilerin kendisi belleğin her yerine dağılmış olabilir.
-> Liste değişkeni ise, bu elemanların bellekte bulunduğu  bölgenin başlangıç adresine işaret eder.

Neden Listeler Kullanmalıyız? (Tek Değişkenlere Karşı)
-> Tek tek değişkenler yerine listeleri kullanmak, kodunuzun ölçeklenebilirliğini, yönetilebilirliğini ve verimliliğini artırır.

1. Gruplama ve Organizasyon:
----------------------------
Tek Değişken: Her veri öğesi (sehir1, sehir2) birbirinden bağımsız ve ilişkisizdir. Birbirine ait olduklarını program bilemez ve külfetli olur.
Liste: İlişkili tüm verileri ("İstanbul", "Ankara", "İzmir") tek bir mantıksal birim (sehirler) altında toplar ve sıralar.

2. Toplu İşlem Gücü (Döngüler):
-------------------------------
Tek Değişken: Bir işlemi 100 farklı değere uygulamak için 100 farklı satır kod yazmanız gerekir (Örn: print(sehir1), print(sehir2)...). Bu, kod tekrarıdır.
Liste: Öğrendiğiniz for döngüsü sayesinde, kaç öğe olursa olsun tüm koleksiyona tek bir satır kodla (for sehir in sehirler: print(sehir)) toplu işlem uygulayabilirsiniz. Bu, kod tekrarını önler (DRY Prensibi).

3. Erişim ve Yönetilebilirlik:
------------------------------
Tek Değişken: Yeni bir değer eklendiğinde, koda yeni bir değişken adı (sehir101) ve yeni bir işlem satırı eklemeniz gerekir.
Liste: Tek bir isim altında sınırsız veriyi indeks numaralarıyla yönetmenize, döngülerle tek seferde işlemenize ve yeni verileri koda dokunmadan dinamik olarak eklemenize olanak tanır.
İndeks Erişimi: Öğelere indeks numarası (sehirler[5]) ile hızlıca erişilebilir.
Dinamik Büyüme: Listenin sonuna yeni bir öğe eklemek (sehirler.append("Bursa")), mevcut döngü kodunuzu otomatik olarak yeni öğeyi de işleyecek şekilde hazırlar.

4. Ölçeklenebilirlik:
---------------------
Tek Değişken: Veri miktarındaki artış, yazdığınız kod satırı sayısını doğrusal olarak artırır (100 veri = 100 satır kod).
Liste: Veri miktarındaki artış, kodunuzun satır sayısını etkilemez. Yazdığınız kod, 3 veri için de 1000 veri için de aynıdır.

-> Bir listede 100 değer tanımlamak, 100 tane ayrı değişken tanımlamaktan 'KESİNLİKLE daha fazla RAM kaplar'.
-> Ancak, bu ekstra maliyet, elde ettiğiniz yönetilebilirlik, hız ve ölçeklenebilirlik avantajlarının yanında ihmal edilir bir fiyattır.

-> Listeler, tek tek değişkenlere göre daha fazla RAM kaplamanın iki temel nedeni vardır:
 1. Ek Yapı Maliyeti (Overhead) Bir liste oluşturduğunuzda, Python bellekte sadece 100 değerin kendisini tutmaz; aynı zamanda listeyi yönetmek için ek veriler saklar. 
-> Bu ek verilere "Yapısal Yük" (Overhead) denir.

 2. Referans Yoluyla Saklama
-> Daha önce bahsettiğimiz gibi, bir liste içindeki değerleri doğrudan tutmaz. Bunun yerine, değerlerin bellekteki adreslerini (referanslarını) tutar.
"""

liste = [50,60,70]
# liste=list("İzmir","İstanbul","Ankara","Bursa") => list() fonksiyonu (constructor), içine tek bir nesne (iterable) bekler. Sen ise ona virgüllerle ayırarak 4 farklı "str" argümanı gönderdin.
# Python bunu şöyle anladı: "Bana 4 tane ayrı paket verdin ama benim kollarım sadece 1 paket tutabilir."

# Şehirleri bir parantez (tuple) içine alarak tek bir paket yapıyoruz:
liste = list( ("İzmir", "İstanbul", "Ankara", "Bursa") ) 
# Dikkat: İç içe çift parantez oldu. Dışarıdaki list(), içerideki tek bir paketi açıp listeye çevirir.

"""
-> list() fonksiyonu, bir fabrikadaki paket açma makinesi gibidir. Bu makinenin kuralı şudur: "Bana sadece 1 tane kapalı kutu getir, ben onu açıp içindekileri listeye dizeyim."
"""

#---------------------------------------
# LİSTE ELEMANLARINA ERİŞİM (INDEXING) :
#---------------------------------------
"""
-> Bir listedeki elemanlara erişmek, onların sıra numaralarını (indekslerini) kullanmakla yapılır.
-> Bu, bir raftaki kitaplara sıra numarasıyla ulaşmaya benzer.
1. >> Pozitif İndeksleme (Baştan Sayma) Python'da ve birçok programlama dilinde, listelerin ilk elemanı 1'inci değil, 0'ıncı indekstedir. Kural: Saymaya 0'dan başlanır ve her zaman N-1 kuralı uygulanır.
2. << Negatif İndeksleme (Sondan Sayma) Negatif indeksleme, Python'ın sunduğu çok kullanışlı bir özelliktir. Listenin sonundaki elemanlara kolayca erişmenizi sağlar. Kural: Saymaya -1'den başlanır. -0 diye bir şey yoktur.
"""
sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa","Antalya","Şanlıurfa"]

# Not: Negatif İndeksleme C, C++ ve Java Dilinde bellek yönetimi ve güvenlik sebebiyle bulunmamaktadır.

print(sehirler[0]) #Çıktı: İstanbul
print(sehirler[2]) #Çıktı: İzmir
print(sehirler[5]) #Çıktı: Şanlıurfa

sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa"]

print(sehirler[-1]) #Çıktı: Bursa (Listenin son elemanı)
print(sehirler[-3]) #Çıktı: Ankara

#-------------------------------------
# LİSTE ELEMAN SAYISI BULMA : -len() :
#-------------------------------------
"""
-> Bir listenin eleman sayısını bulmak için len() komutu kullanılır. Bu komut aynı zamanda String'lerin karakter sayısını bulunurken de kullanılır.
"""
liste = [50,60,70]
uzunluk=len(liste)
print(uzunluk)          #Çıktı: 3


liste = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
liste_uzunlugu = len(liste)
print(liste_uzunlugu)   #Çıktı : 12


#------------------------------------------------------------------------
# 1.append: Listenin sonuna  belirtilen elemanı eklemek için kullanılır .
#------------------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
print(donanim)
donanim.append("bellek")  # Listenin sonuna bellek stringini listeye ekledi.
print(donanim)

liste = [10,20,30]
liste.append(40)
print(liste)

kenksler = ["Ali Arda","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren","Mr.Ali"]
print(kenksler)
kenksler.append("İsmail Furkan")
print(kenksler)


#---------------------------------------------------
# 2.extend: Listeleri birleştirmek için kullanılır .
#---------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
yazilim = ["işletim sistemi","web tarayıcı"]
print(yazilim)
print(donanim)
donanim.extend(yazilim)   # Yazilim listesinin elemanları donanim'in sonuna kalıcı olarak eklendi. 

# NOT: Python'da nokta (.) işaretinden önce yazan isim, "ev sahibi"dir. Büyük olan donanımdır. Yazılım elemanlarını donanım üzerine ekler.
"""Donanım birimlerini (yazıcı, klavye...) al, bunların üzerine yazılım birimlerini (OS, tarayıcı...) de monte et/entegre et ve hepsini tek bir 'donanım' çatısı altında topla."""

print(donanim)
print(donanim+yazilim) # Bu şekilde de yazılabilir.
print(yazilim)

kenks1_grubu = ["Ali","Emre","Qusay","Ümit"]
kenks2_grubu = ["İlker","Muhammed Furkan","İsmail Furkan","Eren","Muhammed Semih"]
kenks3_grubu = ["Baran","Eren","Yusuf","Erol"]

kenks1_grubu.extend(kenks2_grubu)
print(kenks1_grubu)  
print(kenks2_grubu)  
# Burada kenks1_grubunun üzerine kenks2_grubunu ekler.
# Yani kenks1_grubu büyür. kenks2_grubu değişmez.
# extend kullandığında, eklenen listenin elemanları mevcut listenin son indeksinden itibaren sırayla yerleşir.


#------------------------------------------------------------------------------------
# 3.insert: Listenin belirtilen konumuna (indeksine) eleman eklemek için kullanılır .
#------------------------------------------------------------------------------------

# insert kelimesinin Türkçe karşılığı tam olarak "yerleştirmek", "araya eklemek" veya "sokmak" anlamına gelir.
donanim = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanim.insert(7,"bellek")  
donanim.insert(-1,"sabit disk") 

# Negatif İndeksler: Sondan sayma kuralına göre, işaret edilen elemanın önüne ekler.
# Pozitif İndeksler: Baştan sayma kuralına göre, girilen pozisyona (indekse) ekler. Aşarsa sona ekler.
print(donanim)

#Çıktı: ['yazıcı', 'klavye', 'işlemci', 'bellek', 'sabit disk', 'sabit disk', 'bellek'] -> 7 numaralı indeks olmadığı için en son kısma atadı.

liste = [10,20,30]
liste.insert(1,15)
print(liste)  # insert() metodunda 0'dan başlama kuralı hayati önem taşır çünkü Python'da liste indeksleri her zaman 0'dan başlar. Yani sıra derken 1 den başlama hatalı olur.

"""
# Makinenin Davranışı: Güvenli Genişleme :
------------------------------------------
-> Python'da .insert(indeks, eleman) metodunun bu durumu ele alma şekli oldukça kullanıcı dostudur (safe):
-> Eğer belirtilen indeks, listenin geçerli indeks aralığındaysa (örneğin 0 ile 4 arası): Eleman tam olarak o indekse yerleştirilir ve diğer elemanlar sağa kaydırılır.
-> Eğer belirtilen indeks, listenin son elemanının indeksinden büyükse (sizin örneğinizde 7 > 4):
-> Python, bu durumu bir hata olarak görmez.
-> Listenin en sonuna ekleme yapar, tıpkı .append() metodu gibi davranır.

Negatif İndeks Esnekliği :
--------------------------
-> Tıpkı listenin sonunu aşan indekslerde hata vermediği gibi, çok küçük (negatif) indekslerde de Python "güvenli" davranır.
Durum: Eğer listenin başlangıcından çok daha küçük bir negatif indeks verirseniz (örneğin -100), Python bunu yine hata olarak görmez.
Davranış: Elemanı listenin en başına (0. indekse) yerleştirir.
"""


#-----------------------------------------------------------
# 4.remove: Listenin içindeki değeri verilen elemanı siler .
# ---------------------------------------------------------- 
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
donanim.remove("klavye")   # Değere Göre Siler: .remove() indekse değil, parantez içine yazdığın değere odaklanır. Eğer donanim.remove("klavye") dersen, listede "klavye" metnini bulur ve yok eder.
donanim.remove(donanim[1]) # İlk Bulduğunu Siler: Eğer listede iki tane "klavye" varsa, .remove() sadece ilk gördüğünü siler; diğerine dokunmaz. 
print(donanim)             # Aslında burada 2 farklı yöntemle de silindiğini vurgulamaktadır.

liste = [10,20,30]
liste.remove(20)
print(liste)


kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
kenksler.remove("Erol")     
print(kenksler)
#Çıktı: ['Ali', 'Emre', 'Qusay', 'Ümit', 'Baran', 'İlker', 'Eren', 'Muhammed Furkan', 'Muhammed Semih', 'Yusuf', 'Eren']

"""
liste = [10, 20, 30]
liste.remove(2) # 2 değeri listede yok
print(liste)

Sonuç: !!! Hata Çıktısı !!! -> Hata Türü: ValueError: list.remove(x): x not in list

Açıklama: remove() metodu, silinmesi istenen 2 değerini listede bulamaz. 
-> Program bu noktada durur ve ValueError türünde bir istisna (exception) fırlatır.
"""
# Liste içerisinde aynı değer birden çok bulunuyorsa yalnız ilki silinir.
liste = [10,20,30,30,20,10]
liste.remove(10)
print(liste)
# Remove değeri , pop indeksten silme işlemi yapar.


#------------------------------------------------------------
# 5.pop: Listede belirtilen konumdaki(indeks) elemanı siler .
#------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
donanim.pop(3)
print(donanim)  
#Çıktı: ['yazici', 'klavye', 'işlemci', 'sabit disk'] -> Bellek kelimesi listeden silindi.


#-------------------------------------------------------------------------
# 6.clear: Listenin tüm elemanlarını siler ve boş bir liste ortaya çıkar .
#-------------------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
donanim.clear()
print(donanim)
# Python'daki liste metodu olan .clear() metodu, listenin tüm elemanlarını silerek listeyi boş bir liste haline getirmeyi garanti eder.
# Bundaki amaç Listenin içeriğini tamamen sıfırlamak.

kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
kenksler.clear()
print(kenksler)

"""
1.Hafıza (Memory) Yönetimi:
---------------------------
-> Bir listeyi tek tek silmek yerine .clear() kullanmak, Python'ın bellek yönetimini optimize eder. 
-> Liste nesnesinin kendisini yok etmeden içindeki referansları boşaltır. Bu, özellikle binlerce verinin olduğu listelerde performansı artırır.

2.Nesne Kimliğini (ID) Korumak:
-------------------------------
-> Bu en kritik sebeptir. Eğer donanim = [] derseniz, Python hafızada yepyeni bir liste oluşturur.
-> Ancak .clear() kullanırsanız, mevcut liste nesnesi yerinde kalır, sadece içi boşaltılır.
-> Aslında bu örneğe benzetebiliriz: Çöp tenekesi dolduğunda içini boşaltırız gidip de çöp tenekesini komple atmayız veya yeni bir çöp tenekesi almaya gerek yok.

Neden Önemli?
-------------
-> Eğer listeniz başka değişkenlere veya fonksiyonlara bağlıysa, [] ataması yaptığınızda o bağlantılar kopar. .clear() ise bağlantıyı koparmadan içeriği sıfırlar.

3. Döngüsel Veri Akışı (Sıfırlama):
-----------------------------------
-> ESP32 gibi sistemlerde veya veri analizi projelerinde sürekli yeni veriler toplanır.

Örnek: Her 1 saatte bir sensör verilerini bir listeye kaydediyorsunuz. Verileri merkeze gönderdikten sonra listeyi tamamen boşaltıp bir sonraki saat için tertemiz bir sayfa açmanız gerekir. .clear() bu "sıfırlama" işlemini en güvenli şekilde yapar.
"""


#-------------------------------------------------
# 7.index: Bir elemanın listedeki konumunu bulur .
#-------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
print(donanim.index("bellek"))

# donanim.index("bellek"): "Bellek nerede?" sorusuna 3 cevabını verir.
# donanim[2]: "2. sıradaki eleman ne?" sorusuna "işlemci" cevabını verir.


#-----------------------------------------------------------------
# 8.count: Listenin belirtilen elemandan kaç adet olduğunu bulur .
#-----------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk","klavye"]
print(donanim.count("klavye"))

kenksler=["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
print(kenksler.count("Emre")) #Çıktı: 1 -> Emre'den bir tane var :)

"count() tek başına yazılırsa ekranda bir şey görmezsiniz, mutlaka print() içinde veya bir değişkene atanarak kullanılmalıdır."

# Seçenek A: Doğrudan Yazdırma
print(donanim.count("klavye"))
# Burada direkt donanim sayisini saydırabiliriz.

#Seçenek B: Değişkene Atama
klavye_sayisi=donanim.count("klavye")
print(f"Klavye sayisi:{klavye_sayisi}") #Burada f formating ile yazdırıyor.


#--------------------------------------------------------------------------------------------------------------------------------
# 9.Sort: Listenin içindeki elemanları sıralar. Burada liste elemanlarının string,int vb. veri tiplerine uygun olarak sıralanır .
#--------------------------------------------------------------------------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
donanim.sort()
print(donanim)      #Çıktı: ['bellek', 'işlemci', 'klavye', 'sabit disk', 'yazici']

liste=[3,5,1,7,2]
liste.sort()
print(liste)        #Çıktı: [1, 2, 3, 5, 7]

kelimeler = ["zambak","açeyla","hanımeli","begonya"]
kelimeler.sort()
print(kelimeler)    #Çıktı : ['açeyla', 'begonya', 'hanımeli', 'zambak']
# Listenizdeki string'ler (metinler) alfabetik olarak (ASCII sırasına göre) sıralanacaktır:


kenksler=["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
kenksler.sort()
print(kenksler)     #Çıktı: ['Ali', 'Baran', 'Emre', 'Eren', 'Eren', 'Erol', 'Muhammed Furkan', 'Muhammed Semih', 'Qusay', 'Yusuf', 'Ümit', 'İlker']

"""
Soru şu : Neden A dan Z ye giderken İlker ve Ümit en sonra yer aldı ?
Cevap: .sort() metodunun varsayılan olarak ASCII (ve Unicode) değerlerine göre sıralama yapmasıdır.

1. ASCII ve Unicode Önceliği
Bilgisayarlar harfleri doğrudan tanımaz; her harfin sayısal bir karşılığı vardır. İngiliz alfabesindeki standart karakterler (A-Z) daha düşük sayısal değerlere sahipken, Türkçe'ye özgü noktalı harfler (İ, Ü, Ö, Ş, Ç, Ğ) Unicode tablosunda çok daha ilerideki sayılarda yer alır.

-> A harfinin değeri: 65

-> Z harfinin değeri: 90

-> İ (Noktalı I) harfinin değeri: 304

-> Ü harfinin değeri: 220

Sıralama yapılırken Python 65'i (A), 304'ten (İ) küçük bulduğu için "İlker"i listenin en sonuna atar.

2. Büyük/Küçük Harf Farkı :
---------------------------
Listende tüm isimler büyük harfle başlıyor, bu yüzden büyük harf/küçük harf çakışması yaşamamışsın. Ancak unutmamalısın ki; Python'da tüm büyük harfler (A-Z), tüm küçük harflerden (a-z) önce gelir. Eğer listenin içinde küçük "a" ile başlayan bir isim olsaydı, o da Z'den sonra gelirdi.
"""


#--------------------------------------------------------
# 10.Reverse: Listeyi sondan başa doğru yani ters yazar .
#--------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
donanim.sort(reverse=True)
print(donanim)
# Burada dikkat edilmesi gereken husus reverse() komutu "büyükten küçüğe sıralama yapmaz." Sadece listenin mevcut sıralamasını ters çevirir.
liste = [3,5,1,7,2]
liste.reverse()
print(liste)

kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
kenksler.sort(reverse=True)
print(kenksler)     #Çıktı : ['İlker', 'Ümit', 'Yusuf', 'Qusay', 'Muhammed Semih', 'Muhammed Furkan', 'Erol', 'Eren', 'Eren', 'Emre', 'Baran', 'Ali']



# reverse() komutunun tek başına büyükten küçüğe çevirme sıralama gibi bir fonksiyonu yoktur. Ancak sort()komutunun ardından çalıştırılırsa ikisi birlikte büyükten küçüğe sıralama işini yerine getirir.
liste = [3,5,1,7,2]
liste.sort()
liste.reverse()
print(liste)

kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
kenksler.reverse()  #Çıktı: ['Eren', 'Yusuf', 'Muhammed Semih', 'Muhammed Furkan', 'Eren', 'İlker', 'Erol', 'Baran', 'Ümit', 'Qusay', 'Emre', 'Ali']
print(kenksler)


# Sıralama: donanim.sort(reverse=True) metodu, listenin elemanlarını büyükten küçüğe (yani alfabetik olarak sondan başa doğru) sıralar.
# Python, True ve False'un ilk harflerinin büyük olması zorunludur.Çünkü Python küçük yazılınca o ifadeyi değişken zannediyor ve bu hatalara neden oluyor.

#--------------------------------------------------
# 11.Copy: Listeyi yeni bir liste olarak kopyalar .
#--------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
yeni_donanim=donanim.copy()
print(yeni_donanim)

kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
yeni_kenksler=kenksler.copy()
print(yeni_kenksler)

"""
.copy() Metodu Hakkında Bilmen Gerekenler :
-> Bağımsız Yedekleme: .copy() metodu, listenin o anki halinin tıpatıp aynısını oluşturur ama bu yeni liste orijinalinden 'tamamen bağımsızdır'.

-> "Sığ Kopyalama" (Shallow Copy): Listenin içeriğini yeni bir bellek adresine kopyalar. Böylece yeni listede yapacağın bir değişiklik (eleman silme, ekleme, sıralama) orijinal listeyi etkilemez.

Neden yeni_liste = eski_liste Yazmıyoruz? (Kritik Fark)
Eğer .copy() kullanmak yerine sadece eşittir (=) kullanırsan, Python yeni bir liste oluşturmaz; sadece aynı listeye ikinci bir isim verir.

"""

#-------------------------------------------------------------------------------------------------------------------
# 12.del: İndeksi verilen elemanı siler. Pop fonksiyonuna benzer bir fonksiyon olmasına rağmen kullanımı farklıdır .
#-------------------------------------------------------------------------------------------------------------------
donanim = ["yazici","klavye","işlemci","bellek","sabit disk"]
del donanim[2]
print(donanim)

""""
"pop", "remove" ve "del" fonksiyonları silme işlemi yapar. remove fonksiyonunda verilen değer silinirken 
pop ve del fonksiyonlarında verilen indekse göre silme işlemi yapılır. pop ve del fonksiyonlarının yazılışı farklıdır.
"""

liste = ["B","İ","L","Ş","İ","M"]
print(liste)
print("Alfabetik sıralama:", sorted(liste))
print("Listeyi tersten yazdırma", list(reversed(liste)))
print("İ harfi sayısı", liste.count("İ"))
liste.remove("Ş")
print(liste)
liste2=liste.copy()
print(liste2)
liste.clear()
print(liste)
print("L'nin indeksi:", liste2.index("L"))


#------------------------------------------------
# LİSTENİN EN BÜYÜK VE EN KÜÇÜK ELEMANINI BULMA :
#------------------------------------------------
"""
-> Bir listenin en büyük elemanını bulmak için max(), en küçük elemanını bulmak için min() kullanılır.
-> max-min komutları karakter tabanlı listeler üzerinde de işlem yapar. (Yani stringler)
-> Alfabetik sıraya göre listenin en büyük ve en küçük elemanını verir.
"""

liste = [3,5,6,9,8]
b = max(liste)
k = min(liste)
print("Listenin en büyük elemanı:",b,"Listenin en küçük elemanı:",k)

liste = ["zambak","gül","açelya"]
b = max(liste)
k = min(liste)
print("Listenin en büyük elemanı:",b,"Listenin en küçük elemanı:",k)

#Çıktı: Listenin en büyük elemanı: 9 Listenin en küçük elemanı: 3
#Çıktı: Listenin en büyük elemanı: zambak Listenin en küçük elemanı: açelya

#------------------------------------
# LİSTE ELEMANLARI TOPLAMINI BULMA  :
#------------------------------------
liste = [2,4,8,-2,56]
toplam = sum(liste)
print(toplam)

"""
kenksler = ["Ali","Emre","Qusay","Ümit","Baran","Erol","İlker","Eren","Muhammed Furkan","Muhammed Semih","Yusuf","Eren"]
toplam = sum(kenksler)
print(kenksler) #Çıktı : TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

#-------------------
# LİSTE ÜRETEÇLERİ :
#-------------------
"""
-> Liste üreteçleri belirli bir sayı dizilimi ile 'otomatik listeler üretmenin kısa yolunu' sunar.
-> Liste üreteçlerini kullanabilmek için for döngüsüne aşina olmanız gerekmektedir.
-> Liste üreteçleri (list comprehensions), mevcut bir veri yapısından (liste, demet, sözlük veya aralık) yeni bir liste oluşturmak için kullanılan, daha kısa, okunabilir ve genellikle daha hızlı olan bir yazım şeklidir.
"""

liste = [a for a in range(5)]
print(liste)   
#Çıktı: [0, 1, 2, 3, 4]

# Tabi bu kısımı PYTHON 201 dersinde daha detaylı gösterilecektir.


#-------------------------
# İÇ İÇE LİSTE OLUŞTURMA :
#-------------------------

# Burada dikkat edilmesi gereken ikinci listede string şekilde değil fonksiyon şekile çağırmak gerekiyor.
meyveler = ["elma","çilek","armut"]
alisveris_listesi = ["süt","peynir",meyveler]  
print(alisveris_listesi)  #Çıktı : ['süt', 'peynir', ['elma', 'çilek', 'armut']]

# Çünkü meyveleri string yapınca string olarak geliyor. Değişken olarak çağırmak gerekiyor.
bellekler = ["RAM","ROM"]
ekran_kartlari = ["paylaşimli","paylaşımsız"]
sabit_diskler = ["SSD"]
birimler = [bellekler,ekran_kartlari,sabit_diskler]
print(birimler)  #Çıktı: [['RAM', 'ROM'], ['paylaşimli', 'paylaşımsız'], ['SSD']]


#----------------------------------------
# PYTHON LİSTE METOTLARI (LIST METHODS) :
#----------------------------------------

#------------------------------------------------------------------------
#  Metot    | İşlev (Açıklama)                                          |
#------------------------------------------------------------------------
#  append() | Listenin sonuna yeni bir eleman ekler.                    |
#  extend() | Bir listeyi başka bir listeyle birleştirerek genişletir.  |
#  insert() | Belirtilen indeks konumuna eleman yerleştirir.            |
#  remove() | Değeri verilen elemanı listeden siler (İlk eşleşmeyi).    |
#  pop()    | Belirtilen indeksteki elemanı siler ve döndürür.          |
#  clear()  | Listenin tüm elemanlarını temizler (İçini boşaltır).      |
#  index()  | Belirtilen elemanın kaçıncı indekste olduğunu bulur.      |
#  count()  | Listede bir elemandan kaç tane olduğunu sayar.            |
#  sort()   | Elemanları artan sırada (A-Z / 0-9) sıralar.              |
#  reverse()| Listenin mevcut sıralamasını tersine çevirir.             |
#  copy()   | Listenin yepyeni ve bağımsız bir kopyasını oluşturur.     |
#  del      | İndeks numarasına göre elemanı veya dilimi siler.         |
#------------------------------------------------------------------------

# Kalıcı Değişiklik: Yukarıdaki metotların çoğu (sort, reverse, append vb.) listeyi yerinde (in-place) değiştirir.
# Bellek Yönetimi: .copy() kullanımı, orijinal veriyi korumak (Hâl/İlim muhafazası) için kritik öneme sahiptir.


#-------------------
# DEMETLER(TUPLES) :
#-------------------
"""
-> Demetler(tuples), listelere çok benzer ancak tek farkı oluşturulduktan sonra üzerinde ekleme, silme, değiştirme, sıralama gibi işlemler yapılamamasıdır.
-> Python, demetlerin değişmeyeceğini bildiği için belleği (RAM) listelere göre çok daha verimli kullanır.
-> Hız: Demetlerin okunması, listelere göre daha hızlıdır.
-> Eğer bir verinin (örneğin bir köpeğin doğum tarihi veya bir bankanın şube kodu) programın hiçbir yerinde yanlışlıkla değiştirilmesini istemiyorsan, o veriyi Demet içinde saklamalısın. Bu bir "emniyet kemeri"dir.
"""

demet = tuple()                   # Boş bir demet tanımlanır.
demet = ()                        # Boş demet tanımlamanın bir başka yolu
demet = tuple([1,2,3])            # İçerisinde 1,2,3 değerleri olan bir demet tanımlar.
demet = (1,2,3)                   # İçerisinde 1,2,3 değerleri olan demet tanımlamanın bir başka yolu.
demet = ("elma","kiraz","erik")   # String demeti
demet = (1,2,"elma",2.25)         # Farklı türde elemanlardan oluşan bir demet

# ------------------------------------------------------------------------------------------------------------------
#  Özellik           :  Liste (List)                        :  Demet (Tuple)                                       |
#  ------------------: -------------------------------------: ------------------------------------------------------
#  Parantez          :  Köşeli Parantez []                  :  Normal Parantez ()                                  |
#  Değişim (Mantık)  :  Mutable (Değiştirilebilir)          :  Immutable (Sabit/Değişmez)                          |
#  Boyut             :  Dinamik (Artabilir/Azalabilir)      :  Statik (Boyutu sabittir)                            |
#  Hız               :  Daha yavaş (İşlem yükü fazla)       :  Daha hızlı (Hafiftir)                               |
#  Metotlar          :  Çok fazla (append, pop, sort vb.)   :  Çok az (sadece count ve index)                      |
#  Bellek (RAM)      :  Daha çok yer kaplar (Overhead var)  :  Daha az yer kaplar (Tam gerektiği kadar)            |
#  Sözlük Anahtarı   :  Anahtar (Key) OLAMAZ.               :  Anahtar (Key) OLABİLİR (Hashable olduğu için).      |
#  Veri Güvenliği    :  Düşük (Yanlışlıkla değiştirilebilir):  Yüksek (Yazma korumalı / Salt okunur).              |
#  Kullanım Amacı    :  Benzer öğelerin koleksiyonu.        :  Farklı ama ilişkili öğelerin bir yapısı (Record).   |
#  Iteration         :  Daha yavaş döner.                   :  Daha hızlı döner.                                   |
#  Referans Sabitliği:  İçindeki adresler değişebilir.      :  İçindeki adresler asla değiştirilemez.              |
# ------------------------------------------------------------------------------------------------------------------

#--------------------
# 1.Tuple Oluşturma :
#--------------------
birimler = ("bit","inç","byte","hertz","piksel")
print(birimler)

#------------------------------------------------------------------
# 2.Tuple elemanlarına ulaşma:Listelerdeki gibi indeks kullanılır .
#------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
print(birimler[3])  #Çıktı: hertz
print(birimler[-2]) #Çıktı: hertz

demet = (1,2,3)
print(demet[1])     #Çıktı: 2

#---------------------------------------------------------------------------------------------------------------------------------
# 3.İndeks aralığına göre yazdırma:Listelerde olduğu gibi başlangıç ve bitiş indeksleri verilerek istenilen aralık yazdırılabilir .
#---------------------------------------------------------------------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
print(birimler[1:3])    #Çıktı:('inç', 'byte')

#--------------------------------------------------------------------------------------------------------------
# 4.Tuple elemanlarını değiştirme:Tuple veri tipi tanımlanırken elemanların değiştirilmeyeceğinden bahsedildi .
#--------------------------------------------------------------------------------------------------------------

# Eğer tuple veri tipi listeye çevrilirse elemanlar değiştirebilir.
birimler = ("bit","inç","byte","hertz","piksel")
birimler_liste = list(birimler)
birimler_liste[2] = "mega byte" #Çıktı: ['bit', 'inç', 'mega byte', 'hertz', 'piksel']
print(birimler_liste)

#--------------------------------------------------------------------------------------------------------
# 5.Elemanın olup olmadığını sorgulama: Tuple veri tipinde de listelerde de olduğu gibi in operatörü ile
# Bir listede olup olmadığını kontrol edebilir .Eleman tupledaysa True; yoksa false değeri üretir.
#--------------------------------------------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
print("bit" in birimler)

#----------------------------------------------------------------------------
# 6.Tuple uzunluğunu bulma:len fonksiyonu ile tuple'ın eleman sayısı bulunur.
#----------------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
print(len(birimler))

#---------------------------------------------------------------------------------------------------------
# 7.Tuple içinde bir elemanın sayısını bulma: Bu işlem listelerde olduğu gibi count fonksiyonu kullanılır.
#---------------------------------------------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
say = birimler.count("bit")
print(say)

#----------------------------------------------------------------------------------------------------------------
# 8.Tuple içindeki bir elemanın sayısını bulma: Bu işlem için listelerde olduğu gibi index fonksiyonu kullanılır.
#----------------------------------------------------------------------------------------------------------------
birimler = ("bit","inç","byte","hertz","piksel")
print(birimler.index("byte"))

# Önemli Uyarı: Tek elemanlı bir demet tanımlarken elemanın sonuna virgül koymak zorunludur. tekli = (50) -> Bu bir sayıdır (integer). tekli = (50,) -> Bu bir demettir.

#-------------------------------------------------------------------------------------
# 9.Tuple birleştirme: Birden fazla tuple birleştirerek tek bir tuple'da toplanabilir.
#-------------------------------------------------------------------------------------
"""
-> Demetlerde (tuples) .extend() metodu bulunmaz. Bunun sebebi demetlerin "Immutable" (Değiştirilemez) olmasıdır. 
-> .extend() metodu mevcut bir listeyi kalıcı olarak büyütür ve içeriğini değiştirir. Oysa bir demet oluşturulduktan sonra onun içeriğine müdahale edilemez.
Peki, birleştirme işlemi nasıl gerçekleşir?

1. + Operatörü (Toplama) :
--------------------------
-> Senin örneğinde kullandığın birlestir = birimler + degerler yöntemi aslında mevcut demetleri değiştirmez. 
-> Python arka planda şu işlemi yapar:
-> Birimler demetini okur. Degerler demetini okur. Hafızada (RAM) yepyeni bir üçüncü demet oluşturur ve her ikisinin elemanlarını oraya kopyalar.
-> Orijinal birimler ve degerler demetleri oldukları gibi kalır.

2. Neden .extend() yok? :
-------------------------
Listeler: Esnektir. Mevcut listenin sonuna yeni elemanlar ekleyebilir, listeyi uzatabilirler. Bu yüzden .extend() ve .append() metotlarına sahiptirler.

Demetler: Sabittir. Mevcut bir demeti "uzatamazsınız". Ancak toplama işlemi yaparak yeni bir demet "yaratabilirsiniz".
"""
birimler = ("bit","inç","byte","hertz","piksel")
degerler = (8,256,1024)
birlestir = birimler + degerler
print(birlestir)    #Çıktı: ('bit', 'inç', 'byte', 'hertz', 'piksel', 8, 256, 1024)

#---------------------
# 10.DEMET PARÇALAMA :
#---------------------
demet= (50,60,70,80,90)
print(demet[1:4])   #Çıktı: (60, 70, 80) "Bitiş indeksi (90) dahil değildir, yani 1, 2 ve 3. indeksleri alır."

#--------------------------------------------------
# 11.Demetin en büyük ve en küçük elemanını bulma :
#--------------------------------------------------
"""
-> Demetin en büyük elemanı max ile en küçük elemanı min ile bulunur.
"""

demet = (20,30,40,10,50)
b = max(demet)
k = min(demet)
print("En büyük eleman:", b, "En küçük eleman:", k)

#-----------------------------------------
# 12.Demet elemanlarının toplamını bulma :
#-----------------------------------------
demet = (20,30,40,10,50)
toplam = sum(demet)
print(toplam)  #Çıktı : 150
"""
demet.remove(20)  #AttributeError: 'tuple' object has no attribute 'remove' -> Burada tuple veri tipinin değiştirilmeye kapalı olduğunu gösteriyor.
"""

# =======================================================================================
# == BAB 8: KOLEKSİYONLAR-1 PROJELERİ:(COLLECTIONS-1 PROJECTS)(LİSTELER VE DEMETLER) : ==
# =======================================================================================

#----------------------------------------------------------
# ÖRNEK 1: Liste halinde verilen arabalar ile işlem yapma :
#----------------------------------------------------------
"""
1-BMW, Dodge Viper, Aston Martin, Lamborghini, Corvette, Mercedes, Ford Mustang, Mitsubishi, Porsche, Toyota, Lexus, Volkswagen, Golf elemanlarına sahip bir liste oluşturunuz.
"""
araba_listesi = ["BMW","Dodge","Viper","Aston Martin","Lamborghini","Corvette","Mercedes","Ford Mustang","Mitsubishi","Porsche","Toyota","Lexus","Volkswagen", "Golf"]

"""
2-Liste kaç elemanlıdır ?
"""
liste_eleman_sayisi = len(araba_listesi)
print(liste_eleman_sayisi)

"""
3-Listenin ilk ve son elemanı nedir ?
"""
listenin_ilk_elemani = araba_listesi[0]
liste_son_elemani = araba_listesi[-1]
print(listenin_ilk_elemani)
print(liste_son_elemani)

"""
4-Toyota yerine Audi ile değiştirin.
"""
araba_listesi[10] = "Audi"
print(araba_listesi)

"""
5-BMW listenin bir elemanı mıdır ?
"""
elemani_mi="BMW" in araba_listesi
print(elemani_mi)

"""
6-Listenin -1 indeksindeki değeri yazdır ?
"""
son_indeks=araba_listesi[-1]
print(son_indeks)

"""
7-Listenin ilk 2 elemanını alın.
"""
sonuc=araba_listesi[0:2]
sonuc=araba_listesi[:2]

"""
8-Listenin son 2 elemanı yerine "Şahin" ve "Murat131" yaz.
"""
araba_listesi[-2:] = ["Şahin","Murat131"]
print(araba_listesi)

"""
9-Listeye Tofaş ekleyin.
"""
araba_listesi.append("Tofaş")
print(araba_listesi)

"""
10-Liste elemanlarını tersten yazdır.
"""
araba_listesi[::-1]  # Bu ifade ekrana yazdırır ama kalıcı değildir. Sonra silinir. Eğer kalıcı olması isteniyorsa bir değişkene atanmalı! 
print(araba_listesi)

araba_listesi_ters=araba_listesi[::-1]

#------------------------------
# ÖRNEK 2: Sınav Notu Analizi :
#------------------------------
notlar = [85,42,90,42,76,100,55,42]

# 1. Kaç tane 42 notu var? (Count)
kırk_iki_sayisi = notlar.count(42)
print(f"42 alan öğrenci sayısı:{kırk_iki_sayisi}")

# 2. Büyükten küçüğe sırala
notlar.sort(reverse=True)
print(f"Sıralı Azalan Notlar:{notlar}")

# 3. En yüksek ve en düşük notlar
en_yuksek = max(notlar)
en_dusuk = min(notlar)
print(f"En yüksek not: {en_yuksek}, En düşük not: {en_dusuk}")

liste=[1,2,3,4,5]
for i in liste:
    print(i)


index = 0
while (index<len(liste)) :
    print("İndex:",index,"Liste Elemanı:",liste[index])
    index +=1

#-------------------------------------------------
# ÖRNEK 3 : for Döngüsü  ile Listelerde Gezinmek :
#-------------------------------------------------

liste = [1,2,3,4,5,6,7]
for eleman in liste:
    print("Eleman",eleman)

toplam = 0
liste = [1,2,3,4,5,6,7]
for eleman in liste:
    toplam = toplam+eleman
    print("Toplam:{} Eleman: {}".format(toplam,eleman))
    print(toplam) 

liste = [1,2,3,4,34,54,63,78]
for eleman in liste:
    if eleman %2==0:
        print(eleman)

s = "Python"
for i in s:
    print(i)

s = "Python"
for i in s:
    print(i*3)    


#-------------------------------------------------
# ÖRNEK 4 : Demetler Üzerinde Döngü ile Gezinmek :
#-------------------------------------------------

demet = (1,2,3,4,5)
for a in demet:
    print(a)

liste = [(1,2),(3,4),(5,6),(7,8)]
for eleman in liste:
    print(eleman)

for (i,j) in liste:
    print(f"i:{i} j:{j}")

liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print(i*j*k)


#------------------------------------------------------
# ÖRNEK 5: while Döngüsü ile Liste Üzerinde  Gezinmek :
#------------------------------------------------------
liste = [1,2,3,4,5]
index = 0
while (index < len(liste)):
    print("index:",index,"Liste Elemanı:",liste[index])
    index +=1


# =======================================================================================================================================================================
"""
 "Elhamdülillah, 8.Bab ile veriyi 'nizam' (koleksiyon) altına almanın ilmine vakıf olduk. "
 "Dağınık değişkenlerin karmaşasından kurtulup, verileri birer 'Demet' ve 'Liste' halinde organize ederek Amel-i Salih yolunda kodlarımızı daha ölçeklenebilir kıldık."
 "Veri deryasını 5 temel düğümle (örnekle) zapt ederek, dağınıklığı düzene kurban ettik."
"""
# =======================================================================================================================================================================
#  BAB 8: KOLEKSİYONLAR-1 (LİSTELER VE DEMETLER) PROJE LİSTESİ :                                                                                                        |
# =======================================================================================================================================================================
#  ÖRNEK 1 : Otomobil Envanter Yönetimi (Liste Oluşturma, Güncelleme ve Dilimleme)                                                                                      |
#  ÖRNEK 2 : Sınav Notu Analizi (Count, Sort, Max-Min ve Ortalama Hesaplama)                                                                                            |
#  ÖRNEK 3 : For Döngüsü ile Listelerde Gezinmek (Toplu Veri İşleme)                                                                                                    |
#  ÖRNEK 4 : Demetler Üzerinde Döngü ve Unpacking (Demet Parçalama Tekniği)                                                                                             |    
#  ÖRNEK 5 : While Döngüsü ile Dinamik Liste İndeks Kontrolü                                                                                                            |
# =======================================================================================================================================================================

