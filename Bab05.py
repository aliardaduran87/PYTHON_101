# ================================================================================================
# == BAB 5: PYTHON'DA OPERATÖRLER VE OPERANDLAR (CHAPTER 5: OPERATORS AND OPERANDS IN PYTHON) : ==
# ================================================================================================

"""
TANIMLAR:
-> Operatör: Veriler üzerinde aritmetik, mantıksal veya karşılaştırma işlemlerini gerçekleştiren özel sembollerdir (+, -, *, /, == vb.).
-> Operand: Operatörlerin işleme aldığı değerlere veya değişkenlere denir.
   Örn: 'a + 5' ifadesinde 'a' ve '5' operand, '+' ise operatördür.
"""

# -------------------------------------------------
# 1. ARİTMETİK OPERATÖRLER (ARITHMETIC OPERATORS) :
# -------------------------------------------------
"""
-> Matematiksel hesaplamaları yapmak için kullanılırlar.
"""
# Toplama (+): İki değeri toplar.
a = 10 + 5
b = 20 + 37
print(f"Toplama: {a}")
print(f"Toplama: {b}")

# Çıkarma (-): İlk değerden ikinciyi çıkarır.
c = 10 - 5
d = 3-5
print(f"Çıkarma: {c}")
print(f"Çıkarma: {d}")

# Çarpma (*): İki sayıyı çarpar.
e = 10 * 5
f = 32 * 3
print(f"Çarpma: {e}")
print(f"Çarpma: {f}")

# Ondalıklı (Float) Bölme (/): Sonucu daima ondalıklı (float) döndürür.
g = 10 / 4     # Sonuç: 2.5
h = 196 / 38   # Sonuç: 5.157894736842105
print(f"Float Bölme: {g}")
print(f"Float Bölme: {h}")


# Tam (Integer) Bölme (//): Bölümün sadece tam kısmını verir, ondalığı atar.
i = 10 // 4    # Sonuç: 2
j= 196 // 38   # Sonuç: 5
print(f"Tam Bölme: {i}")
print(f"Tam Bölme: {j}")


# Üs Alma (**): Soldaki sayının (taban), sağdaki sayı (üs) kadar kuvvetini alır.
k = 2 ** 3  # 2'nin küpü: 8
l = 4 ** 3  # 4'ün küpü : 64
print(f"Üs Alma: {k}")
print(f"Üs Alma: {l}")

# Kalan / Modül (%): Bölme işleminden kalan sonucu verir.
m = 10 % 3  # 10'un 3'e bölümünden kalan 1'dir.
n = 20 % 6  # 20 ile 6 nın bölümünden kalan 2'dir.
print(f"Modül (Kalan): {m}")
print(f"Modül (Kalan): {n}")


# -----------------------------------------
# 2. İŞLEM ÖNCELİĞİ (OPERATOR PRECEDENCE) :
# -----------------------------------------
"""
Python karmaşık işlemleri şu sırayla çözer:
-------------------------------------------
1. Parantezler ()
2. Üs Alma **
3. İşaret Değiştirme (+x, -x)
4. Çarpma, Bölme, Modül (*, /, //, %)
5. Toplama, Çıkarma (+, -)
6. Karşılaştırma Operatörleri (==, !=, >, <, >=, <=)  
7. Mantıksal NOT                                     
8. Mantıksal AND                                     
9. Mantıksal OR                                      
Not: Aynı önceliğe sahip işlemlerde soldan sağa doğru gidilir.

# Neden Karşılaştırma Operatörleri Alt Sıradadır?
-------------------------------------------------
-> Bunun temel sebebi "Önce Hesapla, Sonra Karşılaştır" mantığıdır. 
-> Eğer karşılaştırma operatörleri aritmetik operatörlerden önce çalışsaydı, Python matematiği yapmadan doğru/yanlış (True/False) sonucunu üretmeye çalışırdı.


# Mantıksal Operatörler (AND, OR, NOT) Neden En Sondadır?
---------------------------------------------------------
-> Mantıksal operatörler, "Kararların Kararını" verir. 
-> Genellikle karşılaştırma operatörlerinden çıkan sonuçları birleştirmek için kullanılırlar.
"""
islem = 10 + 2 * 3 ** 2  # Önce üs (9), sonra çarpma (18), sonra toplama (28).
print(f"İşlem Önceliği Sonucu: {islem}")


