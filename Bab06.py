# ==================================================================================================
# == BAB 6: PYTHON'DA AKIŞ KONTROL MEKANİZMALARI (CHAPTER 6: FLOW CONTROL MECHANISMS IN PYTHON) : ==
# ==================================================================================================

"""
-> Akış Kontrol Mekanizmaları (Flow Control Mechanisms), bir bilgisayar programında komutların ve talimatların hangi sırayla, hangi koşullar altında ve kaç kez yürütüleceğini belirleyen yapısal araçlardır.
-> Akış Kontrol mekanizmaları ; karar yapıları,döngüler ve atlama ifadeleridir.
-> Basitçe söylemek gerekirse, programınızın bir karar verme, tekrarlama ve dallanma yeteneğine sahip olmasını sağlayan temel mimari öğelerdir.
"""

# -----------------------------------------
# 1. KARAR YAPILARI (DECISION STRUCTURES) :
# -----------------------------------------
"""
-> Karar yapıları , programın çalıştırılması esnasında ortaya çıkan koşullara bağlı olarak programın akışını farklı yollara yönlendiren mekanizmalardır.
-> Koşul ifadesi doğru ya da yanlış sonuç üreten , mantıksal bir ifade olmalıdır.
-> Python’da sıfır (0), None ve boş koleksiyonlar ([], {}, "") False kabul edilir; bunların dışındaki tüm değerler True kabul edilir.
-> Koşul kısmında birden fazla durumu and (ve) veya or (veya) ile birleştirerek daha karmaşık kararlar verebilir.
"""

# ---------------------------------
# A. IF YAPISI (THE IF STATEMENT) :
# ---------------------------------
"""
-> "Eğer" anlamına gelen "if" yapısı, herhangi bir koşulun sağlanması durumunda yapılacak işleri ifade etmek için kullanılır. 
-> if yapısı sadece bir koşul kontrolü olarak değil,programımızın dallanması ve seçici eylem yapmasını sağlayan bir araç olarak görmeliyiz.
-> En basit haliyle, if yapısı bir koşulu test eder. Koşul sağlanırsa(yani sonuç True ise), altındaki girintili(indent) kod bloğu çalıştırılır.
-> Eğer if ifadesindeki koşul True olarak değerlendirilmezse, o bloğun içindeki kodlar yürütülmez ve program bir sonraki adıma geçer.

if kosul_ifadesi:
    # Bu blok ,sadece kosul_ifadesi DOĞRU(True) ise çalışır.
    islemi_yap

-> Kritik Nokta: Python'da kod bloğu, süslü parantezler {} yerine girintileme (indentation) ile belirlenir. Bu, temiz kod yazma standardının bir parçasıdır.
-> Bu özellik de Python'u diğer dillerden ayıran özelliklerden biridir.

# if Koşulu Doğru İse (True):
-> Sadece if bloğunun içindeki girintili kod çalışır.
-> Program, else bloğunu tamamen atlar.

# if Koşulu Yanlış İse (False):
-> if bloğunun içindeki kod atlanır.
-> Program, akışı else bloğunun içindeki girintili koda taşır ve bu kod çalışır.
"""

sicaklik = 25                     # Burada 25 değerini sıcaklık değişkenine atadık.
if sicaklik > 24:                 # Burada if yapısını kullandık ama sonuna 2 nokta koymak önemli!.
    print("hava sıcaktır.")       # Burada bir tab boşluk(4 adet boşluk karakteri) bıraktık.Çünkü python girintilere dayalı bir "sözdizimine(syntax)" sahip.
                                  # Girintiler bize bir kod bloğunun nereye ait olduğunu ifade ediyor.


# Python'da if ifadesinden sonra, def (fonksiyon), for, while, class gibi ifadelerin tamamından sonra iki nokta üst üste (:) konulmasının nedeni, bunun blok başlatma işareti (Block Starter) olmasıdır.
# Bu tasarım tercihi, Python'ı diğer dillerden (C++, Java, JavaScript) ayırır ve kodun karmaşık parantez yığınları yerine görsel olarak temiz bir yapıya sahip olmasını sağlar.
sayi = 50
if (sayi % 2 == 0 and sayi % 5 == 0):
    print("sayi çifttir.")
    print("sayi beşin katıdır.")
    print("Yani sayı 10 ile tam bölünebilmektedir.")
print("merhaba")                # Bu satır koşula bağlı olmayan satır. Çünkü kod bloğunun dışında konumlanmış.


not_ortalamasi = 75
devamsizlik = 4

if not_ortalamasi >= 50 and devamsizlik < 10:
    print("Tebrikler, sınıfı geçtiniz!")
    print("Belgeniz hazırlanıyor.")

