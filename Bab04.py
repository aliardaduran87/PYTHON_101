# ============================================================================================
# == BAB 4: TEMEL VERİ TÜRLERİ VE DEĞİŞKENLER (CHAPTER 4 :BASIC DATA TYPES AND VARIABLES) : ==
# ============================================================================================

"""
-> Programlarımız çalıştığında, tüm işlemler bilgisayarın RAM belleği (geçici depolama alanı) üzerinde gerçekleşir.
-> Kalıcı depolama(SSD,HDD) Ram'e göre çok daha yavaştır. Bu yüzden değişkenler Ram'de tutulur ki işlemcinin veriye düşük gecikme ile erişebilmesi için.
-> Program içerisinde kullanılan her veri için bellekte bir yer tahsis edilir.
-> Her bir bellek bölgesinin bir adresi vardır ancak adreslerle işlem yapmak zordur.
-> Bu nedenle bellekteki verilere erişmek için , verinin tutulduğu bellek bölgesine sembolik isimler verilir.
-> Bir bellek bölgesine işaret eden bu sembolik isimlere "değişken" denir.
-> Değişkenler sadece tam sayıları değil ; ondalık sayıları, metinleri, doğru ya da yanlış gibi ifadeleri de hafızada tutabilir.
-> Kısacası değişkenler, bir veri türüne ait değeri tutar.
-> Değişkenler, verinin tutulduğu bellek bölgesine erişmek ve onu program akışı sırasında değiştirmek için kullanılır.
-> Değişkenler, karmaşık bellek yönetimini programcıdan soyutlar (gizler).
-> 0x7A320F adresindeki bir sayıyı okumak yerine, kullanici_yasi gibi anlamlı bir isimle okumak, kodu daha okunabilir hale getirir.
-> Değişkenler, veriyi sadece saklayan "kutular" değildir.
-> Bunlar kodun bakımını kolaylaştıran, hataları azaltan ve programı insana okunabilir kılan soyutlama araçlarıdır. Bir yazılım sisteminin sağlıklı çalışması için olmazsa olmazlardır.

Özet olarak Değişken, bir değeri bilgisayarın geçici belleğinde (RAM) depolamak ve o değere daha sonra ulaşabilmek için ona verdiğimiz isimlendirilmiş bir etikettir.
"""


#--------------------------------
# DEĞİŞKEN ADLANDIRMA KURALLARI :
#--------------------------------
"""
--------------------------------------------------------
# ZORUNLU SÖZ DİZİMİ KURALLARI (Mandatory Syntax Rules) :
--------------------------------------------------------
-> Bu kurallar Python yorumlayıcısı tarafından belirlenir ve herhangi birinin ihlali Syntax Error (Söz Dizimi Hatası) ile sonuçlanır.
-> Değişken adlarının başlarında rakam bulunamaz. Örneğin 1sayi isminde değişken tanımlaması yapılamaz.
-> Yapıldığı takdirde bu  hatayı alır -> SyntaxError: invalid decimal literal -> (Python'da yazım kurallarına uymayan bir sayısal ifade kullandığında karşına çıkan bir Sözdizimi Hatasıdır.)

-> Değişken adları içerisinde başında olmamak kaydıyla rakam kullanılabilir. Örneğin sayi1 isimli değişken tanımlaması geçerlidir.
-> Değişken adlarında boşluk kullanılamaz. Örneğin; ilk sayı şeklinde ,iki kelime arasına boşluk kullanılarak bir değişken tanımlanamaz.
-> sayi 3=4 gibi yazınca şu hata ile karşılaşılır. SyntaxError: invalid syntax

-> Değişken adlarında alt çizgi(_) haricinde özel karakter kullanılamaz. Değişken adlarının başında da alt çizgi karakteri kullanılabilir.
-> Örneğin ; ilk_sayi ya da _sayi şeklinde tanımlanabilir.
-> Programlama dilinin rezerve olduğu kelimeleri değişken adı olarak kullanılamaz. Örneğin ; True,False,if,else,return,class,break,continue,and,or gibi

-> İki farklı kelimeden oluşuyorsa alt tire (_) ile birleştirilir. 

-> Değişkenleri adlandırırken İngiliz alfabesindeki karakterleri kullanmak uygundur.
-> Python dili büyük-küçük harfe duyarlı (case-sensitive) bir dildir.
-> Aslında yukarıdaki cümle şu anlama geliyor: Okunuşları her ne kadar aynı olsa da yazılışları farklı olduğu için Python için 2 ayrı değişkendir alttaki örnek.
   Örneğin ;
"""

sayi=35
print(sayi)       #Çıktı: 35

Sayi=34
print(Sayi)       #Çıktı: 34