# ---------------------------------
# 3. İŞARET VE ATAMA OPERATÖRLERİ :
# ---------------------------------

#------------------------------
# Pozitif-Negatif İşaretçiler :
#------------------------------
pozitif = +5
negatif = -5

print(pozitif)
print(negatif)

# Standart Atama (=): Sağdaki değeri soldaki değişkene aktarır.(Bu her zaman böyledir.)
x = 20 


# Eşittir Operatörü (=):
a = 2 
# a değişkenine 2 değeri atanmıştır.


# Toplayarak Atama Operatörü (+=):
a += 2
# a değişkenine 2 değerini ekleyerek yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a + 2 anlamına gelmektedir.


# Çıkararak Atama Operatörü (-=):
a -= 2
# a değişkeninden 2 değeri çıkarılarak yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a - 2 anlamına gelmektedir.


# Çarparak Atama Operatörü (*=):
a *= 2
# a değişkeni 2 ile çarpılarak yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a * 2 anlamına gelmektedir.


# Bölerek Atama Operatörü (/=):
a /= 2
# a değişkeni 2 değerine bölünerek yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a / 2 anlamına gelmektedir.


# Modunu Alarak Atama Operatörü (%=):
a %= 2
# a değişkeninin 2 değeri ile modu alınarak yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a % 2 anlamına gelmektedir.


# Üs Alarak Atama Operatörü (**=):
a **= 2
# a değişkeninin ikinci kuvveti (a²) alınarak yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a ** 2 anlamına gelmektedir.


# Tam Bölerek Atama Operatörü (//=):
a //= 2
# a değişkeni 2 değerine tam bölünmüş (kalan dikkate alınmadan) ve çıkan değer yine a değişkenine atanmıştır. 
# Başka bir ifadeyle a = a // 2 anlamına gelmektedir.

#------------------------------------------
# Özet Tablo Gösterimi:                   |
#------------------------------------------
# | Operatör  | Örnek | Açıklama          |             
# | =         | a=2   | Atama             |
# | +=        | a+=2  | a = a + 2         |
# | -=        | a-=2  | a = a - 2         |
# | *=        | a*=2  | a = a * 2         |
# | /=        | a/=2  | a = a / 2         |
# | %=        | a%=2  | a = a % 2         |
# | **=       | a**=2 | a = a ** 2        |
# | //=       | a//=2 | a = a // 2        |
#------------------------------------------


# -------------------------------
# 4. KARŞILAŞTIRMA OPERATÖRLERİ :
# -------------------------------
"""
-> İki değeri kıyaslar ve sonuç olarak Boolean (True/False) döndürür.
"""
sayi1 = 15
sayi2 = 10

print(f"Eşit mi? (==):      {sayi1 == sayi2}")  # False
print(f"Eşit değil mi? (!=): {sayi1 != sayi2}") # True
print(f"Büyük mü? (>):       {sayi1 > sayi2}")  # True
print(f"Küçük mü? (<):       {sayi1 < sayi2}")  # False
print(f"Büyük-Eşit mi? (>=): {sayi1 >= sayi2}") # True
print(f"Küçük-Eşit mi? (<=): {sayi1 <= sayi2}") # False


x1=1
x2=2
x3=3
print(x1<x2<x3) #Çıktı: True


yas = 18
limit = 18
puan = 85
kullanici_adi = "python_ogrencisi"

# 1. Equal to (==) -> Eşit mi?
# Değerler tıpatıp aynıysa True döner.
print(f"Yaş 18 mi?: {yas == 18}")          # True
print(f"Yaş 20 mi?: {yas == 20}")          # False

# 2. Not equal to (!=) -> Eşit değil mi? (Farklı mı?)
# Değerler birbirinden farklıysa True döner.
print(f"Yaş 18'den farklı mı?: {yas != 18}") # False (Çünkü eşitler)
print(f"Yaş 25'ten farklı mı?: {yas != 25}") # True

# 3. Greater than (>) -> Büyük mü?
print(f"Puan 80'den büyük mü?: {puan > 80}")  # True
print(f"Puan 90'dan büyük mü?: {puan > 90}")  # False

