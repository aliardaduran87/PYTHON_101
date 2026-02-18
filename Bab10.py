# ====================================================
# == BAB 10: FONKSİYONLAR (CHAPTER 10: FUNCTIONS) : ==
# ====================================================

#----------------------------------------------
# 1. FONKSİYON KAVRAMI VE MODÜLER PROGRAMLAMA :
#----------------------------------------------
"""
-> Anlam olarak bakıldığında fonksiyon kelimesi yerine getirilen bir işi, bir görevi ifade eder.
-> Programlama dilleri için de yerine getirilen bir iş ya da görevi temsil eden komutlar fonksiyon olarak anılır.
-> Fonksiyonlar bir program içerisinde yer alan alt program parçalarıdır. 
-> Her bir fonksiyonun içerisinde belirli bir işi yerine getirecek şekilde yazılmış birden çok kod satırı yer alır.
-> Yani fonksiyonlar iş yapan komut dizilerinin paketlenmiş halidir.
-> Fonksiyonları büyük bir organizasyon içinde yer alan birimlere benzetebiliriz.
-> Bir şirketin personel, yazı işleri ve muhasebe birimleri gibi bağımsız alt organizasyonlar kurmaktır.


#--------------------------------
# FONKSİYONLARIN TEMEL AMAÇLARI : 
#--------------------------------

---------------------------------------------------
 1. Kodun Tekrar Kullanılabilirliği (Reusability) :
---------------------------------------------------
-> "Bir kere yaz, her yerde kullan." Fonksiyonların en büyük amacı budur.,
-> Aynı işlemi programın farklı yerlerinde yapman gerekiyorsa, kodu her seferinde kopyalayıp yapıştırmak yerine bir fonksiyon içine koyarsın ve sadece ismini çağırırsın.
-> Faydası: Zaman kazandırır ve kod kalabalığını önler.


--------------------------------------
 2. Karmaşıklığı Bölmek (Modularity) :
--------------------------------------
-> Büyük bir problem, tek bir parça halinde çözülemeyecek kadar karmaşık olabilir. Fonksiyonlar, bu büyük problemi küçük, yönetilebilir ve anlaşılır parçalara ayırmanı sağlar.
-> Faydası: Bir sorun çıktığında, tüm kodu değil sadece ilgili fonksiyonu kontrol edersin.

-----------------------------
 3. Soyutlama (Abstraction) :
-----------------------------
-> Soyutlama, bir işlemin arka plandaki tüm karmaşık teknik detaylarını gizleyerek, size sadece ihtiyacınız olan "ne yapıyor?" kısmını sunan bir sadeleştirme sanatıdır.
-> Bir fonksiyonu kullanırken, onun içinde ne olduğunu bilmene gerek yoktur; sadece ne iş yaptığını bilmen yeterlidir. 
-> Örnek: print() fonksiyonunun bilgisayar ekranına o karakterleri nasıl gönderdiğini, pikselleri nasıl yaktığını bilmezsin. Sadece içine veri yazarsın ve o işini yapar.
-> Faydası: Zihinsel yükü azaltır, 'ana mantığa odaklanmanı sağlar'.

----------------------------
 4. Okunabilirlik ve Düzen :
----------------------------
-> Fonksiyon isimleri, kodun ne yaptığını anlatan etiketler gibidir. İyi isimlendirilmiş fonksiyonlarla yazılmış bir kod, bir hikaye gibi okunabilir.
-> Örnek: veriyi_temizle(), sonucu_kaydet(), kullaniciyi_dogrula() gibi isimler, kodun akışını anında anlamanı sağlar.
-> Özetle: Fonksiyonlar Birer "Fabrika" Gibidir
-> Fonksiyonları küçük birer fabrika makinesi gibi düşünebilirsin:

-> Girdi (Input): Ham maddeyi verirsin.
-> İşlem: Makine (fonksiyon) içeride bir şeyler yapar.
-> Çıktı (Output): Sana bitmiş ürünü teslim eder.

DRY Prensibi: Yazılımcılar arasında çok popüler olan "Don't Repeat Yourself" (Kendini Tekrar Etme) kuralı, tamamen fonksiyonların bu amaçları üzerine kuruludur.


#---------------------------
# Örnek Hazır Fonksiyonlar :
#---------------------------
# print(): "ekrana veri yazma işini" yerine getirir.
# input(): "ekrandan veri okuma görevini" yerine getirir.
"""

#-------------------------------
# 2. FONKSİYON ÇALIŞMA MANTIĞI :
#-------------------------------
""" 
-> Fonksiyonlar, karmaşık kod yığınlarının bir yerde tanımlanarak birden çok kez kullanılmasını sağlar.
-> Örneğin print() fonksiyonu, ekrandaki pikselleri yönetmek gibi son derece karmaşık bir işlemi "print" ismiyle basitçe çağırmamızı sağlar.
-> Fonksiyon çağrıları komut isminden sonra gelen ( ) sembolleri ile yapılır.
-> Parantez içerisindeki verilere 'argüman' veya 'parametre' denir.
-> Parametre, bir fonksiyonun görevini yerine getirebilmesi için dışarıdan beklediği bilgi veya girdidir.
-> Fonksiyonlar yerine getirdikleri işe göre parametreli veya  parametresiz olabilirler.
"""


# -------------------------------------
# 3. FONKSİYON TANIMLAMA (DEFINITION) :
# -------------------------------------
"""
-> Fonksiyon tanımlamaları "def" anahtar sözcüğü ile başlar.
-> İsim verilirken değişken adlandırma kurallarına dikkat edilmelidir.
-> Python dünyasında fonksiyon tanımlarken kullanılan standart notasyon snake_case (yılan stili) notasyonudur. (BU ÖNEMLİ !)
-> Python'un resmi stil rehberi olan PEP 8, fonksiyon isimlerinin küçük harflerden oluşmasını ve kelimelerin birbirine alt çizgi (_) ile bağlanmasını tavsiye eder.

# Ana Şablon:
# def fonksiyon_ismi(varsa parametre-ler):
#     fonksiyona ait kodlar

# Örnek 3.1: Parametresiz Fonksiyon Tanımı
def mesajyaz():
    print("merhaba")

-> print("merhaba", "python", "programlama") # 3 parametreli kullanım.

"""
#------------------------------------------------
# 4. PARAMETRELİ FONKSİYONLAR VE KAPSAM (SCOPE) :
#------------------------------------------------
# Örnek : İki sayının toplamını ekrana yazan fonksiyonu yazdırın. 
def topla(a,b):
    sonuc=a+b
    print(sonuc)

# Kritik Not:
# - a, b ve sonuc değişkenleri sadece fonksiyon içerisinden erişilebilir.
# - Fonksiyon dışından bu değişkenlere erişmek mümkün değildir.
# - Fonksiyonlar çağrılmadıkları sürece herhangi bir şey yazmazlar.