_ilksayi=33       #Mesela bu kullanım doğrudur.
print(_ilksayi)

kapi_uzunlugu=2.1 #Burada alt tire(_) ile birleştirdik.
print(kapi_uzunlugu)


#-------------------------------
# NOTASYON ADLANDIRMA STİLLERİ :
#-------------------------------
"""
-> Değişkenlere isim verirken belirli bir standart oluşturmak için kullanılır.
-> Zorunlu değildir. Bir kültür niteliğindedir.
-> Python topluluğu standartı olan PEP 8'e uyumu sağlamak için kullanılır.

#--------------------
 1.Pascal Notasyonu :
#--------------------
-> Değişken isimlerindeki her bir kelimenin yalnız ilk harfi büyük yazılır.
-> Genelde Sınıf İsimleri (Class Names) için standarttır.
HesapMakinesi , VeriTabani_Baglantisi , AdSoyad , IlkSayi , SuBasinci

#-----------------------
 2.camelCase Notasyonu : 
#-----------------------
-> İlk kelime tamamen küçük , diğerlerinin ilk harfi  büyük yazılır.
-> Kelimeler arasında boşluk bırakılmaz.
adSoyad, ilkSayi ,suBasinci

#-----------------------
 3.Hungarian Notasyonu : 
#-----------------------
-> Değişken adının ilk birkaç harfi ,değişkenin ne olduğunu çağrıştıran bir kısaltmadır.

fltSayi=float türünde bir değişken için
strAciklama=string türünde bir değişken için

#-------------
 4.UPPERCASE : 
#-------------
-> Değişken adındaki tüm harfler büyük yazılır.
-> Kelimeler alt çizgi(_)ile ayrılır.
-> Genelde program boyunca ASLA değişmeyecek olan Sabitler(Constants) için kullanılır.
ADSOYAD, ILKSAYİ , SUBASINCI , PI_SAYISI, MAX_HIZ_LIMITI

#-------------------
 5.snake_notasyonu : 
#-------------------
-> Değişken adını oluşturan kelimeler arasında alt çizgi(_) kullanılır.
ad_soyad AD_SOYAD
"""


#---------------------------
# DEĞİŞKENLERE DEĞER ATAMA :
#---------------------------
"""
-> Değişkenlere değer ataması yapılırken = operatörü kullanılır.
a=4  -> #Burada 4 değeri a değişkenine atanmıştır.
-> Atama işlemi daima "sağdan sola" olur.

#-------------------------
 Zincirleme atama işlemi :
#-------------------------
a=b=c=d=100

#------------------
 Eş zamanlı atama :
#------------------
x,y,z=3,5,8

-> Burada farklı türlerde de atama yapabilirsin.

x,y,name,isStudent=(1,2.3,"Ali","False")

# Burada da a değişkenine b'nin değeri , b değişkenine a'nın değeri eş zamanlı olarak atanmıştır.
a=1
b=2
a,b=b,a
"""

#--------------------------------------------
# DİNAMİK TİPLEME (DYNAMIC TYPING) ÖZELLİĞİ :
#--------------------------------------------
"""
-> Python, "Dinamik Tipli" (Dynamic Typing) bir dildir. 
-> Statik dillerin (C++, Java, C#) aksine, Python'da bir değişkeni tanımlarken türünü (int, str vb.) belirtmek zorunda değilsiniz.
-> Bir değişkenin türü, ona atanan "değere" göre çalışma anında (runtime) otomatik olarak belirlenir.
-> Aynı değişken ismi, programın ilerleyen safhalarında farklı türden bir veriyi temsil edebilir.
"""

x = 105        # x şu an bir tam sayı (int)
print(type(x)) #Çıktı: <class 'int'>

x = "Python"   # Aynı x artık bir karakter dizisi (str). Python buna izin verir!
print(type(x)) #Çıktı: <class 'str'>

"""
NOT: Bu durum yazılımcıya büyük bir hız ve esneklik kazandırır. 
Ancak değişkenin türü beklenmedik bir anda değişebileceği için, karmaşık projelerde dikkatli takip edilmelidir.
"""

#------------------
# SABİT(CONSTANT) :
#------------------
"""
-> Tamamlandıktan sonra değeri değiştirilemeyen veri demektir.
-> Python'da sabitler için özel bir anahtar kelime yoktur. 
-> Ama geleneksel olarak sabitler tamamen büyük harflerle yazılır.
"""
API_KEY = "XYZABCD"
PI = 3.141592

#-------------
# VERİ (DATA):
#-------------
"""
-> Bilgisayarın depolayabileceği, işleyebileceği, aktarabileceği temsil edilebilir her türlü bilgi parçasıdır.
-> Tek başına anlamı olmayan işlenmemiş ham bilgiye "veri" denir.
"""