# 4. Less than (<) -> Küçük mü?
print(f"Puan 100'den küçük mü?: {puan < 100}") # True

# 5. Greater than or equal to (>=) -> Büyük veya eşit mi?
# Bu operatör 'yas > limit' veya 'yas == limit' durumlarından biri doğruysa True döner.
print(f"Ehliyet alabilir mi? (>=18): {yas >= limit}") # True

# 6. Less than or equal to (<=) -> Küçük veya eşit mi?
print(f"Puan 85'e eşit veya küçük mü?: {puan <= 85}") # True (Çünkü eşit)


# Mesela biz kullanıcı adı ve şifre doğrulama sistemi yazalım.
kullanici_adi="ali_arda87"
girilen_kullanici_adi="ali_arda87"
print(f"Girilen kullanıcı adı doğru mu?: {kullanici_adi==girilen_kullanici_adi}") # True değerini döndürür.

sifre=12345
girilen_sifre=1234
print(f"Girilen şifre doğru mu ?:{sifre==girilen_sifre}") # False değerini döndürür.


# ----------------------------------------------
# 5. MANTIKSAL OPERATÖRLER (LOGICAL OPERATORS) :
# ----------------------------------------------
"""
-> Doğru (True) veya yanlış (False) değeri taşıyan mantıksal ifadeleri bir araya getirmek ve düzenlemek için kullanılır.
"""
saat = 12
sicaklik = 35

#----------------------------
# MANTIKSAL VE İŞLEMİ (AND) : 
#----------------------------

# İki koşulun da doğru olması durumunda True sonucunu üretir.
# Geri kalan bütün olası durumlarda  False sonucunu üretir.
print(f"Mantıksal AND: {saat < 16 and sicaklik > 30}")   #Çıktı: True
print(f"Mantıksal AND: {saat > 13 and sicaklik >30}")    #Çıktı: False


#----------------------------
# MANTIKSAL VEYA İŞLEMİ (OR): 
#----------------------------

# Koşullardan en az birinin doğru olması durumunda True sonucunu üretir.
# Yalnız ikisinin de yanlış olması durumunda False sonucunu diğer aksi durumlarda True sonucunu üretir.
print(f"Mantıksal OR:  {saat < 16 or sicaklik > 40}")   #Çıktı: True


#-------------------------------
# MANTIKSAL DEĞİL İŞLEMİ (NOT) :
#-------------------------------

# Mevcut mantıksal değeri tersine çevirir. Tek operand ile çalışır.
# 1 ise 0 ; 0 ise 1 gibi düşünebiliriz.
print(f"Mantıksal NOT: {not(sicaklik > 35)}")          # True (35>35 False'tur, NOT True yapar)


kullanici_adi="ali_arda87"
girilen_kullanici_adi="ali_arda87"
print(f"Girilen kullanıcı adı doğru mu?: {kullanici_adi==girilen_kullanici_adi}")

sifre=12345
girilen_sifre=1234
print(f"Girilen şifre doğru mu ?:{sifre==girilen_sifre}")

print(f"Doğrulama işlemi başarılı mı ?: {girilen_kullanici_adi==kullanici_adi and sifre==girilen_sifre}") 
# Burada and (ve) operatörü ile yaptığımız için 2 kısmın da doğru olması icap ederken biri yanlış olduğu için False değerini döndürür.

print(f"Doğrulama işlemi başarılı mı ?: {girilen_kullanici_adi==kullanici_adi or sifre==girilen_sifre}")
# Burada or (veya) operatörü ile yaptığımız için 2 kısmın da doğru olmasına gerek olmadan tek bir doğruyla True değerini döndürür.
# Bu yüzden bu tarz sistem yazılımlarında and operatörü kullanılıyor.

# 'and' işleminde ilk ifade False ise Python ikinciye bakmaz (Sonuç zaten False'tur).
# 'or' işleminde ilk ifade True ise Python ikinciye bakmaz (Sonuç zaten True'dur).
# Bu durum işlemciyi yormaz, performansı artırır.

# ------------------------------------------------
#  BİTSEL İŞLEM OPERATÖRLERİ (BITWISE OPERATORS) :
# ------------------------------------------------