# Teknik Not: 'and' operatörü sayesinde her iki koşulun da True olması zorunludur.
# Eğer devamsızlık 12 olsaydı, notu 100 bile olsa bu blok çalışmazdı.
# Ya da tam tersi devamsızlık 0 ama not 49 bile olsa bu blok çalışmazdı.

# -------------------------------------
# B. ELIF YAPISI (THE ELIF STATEMENT) :
# -------------------------------------
"""
-> elif yapısı, birbirine bağlı birden fazla koşulun kontrol edildiği durumlarda, iç içe geçmiş (nested) if-else yığınlarını önleyerek kodun yatayda büyümesini engeller ve okunabilirliği artırır.
-> Bu durumda if else-if oluşur. Python dilinde else-if kısaca elif şeklinde gösterilir.
-> elif bloğu yalnızca kendisinden önceki if (veya varsa önceki elif blokları) koşulları yanlış (False) çıktığında devreye girer.
-> Kısacası ilk koşul doğru olmaması durumunda yedek olarak giren 2.ana karakterimiz gibi. 1.ana karakter varken yok lakin o olmadığınıda devreye giriyormuş gibi düşünebiliriz.
"""

kullanici_yasi = 25

# Birinci bağımsız karar noktası
if kullanici_yasi > 20:
    print("Ödül 1: 20 Yaş Üstü İndirimi Kazanıldı.")
    
# İkinci bağımsız karar noktası
if kullanici_yasi < 30:
    print("Ödül 2: Gençlik Kulübü Üyeliği Kazanıldı.")

# Çıktı:
# Ödül 1: 20 Yaş Üstü İndirimi Kazanıldı. (Çünkü 25 > 20)
# Ödül 2: Gençlik Kulübü Üyeliği Kazanıldı. (Çünkü 25 < 30)

kullanici_yasi = 25

if kullanici_yasi > 20:
    print("Ödül 1: 20 Yaş Üstü İndirimi Kazanıldı.")
elif kullanici_yasi < 30:   # Bu blok hiç çalıştırılmayacak!
    print("Ödül 2: Gençlik Kulübü Üyeliği Kazanıldı.")

# Çıktı:
# Ödül 1: 20 Yaş Üstü İndirimi Kazanıldı.
# (İkinci blok atlandı, çünkü ilk koşul doğruydu.)

# Aslında bu 2 örnek arasındaki farka bakınca elif ile yazmak daha mantıklı çünkü diğerinde doğru çalışmayabiliyor.
sicaklik = 25
if sicaklik > 30:
    print("Hava sıcaktır.")
elif 20 <= sicaklik <= 25:
    print("Hava ılıktır.")
elif 15 <= sicaklik <=20:
    print("Hava hafif soğuk")

"""
-> if sicaklik > 30: satırı çalışıyor mu?	EVET (Değerlendirme yapıyor). Python, 25 > 30 karşılaştırmasını yaparak sonucu False bulmuştur.
-> print("Hava sıcaktır.") kodu çalışıyor mu?	HAYIR (Yürütülmüyor). Koşul yanlış olduğu için, bu kod bloğu atlanır.
-> Yani, koşulun kendisi (değerlendirme) çalışır, ancak sonuç yanlış olduğu için, o koşulun altındaki emirler topluluğu (kod bloğu) çalıştırılmaz.
-> Sonra devreye elif bloğu giriyor. O koşul doğru olduğu için elif bloğundaki kod çalışıyor ve print("Hava ılıktır") ile ekrana yazdırıyor.
"""

# !TEKNİK UYARI!: SIRALAMA HATASI (ORDERING MATTERS):

# elif yapısında program yukarıdan aşağıya doğru ilk bulduğu True kapısından girer.
# Eğer koşulları yanlış sıralarsanız, daha özel olan koşul asla çalışmaz.

derece = 45
if derece > 20:
    print("Hava ılık.")       # Program burayı True bulur ve DURUR!
elif derece > 40:
    print("Hava çok sıcak!")  # Bu satır ASLA çalışmaz. 
# Doğrusu: Her zaman en dar/özel koşul (derece > 40) en başa yazılmalıdır. (Özelden genele doğru gitmeliyiz!)

# "HİÇBİR ŞEY YAPMA" KOMUTU (pass):

# Bazen bir koşul yazarsınız ama içine yazacağınız koda henüz karar vermemişsinizdir.
# Python'da blokların içi boş bırakılamaz. Bu durumda 'pass' kullanılır.
# Çünkü herhangi bir şey yazmadığında program hata veriyor.
if derece > 100:
    pass # Program hata vermez, burayı sessizce geçer.


#----------------------------------
# DEĞERLENDİRME VS YÜRÜTME AYRIMI :
#----------------------------------
"""
-> 'if derece > 30:' satırı her zaman 'ÇALIŞIR' (Yani değerlendirme/kontrol yapılır).
-> Eğer sonuç False ise altındaki 'print' satırı 'YÜRÜTÜLMEZ' (Atlanır).
-> Yani; koşulun kontrol edilmesi ile kodun çalıştırılması farklı aşamalardır.
"""