#---------------------------------
# 5. FONKSİYON ÇAĞRIMI (CALLING) :
#---------------------------------
# Fonksiyonu çalıştırmak için ismini yazıp parantezlerini kullanmak gerekir.

# Örnek 5.1: Parametresiz Çağrım
def mesajYaz():
    print("Merhaba")
mesajYaz() 

# Örnek 5.2: Parametreli Çağrımlar
topla(3, 5)   # a=3, b=5 aktarılır -> Çıktı: 8
topla(10, 15) # Çıktı: 25
topla(80, 90) # Çıktı: 170

# Önemli: Her çağrım bellekte yeni ve bağımsız bir kopya oluşturur.
# Fonksiyon bittiğinde program kaldığı yerden devam eder.


# ===========================================================================================
# == FONKSİYON MUKAYESE TABLOSU (PARAMETRELİ VS PARAMETRESİZ)                              ==
# ===========================================================================================
# -------------------------------------------------------------------------------------------
#  ÖZELLİK          | PARAMETRESİZ FONKSİYON           | PARAMETRELİ FONKSİYON              |
# -------------------------------------------------------------------------------------------
#  Girdi (Input)    | Dışarıdan hammadde almaz.        | Dışarıdan veri (argüman) bekler.   |
#  Esneklik         | Sabittir, hep aynı sonucu verir. | Dinamiktir, veriye göre değişir.   |
#  Çağrım Şekli     | fonksiyon()                      | fonksiyon(sayi1, sayi2)            |
#  Hammadde Kaynağı | Sadece kendi içindeki veriler.   | Dışarıdan "fırlatılan" veriler.    |
#  Scope (Kapsam)   | Değişkenler içeride tanımlanır.  | Parametreler dışarıdan atanır.     |
#  Hata Riski       | Argüman hatası verme ihtimali yok| Eksik veri gönderilirse hata verir.|
#  Temel Görevi     | Standart rutinleri icra eder.    | Gelen veriyi işleyip sonuç üretir. |
# -------------------------------------------------------------------------------------------

# ÖRNEK KARŞILAŞTIRMA:

# 1. Parametresiz: Her çağrıldığında sadece "Merhaba" yazar.
def selamla():
    print("Merhaba")

# 2. Parametreli: Kimin ismi gelirse onu selamlar.
def isme_ozel_selamla(isim):
    print("Merhaba", isim)


#--------------------------------------------------
# 6. FONKSİYONUN GERİYE DEĞER DÖNDÜRMESİ (RETURN) :
#--------------------------------------------------
# "return" anahtar sözcüğü, fonksiyonun ürettiği sonucun çağrılan yere gönderilmesini sağlar.
def topla_return(a, b):
    sonuc = a + b
    return sonuc

# Kullanımı:
islem = topla_return(5, 10) # 15 değeri islem değişkenine aktarılır.
print(islem)

#----------------------------------
# 7. RETURN DEYİMİNİN ÖZELLİKLERİ :
#----------------------------------
# 7.1. Sonlandırma:
# Return ifadesi çalıştığı anda fonksiyon sonlanır; altındaki kodlar çalışmaz.
def topla_sonlandirma(a, b):
    sonuc = a + b
    return sonuc
    print("Bu satır asla çalışmaz!") 

# 7.2. Birden Çok Değer Geri Döndürme:
# Python'da virgül kullanarak birden çok ara sonuç döndürülebilir.
def IkiIslem(a, b):
    toplam = a + b
    carpim = a * b
    return toplam, carpim

k1, k2 = IkiIslem(3, 5) # k1=8, k2=15.

#-------------------------------------
# 8. VARSAYILAN DEĞERLİ PARAMETRELER :
#-------------------------------------
# Eksik argüman gönderildiğinde hata (TypeError) almamak için kullanılır.
# Hata Örneği: MesajYaz("merhaba") -> adet eksik olduğu için hata verir.

# Örnek 8.1: Varsayılan değer verme (adet=1)
def MesajYaz(mesaj, adet=1):
    for i in range(adet):
        print(mesaj)

MesajYaz("merhaba")    # 1 kez yazar.
MesajYaz("merhaba", 3) # 3 kez yazar.

# !!! KRİTİK KURAL !!!
# Varsayılan değerli bir parametreyi, varsayılanı olmayan bir parametre takip edemez.
# def Hata(mesaj="merhaba", adet): # SyntaxError verir.

# DOĞRU: Mecburi olan (isim) önce, yedekli olan (sehir) sonra.
def kayit_yap(isim, sehir="Konya"):
    print(f"İsim: {isim}, Şehir: {sehir}")

# Kullanım:
kayit_yap("Ahmet")              #ÇIKTI: Ahmet, Konya (Yedeği kullandı)
kayit_yap("Mehmet", "Ankara")   #ÇIKTI: Mehmet, Ankara (Senin verdiğini kullandı)


#---------------------------------------------
# 9. İSİMSİZ (SIRALI) VE İSİMLİ PARAMETRELER :
#---------------------------------------------
def sekilCiz(karakter, satir_sayisi, sutunsayisi):
    for i in range(satir_sayisi):
        print(karakter * sutunsayisi)

# 9.1. İsimsiz (Sıralı) Çağrım:
sekilCiz("*", 5, 7) # Tam sıraya göre gönderilmelidir.

# 9.2. İsimli (Keyword) Çağrım:
sekilCiz(satir_sayisi=5, sutunsayisi=7, karakter="*") # Sıra önemsizdir.

# 9.3. Karma Kullanım:
# Kural: İsimsiz parametreler önce, isimli parametreler sonra gelmelidir.
sekilCiz("*", 5, sutunsayisi=7) # Doğru kullanım.

#----------------------------------------------------------
# 10. DEĞİŞKEN SAYIDA PARAMETRE ALAN FONKSİYONLAR (*args) :
#----------------------------------------------------------
# Parametre isminin başına "*" konursa, gelen tüm argümanlar bir 'tuple' olarak tutulur.