# Sayıların bit (binary) halini görmek için bin() fonksiyonunu kullanabiliriz:
print(f"60 sayısının bit hali: {bin(60)}") #Çıktı: 0b111100

"""
-> Bitsel işlem operatörleri verileri bitlerine ayırarak, üzerlerinde bit bit işlem yaparlar.
"""
a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101

#-----------------------
# Bitsel VE İşlemi (&) :
#-----------------------
""" İkili tabandaki sayıları basamak basamak "ve" işlemine tabi tutar. """
c = a & b
print(f"Bitsel VE (&): {c}")     #Çıktı : Bitsel VE (&): 12 sonucu çıkar.


#-------------------------
# Bitsel VEYA İşlemi (|) :
#-------------------------
""" Bitsel veya işlemi, iki değerden en az birinin 1 olması halinde 1 sonucunu üretir. """
c = a | b
print(f"Bitsel VEYA (|): {c}")   #Çıktı: Bitsel VEYA (|): 61 sonucu çıkar.


#------------------------------------
# Bitsel ÖZEL VEYA (XOR) İşlemi (^) :
#------------------------------------
""" Bitsel özel veya işlemi (exclusive or - XOR) karşılaştırılan iki bit birbirinden farklı ise 1, birbirinin aynısı ise 0 sonucunu üretir. """
c = a ^ b
print(f"Bitsel XOR (^): {c}")    #Çıktı: Bitsel XOR (^): 49 sonucu çıkar.


#-------------------------------------
# Bitsel Değil (Tümleyen) İşlemi (~) :
#-------------------------------------
""" 
 -> Bitsel değil işlemi ya da sayının tümleyenini alma işlemi, sayı içerisindeki her bitin terslenmesi işlemidir. 
 -> Yani 1 olan değerleri 0, 0 olan değerleri 1 haline getirir.
 -> Bitsel tümleyen operatörü ile gerçekleştirilir. Tümleyen operatörü tek operandlı bir operatördür.
 -> Kısa yol olarak  sayıyı -(n+1) yapar
"""
c = ~a
print(f"Bitsel NOT (~): {c}")
# Not: Tilda (~) işaretini yapmak için (Alt + 126) tuş kombinasyonunu kullanabilirsin.
# https://www.irongeek.com/alt-numpad-ascii-key-combos-and-chart.html -> Bu siteden diğer Alt Kombinasyonlarına bakabilirsiniz :)


#-----------------------------------
# BİTSEL SOLA KAYDIRMA İŞLEMİ (<<) :
#----------------------------------- 
"""
-> Bitsel sola kaydırma işlemi bir sayı içerisinde yer alan bitler ikinci operand ile belirtilen basamak sayısı kadar sola kaydırılır.
-> Sol tarafın en sonunda yer alan kaydıran bit sayısı kadar basamak atılarak, atılan basamak sayısı kadar sağ taraftan 0 ilave edilir.
-> Bitsel sola kaydırma işleminde sayı büyür.
-> 1 bit sola kaydırma işlemi ile sayı 2 katına çıkar.
"""
a = 60
a = a << 2
print(f"Sola Kaydırma Sonucu: {a}")  #Çıktı: Sola Kaydırma Sonucu: 240 (4 Katına çıktı.)


#-----------------------------------
# BİTSEL SAĞA KAYDIRMA İŞLEMİ (>>) :
#-----------------------------------
"""
-> Bitsel sağa kaydırma işlemi bir sayı içerisinde yer alan bitler ikinci operand ile belirtilen basamak sayısı kadar sağa kaydırılır.
-> Kaydırılan bit sayısı kadar sol taraftan 0 ilave edilir.
-> En sağdaki kaydırılan sayısı kadar bit ise atılır.
-> 1 bit sağa kaydırma işlemi ile sayı 1/2 katına çıkar.
"""
a = 60
a = a >> 2
print(f"Sağa Kaydırma Sonucu: {a}") #Çıktı: Sağa Kaydırma Sonucu: 15 (1/4 Katına indi.)