# -------------------------------------
# C. ELSE YAPISI (THE ELSE STATEMENT) :
# -------------------------------------
"""
-> else yapısı; if ve elif bloklarının tamamı yanlış (False) çıktığında, yani hiçbir koşulun sağlanmadığı durumda devreye giren, bir nevi varsayılan (default) yol olarak çalışan akış kontrol bileşenidir.
-> else kullanımı, tüm olası durumları ele aldığınızı garanti etmenin en temiz yoludur.
-> else bloğu bir başına kullanılamaz; mutlaka bir if (veya elif) bloğundan sonra gelmelidir. Olay örgüsünün son halkasıdır.
-> else ifadesinin yanında bir koşul (condition) yazılmaz. Çünkü o, yukarıdaki tüm şartların elendiği "diğer tüm durumlar" kümesini temsil eder.
-> else ifadesinin yanına bir koşul yazarsan Python "Ben bunu anlamadım" der ve "SyntaxError"(Sözdizimi Hatası) verir.
"""


# --- TEKNİK ÖRNEK 1: SICAKLIK ANALİZİ ---

print("Merhaba")
# sicaklik = float(input("Lütfen şehrinizdeki sıcaklık değerini giriniz:"))
sicaklik = 25

if sicaklik >= 30:
    print("Hava çok sıcak.")
elif 30 > sicaklik >= 20:
    print("Hava sıcak.")
elif 10 <= sicaklik < 20:
    print("Hava ılıktır.")
elif 0 <= sicaklik < 10:
    print("Hava soğuktur.")
else:
    # Yukarıdaki hiçbir aralığa girmeyen durumlar (Örn: -5 derece) buraya düşer.
    print("Hava çok soğuktur.")

# Teknik Not: 'elif 20 <= sicaklik <= 30:' şeklinde de yazılabilirdi, aynı sonucu verir.
# Eğer tüm koşullarda eşittir (>=) kullanılsaydı, Python ilk doğru bulduğu blokta dururdu.

"""
-> 30 > sicaklik >= 20: gösterimi Python'a özeldir. 
-> Python'daki 30 > sicaklik >= 20 kullanımı teknik literatürde "Chained Comparison" (Zincirleme Karşılaştırma) olarak geçer. 
-> Bu, Python'ın okunabilirliğini artıran en sevilen özelliklerinden biridir.
-> C++, Java, C# gibi dillerde bu yazımda mantık hatası olur.
-> Oralarda bunu 30 > sicaklik and sicaklik >= 20 şeklinde ayırman gerekir. Python buna izin veriyor.
-> Fakat bu şekilde de yazılabilir .
"""
if sicaklik >= 30:
    print("Hava çok sıcak.")
elif sicaklik >= 20:    # Zaten 30'dan küçük olduğu kesinleşti
    print("Hava sıcak.")
elif sicaklik >= 10:    # Zaten 20'den küçük olduğu kesinleşti
    print("Hava ılıktır.")
elif sicaklik >= 0:     # Zaten 10'dan küçük olduğu kesinleşti
    print("Hava soğuktur.")
else:
    print("Hava çok soğuktur.")


# --- TEKNİK ÖRNEK 2: NEM ORANI (CLEAN CODE YAKLAŞIMI) ---

print("Merhaba")
# nem_orani = float(input("Lütfen nem oranınızı (%) cinsinden giriniz:"))
nem_orani = 45

if nem_orani >= 71:
    print("Çok yüksek/Aşırı nem oranı")
elif nem_orani >= 51:  # Zaten 71'den küçüktür.
    print("Yüksek nem oranı")
elif nem_orani >= 31:  # Zaten 51'den küçüktür.
    print("Normal/ideal nem oranı")
else:                  # Zaten 31'den küçüktür.
    print("Çok düşük/kuru nem oranı")


# --- TEKNİK ÖRNEK 3: RÜZGAR HIZI VE ACİL DURUM YÖNETİMİ ---

# ruzgar_hizi = float(input("Lütfen rüzgar hızını (km/saat) giriniz:"))
ruzgar_hizi = 75

if ruzgar_hizi >= 89:
    # 89 km/saat ve üzeri
    print("ACİL DURUM: Fırtına/Kasırga tehlikesi!")
    
elif ruzgar_hizi >= 62:
    # Buraya ulaştıysa Hız < 89'dur. Aralık: 62 - 88 km/saat
    print("Şiddetli rüzgar, dışarı çıkmayın.")
    
elif ruzgar_hizi >= 39:
    # Buraya ulaştıysa Hız < 62'dir. Aralık: 39 - 61 km/saat
    print("Kuvvetli rüzgar, dikkatli olun.")
    