#----------------------------
# VERİ TÜRLERİ (DATA TYPES) :
#----------------------------
"""
-> Bir verinin bellekte nasıl saklanacağını ve onunla hangi işlemlerin yapılabileceğini belirleyen sınıflandırmadır.
-> Python'da 3 ana temel veri türü vardır.Bunlar;

1.Sayısal türler (tam sayi,ondalikli sayı,karmaşık sayı türleri)
2.Karakter dizileri
3.Mantıksal veri türleri (doğru/yanlış)

-> Ama aslında diğer veri türleri bu ana veri türlerinin altındaki veri türleridir.

-----------------------------------------
| int > Tam sayılar                     |
| float > Ondalıklı sayılar             |
| complex > Karmaşık sayılar            |
-----------------------------------------
| str > Metin                           |
-----------------------------------------
| bool > Mantıksal değerler             |
-----------------------------------------
| list  > Liste                         |
| tuple > Değiştirilemez liste          |
| dict  > Sözlük(anahtar-değer yapısı)  |
| set   > Benzersiz elemanlar kümesi    |
-----------------------------------------
| NoneType > Boş değer                  |
-----------------------------------------

NOT: Eğer Python'da bir değişkenin değerini sonradan belirlemek istersek geçici olarak None (atanmamış anlamında) değerine eşitleyebilirsiniz.
"""

#-----------------------------------------
# 1.SAYISAL VERİ TÜRÜ (NUMBER DATA TYPE) :
#-----------------------------------------

"""
-> Python3 içerisinde 3 farklı sayısal veri türü vardır.Bunlar:

-------------------------------------------------------
 int      -> Tam sayılar için. Örneğin 35             |
 float    -> Ondalık kısmı olan sayılar için. 1.37    |
 complex  -> Karmaşık sayılar için . Örneğin 9+4j     |
-------------------------------------------------------
"""
a = 35
b = 1.37
c = 9+4j

print(type(a))
print(type(b))
print(type(c))

#-------------------------------
# 2.KARAKTER DİZİLERİ (STRING) :
#-------------------------------
"""
-Karakter dizileri bir ya da birden fazla karakterin birleşimi ile oluşan sözcük yapılarıdır.
-Python'da tek veya çift tırnak işareti ile gösterilir.

"""
str1 = 'Merhaba'
str2 = 'günaydin'
karakter1 = "a"
karakter2 = "b"

print(str1)
print(str2)
print(karakter1)
print(karakter2)
print(type(str1))


#----------------------------------
# 3.MANTIKSAL VERİ TÜRÜ (BOOLEAN) :
#----------------------------------
"""Mantıksal veri türü içerisinde doğru ya da yanlış ifadeleri saklanabilir. Python'da doğru, True ifadesi ile ; yanlış , False ifadesi ile gösterilir."""
m1 = True
m2 = False
m3 = 2 < 3
print(m3)

"""
deneme="merhaba'
print(deneme)
-> Bu ifade şu hatayı verir. SyntaxError: unterminated string literal (Sonlandırılmamış Dize Sabiti hatası)
"""

"""
------------------
 Karakter (char) :
------------------
-> Tanım: Tek bir sembolü temsil eder. Örneğin 'a', '5', '?'.
-> Boyut: Genellikle bellekte 1 byte (8 bit) yer kaplar (dil ve encoding’e göre değişebilir).
-> Kullanım: Tek bir harf veya sembol üzerinde işlem yapmak için kullanılır.

---------------------------
 Karakter Dizisi (String) :
---------------------------
-> Tanım: Birden fazla karakterin yan yana gelmesiyle oluşan dizidir. Örneğin "Ali", "12345", "Merhaba Dünya".
-> Boyut: Uzunluğuna bağlı olarak birden fazla byte kaplar.
-> Kullanım: Metinleri saklamak, işlemek, üzerinde arama/substring gibi işlemler yapmak için kullanılır.

-> Böylelikle bu farkı da anla çünkü çoğu programlama dilinde karakter ve karakter dizileri ayrı ayrı veri türleridir.
-> Tek bir karakter ifade edilirken tek tırnak içerisinde, karakter dizisinde çift tırnak ile gösterilir. 
-> Python'da ister tek karakter ister çift karakter hepsi string olarak ifade edilir.
-> Yani tek tırnak ya da çift tırnak kullanımı fark etmez. 

"""
#---------------------------------------------
# TÜR DÖNÜŞÜMÜ(TYPE CONVERSION/TYPE CASTING) :
#---------------------------------------------