#---------------------------------------------
# AİTLİK OPERATÖRLERİ (MEMBERSHIP OPERATORS) :
#---------------------------------------------
"""
-> Herhangi bir elemanın bir koleksiyona ait olup olmama durumunu kontrol eden operatörlerdir.
-> İki adet aitlik operatörü vardır: "in" ve "not in".
"""
print("a" in "merhaba")      #Çıktı: True
print("b" not in "merhaba")  #Çıktı: True
print("h" in "ali")          #Çıktı: False


#-------------------------------------------
# KİMLİK OPERATÖRLERİ (IDENTITY OPERATORS) :
#-------------------------------------------
"""
-> Tüm programlama dillerinde, program içerisinde tanımlı nesneler bilgisayarın belleği üzerinde yer kaplar.
-> Her bir bellek bölgesi eşsiz bir adrese sahiptir.
-> Program içerisindeki herhangi bir nesnenin bellek adresi, nesnenin kimliği olarak ifade edilir.
-> Python'da "id" komutu, herhangi bir nesnenin kimliğini verir. id ifadesi İngilizcedeki "identity (kimlik)" kelimesinin kısaltmasıdır.
-> Kimlik operatörleri, iki nesnenin bellek adreslerini yani id'lerini karşılaştıran operatörlerdir.
-> İki adet kimlik operatörü vardır: "is" ve "is not".
"""
a = 20
print(id(a))       # a değişkeninin bellek adresini ekrana basar.

b = 30
print(a is b)      #Çıktı: False (Adresler farklı)
print(a is not b)  #Çıktı: True  (Adresler farklı olduğu için True)

# ÖNEMLİ (Bellek Yönetimi Notu):
a = 20
b = 20
print(a is b) 

"""
-> Burada a ve b iki ayrı değişken olarak yer almaktadır ve normal şartlarda ayrı değişkenler bellekte ayrı hücrelerde tutulmalıdır.
-> Ancak Python, bellekten tasarruf ve performansı arttırmak için aynı değerler için bellekte ayrı ayrı yer tahsis etmez.
-> Bunun yerine ikinci değişkeni oluşturan değişkenle aynı adrese yönlendirir.
-> Bu durumda a ve b değişkenlerinin bellekte gösterdiği adresler ve id'leri birbirine eşit olur.
-> Burada ince bir detay var. Bu operatör (==) değerleri kontrol eder, is adresleri kontrol eder. 2'sinin farkı önemli bir detay.
"""


# ===========================================================================================================
# == BAB 5: PYTHON'DA OPERATÖRLER VE OPERANDLAR  PROJELERİ (CHAPTER 5: OPERATORS AND OPERANDS IN PYTHON) : ==
# ===========================================================================================================

#----------------------------------------------------------
# ÖRNEK 1: Banka Kredisi Onay Mekanizması (AND Kullanımı) :
#----------------------------------------------------------
""" 
Senaryo:Kredi çıkması için hem gelirin yüksek olması hem de kredi puanının iyi olması gerekir. 
"""
gelir_yeterli = True
kredi_puani_yuksek = False

kredi_onay = gelir_yeterli and kredi_puani_yuksek
print(f"Kredi onaylandı mı?: {kredi_onay}") # False (Çünkü biri eksik)


#-------------------------------------------------
# ÖRNEK 2: İndirim Kuponu Sistemi (OR Kullanımı) :
#-------------------------------------------------
""" 
Senaryo: İndirim için ya kupon kodu olmalı ya da kişinin doğum günü olmalı. 
"""
kupon_var = False
dogum_gunu_mu = True

indirim_uygula = kupon_var or dogum_gunu_mu
print(f"İndirim hakkı var mı?: {indirim_uygula}") # True (Bir tanesi yeterli)


#---------------------------------------------
# ÖRNEK 3: Sistem Bakım Modu (NOT Kullanımı) :
#---------------------------------------------
"""
Senaryo:Eğer sistem bakımda DEĞİLSE giriş yapılmasına izin ver.
"""
sistem_bakimda = False

giris_izni = not sistem_bakimda
print(f"Sisteme giriş izni var mı?: {giris_izni}") # True