elif ruzgar_hizi >= 12:
    # Buraya ulaştıysa Hız < 39'dur. Aralık: 12 - 38 km/saat
    print("Orta hızlı rüzgar.")
    
else:
    # Buraya ulaştıysa Hız < 12'dir. Aralık: 0 - 11 km/saat
    print("Sakin/Hafif rüzgar.")


# ---------------------------------
#  İÇ İÇE IF YAPILARI (NESTED IF) :
# ---------------------------------
"""
-> Bir koşulun sonucuna bağlı olarak başka bir koşulun test edilmesi gerektiği durumlarda kullanılır.
-> Bir nevi karar hiyerarşisi oluşturur.
-> İç içe if yapıları, özellikle verinin birden fazla özelliğini kontrol etmeniz gerektiğinde idealdir.
"""

renk1 = "kırmızı"
renk2 = "mavi"
if renk1 == "kırmızı":
    if renk2 == "mavi":
        print("iki rengi karışımı mordur.")
    elif renk2 == "beyaz":
        print("İki rengin karışımı pembedir.")
elif renk1 == "yeşil":
    if renk2 == "beyaz":
        print("İki rengin karışımı açık yeşildir.")


# Şimdi hepsini birleştirelim.
print("--- Detaylı Hava Durumu Analizi ---")
sicaklik = float(input("1. Sıcaklık değerini (°C) giriniz: "))
nem_orani = float(input("2. Nem oranını (%) giriniz: "))
ruzgar_hizi = float(input("3. Rüzgar hızını (km/saat) giriniz: "))

print("-----------------------------------")


# 1. Dış Koşul: SICAKLIK (Ana Kategori)
if sicaklik >= 30:
    print("Durum: ÇOK SICAK BÖLGE")
    
    # 1A. İç Koşul: Nem Kontrolü
    if nem_orani >= 70:
        print("UYARI: Bunaltıcı Yoğun Nem. Hissedilen sıcaklık çok yüksek.")
        
    # 1B. İç Koşul: Rüzgar Kontrolü (Sıcak havada rüzgar durumu)
    elif ruzgar_hizi >= 39:
        print(" Rahatlatıcı: Hava sıcak ama kuvvetli rüzgar etkiyi azaltıyor.")
    else:
        print("Normal: Sadece sıcak, diğer faktörler normal.")

# 2. Orta Seviye Koşul: ILIK/NORMAL SICAKLIK
elif sicaklik >= 10:
    print("Durum: ILIK/NORMAL BÖLGE")
    
    # 2A. İç Koşul: Rüzgarın Tehlikesi Kontrolü
    if ruzgar_hizi >= 62:
        print("TEHLİKE: Fırtına Öncesi Rüzgar! Sıcaklık iyi ama rüzgar yüzünden dışarı çıkmayın.")
    elif nem_orani <= 30:
        print("İdeal ve Kuru: Hava durumu en konforlu seviyede.")
    else:
        print("Normal, dengeli hava.")

# 3. Son Koşul: SOĞUK/ÇOK SOĞUK
else:
    print("Durum: SOĞUK BÖLGE")
    
    # 3A. İç Koşul: Aşırı Soğuk ve Rüzgar Kontrolü (Rüzgar Üşütme Etkisi)
    if sicaklik < 0 and ruzgar_hizi >= 12:
        print("DON RİSKİ: Rüzgarın Üşütme Etkisi (Wind Chill) çok yüksek. Kalın giyinin.")
    else:
        print("Sadece soğuk, ancak rüzgar tehlikesi yok.")

print("-----------------------------------")


#--------------------------------------------------------------
# KOŞULA BAĞLI TEK BİR İFADE (INLINE CONDITIONAL EXPRESSIONS) :
#--------------------------------------------------------------
"""
-> Eğer koşula bağlı olarak çalıştırılacak tek bir ifade varsa bunu koşulun devamına aşağıdaki gibi yazılabilir.
-> Eğer 'if' bloğu içinde çalışacak kod tek bir satırdan oluşuyorsa, kodun daha kompakt görünmesi için iki nokta (:) sonrasına yazılabilir.
-> Bu yöntem genellikle çok basit kontrollerde tercih edilir. 
-> Ancak PEP 8 (Python Yazım Standartları) karmaşık durumlarda kodun okunabilirliğini korumak için alt satıra geçilmesini önerir.
"""
sayi = 50
if sayi %2 == 0:print("sayi çifttir.")  # Aslında burada alt satıra geçip 2 satırda yazmak yerine tek satırda yazıp işi bitiriyoruz.    
else:print("sayı tektir.")              # Aslında List Comprehension a benziyor lakin o ileriki konularda  (Python 201 dersinde) farkı anlatılacaktır.

yas = 20
statü = "Reşit" if yas >= 18 else "Reşit Değil"
# Çıktı: statü = "Reşit"