"""
-> Bir veri türündeki bir değeri alıp , onu başka bir veri tipine çevirme işlemidir.

#------------------------------------------------------
 1.Örtülü Dönüşüm:(Implicit Conversion/Type Coercion) :
#------------------------------------------------------
-> Python gibi programlama dilinin bir işlem sırasında veri kaybını önlemek veya işlemi mümkün kılmak için "programcıdan izin almadan otomatik olarak yaptığı" dönüşümdür.
-> Genellikle matematiksel işlemler sırasında , farklı veri tipleri araya geldiğinde gerçekleşir.
-> Daha dar tip daha geniş tipe yükseltilir.
"""
print(2+4.5)   #Çıktı: 6.5 Burada integer olan 2 veri tipi otomatik olarak 2.0 float veri tipine dönüştürülür.

"""
#--------------------------------------------------
 2.Açık Dönüşüm(Explicit Conversion/Type Casting) :
#--------------------------------------------------
-> Programcının kod içinde bir fonksiyon kullanarak bir tipi bilinçli ve zorla bir tipe çevirmesi işlemidir.
-> input() fonksiyonu ile aldığımız metni sayıya çevirmek gibi otomatik dönüşümün yetersiz kaldığı veya "veri kaybını programcının onayıyla olan durumlarda" yapılır.
"""
a = int(3.6)
print(a)       #Çıktı: 3 veri kaybı var

"""
-> Bir sayı (int) ile bir string toparlanamayacağından dolayı aşağıdaki kod hata verir.
print(1+"2")   #Çıktı: TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

#---------------------
# input() FONKSİYONU :
#---------------------
"""
-> Kullanıcıdan veri almayı sağlayan input() fonksiyonu , herhangi bir programın (etkileşimli) olmasını sağlayan temel bir araçtır.
"""

"""
int()
-> Başka bir türdeki veriyi tam sayıya dönüştürmek için kullanılır.

float()
-> Herhangi bir türdeki veriyi ondalıklı sayıya(kayan noktalı sayı) dönüştürmek için kullanılır.

str()
-> Herhangi bir türü karakter dizisine (string) dönüştürmek için kullanılır.

chr()
-> Sayısal bir değeri karaktere dönüştürmek için kullanılır.

ord()
-> chr() ile tam tersi işlevde olan ord(), herhangi bir karakterin onlu tabandaki sayı karşılığını verir.

bool()
-> Herhangi bir verinin mantıksal karşılığnı elde etmek için kullanılır.


NOT: Lakin her dönüşüm başarıyla olmuyor.
int("Merhaba") 
# Hata: ValueError: invalid literal for int() with base 10: 'Merhaba'