#----------------------------------------------------
# ÖRNEK 4: Karmaşık Bir Karşılaştırma (Kombinasyon) :
#----------------------------------------------------
""" 
Senaryo: Bir öğrencinin dersten geçmesi için devamsızlığın 10'dan az olması VE (vize ile final ortalamasının 50'den büyük olması VEYA finalinin 70 olması) gerekir. 
"""

devamsizlik = 5
vize = 40
final = 75

# Önce parantez içi, sonra 'and' işlemi yapılır.
gecme_durumu = devamsizlik < 10 and ((vize + final) / 2 >= 50 or final >= 70)
print(f"Öğrenci dersi geçti mi?: {gecme_durumu}") # True


#-------------------------------------------------------
# ÖRNEK 5: Pratik Kasa Hesaplayıcı (Aritmetik & Atama) :
#-------------------------------------------------------
""" 
Senaryo: Bir markette alışveriş yapıyorsun ve aldığın ürünlerin KDV dahil fiyatını hesaplaman gerekiyor.Ama tutar belli değil kullanıcıdan alacaksın o fiyatı.
"""

fiyat=float(input("Lütfen tutarı TL cinsinden giriniz."))
kdv_orani=0.20  # -> %20 KDV

# İşlemli atama kullanarak fiyatı güncelle
fiyat += (fiyat * kdv_orani)  # Aslında mana şu : fiyat=fiyat +(fiyat*kdv_orani) 
                              # Fiyatın üzerine KDV eklenir.

print(f"Ödenecek Toplam Tutar:{fiyat} TL")
print(f"Ödenecek Kuruş Kısmı:{fiyat %1}") #Mod operatörü ile kuruş kontrolü (1 ile bölümünden kalan)


#----------------------------------------------------------------
# ÖRNEK 6: Akıllı Ehliyet Sorgulama (Mantıksal & Karşılaştırma) :
#----------------------------------------------------------------
"""
Senaryo: Yaş, sağlık ve sabıka durumuna göre ehliyet alınıp alınamayacağını kontrol eden bir mantık kur.
"""
yas=19
saglik_raporu=True
sabika_kaydi=False

# Şart: Yaş 18'den büyük/eşit OLMALI ve Diğer şartlar sağlanmalı.
onay=((yas>18) and saglik_raporu and (not sabika_kaydi))
print(f"Ehliyet alabilir mi ?:{onay}")  # -> True veya False döner.


#------------------------------------------------------
# ÖRNEK 7: Yasaklı Kelime Filtresi (Aitlik Operatörü) :
#------------------------------------------------------
"""
-> Senaryo: Bir kullanıcının yazdığı mesajda istemediğimiz bir kelime olup olmadığını denetle.
"""
mesaj="Python öğrenmek gerçekten harika ve çok eğlenceli!"
yasakli_kelime="kötü"

# in ve not in kullanımı
var_mi= yasakli_kelime in mesaj
guvenli_mi="harika" in mesaj and "kötü" not in mesaj

print(f"Mesajda yasaklı kelime var mı ?: {var_mi}")
print(f"Mesaj yayınlanabilir mi ?:{guvenli_mi}")


#------------------------------------------
# ÖRNEK 8: Bellek Dedektifi (Kimlik & id) :
#------------------------------------------
"""
-> Senaryo: Python'un belleği nasıl yönettiğini (Interning) test eden küçük bir deney yap.
"""
a=256
b=256
c=300
d=300

print(f"a ve b aynı adreste mi ? : {a is b}")
print(f"c ve d aynı adreste mi ? : {c is d}")
print(f"id(a):{id(a)}| id(c):{id(c)}")

#Çıktı: a ve b aynı adreste mi ? : True
#Çıktı: c ve d aynı adreste mi ? : True
#Çıktı: id(a):140715902145416| id(c):2783382396944