def topla_esnek(*sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc = sonuc + i
    return sonuc

# Çağrımlar:
# topla_esnek(5, 10)
# topla_esnek(2, 8, 12, 20, 25, 50)
# İster 0, ister 1, ister 1000 tane sayı gönder; hata vermez.

#----------------------------------------------------
# 11. FONKSİYONLARLA İLGİLİ 10 GENEL ÖZELLİK (Özet) :
#----------------------------------------------------
# 1. Belirli bir iş sürecini barındıran paketlerdir.
# 2. ( ) sembolü parametre parantezi olarak adlandırılır.
# 3. Parametreli veya parametresiz olabilirler.
# 4. Yerel değişkenler sadece fonksiyon içinde geçerlidir.
# 5. Çağrıldıkları satırdan önce tanımlanmış olmalıdırlar.
# 6. 'return' kullananlara değer döndüren fonksiyon denir.
# 7. Bir fonksiyon birden fazla değeri döndürebilir.
# 8. Varsayılanı olmayan parametrelere değer aktarımı zorunludur.
# 9. Varsayılan değerli bir parametreden sonra boş parametre gelemez.
# 10. Argümanlar sıralı (isimsiz) veya isimli olarak aktarılabilir.

#--------------------------------------------------
# 12. ÖZYİNELİ FONKSİYONLAR (RECURSIVE FUNCTIONS) :
#--------------------------------------------------
# Belirli algoritmalar kendi içerisinde kendini tekrar eder.

# Örnek 12.1: Faktöriyel Hesabı (Iterative/Döngü ile)
def defFaktoriyel_Iterative(sayi):
    carpim = 1
    for i in range(sayi, 1, -1):
        carpim = carpim * i
    return carpim

# Örnek 12.2: Faktöriyel Hesabı (Recursive/Özyineli)
def Faktoriyel(sayi):
    if sayi <= 1: # Bitiş koşulu
        return 1
    return sayi * Faktoriyel(sayi - 1)

# Örnek 12.3: Fibonacci Serisi
# 1 1 2 3 5 8 13 21 34 55 ...
def Fibonacci(sirano):
    if sirano == 1 or sirano == 2:
        return 1
    return Fibonacci(sirano - 1) + Fibonacci(sirano - 2)


# =========================================================================================
# == ANALİZ: METOT (METHOD) NEDİR? NEDEN KULLANILIR?                                     ==
# =========================================================================================
# -----------------------------------------------------------------------------------------
#  SORU             | CEVAP VE MANTIK                                                     |
# -----------------------------------------------------------------------------------------
#  Nedir?           | Bir nesneye (object) veya veri tipine bağlı olan fonksiyonlardır.   |
#  Farkı Nedir?     | Fonksiyonlar özgürdür (print), metotlar birine aittir (s.upper).    |
#  Neden Kullanılır?| Veri üzerinde o veriye has işlemleri hızlıca yapmak için kullanılır.|
#  Ne İşe Yarar?    | Kodun okunabilirliğini artırır ve veriyi kolayca manipüle eder.     |
# -----------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
#  GÖRSEL KARŞILAŞTIRMA (FONKSİYON VS METOT)                                               |
# ------------------------------------------------------------------------------------------
#  Fonksiyon: topla(a, b)      --> Bağımsızdır, herkes çağırabilir.                        |
#  Metot:     metin.upper()    --> "metin" değişkenine muhtaçtır, nokta (.) ile çağrılır.  |
# ------------------------------------------------------------------------------------------

# GERÇEK HAYAT BENZETMESİ:
# Fonksiyon: Bir çekiç gibidir. Masanın üstünde durur, herkes her şeyi çivilemek için alır.
# Metot: Bir arabanın "Klima Açma" düğmesi gibidir. Arabaya aittir, araba olmadan çalışmaz.
# =========================================================================================

"""
-> Metot yapısı, Türkçedeki 'Belirtili İsim Tamlaması' mantığıyla birebir örtüşür.
-> Nasıl ki tamlanan (kliması), tamlayana (araba) aitse ve ona bağlıysa; metot da (upper) çağrıldığı nesneye (metin) sıkı sıkıya bağlıdır.
-> Bu sahiplik ilişkisi gereği metotlar, bağlı oldukları nesnenin "yeteneklerini" ve "özelliklerini" temsil ederler.
-> Özetle: Nesne tamlayan, metot ise o nesneye ait olan tamlanandır.
   Örn: "Arabanın kliması" -> araba.klima_ac()
"""

#------------------------------------------------------
# 13. PYTHON DİLİNE AİT HAZIR (BUILT-IN) FONKSİYONLAR :
#------------------------------------------------------
import math     # Modül dahil edilmelidir.

# MATEMATİKSEL FONKSİYONLAR :

# ------------------------------------------------
# MUTLAK DEĞER FONKSİYONLARI (abs vs. math.fabs) :
# ------------------------------------------------
"""
-> Mutlak değer  herhangi bir sayının 0'a olan uzaklığını verir. Daima  pozitif bir değer sonucu çıkar.
-> Herhangi bir sayının mutlak değerini bulmak için fabs() fonksiyonu kullanılır.
-> Mutlak değerin ingilizce karşılığı "Absolute Value" kelimesinin karşılığından üretilmiştir.
-> Ama abs ile fabs fonksiyonları arasında da teknik bir farklar vardır . Aşağıdaki tabloda verilmiştir.
"""

# 1. abs(x) 
#   -> Python'ın yerleşik (built-in) fonksiyonudur.
#   -> Herhangi bir "import" işlemi gerektirmez.
#   -> Girilen sayının tipini korur (int ise int, float ise float döner).
#   -> Karmaşık (complex) sayılarla çalışabilir.

# 2. math.fabs(x) 
#   -> "math" modülüne ait bir fonksiyondur.
#   -> Kullanmak için "import math" yazmak zorunludur.
#   -> Sonuç her zaman "float" (ondalıklı) döner.
#   -> Karmaşık sayılarda hata verir (sadece reel sayılar içindir).

# ------------------------------------------------------------
#  abs() ve math.fabs() FONKSİYONU TABLO KARŞILAŞTIRMASI :   |
# ------------------------------------------------------------
# | Özellik         | abs(x)             | math.fabs(x)      |
# |-----------------|--------------------|-------------------|
# | Kütüphane       | Yerleşik (Built-in)| math modülü       |
# | Dönüş Tipi      | Esnek (int/float)  | Her zaman float   |
# | Karmaşık Sayı   | Destekler          | Desteklemez       |
# ------------------------------------------------------------

a_fabs = math.fabs(-2)      # float: 2.0
a_abs = abs(-2)             # int: 2


sayi_int = -10
sayi_float = -10.5
sayi_complex = 3 + 4j

# abs() Kullanımı:
print(abs(sayi_int))      #Çıktı: 10     (int olarak kaldı)
print(abs(sayi_float))    #Çıktı: 10.5   (float olarak kaldı)
print(abs(sayi_complex))  #Çıktı: 5.0    (Vektörel uzunluk/Magnitüd)

# math.fabs() Kullanımı:
print(math.fabs(sayi_int))   #Çıktı: 10.0   (float'a dönüştürdü!)
print(math.fabs(sayi_float)) #Çıktı: 10.5   (zaten float'tı)
# print(math.fabs(sayi_complex)) # <-- BU SATIR HATA VERİR (TypeError)

#---------------------------
# SAYI YUVARLAMA İŞLEMLERİ :
#---------------------------
import math
"""
-> Ondalıklı kısımları bulunan sayıları tam sayıya yuvarlamak için ceil() ve floor() fonksiyonları kullanılır.

-> İngilizcede "ceiling" (tavan) kelimesinin kısaltılmışı olan ceil, sayının ondalıklı kısmı sıfırdan farklı ise sayıyı DAİMA bir üst tam sayıya yuvarlar.

-> "floor" (taban) ise ondalıklı kısmı ne olursa olsun sayıyı alt tam sayıya yuvarlar.
"""

# --- 1. Uygulamalı Örnekler ---
a_tavan = math.ceil(2.015)      #Çıktı: 3 (Tavan)
a_taban = math.floor(2.456)     #Çıktı: 2 (Taban)

a_round1 = round(2.51)          # Yakın tam sayıya-> Çıktı:3
a_round2 = round(2.49)          # Yakın tam sayıya-> Çıktı:2

#----------------------------------------------------------------------------------
# | Fonksiyon      | Giriş (2.1) | Giriş (2.9) | Temel Görevi                     |
# |----------------|-------------|-------------|----------------------------------|
# | math.ceil()    | 3           | 3           | Daima Yukarı (Tavan)             |
# | math.floor()   | 2           | 2           | Daima Aşağı (Taban)              |
# | round()        | 2           | 3           | En Yakın (0.5 sınırına bakar)    |
# | int()          | 2           | 2           | Ondalığı Atar (Keser)            |
#----------------------------------------------------------------------------------

# --- 3. Kritik Not: Banker's Rounding (Bankacı Yuvarlaması) ---
# Python'da round() fonksiyonu tam .5 olan durumlarda en yakın ÇİFT sayıya gider.
# Örnek:
print(round(2.5)) # Sonuç: 2 (Çünkü 2 çifttir)
print(round(3.5)) # Sonuç: 4 (Çünkü 4 çifttir)


# --- 4. Negatif Sayılarda Durum (Sayı Doğrusu Mantığı) ---
# Negatiflerde 'yukarı' demek sıfıra yaklaşmak demektir.
negatif_ceil = math.ceil(-2.9)      # Sonuç: -2
negatif_floor = math.floor(-2.1)    # Sonuç: -3


import math

#----------------
# ÜS VE KAREKÖK :
#----------------
"""
-> math.pow(x, y) fonksiyonu, x sayısının y. kuvvetini hesaplar.
-> math.sqrt(x) fonksiyonu, bir sayının karekökünü (1/2. kuvveti) verir.
"""

# --- 1. Uygulamalı Örnekler ---
a_pow = math.pow(3, 2)              #Çıktı: 9.0 (Daima float)
a_pow_frac = math.pow(27, 1/3)      #Çıktı: 3.0 (Küp kök hesabı)
a_sqrt = math.sqrt(25)              #Çıktı: 5.0 (Karekök)

#----------------------------------------------------------------------------------
# | Yöntem           | Örnek         | Sonuç Tipi | Not                           |
# |------------------|---------------|------------|-------------------------------|
# | x ** y           | 3 ** 2        | int/float  | Operatör (Daha hızlıdır)      |
# | math.pow(x, y)   | math.pow(3, 2)| Daima float| Fonksiyon (Standart çıktı)    |
# | math.sqrt(x)     | math.sqrt(25) | Daima float| Karekök için özel fonksiyon   |
# | x ** 0.5         | 25 ** 0.5     | float      | Karekökün operatör hali       |
#----------------------------------------------------------------------------------

# --- 3. Kritik Not: math.pow() vs (**) Operatörü ---
# Python'daki ** operatörü, tam sayılarla çalışırken tam sayı döner; 
# ancak math.pow() her zaman float (ondalıklı) değer döndürür.
print(3 ** 2)          #Çıktı: 9 (int)
print(math.pow(3, 2))  #Çıktı: 9.0 (float)

# --- 4. Gelişmiş Köklü Sayı Hesapları ---
# Herhangi bir kök derecesini (n), 1/n şeklinde üs alarak bulabiliriz:
# 5. dereceden kök 32:
kok_bes = math.pow(32, 1/5) #Çıktı: 2.0


#----------------------------
# LOGARİTMA VE TRİGONOMETRİ :
#----------------------------
"""
-> math.log(sayi, taban): Belirtilen tabanda logaritma hesaplar. 
   Eğer taban yazılmazsa "e" tabanında (ln) hesap yapar.
-> Trigonometrik fonksiyonlar (sin, cos, tan) RADYAN cinsinden değer bekler.
-> math.radians(derece): Dereceyi radyana çevirir. 
   Formül: Radyan = (Derece * pi) / 180
"""
# --- 1. Uygulamalı Örnekler ---

# Logaritma:
log_sonucu = math.log(1000, 10)
print(log_sonucu)                   #Çıktı: 3.0

# Dereceden Radyana Geçiş:
aci_derece = 30
aci_rad = math.radians(aci_derece)  #Çıktı: 0.5235987755982989

# Trigonometrik Hesaplamalar:
sin_degeri = math.sin(aci_rad)      #Çıktı: 0.49999999999999994 (Yaklaşık 0.5)
cos_degeri = math.cos(aci_rad)      #Çıktı: 0.8660254037844387
tan_degeri = math.tan(aci_rad)      #Çıktı: 0.5773502691896257

#-------------------------------------------------------------------------------------------
# | Fonksiyon        | Kullanım Amacı                   | Dikkat Edilmesi Gereken          |
# |------------------|----------------------------------|----------------------------------|
# | math.log(x, b)   | x'in b tabanında logaritması     | b yazılmazsa doğal logaritma (ln)|
# | math.log10(x)    | 10 tabanında kısa yol            | math.log(x, 10) ile aynıdır      |
# | math.radians(d)  | Dereceyi Radyana çevirir         | sin/cos/tan için zorunludur      |
# | math.degrees(r)  | Radyanı Dereceye çevirir         | Sonucu anlamlandırmak için       |
#-------------------------------------------------------------------------------------------

# --- 3. Kritik Notlar ---

# Not 1: Neden doğrudan sin(30) yazmıyoruz?
# Çünkü math.sin(30) yazarsan Python bunu "30 radyan" olarak algılar ve yanlış sonuç verir.
yanlis_hesap = math.sin(30) 
# Çıktı: -0.9880... (İstenen bu değil!)

# Not 2: Sabit Sayılar
print(math.pi)  # Çıktı: 3.141592653589793
print(math.e)   # Çıktı: 2.718281828459045


#--------------------------------------------------
# 1. EN BÜYÜK, EN KÜÇÜK VE TOPLAM (MAX, MIN, SUM) :
#--------------------------------------------------
"""
-> max(): Bir liste veya değişken grubu içindeki EN BÜYÜK değeri bulur.
-> min(): Bir liste veya değişken grubu içindeki EN KÜÇÜK değeri bulur.
-> sum(): Bir liste içindeki tüm sayıların TOPLAMINI hesaplar.
"""

sayi_listesi = [10, 20, 5, 45, 30]

en_buyuk_sayi = max(sayi_listesi)       #Çıktı: 45
en_kucuk_sayi = min(sayi_listesi)       #Çıktı: 5
sayilarin_toplami = sum(sayi_listesi)   #Çıktı: 110

# Doğrudan virgülle ayrılmış sayılarla da kullanılabilir:
en_buyuk_tekil = max(100, 250, 85)      #Çıktı: 250


#-----------------------------
# 2. BÖLÜM VE KALAN (DIVMOD) :
#-----------------------------
"""
-> divmod(sayi1, sayi2): İki sayıyı birbirine böler.
-> Sonuç olarak hem BÖLÜMÜ hem de KALANI bir demet (tuple) olarak döner.
-> Örnek kullanım: (bölüm, kalan)
"""

bolum_ve_kalan = divmod(17, 3)          #Çıktı: (5, 2)
# Burada 17'nin 3'e bölümü 5, kalanı ise 2'dir.


#----------------------------------
# 3. İKİLİ TABAN DÖNÜŞTÜRME (BIN) :
#----------------------------------
"""
-> bin(sayi): Tam sayıyı ikilik (binary) tabandaki karşılığına çevirir.
-> Sonucun başındaki '0b' takısı, sayının BINARY olduğunu belirtir.
"""

ikilik_taban_karsiligi = bin(10)        #Çıktı: '0b1010'
ikilik_taban_karsiligi_8bit = bin(255)  #Çıktı: '0b11111111'

#--------------------------------------------------------------------------
# TEKNİK ÖZET TABLOSU                                                     |
#--------------------------------------------------------------------------
# | Fonksiyon      | Kullanım Amacı                   | Dönüş Tipi        |
# |----------------|----------------------------------|-------------------|
# | max()          | En yüksek değeri seçer           | int / float       |
# | min()          | En düşük değeri seçer            | int / float       |
# | sum()          | Tüm elemanları toplar            | int / float       |
# | divmod(x, y)   | Bölüm ve kalanı aynı anda verir  | tuple (ikili)     |
# | bin(x)         | 10'luk sistemden 2'liğe çevirir  | string (metin)    |
#--------------------------------------------------------------------------



# -------------------------------------------
# 14. HAZIR (BUILT-IN) STRING FONKSİYONLARI :
# -------------------------------------------
s = "python güçlü bir programlama dilidir"

# replace(): Karakter/grup değiştirme
s_rep = s.replace("p", "P")             # Orijinali etkilemez
s_rep2 = "element".replace("e", "", 1)  # Sadece ilk 'e'yi siler

# Dönüşümler:
print("çiçek".upper())          # ÇİÇEK
print("PYTHON".lower())         # python
print("python".capitalize())    # Python
print("aYvA".swapcase())        # AyVa
print("python dili".title())    # Python Dili

# Temizleme:
print("  merhaba  ".strip())  # Boşlukları siler
print("ayva".strip("a"))      # Belirtilen harfi siler: yv
print("merhaba ".rstrip())    # Sadece sağdan


#---------------------------------------------
# METİN DÜZENLEME METOTLARI (STRING METHODS) :
#---------------------------------------------
"""
-> upper(): Tüm harfleri BÜYÜK harfe çevirir.
-> lower(): Tüm harfleri küçük harfe çevirir.
-> capitalize(): Sadece cümlenin İLK harfini büyük yapar.
-> title(): Her kelimenin ilk harfini büyük yapar.
-> swapcase(): Büyükleri küçük, küçükleri büyük harfe çevirir.
-> replace(eski, yeni): Metin içindeki bir parçayı başkasıyla değiştirir.
"""

ornek_metin = "merhaba dunya. python ogreniyorum."

# 1. Harf Durumu Değiştirme
metin_buyuk = ornek_metin.upper()          # Çıktı: 'MERHABA DUNYA. PYTHON OGRENIYORUM.'
metin_kucuk = metin_buyuk.lower()          # Çıktı: 'merhaba dunya. python ogreniyorum.'
metin_ilk_harf = ornek_metin.capitalize()  # Çıktı: 'Merhaba dunya. python ogreniyorum.'
metin_baslik = ornek_metin.title()         # Çıktı: 'Merhaba Dunya. Python Ogreniyorum.'
metin_ters_durum = "PyThOn".swapcase()     # Çıktı: 'pYtHoN'

# 2. Metin Değiştirme (Replace)
# "dunya" kelimesini "evren" ile değiştirelim:
yeni_metin = ornek_metin.replace("dunya", "evren") # Çıktı: 'merhaba evren. python ogreniyorum.'


#------------------------------------------------------------------------------
# TEKNİK ÖZET TABLOSU                                                         |
#------------------------------------------------------------------------------
# | Metot           | Kullanım Amacı                    | Sonuç Örneği        |
# |-----------------|-----------------------------------|---------------------|
# | .upper()        | Tamamını büyük yapar              | PYTHON              |
# | .lower()        | Tamamını küçük yapar              | python              |
# | .capitalize()   | Sadece ilk karakteri büyük yapar  | Python ogreniyorum  |
# | .title()        | Her kelimeyi büyükle başlatır     | Python Ogreniyorum  |
# | .swapcase()     | Büyük/Küçük durumunu tersine çevir| pYTHON -> Python    |
# | .replace(a, b)  | a değerlerini b ile değiştirir    | elma -> armut       |
#------------------------------------------------------------------------------

# Kritik Not: Metotlar orijinal metni değiştirmez, yeni bir metin döndürür!
# Yani ornek_metin hala "merhaba dunya..." olarak kalır.


#---------------------------------------------
# 1. METİN TEMİZLEME (STRIP, RSTRIP, LSTRIP) :
#---------------------------------------------
"""
-> strip(): Metnin başındaki ve sonundaki boşlukları (veya belirtilen karakterleri) siler.
-> lstrip(): Sadece SOL (left) taraftaki boşlukları siler.
-> rstrip(): Sadece SAĞ (right) taraftaki boşlukları siler.
"""

kirli_metin = "   merhaba python   "

temiz_metin = kirli_metin.strip()      #Çıktı: 'merhaba python'
sol_temiz = kirli_metin.lstrip()       #Çıktı: 'merhaba python   '
sag_temiz = kirli_metin.rstrip()       #Çıktı: '   merhaba python'

# Belirli karakterleri temizleme:
dosya_adi = "...dosya_notlari..."
formatli_isim = dosya_adi.strip(".")   #Çıktı: 'dosya_notlari'



#-------------------------------------------
# 2. METİN KONTROLÜ (STARTSWITH, ENDSWITH) :
#-------------------------------------------
"""
-> startswith(deger): Metin belirtilen değerle mi başlıyor? (True/False)
-> endswith(deger): Metin belirtilen değerle mi bitiyor? (True/False)
"""

web_sitesi = "https://www.google.com"

baslangic_kontrol = web_sitesi.startswith("https") #Çıktı: True
uzanti_kontrol = web_sitesi.endswith(".com")       #Çıktı: True



#----------------------------------
# 3. METİN BİÇİMLENDİRME (FORMAT) :
#----------------------------------
"""
-> format(): Metin içindeki süslü parantezlere {} dışarıdan veri yerleştirir.
"""
ad = "Gemini"
surum = 2.0

# Temel kullanım:
formatli_metin = "Merhaba, ben {}. Sürümüm: {}".format(ad, surum)
# Çıktı: 'Merhaba, ben Gemini. Sürümüm: 2.0'

# İndeksli kullanım:
sirali_metin = "{1} bir {0} dilidir.".format("programlama", "Python")
# Çıktı: 'Python bir programlama dilidir.'

#----------------------------------------------------------------------------------
# TEKNİK ÖZET TABLOSU                                                             |
#----------------------------------------------------------------------------------
# | Metot                   | Kullanım Amacı                         | Dönüş Tipi |
# |--------------------     |----------------------------------------|------------|
# | .strip()                | İki uçtaki boşlukları/karakterleri atar| string     |
# | .lstrip() / .rstrip()   | Sadece sol veya sağ ucu temizler       | string     |
# | .startswith()           | Başlangıcı kontrol eder                | boolean    |
# | .endswith()             | Sonu kontrol eder                      | boolean    |
# | .format()               | Metin içine dinamik veri yerleştirir   | string     |
#----------------------------------------------------------------------------------



# ===================================================================
# == BAB 10: FONKSİYONLAR - UYGULAMA VE ÇÖZÜM TESTİ                ==
# ===================================================================
# Bu dosya, 1.jpeg - 31.jpeg arasındaki teknik dökümanlara dayalı 
# 10 adet özgün soru ve detaylı çözümlerini içermektedir.
# ===================================================================

# -------------------------------------------------------------------
# SORU 1: TEMEL TANIMLAMA VE ÇAĞIRMA
# Soru: Parametre olarak aldığı ismi "Sayın [isim], hoş geldiniz." 
# şeklinde ekrana yazdıran fonksiyonu tanımlayıp çağırınız.
# -------------------------------------------------------------------
def karsila(isim):
    print(f"Sayın {isim}, hoş geldiniz.")

karsila("Ahmet") # Çıktı: Sayın Ahmet, hoş geldiniz.


# -------------------------------------------------------------------
# SORU 2: DEĞER DÖNDÜREN (RETURN) FONKSİYONLAR
# Soru: Bir karenin kenar uzunluğunu alıp alanını hesaplayarak 
# sonucu geriye döndüren fonksiyonu yazınız.
# -------------------------------------------------------------------
def alan_hesapla(kenar):
    return kenar * kenar

sonuc = alan_hesapla(5)
print("Karenin Alanı:", sonuc) # Çıktı: 25


# -------------------------------------------------------------------
# SORU 3: VARSAYILAN DEĞERLİ PARAMETRELER
# Soru: Bir metni ve kaç kez yazılacağını parametre olarak alan, 
# eğer adet belirtilmezse metni 1 kez yazdıran fonksiyonu yazınız.
# -------------------------------------------------------------------
def metin_yazdir(metin, adet=1):
    for i in range(adet):
        print(metin)

metin_yazdir("Merhaba")    # 1 kez yazar.
metin_yazdir("Python", 3)  # 3 kez yazar.


# -------------------------------------------------------------------
# SORU 4: ÇOKLU DEĞER DÖNDÜRME
# Soru: İki sayıyı parametre alıp, bu sayıların toplamını ve 
# farkını aynı anda döndüren fonksiyonu yazınız.
# -------------------------------------------------------------------
def hesapla(a, b):
    toplam = a + b
    fark = a - b
    return toplam, fark

t, f = hesapla(20, 10)
print(f"Toplam: {t}, Fark: {f}") # Çıktı: Toplam: 30, Fark: 10


# -------------------------------------------------------------------
# SORU 5: ESNEK PARAMETRE (*ARGS)
# Soru: İçerisine kaç tane sayı gönderileceği belli olmayan bir 
# durumda, gelen tüm sayıların çarpımını dönen fonksiyonu yazınız.
# -------------------------------------------------------------------
def carp(*sayilar):
    sonuc = 1
    for s in sayilar:
        sonuc *= s
    return sonuc

print("Çarpım:", carp(2, 3, 4)) # Çıktı: 24


# -------------------------------------------------------------------
# SORU 6: ÖZYİNELİ (RECURSIVE) FONKSİYONLAR
# Soru: Faktöriyel hesabını özyineli (kendini çağıran) yöntemle 
# gerçekleştiren fonksiyonu yazınız.
# -------------------------------------------------------------------
# 
def faktoriyel(n):
    if n == 1: # Durma kuralı (Base Case)
        return 1
    else:
        return n * faktoriyel(n - 1)

print("5 Faktöriyel:", faktoriyel(5)) # Çıktı: 120


# -------------------------------------------------------------------
# SORU 7: MATEMATİK MODÜLÜ (MATH)
# Soru: Kullanıcıdan alınan ondalıklı bir sayıyı her zaman yukarıdaki 
# tam sayıya yuvarlayan kodu math modülü ile yazınız.
# -------------------------------------------------------------------
import math

sayi = 4.12
yukari_yuvarla = math.ceil(sayi)
print(f"{sayi} -> {yukari_yuvarla}") # Çıktı: 5


# -------------------------------------------------------------------
# SORU 8: STRING METOTLARI (REPLACE & STRIP)
# Soru: "  python programlama dili  " ifadesindeki baş ve sondaki 
# boşlukları silip, boşluk karakterlerini "-" ile değiştiriniz.
# -------------------------------------------------------------------
metin = "  python programlama dili  "
temiz_metin = metin.strip().replace(" ", "-")
print(temiz_metin) # Çıktı: python-programlama-dili


# -------------------------------------------------------------------
# SORU 9: İSİMLİ (KEYWORD) ARGÜMANLAR
# Soru: 'karakter', 'satir' ve 'sutun' parametreleri alan bir 
# fonksiyonu, sıralarına uymadan isimlerini belirterek çağırınız.
# -------------------------------------------------------------------
def ciz(karakter, satir, sutun):
    for i in range(satir):
        print(karakter * sutun)

# İsimli çağırmada sıra önemsizdir:
ciz(sutun=10, karakter="#", satir=2)


# -------------------------------------------------------------------
# SORU 10: FORMAT() METODU İLE ÇIKTI BİÇİMLENDİRME
# Soru: Bir öğrencinin adı ve notunu alıp "Öğrenci: [ad], Not: [not]" 
# formatında yazdıran kodu format() ile yazınız.
# -------------------------------------------------------------------
ad = "Zeynep"
notu = 95
print("Öğrenci: {}, Not: {}".format(ad, notu)) #

# ===================================================================
# BAB 10 UYGULAMA TESTİ SONU.
# ===================================================================

#---------------------------------------------------------------------------
# ÖRNEK 1: FONKSİYONLARIN BİRLİKTE KULLANIMI VE BELGELENDİRME (DOCSTRING) :
#---------------------------------------------------------------------------

# Fonksiyonu Tanıtma
def yasHesapla(dogumYili):
    """Girilen doğum yılına göre yaşı hesaplar."""
    return 2026 - dogumYili

def EmekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldığını hesaplar.
    INPUT: dogumYili (int), isim (str)
    OUTPUT: Ekrana emeklilik durumu bilgisini yazdırır.
    """
    yas = yasHesapla(dogumYili) # Başka bir fonksiyonu içinde çağırdık.
    emeklilik = 65 - yas 
    
    if emeklilik > 0:
        print(f"Sayın {isim}, emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print(f"Sayın {isim}, zaten emekli oldunuz veya emeklilik yaşınız gelmiş.")

# Fonksiyonu Çağırma
EmekliligeKacYilKaldi(1995, "Ahmet")



# ===========================================================================================================
# == BAB 14: PYTHON'DA FONKSİYONLARIN TEKNİK İNŞASI (CHAPTER 14: TECHNICAL CONSTRUCTION OF FUNCTIONS)      ==
# ===========================================================================================================

#----------------------------------------------------------
# ÖRNEK 1: Parametresiz Temel Fonksiyon (Tanımlama ve Çağırma)
#----------------------------------------------------------
""" 
Senaryo: Herhangi bir girdi almadan sabit bir işlem gerçekleştiren en basit yapı.
"""
def sistem_durumunu_yazdir():
    print("Sistem aktif, veri akışı bekleniyor.")

sistem_durumunu_yazdir()


#-------------------------------------------------
# ÖRNEK 2: Parametreli Fonksiyon (Girdi İşleme)
#-------------------------------------------------
""" 
Senaryo: Dışarıdan alınan bir argümanı yerel kapsamda işleyerek çıktı üretme.
"""
def kullanici_selamla(isim):
    print(f"Sisteme giriş yapıldı: {isim}")

kullanici_selamla("Mühendis_1")


#---------------------------------------------
# ÖRNEK 3: Değer Döndüren Fonksiyonlar (Return)
#---------------------------------------------
"""
Senaryo: Bir işlemin sonucunu çağıran yere geri ileten (return) yapı.
"""
def karesini_hesapla(sayi):
    return sayi ** 2

sonuc = karesini_hesapla(8)
print(f"İşlem Sonucu: {sonuc}")


#----------------------------------------------------
# ÖRNEK 4: Çoklu Parametre Kullanımı (Aritmetik)
#----------------------------------------------------
""" 
Senaryo: Birden fazla değişkenin belirli bir formül dahilinde işlenmesi.
"""
def dikdortgen_alani(en, boy):
    return en * boy

print(f"Alan: {dikdortgen_alani(5, 12)}")


#-------------------------------------------------------
# ÖRNEK 5: Varsayılan Parametre Değeri (Default Arguments)
#-------------------------------------------------------
""" 
Senaryo: Parametre girilmediğinde sistemin önceden belirlenmiş bir sabit değeri kullanması.
"""
def kdv_hesapla(tutar, oran=0.20):
    return tutar * oran

print(f"Varsayılan KDV: {kdv_hesapla(100)}") # 0.20 kullanılır
print(f"Özel KDV: {kdv_hesapla(100, 0.10)}") # 0.10 kullanılır


#----------------------------------------------------------------
# ÖRNEK 6: Koşullu Mantık İçeren Fonksiyonlar (Branching)
#----------------------------------------------------------------
"""
Senaryo: Gelen verinin durumuna göre farklı mantıksal yollar izleyen yapı.
"""
def kontrol_et_yas(yas):
    if yas >= 18:
        return "Erişim Onaylandı"
    else:
        return "Erişim Reddedildi"

print(kontrol_et_yas(20))


#------------------------------------------------------
# ÖRNEK 7: Döngüler ve Fonksiyon Kombinasyonu (Iteration)
#------------------------------------------------------
"""
Senaryo: Bir koleksiyon (liste) içindeki elemanları fonksiyon içinde itere etme.
"""
def liste_toplami(sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam

print(f"Liste Toplamı: {liste_toplami([10, 20, 30, 40])}")


#------------------------------------------
# ÖRNEK 8: Yerel ve Küresel Kapsam (Local vs Global Scope)
#------------------------------------------
"""
Senaryo: Fonksiyon içindeki değişkenlerin dış dünyadan izole edilmesi deneyi.
"""
x = 50 # Global değişken

def kapsam_deneyi():
    x = 100 # Local (Yerel) değişken
    return x

print(f"Global X: {x} | Local X: {kapsam_deneyi()}")


#-----------------------------------------------
# ÖRNEK 9: Metin Analizi Yapan Fonksiyonlar
#-----------------------------------------------
"""
Senaryo: String metodlarını fonksiyon içinde kullanarak veri manipülasyonu sağlama.
"""
def formatli_isim(ad, soyad):
    return f"{ad.capitalize()} {soyad.upper()}"

print(formatli_isim("ali", "arda"))


#------------------------------------------------------------
# ÖRNEK 10: Dinamik Sayıda Parametre (*args)
#------------------------------------------------------------
"""
Senaryo: Fonksiyona kaç tane argüman geleceğinin bilinmediği durumlarda tuple paketleme.
"""
def coklu_topla(*sayilar):
    return sum(sayilar)

print(f"3 Sayı Toplamı: {coklu_topla(1, 2, 3)}")
print(f"5 Sayı Toplamı: {coklu_topla(1, 2, 3, 4, 5)}")



#------------------------------------------------------------
# ÖRNEK 11: İsimlendirilmiş Dinamik Parametreler (**kwargs)
#------------------------------------------------------------
"""
Senaryo: Verileri anahtar-değer (dictionary) çifti olarak paketleyip işleme.
"""
def kullanici_bilgileri(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

kullanici_bilgileri(Ad="Ali", Yas=25, Sehir="Istanbul")


#------------------------------------------------------------
# ÖRNEK 12: Lambda Fonksiyonları (Anonim Fonksiyonlar)
#------------------------------------------------------------
"""
Senaryo: Tek satırlık, isimsiz matematiksel ifadelerin tanımlanması.
"""
us_al = lambda taban, us: taban ** us
print(f"2 üzeri 4: {us_al(2, 4)}")


#------------------------------------------------------------
# ÖRNEK 13: Liste Üreticileri (List Comprehension) ve Fonksiyonlar
#------------------------------------------------------------
"""
Senaryo: Fonksiyon içinde hızlı liste oluşturma tekniklerini kullanma.
"""
def cift_sayilari_filtrele(liste):
    return [x for x in liste if x % 2 == 0]

print(f"Filtrelenmiş Liste: {cift_sayilari_filtrele([1, 2, 3, 4, 5, 6])}")


#------------------------------------------------------------
# ÖRNEK 14: Fonksiyon İçinde Fonksiyon (Nested Functions)
#------------------------------------------------------------
"""
Senaryo: Bir görevin alt görevlere bölünerek ana fonksiyon içinde kapsüllenmesi.
"""
def dis_islem(sayi):
    def ic_islem(s):
        return s + 10
    return ic_islem(sayi) * 2

print(f"Nested Sonuç: {dis_islem(5)}")


#------------------------------------------------------------
# ÖRNEK 15: Özyinelemeli (Recursive) Fonksiyonlar
#------------------------------------------------------------
"""
Senaryo: Bir fonksiyonun belirli bir durma noktasına kadar kendisini çağırması.
"""
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    return n * faktoriyel(n - 1)

print(f"5 Faktöriyel: {faktoriyel(5)}")



#------------------------------------------------------------
# ÖRNEK 16: Tip İpucu (Type Hinting) Kullanımı
#------------------------------------------------------------
"""
Senaryo: Parametrelerin ve dönüş değerinin tipini belirterek kodun okunabilirliğini artırma.
"""
def selamla_teknik(isim: str, yas: int) -> str:
    return f"Personel: {isim}, {yas} yaşında."

print(selamla_teknik("Arda", 21))


#------------------------------------------------------------
# ÖRNEK 17: Boolean Değer Döndüren Sorgu Fonksiyonları
#------------------------------------------------------------
"""
Senaryo: Mantıksal bir durumu denetleyip True/False yanıtı üreten yardımcı yapılar.
"""
def asal_mi(sayi):
    if sayi < 2: return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0: return False
    return True

print(f"17 Asal mı?: {asal_mi(17)}")


#------------------------------------------------------------
# ÖRNEK 18: Docstring (Dökümantasyon Dizgisi) Kullanımı
#------------------------------------------------------------
"""
Senaryo: Fonksiyonun ne yaptığını teknik dökümantasyon kuralları ile açıklama.
"""
def kuvvet_hesapla(f, d):
    """Verilen kuvvet ve mesafe ile fiziksel işi hesaplar (W = F * d)."""
    return f * d

print(f"Doküman Bilgisi: {kuvvet_hesapla.__doc__}")


#------------------------------------------------------------
# ÖRNEK 19: Map Fonksiyonu ile Entegrasyon
#------------------------------------------------------------
"""
Senaryo: Bir fonksiyonu bir listenin tüm elemanlarına tek seferde uygulama.
"""
def metni_temizle(kelime):
    return kelime.strip().lower()

veriler = ["  PYTHON ", " Java", "C++ "]
temiz_veriler = list(map(metni_temizle, veriler))
print(f"Temizlenmiş Veriler: {temiz_veriler}")


#------------------------------------------------------------
# ÖRNEK 20: Karmaşık Veri Yapısı (List of Dicts) Dönüştürücü
#------------------------------------------------------------
"""
Senaryo: Sözlüklerden oluşan bir listeden belirli verileri çekip yeni bir formatta birleştirme.
"""
def rapor_olustur(liste):
    rapor = {}
    for eleman in liste:
        rapor[eleman['id']] = eleman['skor']
    return rapor

veriler = [{'id': 'A1', 'skor': 85}, {'id': 'B2', 'skor': 90}]
print(f"Sistem Raporu: {rapor_olustur(veriler)}")


# ===========================================================================================================================================
#  BAB 10 (PYTHON'DA FONKSİYONLAR) PROJE LİSTESİ :                                                                                          |
# ===========================================================================================================================================
#  ÖRNEK 1 : Parametresiz Temel Fonksiyon (Tanımlama ve Çağırma)                                                                            |
#  ÖRNEK 2 : Parametreli Fonksiyon (Girdi İşleme)                                                                                           |
#  ÖRNEK 3 : Değer Döndüren Fonksiyonlar (Return Mekanizması)                                                                               |
#  ÖRNEK 4 : Çoklu Parametre Kullanımı (Aritmetik Hesaplamalar)                                                                             |
#  ÖRNEK 5 : Varsayılan Parametre Değeri (Default Arguments Kurgusu)                                                                        |
#  ÖRNEK 6 : Koşullu Mantık İçeren Fonksiyonlar (Branching)                                                                                 |
#  ÖRNEK 7 : Döngüler ve Fonksiyon Kombinasyonu (Iteration)                                                                                 |
#  ÖRNEK 8 : Yerel ve Küresel Kapsam Analizi (Scope Management)                                                                             |
#  ÖRNEK 9 : Metin Analizi ve String Metodları Entegrasyonu                                                                                 |
#  ÖRNEK 10: Dinamik Sayıda Parametre Yönetimi (*args Yapısı)                                                                               |
#  ÖRNEK 11: İsimlendirilmiş Dinamik Parametreler (**kwargs Yapısı)                                                                         |
#  ÖRNEK 12: Lambda (Anonim) Fonksiyon Tasarımı                                                                                             |
#  ÖRNEK 13: Liste Üreticileri (List Comprehension) ve Fonksiyon Entegrasyonu                                                               |
#  ÖRNEK 14: Kapsüllenmiş Fonksiyonlar (Nested Functions Yapısı)                                                                            |
#  ÖRNEK 15: Özyinelemeli (Recursive) Fonksiyon Mimarisi                                                                                    |
#  ÖRNEK 16: Tip İpucu (Type Hinting) ve Kod Dökümantasyonu                                                                                 |
#  ÖRNEK 17: Boolean Sorgu Fonksiyonları ve Asallık Kontrolü                                                                                |
#  ÖRNEK 18: Teknik Dökümantasyon (Docstring) Kullanım Standartları                                                                         |
#  ÖRNEK 19: Yüksek Seviyeli Fonksiyonlar (Map Uygulaması)                                                                                  |
#  ÖRNEK 20: Karmaşık Veri Yapısı (List of Dicts) Dönüştürücü                                                                               |
# ===========================================================================================================================================