-> int(3.99)  3 (3.99'u 4'e yuvarlamaz, 0.99'u keser.)
"""
a = "12"
b = int(a)
print(b) #Çıktı:12
"""
a=int(input("Lütfen sayı giriniz:"))
c=a+5
print(c)
"""

a = 2.5
b = int(a)
print(b) #Çıktı:2

sayi = float(input("Bir sayi giriniz:"))
print(sayi)
print(type(sayi))

no = 185
adres = str(185)+".cadde"
print(adres)      #Çıktı:185.cadde

karakter = chr(65)
print(karakter)   #Çıktı:A

sayi = ord("A")
print(sayi)       #Çıktı:65
 
print(bool(1))
print(bool(0))
print(bool("a")) # İçinde en az bir karakter olan (boş olmayan) tüm metinler (string) True kabul edilir.
print(bool(""))  # Boş bir metin (""), hiçbir veri içermediği için "yokluk" belirtir ve False döner.


#----------------------------------------------------
# Print() komutu ile karakter dizilerinin kullanımı :
#----------------------------------------------------
"""
-> 3 farklı seçenek vardır.
1.Tek tırnak('')
2.Çift tırnak("")
3.Üç adet çift tırnak(""" """)

-> Tek veya çift tırnak "string ifadeleri" belirtmek için kullanılır.
"""
print('merhaba dünya')
print("merhaba dünya")
print("""merhaba dünya""")

#-> """ """ çok satırlı yorum” gibi kullanır.

print(""" ----------------------Lütfen seçim yapınız------------------)
      1.Kayıt ekle
      2.Ara
      3.Çıkış
      ---------------------------------------------------------""")
#-------------------
# Yorum Satırı (#) : => Yorum satırını da yorum satırına aldık :)
#-------------------
# Gerçek yorum: Python yorum satırlarını # ile tanır.
# Çalıştırılmaz, ekrana basılmaz, belleğe alınmaz.
print("#Bu açıklama satırı değildir.")


#-------------------------------------------
# Üç Tırnak (""" ... """ veya ''' ... ''') :
#-------------------------------------------
"""
-> Çok satırlı string oluşturur.
-> Eğer bir değişkene atanırsa string olarak saklanır.
-> Eğer atanmazsa, Python onu görmezden gelir → genellikle docstring (belge açıklaması) olarak kullanılır.
"""


#----------------------------
# PARAMETRELER (PARAMETERS) : 
#----------------------------
"""
-> Parametre (Teknik Tanım) : Bir fonksiyonun görevini nasıl yapacağını belirleyen dışarıdan gelen ayarlardır.
-> print() fonksiyonu, sadece ekrana yazı yazmaz; yazıyı "nasıl" yazacağını da bu parametrelerle belirler.
"""


#---------------------------------
# 1. SEP (SEPARATOR) PARAMETRESİ : 
#---------------------------------
"""
-> Anlamı : Ayırıcı (Separator) demektir.
-> Görevi : print() içinde virgülle ayırdığımız her bir veri arasına ne koyulacağını belirler.
-> Ön Tanımlı Değeri : Eğer biz bir şey yazmazsak, Python otomatik olarak bir boşluk (" ") koyar.
-> sep parametresi ile belirtilen ayraç mutlaka bir karakter dizisi olmalıdır. Bir sayı ya da başka veri türü ayraç olarak kullanılamaz. Yoksa hata veriyor.
"""

print("İstanbul","Ankara","İzmir",sep="-")   #Çıktı: İstanbul-Ankara-İzmir
print("Türkçe","Matematik","Fen Bilimleri","Sosyal Bilgiler","Din Kültür","İngilizce",sep="-")  #Çıktı: Türkçe-Matematik-Fen Bilimleri-Sosyal Bilgiler-Din Kültür-İngilizce
print(1,2,3,4,5,sep="0")  #Çıktı: 102030405

"""
print(1,2,3,4,5,sep=0) 
#Çıktı:TypeError: sep must be None or a string, not int -> 4.maddedeki hata bu .
"""

#--------------------
# 2.END PARAMETRESİ : 
#--------------------
"""
-> Anlamı : Son (End) demektir.
-> Görevi : print() fonksiyonu işini bitirdikten sonra en sona ne koyacağını belirler.
-> Ön Tanımlı Değeri : Alt satıra geçme komutudur (\n). Bu yüzden her print bir alt satıra geçer.
-> Örn : print("Selam", end="!") -> Çıktı: Selam! (Alt satıra geçmez)
"""

print("Python öğrenmek çok kolay",end="!")
print("Artık ne zaman başlayacaksın",end="!")


#----------------------------------------------
# yıldız* işareti ile karakterleri ayrıştırma :
#----------------------------------------------

print("1","2","3","4","5",sep="-") 
#-> Yukarıdaki satırdaki gibi yapmak terine şu şekilde yapılabilir.


print(*"12345",sep="-")
# Bu kodda ifadenin başında yıldız olduğuna dikkat edin. Bu işaret kendinden sonra gelen karakter dizisi içerisindeki her bir karakteri birbirinden ayırma fonksiyonu yerine getirir.
# Her bir karakteri birbirinden ayırma fonksiyonu yerine getirir.


#---------------------
# KAÇIŞ PARAMETRELERİ: 
#---------------------
"""
-> Bir karakter dizisi içerisinde yer alan ve özel anlamları olan karakterlerdir."\" işaretinden sonra gelen bir karakter ile gösterilir.
-> Tanım : Metin dizileri (string) içerisinde özel bir anlam ifade eden veya yazılması 
   doğrudan mümkün olmayan karakterleri belirtmek için kullanılır.
-> Yapı : Daima ters bölü ( \ ) işareti ile başlar. Buna "kaçış" denmesinin sebebi, 
   Python'un o anki karakteri normal okuma düzeninden "kaçırıp" özel bir anlam yüklemesidir.


\n karakteri:(newline->yeni satır)
-> Bir string içerisinde bulunduğu yerden itibaren yeni bir satıra geçileceğini gösterir.

\t karakteri:(Horizontal Tab-Sekme)
-> String ifade içerisinde kullanıldığı yerde Tab karakteri kadar boşluk bırakılmasını sağlar.

\a karakteri:
-> Zil ya da alarm karakteri olarak bilinen \a bilgisayar üzerinde "bip" sesi çıkmasını sağlar.  #Ama denememe rağmen başaramadım :( 

\b karakteri:(backspace)
-> Klavye üzerindeki Backspace tuşunun görevini yerine getirir.
-> Karakter dizisi içerisinde bulunduğu noktada, imleci bir karakter sola kaydırarak silme işlemi yapar.