"""
 Normalde teorik olarak 256 sınırı beklense de, senin bilgisayarında (veya kullandığın editörde) her iki sonucun da True çıkmasının çok mantıklı ve profesyonel bir sebebi var.
 Senin tarzında, bu durumu ve Python'un arka planındaki o "uyanıklığı" açıklayalım:

Neden İkisi de True Çıktı?
-> 1. Derleyici Optimizasyonu (Constant Folding): Modern Python sürümleri ve özellikle PyCharm, VS Code gibi editörler ya da bir dosyayı bütün olarak çalıştırdığında; Python kodu çalıştırmadan önce bir "tarama" yapar.
 Eğer aynı satırlarda veya aynı kod bloğunda aynı sabit değerlerin (300 gibi) kullanıldığını görürse, bunları bellekte tek bir yere kaydeder ve her iki değişkeni de oraya yönlendirir.
-> 2. Etkileşimli Kabuk (Shell) vs. Dosya: Eğer bu kodu satır satır Python terminaline (IDLE veya CMD gibi) yazsaydın, 300 için büyük ihtimalle False alacaktın. 
 Çünkü terminal her satırı ayrı ayrı değerlendirir. Ama bir .py dosyası olarak çalıştırdığında Python "Bu iki değer de aynı, neden boşuna yer kaplayayım?" diyerek ikisini de aynı adrese bağlar.
"""

#-----------------------------------------------
# ÖRNEK 9: Basit Birim Dönüştürücü (Aritmetik) :
#-----------------------------------------------
"""
-> Senaryo: İnç olarak verilen bir uzunluğu santimetreye çevir ve sonucun sadece tam kısmını göster.
"""

inc_degeri=10
cm_karsiligi=inc_degeri*2.54  # -> 1 inç = 2.54 cm

# Sonucun tam kısmını (integer) ve ondalık kısmını ayır
print(f"Toplam CM: {cm_karsiligi}")
print(f"Sadece Tam Kısmı: {cm_karsiligi // 1}") # -> Tam bölme operatörü


#------------------------------------------------------------
# ÖRNEK 10: Gelişmiş Giriş Kontrolü (Short-Circuit & Logic) :                                 
#------------------------------------------------------------
kullanici_adi = "admin"
sifre = "1234"
giris_denemesi = "admin"
sifre_denemesi = "1234"

# En profesyonel karşılaştırma:
basarili = (giris_denemesi == kullanici_adi) and (sifre_denemesi == sifre)
print(f"Sisteme Giriş Başarılı mı?: {basarili}")


# ===========================================================================================================================================
"""
 Elhamdülillah, 5.Bab ile operatörlerin ilmine vakıf olduk ve 10 ayrı mesele üzerinde tefekkür ederek zihnimizi keskinleştirdik. 
 Bu on uygulama, kuru bir bilgiden ibaret kalmayıp, programın ruhuna nüfuz eden birer 'Hâl'  ve meyve veren birer 'Amel' olmuştur.
"""
# ===========================================================================================================================================
#  BAB 5 (PYTHON'DA OPERATÖRLER VE OPERANDLAR) PROJE LİSTESİ :                                                                              |
# ===========================================================================================================================================
#  ÖRNEK 1 : Banka Kredisi Onay Mekanizması (Mantıksal 'and' Operatörü Uygulaması)                                                          |  
#  ÖRNEK 2 : İndirim Kuponu Sistemi (Mantıksal 'or' Operatörü Uygulaması)                                                                   |
#  ÖRNEK 3 : Sistem Bakım Modu Güvenlik Katmanı (Mantıksal 'not' Operatörü Uygulaması)                                                      |  
#  ÖRNEK 4 : Karmaşık Akademik Başarı Filtresi (Operatör Önceliği ve Parantez Kurgusu)                                                      |  
#  ÖRNEK 5 : Pratik Market Kasası ve KDV Hesaplayıcı (Bileşik Atama ve Modül Operatörü)                                                     |     
#  ÖRNEK 6 : Akıllı Ehliyet Sorgulama Sistemi (Karşılaştırma ve Mantık Kombinasyonu)                                                        |
#  ÖRNEK 7 : Güvenli Mesaj ve Yasaklı Kelime Filtresi (Aitlik 'in/not in' Operatörleri)                                                     |
#  ÖRNEK 8 : Bellek Dedektifi ve Interning Deneyi (Kimlik 'is' ve id() Analizi)                                                             |
#  ÖRNEK 9 : Birim Dönüştürücü ve Tam Sayı Raporlama (Aritmetik ve Tam Bölme '//')                                                          |
#  ÖRNEK 10: Gelişmiş Giriş Kontrolü (Short-Circuit & Logic)                                                                                |
# ===========================================================================================================================================