# ===================================================================================================================
# == BAB 6: PYTHON'DA AKIŞ KONTROL MEKANİZMALARI PROJELERİ(CHAPTER 6: Flow Control Mechanism Projects in Python) : ==
# ===================================================================================================================

#------------------------------------------------------------------------------------------------------------------
# ÖRNEK 1: Girilen 3 Yazılı Ortalaması ile Öğrencinin Sınıf Geçme Durumunu (GEÇTİ – KALDI) Gösteren Python Örneği :
#------------------------------------------------------------------------------------------------------------------
yazili_1 = float(input("Lütfen 1.sınavınızı giriniz:"))
yazili_2 = float(input("Lütfen 2.sınavınızı giriniz:"))
yazili_3 = float(input("Lütfen 3.sınavınızı giriniz:"))
ortalama = (yazili_1+yazili_2+yazili_3) / 3
if ortalama > 50:
    print("Dersi geçtiniz.")
else:
    print("Dersten kaldınız.")

# Aslında bu ortaokul-lise hesaplamasına örnek.

#--------------------------------------------------------------------------------------------------------------------------------------
# ÖRNEK 2: Girilen Vize-Final ile  Ortalaması ile Öğrencinin Sınıf Geçme Durumunu (GEÇTİ – KALDI ve HARF NOTU) Gösteren Python Örneği :
#--------------------------------------------------------------------------------------------------------------------------------------
vize = float(input("Lütfen vize notunuzu giriniz: "))
final = float(input("Lütfen final notunuzu giriniz: "))

ortalama = (vize*0.4+final*0.6)
print(f"Ortalamanız:{ortalama}") 
if ortalama >= 95:
    harf_notu="AA"

elif ortalama >= 90:
    harf_notu="BA"

elif ortalama >= 80:
    harf_notu="BB"

elif ortalama >= 70:
    harf_notu="CB"

elif ortalama >= 60:
    harf_notu="CC"

elif ortalama >= 50:
    harf_notu="DC"

elif ortalama >= 45:
    harf_notu="DD"
    print("Dersi koşullu bir şekilde geçtiniz.")

else:
    harf_notu ="FD/FF"
    print("Dersten kaldınız.")

print(harf_notu)

#-----------------------------------------------------------------------
# ÖRNEK 3: Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python Örneği :
#-----------------------------------------------------------------------
sayi = int(input("Lütfen sayı giriniz: "))
if sayi %2 == 0 :
    print("Sayı Çifttir.")
else:
    print("Sayı tektir.")

# Bu kodu daha profesyonelce böyle yazılabilirdi.Burada yukarıdaki anlattığımız "Inline Conditional Expressions kullanıldı."
sayi = int(input("Lütfen sayı giriniz: "))
sonuc = "Çifttir" if sayi % 2 == 0 else "Tektir"
print(f"Sayı {sonuc}.")


#--------------------------------------------------------------------------------------
# ÖRNEK 4: Girilen Tam Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği :
#--------------------------------------------------------------------------------------
tahmin_edilen_sayi = int(input("Lütfen sayıyı giriniz:"))
if tahmin_edilen_sayi > 0:
    print("Sayımız Pozitif bir sayıdır..")
elif tahmin_edilen_sayi == 0:
    print("Sayı 0'a eşittir.")
else:
    print("Sayımız Negatif bir sayıdır.")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ÖRNEK 5: Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boy metre cinsinden verilmeli) hesaplayan Python Örneği : 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
 VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile < 30 aralığındaysa kilolu, VKİ 30 
 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. 
 VKİ‟ni hesaplayarak kişinin durumunu yazdırınız 