\r karakteri:(return)
-> Karakter dizisi içerisindeki bulunduğu noktadan itibaren satır başına kadar olan kısmı siler. 
-> Satır başına dönme (return) karakteridir.
"""


print("merhaba\npython")
print("A\tB\tC")
print("\a")
print("pythoo\bn")
print("python\rprogramlama")

#-------------------------------------------
# KAÇIŞ KARAKTERLERİNİ ETKİSİZ HALE GETİRME:
#-------------------------------------------
"""
Stringin doğasında olan \ ile başlayan ifadelerin escape olarak yorumlanmaması için :
1-) İki tane \\ kullanılabilir.
2-) String ifadenin başına r harfi konulabilir.
"""
print("D:\nevşehir\gezi")
print("D:\\nevşehir\gezi")
print("E:\taslak\raporlar\nisan 2016")
print(r"E:\taslak\raporlar\nisan 2016")


#--------------------------------------------
# STRİNG BİRLEŞTİRME (STRING CONCETENATION) :
#--------------------------------------------
"""
-> İki veya daha fazla metin dizisini (stringi) alıp art arda ekleyerek yeni ve tek bir metin dizisi oluşturma işlemidir.
"""
#---------------------------
# 1.Temel Artı(+)Operatörü :
#---------------------------
"""
-> Bu, küçük sayıda stringi birleştirmek için en anlaşılır ve hızlı yazılan yöntemdir.
-> + operatörü çok sayıda stringi birleştirirken çok verimsizdir ve yavaş çalışır.
"""
str1="Merhaba"
str2="Python"
str3=str1+str2
print(str3)

#--------------------------------------------------------------
# 2.EN OKUNABİLİR YÖNTEM F-stringler (Formatlanmış Stringler) :
#--------------------------------------------------------------
"""
-> Bu yöntem , Python 3.6 ve sonrası için en çok önerilen ve en okunabilir yöntemdir.
-> Değişkenleri metnin içine süslü parantez {} kullanarak doğrudan yerleştirmemize olanak tanır.
-> Stringin başına f koymak zorunludur.
-> String interpolasyonu olarak da geçer.
"""

isim = input("Lütfen isminizi giriniz: ")
soyisim = input("Lütfen soyisminizi giriniz: ")
print(f"İsmim:{isim}\n soyisimim:{soyisim}")

#--------------------
# 3. .format METODU :
#--------------------
s1 = "Ali"
s2 = "Merhaba"
s3 = "{a1} Sayin {a2} Nasılsiniz ?".format(a1=s1,a2=s2)
print(s3)

#-------------------------------------
# 4.EN VERİMLİ YÖNTEM (.join metodu) :
#-------------------------------------
"""
-> Büyük veri kümelerini veya bir iterasyondaki tüm ögeleri birleştirmek için performansı en yüksek yöntemdir.
-> Diğer yöntemlere göre daha hızlı olmasının nedeni bellek yönetimi ve tek bir işlemde birleştirme yeteneğidir.
-> iterable (üzerinde gezilebilir) olan her türlü veri yapısıyla çalışır.
iterasyon=Bir veri kümesinin üzerindeki her bir ögeye sırayla erişme ve bunları tek tek işleme sürecidir.
"""

kelimeler = ["Python","101","öğreniyorum"]
ayirici = ""
sonuc = ayirici.join(kelimeler)
print(sonuc)

#-------------------------------
# BİR İFADEYİ ÇOK KEZ YAZDIRMA :
#-------------------------------
"""
-> Print() içindeki belirli bir ifadeyi çok kez yazdırmak için tekrar edeceği adet çarpan olarak yazılır.
"""
print(5*"merhaba\n")
# ifadeyi 5 kez alt alta yazar.

# Format fonksiyonlarını akılda tutmak zor olduğu için ve fazla olduğu için unuttuğunda şu siteye bakabilirsin.
# https://pyformat.info/

#------------------------------------------------
# input() FONKSİYONU İLE KULLANICIDAN VERİ ALMA :
#------------------------------------------------
"""
-> Programlamada bazı değerlerin kullanıcılar tarafından girilmesi gerekebilir.
-> Kullanıcıdan değer almak için input() fonksiyonu kullanılır.
-> Lakin kullanıcı hatalı bir şey girerse program hata verir.
-> İleriki konularda (try except ile hata ayıklama konusunda) anlatılacaktır.

->Parantez işareti fonksiyon çağırıyor.(Function Call)

1.Duraklama: Program, input() fonksiyonuyla karşılaştığında kullanıcının giriş yapmasını beklemek üzere beklemeye geçer.
2.İstem(Prompt): Fonksiyonun içine bir metin (string) geçirerek kullanıcıya ne girmesi gerektiğini belirten bir mesaj gösterebilirsiniz. Buna prompt (istem) denir.
3.Giriş ve Onay: Kullanıcı bir şeyler yazar ve genellikle enter tuşuna basar.Hatta enter tuşuna basasıya kadar program bekler.
4.Dönüş Değeri: Kullanıcının girdiği tüm değer, input() fonksiyonundan String veri tipi olarak geri döner ve bir değişkene atanır.
"""

# ========================================================================================================
# == BAB 4:  TEMEL VERİ TÜRLERİ VE DEĞİŞKENLER PROJELERİ (PROJECTS ON BASIC DATA TYPES AND VARIABLES) : ==
# ========================================================================================================

#--------------------------------------------------------------------------------------
# ÖRNEK 1: Kullanıcının ismini alarak Merhaba (Kullanıcı ismi) yazdıran Python örneği :
#--------------------------------------------------------------------------------------
isim = input("İsminizi giriniz: ")
print("Merhaba"+isim)


#----------------------------------------------------------------------------------------------
# Örnek 2: Girilen 2 sayının toplamını ve ortalamasını bulan ve ekrana yazdıran Python örneği :
#----------------------------------------------------------------------------------------------

# Örnek 1: Erken Dönüşüm
sayi1 = float(input("Lütfen 1.sayıyı giriniz: ")) # Giriş anında string'i float'a çevir
sayi2 = float(input("Lütfen 2.sayıyı giriniz: ")) # Giriş anında string'i float'a çevir
toplam = sayi1 + sayi2
ortalama = (toplam) / 2 
print("Toplam:",toplam)
print("Ortalama:",ortalama)

# Örnek 2: Geç Dönüşüm
sayi1 = input("Lütfen 1.sayıyı giriniz: ")           # sayi1 burada string'dir
sayi2 = input("Lütfen 2.sayıyı giriniz: ")           # sayi2 burada string'dir
toplam = float(sayi1) + float(sayi2)                 # Toplama yaparken string'i float'a çevir
ortalama = float((float(sayi1) + float(sayi2)) / 2)  # Tüm işlemi parantez içine alıp sonucu float'a çevir
print(toplam)
# Ortalamada yine 'sayi' hatası var ve gereksiz 'float()' kullanımı mevcut.


#---------------------------------------------------------------------------------------------
# Örnek 3: Girilen Vize ve Final Notu Ortalaması Hesaplayan ve ekrana yazdıran Python Örneği :
#---------------------------------------------------------------------------------------------
vize = float(input("Lütfen vize notunu giriniz: "))
final = float(input("Lütfen final notunu giriniz: "))
ders_Notu = (vize*0.4) + (final*0.6)
print(ders_Notu)

print(f"Ortalamam: {ders_Notu}") # Bu tarz formatting ile de yazılabilir tercih kullanıcıya kalmış.


#------------------------------------------------------------------------------------------------------------------------------
# Örnek 4: Girilen ilk sınav %10 ikinci sınav %20 üçüncü sınav %30 dördüncü sınav ise %40 olan sınav sistemi notunu hesaplama :
#------------------------------------------------------------------------------------------------------------------------------
sinav1 = float(input("Lütfen 1.sınav notunu giriniz: "))
sinav2 = float(input("Lütfen 2.sınav notunu giriniz: "))
sinav3 = float(input("Lütfen 3.sınav notunu giriniz: "))
sinav4 = float(input("Lütfen 4.sınav notunu giriniz: "))
ortalama = (sinav1*0.1) + (sinav2*0.2) + (sinav3*0.3) + (sinav4*0.4)
print(ortalama)


#-------------------------------------------------------------------------------------------------------------------
# Örnek 5: Kullanıcıdan alınan değerlerle dikdörtgen alan ve çevresini hesaplayan ve ekrana yazdıran Python Örneği :
#-------------------------------------------------------------------------------------------------------------------
kisa_kenar = float(input("Lütfen kısa kenar uzunluğunu giriniz: "))
uzun_kenar = float(input("Lütfen uzun kenar uzunluğunu giriniz: ")) 
dikdortgen_Cevresi = (kisa_kenar+uzun_kenar)*2
dikdortgen_Alani = (kisa_kenar*uzun_kenar)
print(dikdortgen_Cevresi)
print(dikdortgen_Alani)

#Aslında burada okunabilirliği arttırabilmek için x,y yerine uzun ama okunabilir değişken adları tercih edilmesi daha makuldür.


#----------------------------------------------------------------------------------------------------------------
# Örnek 6: Kullanıcıdan alınan değerlerle karenin alan ve çevresini hesaplayan ve ekrana yazdıran Python Örneği :
#----------------------------------------------------------------------------------------------------------------
kenar_uzunlugu = float(input("Lütfen, karenin kenar uzunluğunu giriniz: "))
karenin_Alani = (kenar_uzunlugu*kenar_uzunlugu)
karenin_Cevresi = (kenar_uzunlugu*4)
print(karenin_Alani)
print(karenin_Cevresi)


#----------------------------------------------------------------------------------------------------------------
# Örnek 7: Kullanıcıdan alınan değerlerle üçgenin alan ve çevresini hesaplayan ve ekrana yazdıran Python Örneği :
#----------------------------------------------------------------------------------------------------------------
kenar1 = float(input("Lütfen 1.kenar uzunluğunu giriniz: "))
kenar2 = float(input("Lütfen 2.kenar uzunluğunu giriniz: "))
kenar3 = float(input("Lütfen 3.kenar uzunluğunu giriniz: "))
ucgenin_Cevresi = (kenar1+kenar2+kenar3)
yari_cevre = (ucgenin_Cevresi)/2
s = yari_cevre
ucgenin_Alani = (s*(s-(kenar1))*(s-(kenar2))*(s-kenar3))**0.5 # Aslında burada karekök almamak için 1/2 nci kuvvetini aldık.

# Ayriyeten şuan görmediğimiz için math kütüphanesini kullanmamaya çalıştık.İlerleyen yerde gösterilecek.
print(ucgenin_Alani)
print(ucgenin_Cevresi)
# Sadece üçgen eşitsizliğini sağlayan değerler için çalışır. Eğer kullanıcı 1, 1, 10 girerse karekökün içi negatif olacağı için kod çöker.


#-----------------------------------------------------------------------------------------------------------------
# Örnek 8: Kullanıcıdan alınan değerlerle dairenin alan ve çevresini hesaplayan ve ekrana yazdıran Python Örneği :
#-----------------------------------------------------------------------------------------------------------------
r = float(input("Lütfen yarıçap değerini giriniz: "))
Pİ_DEGERİ = 3.14 #Genelde sabitler büyük harflerle değişken tanımlaması oluyor.
dairenin_Cevresi = 2*Pİ_DEGERİ*r
dairenin_Alani = Pİ_DEGERİ*r*r
print(dairenin_Cevresi)
print(dairenin_Alani)


#----------------------------------------------------------------------------------------------------------------------
# Örnek 9: Kullanıcıdan doğum yılı alıp 2026 yılında kaç yaşında olduğunu hesaplayan ve ekrana yazdıran Python Örneği :
#----------------------------------------------------------------------------------------------------------------------
mevcut_yil = 2026
dogum_yili = int(input("Lütfen doğum yılını giriniz: "))
yas = (mevcut_yil-dogum_yili)
print(f"2026 yılında yaşınız:{yas}")


# =============================================================================================================================================
"""                                                                                                                                            
 Elhamdülillah, 4.Bab'ın kapısını ilimle aralayıp, hakikatin dokuz farklı tezahürünü (örneğini) amel-i salih niyetine kodlarımıza nakşettik.    
 İlim bir ağaç ise, bu dokuz örnek o ağacın bu fasıldaki kemale ermiş meyveleridir.                                                             
 Ayrıyeten bazı örneklerimizde bazı durumlar (try-except) kısmı şuanlık göz ardı edilip problemin çözümünde özü algılama niyetiyle yaklaştık.   
 Bununla birlikte bu tarz durumlar ilerleyen Bablarda daha detaylı gösterilecektir.                                                             