"""

print("Vücut kitle indeksini hesaplayan programa hoşgeldiniz.")
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz:"))
kilo=float(input("Lütfen kilonuzu kilogram cinsinden giriniz:"))

VKI = kilo/(boy*boy)

if VKI >=35:
    print("CİDDİ OBEZ")

elif VKI>=30:
    print("OBEZ")

elif VKI>=25:
    print("Kilolu")

elif VKI>=18:
    print("Normal")

else:
    print("Zayıf")

print(f"VKI'niz: {VKI}")

# Bu temel olarak böyle lakin genişletip şöyle yapabiliriz.



print("--- Sağlık Analiz Sistemine Hoş Geldiniz ---")

# 1. VERİ GİRİŞİ (INPUT)
yas = int(input("Lütfen yaşınızı giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz (Örn: 1.75): "))
kilo = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))

# 2. ÖN KONTROL (GUARD CLAUSE)
# Programın ana mantığına girmeden önce kapsam dışı durumları (çocuklar) ayırıyoruz.
if yas < 18:
    print("BİLGİ: 18 yaş altı için standart VKİ skalası geçersizdir.")
    print("Lütfen bir pediatri uzmanına danışınız.")

else:
    # 3. HESAPLAMA VE ANALİZ (PROCESS)
    vki = kilo / (boy ** 2)
    ideal_vki = 22  # Bilimsel referans noktası
    ideal_kilo = ideal_vki * (boy * boy)
    
    print("-" * 40)
    print(f"Hesaplanan VKİ: {round(vki, 2)}") # Burada round() fonksiyonu kullanıldı.Virgülden sonra 2 den fazla kısımla ilgilenmiyor.
    print(f"İdeal Kilo Hedefiniz: {round(ideal_kilo, 1)} kg")
    print("-" * 40)

    # 4. KARAR HİYERARŞİSİ (DECISION LOGIC)
    # En yüksek değerden başlayarak (Descending Order) kontrol yapıyoruz.
    if vki >= 35:
        durum = "CİDDİ OBEZ (3. Derece Obezite)"
        tavsiye = "Acilen tıbbi destek ve diyetisyen kontrolü önerilir."
    elif vki >= 30:
        durum = "OBEZ (1. veya 2. Derece Obezite)"
        tavsiye = "Düşük kalorili diyet ve artırılmış fiziksel aktivite gereklidir."
    elif vki >= 25:
        durum = "KİLOLU"
        tavsiye = "Beslenme alışkanlıkları düzenlenmeli, egzersiz artırılmalıdır."
    elif vki >= 18.5:
        durum = "NORMAL"
        tavsiye = "Tebrikler! Mevcut formunuzu korumaya devam edin."
    else:
        durum = "ZAYIF"
        tavsiye = "Yüksek besin değerli bir programla kilo alımı hedeflenmelidir."

    # 5. SONUÇ ÇIKTISI (OUTPUT)
    print(f"TEŞHİS: {durum}")
    print(f"ÖNERİ: {tavsiye}")

print("-" * 40)


#----------------------------------------------------------------------------------
# ÖRNEK 6: Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python Örneği :
#----------------------------------------------------------------------------------
kullanici_yasi = int(input("Lütfen yaşınızı giriniz: "))
if kullanici_yasi > 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet almaya yaşınız yetmiyor.")
    kalan_yil = 18-kullanici_yasi
    print(f"Ehliyet alamazsınız.{kalan_yil} yıl sonra başvurabilirsiniz.")

"Not: Kullanıcının sadece sayı girdiği varsayılmıştır, hata yönetimi ileride anlatılacaktır."


#---------------------------------------------------------------------------------------
# ÖRNEK 7: Yaşı girilen Kişinin Seçimde Oy Verip Veremeyeceğini Gösteren Python Örneği :
#---------------------------------------------------------------------------------------
girilen_yas = int(input("Lütfen yaşınızı giriniz:"))
if girilen_yas >= 18:
    print("Oy vermeye yaşınız yetiyor.")
else:
    kalan_yil = 18-girilen_yas
    print(f"Oy vermeye yaşınız yetmiyor lakin {kalan_yil} yıl sonra oy kullanabilirsiniz.")

"Not: Kullanıcının sadece sayı girdiği varsayılmıştır, hata yönetimi ileride anlatılacaktır"


#---------------------------------------------------------------------------------------------------
# ÖRNEK 8: İkinci dereceden denklemin kökleri durumları arasındaki ilişkiyi Gösteren Python Örneği :
#---------------------------------------------------------------------------------------------------
print("Denklemin katsayılarını giriniz:(ax^2+bx+c)")
a = float(input("a katsayısını giriniz: "))
b = float(input("b katsayısını giriniz: "))
c = float(input("c katsayısını giriniz: "))

delta=(b**2)-4*a*c

if delta > 0:
    print("Denklemin kökleri gerçek sayılardır.Denklemin iki farklı reel kökü vardır.")
    x1 =(-b + delta**0.5)/(2*a)
    x2 =(-b - delta**0.5)/(2*a)
    print(f"Kök 1:{x1} kök 2:{x2}")

elif delta==0:
    print("Birbirine eşit iki reel kök (çakışık kök) vardır.")
    x1 =(-b + delta**0.5)/(2*a)         # x1=x2 olduğu için aynı şeyi 2 defa yazmadık.

else :
    print("Denklemin reel kökü yoktur.Karmaşık iki kökü vardır.")
    x1 =(-b + delta**0.5)/(2*a)
    x2 =(-b - delta**0.5)/(2*a)
    print(f"Kök 1:{x1} kök 2:{x2}")   # Eğer Delta <0 ise kökler karmaşık sayı olur. Python’da bunu hesaplamak için "cmath" modülünü kullanmalısın.


#----------------------------------------------------------------------------
# ÖRNEK 9: "kuru bilgi" ile "hikmet" arasındaki ayrımını test eden bir akış :
#----------------------------------------------------------------------------

# 1. Basamak: Mahsûsât (Veri alma)
bilgi = input("Öğrendiğiniz bir ilmi yazın: ")

# 3. Basamak: Tefekkür (Düşünce süzgeci)
tefekkur = input("Bu bilgiyi derinlemesine tefekkür ettiniz mi? (evet/hayir): ")

if tefekkur == "evet":
    # 5. Basamak: Amel ve Hikmet
    amel = input("Bu bilgiyi hayatınızda uyguluyor musunuz? (evet/hayir): ")
    
    if amel == "evet":
        print("Tebrikler! (Hikmet ve Amel-i Salih) ulaştınız.")
    else:
        print("Dikkat: Bilginiz (Kuru İlim) kaldı, henüz meyve vermedi.")
else:
    print("Düşünülmeyen bilgi sadece bir veri yığınıdır.")


#-----------------------------------------------------------------
# ÖRNEK 10: Sınır Kapısı Geçiş Algoritmasını bulan Python Örneği :
#-----------------------------------------------------------------

print("--- Sınır Kapısı Geçiş Kontrol Sistemi ---")

# Veri Girişleri
pasaport_yili = int(input("Pasaport geçerlilik süresi (yıl): "))
vize_durumu = input("Vizeniz var mı? (Evet/Hayır): ")
yas = int(input("Yaşınız: "))
adli_sicil_kirli_mi = input("Adli sicil kaydınız var mı? (Evet/Hayır): ")
butce = float(input("Toplam bütçeniz (Dolar): "))

# Karar Mekanizması
if pasaport_yili >= 1: # 1 yıl ve üzeri geçerli kabul edelim
    if vize_durumu.upper() == "EVET":
        if yas >= 18:
            if adli_sicil_kirli_mi.upper() == "HAYIR":
                if butce >= 500: # Toplam bütçe kontrolü
                    print("\nTEBRİKLER: Sınır kapısından geçebilirsiniz. İyi yolculuklar!")
                else:
                    print("\nRET: Maddi yetersizlik. En az 500$ gerekli.")
            else:
                print("\nRET: Adli sicil kaydı nedeniyle geçiş yasaktır!")
        else:
            print("\nRET: 18 yaşından küçükler tek başına geçemez.")
    else:
        print("\nRET: Vizeniz bulunmamaktadır.")
else:
    print("\nRET: Pasaport süreniz dolmuş veya yetersiz.")


#------------------------------------------------------
# ÖRNEK 11 : if else kullanarak hesap makinesi yapımı :
#------------------------------------------------------
sayi1 = int(input("Lütfen 1.sayıyı giriniz:"))
sayi2 = int(input("Lütfen 2.sayıyı giriniz:"))
islem=input("Lütfen yapacağınız işlemi seçiniz(+,-,*,/):")

if islem == "+":
    sonuc = sayi1+sayi2
    print(sonuc)

elif islem == "-":
    sonuc = sayi1-sayi2
    print(sonuc)

elif islem == "*":
    sonuc = sayi1*sayi2
    print(sonuc)

elif islem == "/":
    sonuc = sayi1/sayi2
    print(sonuc)

else:
    print("Lütfen geçerli bir operatör giriniz.")

# Burada tabiki bölüm kısımında 0/0 belirsizliği çıkacağını düşünmüş olabilirsiniz.
# Şuanlık amaç basit bir hesap makinesi yapmak. Try-except kullanmadan if else ile yapabilmektir.
# İlerleyen süreçlerde daha profesyoneli yapılacaktır.


#---------------------------------------------------------------------------------------------------------------------------------
# ÖRNEK 12 : Dışarıdan okunan iki sayıdan büyük olanının tek sayı mı, çift sayı mı olduğunu belirleyen bir programın algoritması :
#---------------------------------------------------------------------------------------------------------------------------------
sayi1 = int(input("Lütfen 1.sayıyı giriniz: "))
sayi2 = int(input("Lütfen 2.sayıyı giriniz: "))

if sayi1 > sayi2:
    buyuk_sayi = sayi1
    if buyuk_sayi %2 == 0:
        print("Büyük olan sayı çift sayıdır.")
    else:
        print("Büyük olan sayı tek sayıdır.")

elif sayi1 == sayi2:
    buyuk_sayi = sayi1    # Burada sayi2 de diyebilirdik tercih yazılımcıda.
    if buyuk_sayi %2 == 0:
        print("Çift sayıdır.")
    else:
        print("Tek sayıdır.")

elif sayi1 < sayi2:
    buyuk_sayi = sayi2
    if buyuk_sayi %2 == 0:
        print("Çift sayıdır.")
    else:
        print("Tek sayıdır.")
else:
    print("Geçerli bir şey giriniz!")

# Lakin bu üstteki yazılım kodu çalışsa da bir eksiklik var. Kod kendini fazla tekrar ediyor.
# --- ÖRNEK 12: GELİŞTİRİLMİŞ VERSİYON ---
sayi1 = int(input("Lütfen 1. sayıyı giriniz: "))
sayi2 = int(input("Lütfen 2. sayıyı giriniz: "))

# 1. ADIM: Büyük olan sayıyı tespit et (Mantık Süzgeci)
if sayi1 > sayi2:
    buyuk_sayi = sayi1
    mesaj = "1. sayı daha büyük."
elif sayi2 > sayi1:
    buyuk_sayi = sayi2
    mesaj = "2. sayı daha büyük."
else:
    buyuk_sayi = sayi1
    mesaj = "Sayılar birbirine eşit."

# 2. ADIM: Tek bir noktada kontrol yap (DRY Prensibi)
if buyuk_sayi % 2 == 0:
    tur = "Çift"
else:
    tur = "Tek"

# 3. ADIM: Sonucu ekrana yazdır
print(f"Analiz Sonucu: {mesaj} Tespit edilen sayı ({buyuk_sayi}) bir {tur} sayıdır.")

"""
-> DRY (Don't Repeat Yourself) Prensibi: İyi bir yazılımcı, aynı mantığı veya kod bloğunu birden fazla kez yazmaz.
-> Eğer bir kontrolü (örneğin % 2 == 0) her dalda (if/elif/else) ayrı ayrı yapıyorsan, bu kodu "refaktör" ederek (tekrar düzenleyerek) ortak bir noktaya toplaman gerekir.
-> Bu, kodun bakımını kolaylaştırır.
-> Yazılım dünyasında bir tabir vardır: "Code is a liability, not an asset." (Kod bir yüktür, varlık değildir.) 
-> Ne kadar çok kod yazarsan, o kadar çok hata potansiyeli ve o kadar çok bakım zahmeti üretirsin. 
-> DRY (Don't Repeat Yourself) prensibi, tam olarak bu yükü hafifletmek için ortaya atılmış en temel "kutsal" kurallardan biridir.
-> Özet olarak önce kodundaki tüm tekrarları ve ortak mantığı tespit et, sonra onları tek bir noktada (fonksiyon veya değişken) toplayarak tüm sistemi o merkezden yönet.
"""


# ============================================================================================================================================
""""
 Elhamdülillah, 6. Bab tamamına erdi; on iki örnekle ilim amele tebdil edildi. 
 Zira 'Amelsiz ilim, meyvesiz ağaca benzer' düsturuyla, mantığın iskeletini on iki düğümle (örnekle) sağlamlaştırdık.
"""
# ============================================================================================================================================
#  BAB 6 (PYTHON AKIŞ KONTROL MEKANİZMALARI) PROJE LİSTESİ :                                                                                 |
# ============================================================================================================================================
#  ÖRNEK 1 : Akademik Başarı ve Sınıf Geçme Analizi (Temel Aritmetik ve 'if-else' Dengesi)                                                   |
#  ÖRNEK 2 : Üniversite Not Sistemi ve Harf Notu Skalası (Çoklu Koşul 'elif' Hiyerarşisi)                                                    |
#  ÖRNEK 3 : Tam Bölünebilme ve Teklik-Çiftlik Kontrolü (Modül '%' ve 'and' Operatörü Kombinasyonu)                                          | 
#  ÖRNEK 4 : Sayısal Yön Analizi ve Sıfır Noktası Denetimi (Karşılaştırma Operatörleri Uygulaması)                                           |
#  ÖRNEK 5 : Gelişmiş Sağlık Analizi ve İdeal Kilo Öngörüsü (Kuvvet Alma '**' ve Guard Clause Yaklaşımı)                                     |
#  ÖRNEK 6 : Yaş Sınırı ve Ehliyet Uygunluk Sorgulama (Fark Alma ve Dinamik Bilgilendirme)                                                   |
#  ÖRNEK 7 : Demokratik Katılım ve Seçmenlik Hak Edişi (Büyük-Eşittir '>=' Mantıksal Süzgeci)                                                |
#  ÖRNEK 8 : İkinci Dereceden Denklem ve Karmaşık Kök Analizi (Delta Karar Yapısı ve Karekök Hesaplama)                                      |
#  ÖRNEK 9 : Gazâlî Perspektifi: İlimden Hikmete Dönüşüm Testi (Tefekkür ve Amel Süzgeci Sorgusu)                                            |
#  ÖRNEK 10: Çok Katmanlı Sınır Kapısı Geçiş Algoritması (İç İçe 'if' ve Mantıksal Kapılar)                                                  |
#  ÖRNEK 11: Basit Hesap Makinesi (Sıfıra Bölme Hatası 'ZeroDivision' Kontrolü)                                                              |
#  ÖRNEK 12: İki sayıdan maksimum olanın parite (teklik-çiftlik) Analizi                                                                     |
# ============================================================================================================================================