"""                                                                                                                                             
# =============================================================================================================================================
#  BAB 4: TEMEL VERİ TÜRLERİ VE DEĞİŞKENLER PROJE LİSTESİ :                                                                                    |
# =============================================================================================================================================
#  ÖRNEK 1 : Kullanıcı Karşılama ve Metin Birleştirme Örneği                                                                                   |   
#  ÖRNEK 2 : İki Sayının Toplamı ve Ortalaması (Erken ve Geç Dönüşüm Kıyaslaması)                                                              |  
#  ÖRNEK 3 : Vize ve Final Notu Ortalaması Hesaplayıcı (%40 - %60 Ağırlıklı)                                                                   |
#  ÖRNEK 4 : Çoklu Sınav Sistemi Not Hesaplayıcı (%10, %20, %30, %40 Ağırlıklı)                                                                |
#  ÖRNEK 5 : Dikdörtgenin Alan ve Çevresini Hesaplama (Kullanıcı Girdisi ile)                                                                  |
#  ÖRNEK 6 : Karenin Alan ve Çevresini Hesaplama                                                                                               |
#  ÖRNEK 7 : Üçgenin Çevresini ve Alanını Hesaplama (Heron Formülü ve Üs Alma Metodu)                                                          |
#  ÖRNEK 8 : Dairenin Alanını ve Çevresini Hesaplama (Sabit PI Değeri Kullanımı)                                                               |  
#  ÖRNEK 9 : Doğum Yılı ile Yaş Hesaplama                                                                                                      |
# =============================================================================================================================================
