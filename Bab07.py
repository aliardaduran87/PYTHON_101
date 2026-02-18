# ==============================================================
# == BAB 7: PYTHON'DA DÖNGÜLER (CHAPTER 7: LOOPS IN PYTHON) : ==
# ==============================================================

"""
-> Belirli bir koşul sağlanmaya devam ettiği sürece, belirlenen kod bloğunu tekrar ettiren yapılara "DÖNGÜ (LOOP)" denir.
-> Döngüler, manuel kod tekrarını engelleyen, otomasyonun ve nizamın temelini oluşturan kontrol mekanizmalarıdır.
-> Python dilinde 2 adet (while,for) döngü yapısı bulunaktadır.
"""

# -----------------------------------------------------
# 1. DÖNGÜLERİN ÇALIŞMA PRENSİBİ (LOGIC OF ITERATION) :
# -----------------------------------------------------
"""
1. Program akışı döngü satırına ulaştığında, önce döngünün KOŞULU değerlendirilir.
2. Koşul DOĞRU (True) ise; döngüye bağlı kod bloğu çalıştırılır.
3. Blok bittiğinde program otomatik olarak başa döner ve KOŞULU tekrar kontrol eder.
4. Koşul sağlandığı sürece bu devir (cycle) devam eder.
5. Koşul YANLIŞ (False) olduğu anda döngü sonlanır ve döngü kod bloğundan çıkar ve program bir sonraki satıra geçer.
"""

"""
Amacı (Mühendislik Perspektifi):
-> Tekrarı Önleme (Don't Repeat Yourself - DRY): Aynı talimat dizisini tekrar tekrar yazmak yerine, döngü içine alarak kodunuzu sadeleştirir.
-> Veri İşleme: Listeler, Sözlükler veya veri setleri gibi büyük veri yapıları üzerindeki her öğeye tek tek erişerek işlem yapmayı sağlar. (Özellikle for döngüsünde)
-> Verimlilik: Programın gereksiz satırları çalıştırmasını engelleyerek performansı artırır.
-> Dinamik Yapı Oluşturma: Programın çalışma anında (runtime) verinin boyutunu bilmediği durumlarda, döngüler verinin sonuna kadar otomatik olarak ilerleyerek esneklik sağlar.
-> Bellek Yönetimi (Memory Efficiency): Özellikle iterator (yineleyici) mantığıyla çalışan döngüler, tüm veriyi bir anda belleğe yüklemek yerine, her seferinde sadece ilgili parçayı işleyerek kaynak tüketimini optimize eder.
"""


#----------------
# while DÖNGÜSÜ :
#----------------
"""
-> while kelimesi Türkçe'de "iken,doğru olduğu sürece" gibi anlamlarına gelir. 
-> Belirli bir koşul sağlanıyorken tekrarlanması gerekli işlemler while döngüsü ile şu şekilde gösterilir.
-> Döngünün kaç kez çalışacağını önceden bilmediğiniz durumlarda ve belirli bir koşul doğru (True) olduğu sürece tekrar etmesini istediğinizde kullanılır.
-> Döngünün sonsuza kadar çalışmaması için, döngü içindeki bir noktada koşulun yanlış (False) olmasını sağlayacak bir mekanizma (sayaç, durum değiştirici vb.) bulunmalıdır.
-> while döngüsünün koşulu, daha ilk kontrolde Yanlış (False) çıkarsa, döngünün içindeki kod bloğu hiç çalıştırılmaz ve program akışı döngüden sonraki ilk satıra atlar.
-> while döngüsü, ön koşullu (pre-test) bir döngü olarak adlandırılır. Bu, demektir ki, döngü bloğuna girmeden önce koşulu kontrol eder.

"Özet olarak while döngüsü koşul doğru olduğu sürece çalışır. Genellikle tekrar sayısı 'belirsiz durumlarda' tercih edilir."

while(koşul):
    koşula bağlı tekrarlanacak ifadeler
"""
sayi = 1
while sayi <= 10:
    print(sayi)
    sayi+=1
print("Program devam ediyor.")

i=0
while i < 10:
    print("Python öğreniyorum")
    i+=1
print("Program devam ediyor.")
"""
sayi = 0
while sayi < 10:   # Buna dikkat etmek gerek burada + işlemi yapılmadığı için sonsuz döngüye girdi.
    print(sayi)
"""

# 1.Program önce sayi değişkenine 1 değerini atayan satırı çalıştırır.
# 2.Program while döngü satırına gelerek sayi değişkeninin 10'dan küçük ya da eşit olma durumunu kontrol eder.
# 3.Koşul sağlanıyorsa sayi değişkenini ekrana yazar(Ekrana 1 yazıldı.)
# 4.Ardından sayi değişkeninin değerini 1 arttırır (sayinin değeri 2 oldu.)
# 5.Program tekrar döngünün başladığı yere giderek koşulu kontrol eder.(sayi 2 için sayi<=10 kontrol edilir ve True sonuç elde edilir.)
# 6.Koşul sağlandığı sürece ekrana sayi değişkenini yazıp değişkenin değerini 1 arttırır ve başa döner.
# 7.Sayi değişkeni 10 değerine sahipken sayi<=10 koşulu sağlanır ve sayi ekrana yazılır.Ardından sayı 1 arttırılarak 11 yapılır. Program tekrar döngünün başına döner.
# 8.Sayi değeri 11 olduğu için sayi<=10 koşulunu sağlamaz. Program döngü içine girmeden döngü sonrası ilk satırdan çalışmaya devam eder;print("program devam ediyor.") satırı çalışır.

# Sonuç olarak program 1 den 10 a kadar olan sayıları ekrana yazdırdı.


while True:         
    islem=input("Yapmak istediğiniz işlemi seçiniz (+,-,*,/):")
    if islem   == "+":print("toplama")
    elif islem == "-":print("çıkarma")
    elif islem == "*":print("çarpma")
    elif islem == "/":print("bölme")
    elif islem ==  "q":
        print("Programdan çıkılıyor. Güle güle!")
        break # Döngüyü anında sonlandırır.
    else:print("Lütfen geçerli bir işlem giriniz.")


# while True : Aslında özeti doğru olduğu müddetçe çalış demek.
# Döngü koşulu sürekli True olduğu için program kullanıcıdan yapmak istediği işlemi isteyecek.
# Ardından işlemi yerine getirecek. Sonra tekrar yapmak istediği işlemi soracak ve bu süreç 'hiç durmadan' devam edecektir.
# while False: ise, döngünün daha başlamadan bitmesine neden olurdu.
# True ifadesinin büyük yazılma nedeni True kelimesinin bir anahtar kelime (keyword) ve özel bir Boolean (Mantıksal) değer olmasından kaynaklanır.
"""
Boolean Değerler: Programlamada mantıksal kararları temsil eden sadece iki değer vardır: Doğru ve Yanlış. Python'da bu değerler özel olarak tanımlanmıştır:
-> True: Mantıksal Doğru değeri temsil eder.
-> False: Mantıksal Yanlış değeri temsil eder.

Case Sensitive (Büyük/Küçük Harf Duyarlılığı): Python küçük/büyük harfe duyarlı bir dildir. Bu nedenle:
-> True ve False, Python'ın tanıdığı özel Boolean sabitleridir.
-> true, false, TRUE veya FALSE gibi yazımlar, Python için tanımsız veya sıradan değişken isimleri anlamına gelir ve mantıksal değer olarak kullanılamazlar.
"""

#--------------
# for DÖNGÜSÜ :
#--------------
"""
-> for döngüsü Türkçe'de için anlamına gelir.
-> while döngüsüne benzer şekilde for döngüsü de belirli koşul için tekrar edecek kod bloklarını belirtirken kullanılır.
-> Ancak for döngüsü while döngüsüne göre daha yetenekli ve kullanım alanı geniştir.
-> for döngüsü genellikle , belirli bir sayıda tekrar etmesi istenen işlemler için ya da bir veri kümesi içindeki elemanlar üzerinde gezinmek için kullanılır.
-> for döngüsü, belirli bir veri koleksiyonundaki (liste, dize, sözlük, küme veya sayı aralığı) her bir öğe üzerinde sırayla işlem yapmak için kullanılır. Bu tür döngülere "İterasyon Temelli Döngü" de denir.
-> for döngüsünün karakter dizileri (string) üzerindeki en temel özelliği budur: String'i bir "koleksiyon" (collection) olarak görür ve her bir harfi (karakteri) tek tek ele alarak döngü gövdesine sokar.
-> for döngüsünde karakterleri parçalarken 'otomatik olarak alt alta yazar' .
"""

harfler = "abcd"
for h in harfler:
    print(h)

"""
Adım Adım İşleyiş :
-------------------
1.Değişken Tanımlama: Harfler isimli bir kutuya "abcd" metnini koyuyoruz.

2.Döngüye Giriş: for h in harfler: satırı şunu söyler: "harfler kutusunun içine bak, bulduğun ilk karakteri h ismini verdiğim geçici bir değişkene ata."

3.İşlem: Döngünün içindeki print(h) komutu, o an h değişkeninde ne varsa (önce 'a', sonra 'b'...) onu ekrana basar.

4.Tekrar: Metnin sonuna gelene kadar bu işlem otomatik olarak devam eder.
"""

sehirler = ["İstanbul","Ankara","İzmir","Antalya","Bursa","Şanlıurfa","Aydın"]
for sehir in sehirler:
    print(f"Ziyaret edilecek şehir: {sehir}")

# sehirler değişkeninin içindeki bilgileri (elemanları) alıp, döngünün her adımında geçici olarak sehir değişkenine parçalayıp (ayrıştırıp) atıyor ve sonra bu değeri yazdırıyor.

# Çıktı:
# Ziyaret edilecek şehir: İstanbul
# Ziyaret edilecek şehir: Ankara
# Ziyaret edilecek şehir: İzmir
# Ziyaret edilecek şehir: Antalya
# Ziyaret edilecek şehir: Bursa
# Ziyaret edilecek şehir: Şanlıurfa
# Ziyaret edilecek şehir: Aydın

"""
-> Ne Zaman for Kullanılmalı ? Bir koleksiyonun tamamını veya belirli bir sayı aralığını baştan sona gezmek istediğinizde while yerine for kullanmayı tercih edin. Çünkü for döngüsü daha kısa, daha okunaklı ve genellikle Python'da daha verimlidir.
-> Sayaç Yönetimi Yok: while döngüsünde olduğu gibi, sayacı manuel olarak artırmanız (sayi += 1) gerekmez. Python bu işi sizin için otomatik olarak yapar, bu da sonsuz döngü riskini ortadan kaldırır.
for döngü_değişkeni in üzerinde _dolaşılacak_veri:
    döngü_içi_işlemler

for eleman in liste_adi:
    # 'eleman', her adımda listenin o anki değerini tutar
    # Bu blok, listedeki eleman sayısı kadar çalışır.
"""

# 'in' operatörü, Python'da bir 'aitlik' (membership) operatörüdür.
# Bir değerin, belirtilen veri kümesi (string, liste, range vb.) içinde olup olmadığını kontrol eder.
# Eğer aranan değer küme içerisinde mevcut ise 'True', mevcut değilse 'False' sonucunu üretir.

# for döngüsü içerisinde 'in' operatörü bir motor görevi görür:
# Döngü değişkeni, 'in' ifadesinden sonra gelen veri kümesinin ilk elemanından başlar.
# Değişken, veri kümesinin son elemanına kadar her adımda sırayla ilerleyerek değerleri üzerine alır.
# Veri kümesinin sınırları içerisinde kalındığı sürece 'in' operatörü 'True' değer üretmeye devam eder.
# Küme sınırlarının dışına çıkıldığı (eleman kalmadığı) anda 'False' sonucu döner ve döngü sonlanır.

#-------------------
# range FONKSİYONU :
#-------------------
"""
-> range() fonksiyonu, belirli bir aralıkta tam sayılardan oluşan bir "dizilim" (iterable) üretir.
-> Hafıza dostudur; tüm sayıları RAM'de saklamaz, sadece ihtiyaç duyulduğunda sıradaki sayıyı üretir.
-> Üç farklı kullanım parametresine sahiptir: range (başlangıç, bitiş, artış_miktarı)

 
range * operatörü:
-> Bir kabın (liste, tuple) içindekileri dışarı döker.
-> Fonksiyonlara, elindeki listeyi "parça parça" parametre olarak göndermeni sağlar.
"""

range(0,20)
print(range(0,20))
print(*range(0,20))  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 (1 den 20 'ye kadar olan sayıları yazar (20 dahil değil))

# YAVAŞ VE BELLEK TÜKETEN YOL:
# liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# PYTHONIC VE HIZLI YOL:
for i in range(10):
    print("Tekrar") # Bu satır tam 10 kez çalışır.
    # Aslında  0 ile 10 aralığında (0 dahil 10 hariç) 0 1 2 3 4 5 6 7 8 9 sayılarını üretir.

for sayi  in range(5,15): # 5 ten başlayıp 15 e kadar 5 6 7 8 9 10 11 12 13 14 (15 dahil değil) sayıları üretir.
    print(sayi)

# range fonksiyonu 3 farklı kullanımı vardır.
# 1.range(son_değer):0 ile son_değer arası 1'er artışla sayılar üretir.(0 dahil,son_değer hariç).
# 2.range(ilk_değer,son_değer):ilk_değer ile son_değer arasında 1'er artışlarla sayılar üretir.(ilk değer dahil,son_değer hariç).
# 3.range(ilk_değer,son_değer,artış_miktarı):ilk_değer ile son_değer aralığında,belirlenmiş artış_miktarı ile sayılar üretir.

for sayi in range(10,5,-1):
    print(sayi)
# Burada artış miktarı -1 olduğu sayılar 1'er 1'er azaltılarak ekrana yazdırmaktadır.10 sayısından başlar 5 e kadar (5 dahil değil ) ilerler.


#---------------------------------------
# 3.ATLAMA İFADELERİ (JUMP STATEMENTS) :
#---------------------------------------
"""
-> Herhangi bir döngü ya da karar yapısı içerisinde, mevcut işlemi kırıp bir sonraki adıma geçmek ya da döngüyü tümden sonlandırmak veya bir fonksiyonu sonlandırmak için kullanılan sözcüklerdir.
-> break,continue,pass,return ifadeleri birer atlama deyimidir.
-> Kısacası döngülerin ve koşullu yapıların doğal akışını değiştirmek için kullanılırlar.
"""

#-------------------
# A) break İFADESİ :
#-------------------
"""
-> Kelime anlamı olarak "kırmak" olan break herhangi bir koşul sağlandığında döngüyü tamamen kırmak,sonlandırmak için kullanılan bir sözcüktür.
-> break ifadesi çalıştıktan sonra döngü sonlanır ve program sonrasında çalışmaya devam eder.
-> Kısacası döngüyü 'anında sonlandırır'.
-> Döngü henüz bitmemiş olsa bile anında döngüyü durdurur ve program akışı döngüden hemen sonraki satırdan devam eder.
"""

toplam = 0
while True:
    sayi = int(input("Bir sayı giriniz:"))
    if sayi < 0:
        break
    toplam+=sayi
print("Toplam:",toplam)

# Burada toplamı 0 olan ve girilen sayılar 0 dan büyükse toplama yazılacağı ama 0 dan küçükse programın durup toplamı yazılacağı şekilde yazılmıştır.

isim = "Ali Arda"
for harf in isim:
    if harf == "A":
        break
    print(harf)

"""
-> Döngü "A" harfiyle karşılaştığı anda "Ben gidiyorum, oyun bitti" der ve döngüden çıkar. 
-> print komutu break satırının altında olduğu için, "A" harfi henüz ekrana yazılmadan döngü sonlanır. 
-> Bu yüzden ekranda hiçbir şey göremezsin.
"""

kelime = "merhaba"
for k in kelime:
    if k == "h":
        break
        print(k) # Burası break'in altında kaldığı için asla çalışmaz. Buna dead code (ölü kod) denir.
    print(k)     # İşte bu kod çalışır.
print("Program sonlandı.")

# Yukarıdaki kod bloğunda ise kelime değişkeni içerisinde merhaba kelimesinin harfleri sıra ile ekrana yazılmaktadır.
# h harfine ulaştığında döngü break komutu ile sonlandırılmakta ve döngünün sonraki komut çalışarak ekrana "Program sonlandı." yazmaktadır.
# Bu kodun ekran çıktısı şu şekildedir.
# m
# e
# r
# Program sonlandı.

#----------------------
# B) continue İFADESİ :
#----------------------
"""
-> Kelime anlamı olarak "devam etmek" olan continue deyimi, döngünün mevcut adımı sonlandırıp bir sonraki adıma geçmesini sağlar.
-> break deyiminde olduğu gibi döngüyü tümden sonlandırmaz.
-> Yalnız mevcut adımını sonlandırır.
"""
for i in range(10):
    if not i % 2 == 0:
        continue
    print(i)

# Yukarıdaki kod bloğu çift sayıları ekrana yazdırmakta , tek sayı gördüğünde ise continue ile döngüyü direkt bir sonraki adıma atlamaktadır.

isim = "Ali Arda"
for harf in isim:
    if harf == "A":
        continue
    print(harf)

"""
-> Döngü "A" harfiyle karşılaştığında "Bu harfi pas geçiyorum, bir sonrakine bakalım" der. 
-> print komutuna uğramadan hemen döngünün başına (bir sonraki harfe) döner. 
-> Bu yüzden sadece "A" harfleri yazdırılmaz, geri kalan her şey ("l", "i", " ", "r", "d", "a") yazdırılır.
"""

karakter = "çğiöşü"
kelime = "yağmur çiselersen şarkı söylüyordu"
for a in kelime:
    if a in karakter:
        continue
    print(a)
# Bu kodda for döngüsü kelime içindeki her bir harfi almakta, eğer türkçe karakterler içerisinde varsa döngü continue ile bir sonraki adıma atlanmaktadır değilse karakter ekrana yazılmaktadır.

liste = [1,2,3,4,5,6,7,8,9,10]
for i in liste:
    print("i:",i)

for i in liste:
    if (i==3) or (i==5):
        continue
    print("i:",i)

# Continue ifadesinde while döngüleriyle kullanıldığı zaman sonsuz döngü olayına yol açabilmektedir. O yüzden dikkatli kullanılmalıdır.
"""
i = 0
while i < 10:
    if (i==2):
        continue    # Buradan en başa, 'while i < 10' satırına döner.
    print(i) 
    i+=1
-> Eğer çalıştırırsak sonsuz döngüyü "Kernel" sekmesinde gözükür.
"""

i = 0
while i < 10:
    if (i==2):
        i+=1
        continue
    print(i) 
    i+=1

#------------------
# C. pass İFADESİ :
#------------------
"""
-> Kelime anlamı "geçmek" olan pass komutu; Python'da "hiçbir işlem yapmadan devam et" anlamına gelir.
-> Teknik olarak bir 'Null Operation' (Etkisiz İşlem) komutudur; CPU seviyesinde hiçbir eylem gerçekleştirmez ancak sözdizimi (syntax) hatasını engeller.
-> Ancak Python sözdiziminin gerektirdiği boşlukları doldurur.
-> Bazen sonradan kod yazacağımız zamanlarda atlayıp sonradan doldurmak için kullanılır.
-> Geliştiriciler bazen bir fonksiyonun veya sınıfın ismini belirler ama içini o an doldurmak istemezler. 
-> Python'da bir blok (if, for, def, class) açıp içini boş bırakırsanız hata alırsınız ve pass burada kurtarıcıdır.
""" 

harfler="adchtx"
while True:
    tahmin=input("Bir harf tahmini giriniz:")
    if tahmin not in harfler:
        pass
    else:
        print("Bir harfi doğru tahmin ettiniz.")
        break

# Yukarıdaki kod bloğunda, kullanıcının harfler isimli değişken içerisinde yer alan harflerden birini doğru tahmin etmesi istenmektedir.
# Eğer kullanıcının girdiği tahmin belirlenen harfler içerisinde yoksa program hiçbir şey yapmadan devam edecek kullanıcıdan yeni bir harf girişi yapmasını isteyen süreç tekrar edecektir.

# Burada pass deyimi yerine continue yazmanın sonucu değiştirmediği görülsede küçük bir anlam farkı vradır. Şu değişikliği yaparsak

harfler = "adchtx"
while True:
    tahmin = input("Bir harf tahmini giriniz:")
    if tahmin not in harfler:
        continue
        print("Yanlış tahmin")
    else:
        print("Bir harfi doğru tahmin ettiniz.")
        break

# Yukarıdaki kod bloğunda yanlış bir tahmin girildiğinde pass deyiminden sonra gelen satırın da çalıştığı görülür.
# pass deyimi aslında boş bir işlemi temsil eder.
# pass deyimine ait program "hiçbir iş" yapıp kaldığı yerden çalışmasını sürdürür.
# pass deyiminin altındaki "Yanlış tahmin" ifadesi de çalışır.
# Oysa continue komutu çalıştığı yerde işlem adımını sonlandırıp alttaki kod satırlarının çalışmasına izin vermeden while döngüsünün bir sonraki adımına geçişi sağlar.
# Yani continue kullanılması halinde "Yanlış tahmin" ifadesi ekrana yazılmaz.
# while True Programın, kullanıcı ya doğru girene kadar ya da hakları bitene kadar çalışmaya devam etmesini sağlar. Eğer bu döngü olmasaydı, kullanıcı tek bir hatalı girişte programdan tamamen atılırdı.


#--------------------
# D) return İFADESİ :
#--------------------
"""
-> Kelime anlamı "döndürmek" veya "geri vermek" olan return; fonksiyonların işini bitirip ürettiği sonucu çağıran yere teslim etmesini sağlar.
-> return, fonksiyonun içindeki 'tefekkür' sürecinin sonunda elde edilen 'hikmet' veya 'meyve' gibidir.
-> Bir fonksiyon içinde return satırı çalıştırıldığı anda fonksiyon sona erer; return'den sonraki satırlar (aynı blokta) asla çalışmaz.
-> Sadece ekrana yazdırmakla (print) karıştırılmamalıdır; print sadece gösterir, return ise o değeri kodun başka yerinde kullanılmak üzere 'elde tutulur' hale getirir.
"""

def toplam_yap(a, b):
    sonuc = a + b
    return sonuc  # Sonucu paketleyip fonksiyonun dışına gönderir
    print("Bu satır asla çalışmaz!") # Return'den sonra olduğu için 'dead code' olur.


# Fonksiyondan dönen değeri bir değişkene atayabiliriz:
hesaplanan_deger = toplam_yap(10, 20)
print("Fonksiyondan gelen meyve:", hesaplanan_deger)


#--------------------------------------------------------
# return ile print Arasındaki Fark (Görünürlük vs Veri) :
#--------------------------------------------------------

def sadece_yazdir(sayi):
    print(sayi * 2) # Sadece ekranda görürüz, elimizde veri kalmaz.

def degeri_dondur(sayi):
    return sayi * 2 # Veriyi bize verir, başka işlemlerde kullanabiliriz.

# Kullanım:
x = sadece_yazdir(5) # Ekrana 10 yazar ama 'x' değişkeni boş (None) kalır.
y = degeri_dondur(5) # Ekrana bir şey yazmaz ama 'y' artık 10 değerine sahiptir.
print("Y'nin içindeki değerle işlem yapabiliriz:", y + 5) # Sonuç 15 olur.

#--------------------------------------------
# Fonksiyonu Erken Bitirme (Koşullu return) :
#--------------------------------------------

def ehliyet_kontrol(yas):
    if yas < 18:
        return "Ehliyet alamazsınız." # Koşul sağlanırsa fonksiyon burada durur.
    
    # Yas 18'den küçükse yukarıdaki return fonksiyonu bitirdiği için buraya gelinmez.
    return "Ehliyet başvurusu yapabilirsiniz."

print(ehliyet_kontrol(15))
print(ehliyet_kontrol(20))

"""
Özetle:
1. return fonksiyonu sonlandırır (break'in döngüyü bitirmesi gibi).
2. Fonksiyonun ürettiği değeri "dış dünyaya" (ana programa) çıkarır.
3. Bir fonksiyon bir değer return etmiyorsa, varsayılan olarak 'None' döndürür.
"""


# -----------------------------------------------------------------------------------------------------------
#  break    : Döngüyü tamamen kırar, sonlandırır ve döngüden 'firar' ederek dışarı çıkar.                   |
#  continue : Döngünün o anki adımını (iterasyonunu) terk eder ve bir sonraki adıma fırlar.                 |
#  pass     : Akışı hiçbir şekilde etkilemez; sadece bloğun boş görünmesini engelleyerek alt satıra geçer.  |
#  return   : Fonksiyonu sonlandırır ve fonksiyonun ürettiği değeri çağıran noktaya teslim eder.            |
# -----------------------------------------------------------------------------------------------------------

"""Not: break, continue, pass, return ifadelerinin sonuna iki nokta koymayız çünkü onlar bir blok başlatmaz, sadece o blok içindeki bir eylemi/komutu temsil ederler."""

#--------------
# case YAPISI :
#--------------
"""
-> Çoklu koşullu ifadeleri daha temiz ve okunaklı şekilde yönetmek için kullanılan yapıdır.
-> Bu yapıya genellikle "switch" veya "switch-case" yapısı denir.
-> Lakin bu Python'da bulunmamaktadır. Bunun yerine 3.10 sürümü ile eklenen "match-case" yapısı vardır.

#---------------
# 1.Match-case :
#---------------
-> Match ifadesi, bir değişkenin yerini alır ve bu değeri sırasıyla case bloklarında tanımlanan desenlerle (pattern) eşleştirmeye çalışır.
-> Veri eşleştirme denilen çok daha gelişmiş bir özelliğe sahiptir.
-> match ifadesinden sonra bir mantıksal karşılaştırma yer almaz.
-> Doğrudan değişkenin kendi yazılır.
-> Değişkenin "eşitlik" durumunu kontrol edebileceği her bir değer ayrı bir case olarak yazılır.
-> Herhangi bir eşleme olmadığında yapılması istenen iş case _: veya case other: olarak belirtilir.
"""

kod = input("Ülke kodu giriniz:")
match kod:
    case "tr":
        print("Türkiye")
    case "en":
        print("İngiltere")
    case "de":
        print("Almanya")
    case _:
        print("tanımsız")

"""
-> Eğer aynı sonucu üretecek birden fazla değer söz konusu ise bunlar ayrı case olarak yazılabileceği gibi | ile birleştirilebilir.
"""

match kod:
    case"tr":
        print("türkçe")
    case "de":
        print("almanca")
    case "au":
        print("almanca")

# case "de"|"au":print("almanca") şeklinde yazılabilir.

# ==============================================================================
# == BAB 7: PYTHON'DA DÖNGÜLER PROJELERİ (CHAPTER 7: PYTHON LOOPS PROJECTS) : ==
# ==============================================================================

#---------------------------------------------------------------
# ÖRNEK 1: Python ile 1-100 Arası Sayılarla İşlem Yapma Örneği :
#---------------------------------------------------------------
""" A-) ÖRNEK 1 : 1-100 Arası Sayıları Ekranda Listeleyen Python Örneği : """
for i in range (1,101):
    print(i)


""" B-) ÖRNEK 2 : 1-100 arası Çift Sayıları Listeleyen Python Örneği : """
for i in range(1,101):
    if i % 2 == 0:
        print(i)


""" C-) ÖRNEK 3 : 1-100 Arası Tek Sayıları Listeleyen Python Örneği : """
for i in range(1,101):
    if i % 2 == 1:
        print(i)


""" D-) ÖRNEK 4: 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python Örneği : """
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


""" E-) ÖRNEK 5: 1-100 Arası Sayıların Toplamını Bulan Python Örneği : """
toplam=0
for i in range(1,101):
    toplam +=i
print(f"1-100 arası sayıların toplamı:{toplam}")


""" F-) ÖRNEK 6: 1-100 Arası Sayılardan Hem 4'e Bölünmeyen Hem 6'ya Bölünmeyenleri Bulan Python Örneği : """
for i in range(1,101):
    if i % 4 != 0 and i % 6 != 0:
        print(i)

""" G-) ÖRNEK 7: 1-100 Arası Sayıların Karelerini Yan Yana Yazdıran Örnek : """
for i in range(1,101):
    print(i**2,end="")

""" H-) ÖRNEK 8: 1-100 Arası Sayıların Kaç Tanesinin 7'ye Bölündüğünü Bulma (Sayaç Mantığı) : """
adet=0
for i in range(1,101):
    if i % 7 == 0:
        adet+=1
print(f"1-101 arasında 7'ye bölünen toplam {adet} sayı var.")

""" G-) ÖRNEK 9: 1-100 arası girilen sayıya kadar toplamını bulan Python Örneği : """
sayi_input=input("Lütfen 1-101 arası bir sayı giriniz:")
ust_sınır=int(sayi_input)
toplam=0
i=1
while i<=ust_sınır:
    toplam+=i
    i+=1
print(f"1'den {ust_sınır} sayısına kadar olan toplam: {toplam}")

# 2.Yazım: Bu şekilde for döngüsü ile de yazılabilir.
sayi = int(input("Lütfen sayıyı giriniz: "))
toplam = 0
for i in range(1, sayi + 1): # Başlangıç noktası doğrudan 1 olarak verildi.
    toplam += i
print(f"Toplam Sonucu: {toplam}")


#-------------------------------------------------------------------------------------
# ÖRNEK 2: 1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python Örneği :
#-------------------------------------------------------------------------------------
sayi = int(input("Lütfen sayı giriniz: "))
for i in range(1, sayi + 1):
    print(i)


#---------------------------------------------------------------------
# ÖRNEK 3: Girilen Metnin Harflerini Alt Alta Yazdıran Python Örneği :
#---------------------------------------------------------------------
metin = input("Lütfen bir metin giriniz: ")
for harf in metin:
    print(harf)

"""
-> Biraz sınırları zorlayalım . while döngüsü ile yazmayı deneyelim.
"""

#---------------------------------------------------------------------------------------
# ÖRNEK 3: Girilen Metnin Harflerini Alt Alta Yazdıran Python Örneği (While Versiyonu) :
#---------------------------------------------------------------------------------------

metin = input("Lütfen bir metin giriniz: ")
indeks = 0

# Şartımız: Sıra numarası, metnin toplam uzunluğundan küçük olduğu müddetçe çalış
while indeks < len(metin):
    # Metnin o sıradaki harfine erişiyoruz
    print(metin[indeks])

    # SENIOR NOTU: Sayacı artırmayı unutma, yoksa sonsuz döngüye girer!
    indeks += 1

else:
    # Döngü başarıyla tamamlandığında çalışacak kısım
    print("\nListeleme işlemi bitti.")


#---------------------------------------------------------------------------------------------
# ÖRNEK 4: Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği : 
#---------------------------------------------------------------------------------------------
baslangic = int(input("Başlangıç sayısını giriniz: "))
bitis = int(input("Bitiş sayısını giriniz: "))
toplam = 0

for i in range(baslangic, bitis + 1):
    toplam += i

print(f"{baslangic} ile {bitis} arasındaki sayıların toplamı: {toplam}")


# 2.Yazım Türü bu şekilde de yazılabilir. Biz buna yazılımda 'Defansif Kodlama' diyoruz.
sayi1=int(input("Lütfen 1.sayıyı giriniz: "))
sayi2=int(input("Lütfen 2.sayıyı giriniz: "))
toplam=0

if sayi1 > sayi2:
    for i in range(sayi2,sayi1+1):
        toplam+=i
elif sayi1 < sayi2:
    for i in range(sayi1,sayi2+1):
        toplam+=i
else:
    print("Eşit sayı girdiniz. Sonuç 0")

print(toplam)


#------------------------------------------------------------------------------------------
# ÖRNEK 5: Klavyeden girilen n sayısına kadar çiftleri toplayan, tekleri çarpan algoritma :
#------------------------------------------------------------------------------------------
"""
-> Hatırlıyorsanız bunu Bab 1 'de Algoritma Örneği olarak vermiştik. Pseudocode ve doğal algoritmik dille yazmıştık .
-> Eğer bakmak istersen Bab 1 95.satırdan itibaren bakabilirsin .
"""
# 1. ADIM: Kullanıcıdan sınır değerini (n) alıyoruz.
n = int(input("Hangi sayıya kadar işlem yapılsın? (n): "))

# 2. ADIM: Biriktirici (Accumulator) değişkenleri tanımlıyoruz.
# Toplama işleminin etkisiz elemanı 0, çarpma işleminin etkisiz elemanı 1'dir.
cift_toplam = 0
tek_carpim = 1

# 3. ADIM: 1'den n'e kadar (n dahil) döngüyü başlatıyoruz.

for i in range(1, n + 1):
    
    # 4. ADIM: Sayının çiftlik-teklik (Parity) kontrolünü yapıyoruz.
    if i % 2 == 0:
        # Sayı çift ise toplamın üzerine ekle
        cift_toplam += i
    else:
        # Sayı tek ise çarpım değerini güncelle
        # NOT: tek_carpim *= i ifadesi, tek_carpim = tek_carpim * i demektir.
        tek_carpim *= i

# 5. ADIM: Sonuçları raporluyoruz.
print("-" * 30)
print(f"1'den {n} sayısına kadar:")
print(f"Çift sayıların toplamı: {cift_toplam}")
print(f"Tek sayıların çarpımı: {tek_carpim}")
print("-" * 30)


#-------------------------------------------------------
# ÖRNEK 6: Döngülerle Gelişmiş Kullanıcı Girişi Örneği :
#-------------------------------------------------------
print("-----------------------Kullanıcı Girişi Programı-----------------------")
sistem_kullanici_adi = "Ali"
sistem_parola = "12345"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanici Adini Giriniz:")
    parola = input("Parolayı Giriniz:")
    
    if (kullanici_adi == sistem_kullanici_adi and parola == sistem_parola):
        print("Sisteme başarıyla giriş yapıldı...")
        break # Doğru girişte döngüden çıkar.
    else:
        print("Kullanıcı adı veya parola hatalı!")
        giris_hakki-=1 
        print(f"Kalan Giriş Sayısı:{giris_hakki}")

    if(giris_hakki==0):
        print("Giriş Hakkınız bitti, sistem bloke edildi.")
        break # Sadece hak bittiğinde döngüden çıkar.

# Ama bu şu şekilde de yazılabilir ve daha profesyonel olur ve mantık açısından daha doğrudur.

print("-----------------------Kullanıcı Girişi Programı-----------------------")
sistem_kullanici_adi = "Ali"
sistem_parola = "12345"
giris_hakki = 3
        
while True:
    kullanici_adi = input("Kullanici Adini Giriniz:")
    parola = input("Parolayı Giriniz:")
    if (kullanici_adi !=sistem_kullanici_adi and parola==sistem_parola) : # Hatayı/İstisnayı Arıyorsan (!=) kullancaksın.
        print("Kullanıcı Adı Hatalı...")
        giris_hakki-=1  # Giriş hakkı 1 azaltılıyor.

    elif (kullanici_adi==sistem_kullanici_adi and parola !=sistem_parola) :
        print("Parola hatalı...")
        giris_hakki-=1

    elif (kullanici_adi!=sistem_kullanici_adi and parola !=sistem_parola) :
        print("Parola veya Kullanıcı Adı Hatalı...")
        giris_hakki-=1
    
    else:
        print("Sisteme başarıyla giriş yapıldı.")
        break

    if(giris_hakki==0):
        print("Giriş Hakkınız bitti, sistem bloke edildi.")
        break  # Sadece hak bittiğinde döngüden çıkar.
"""
Neden 2. Çözümü Tercih Etmeliyiz?
---------------------------------

1.Granüler (Detaylı) Geri Bildirim: 
-> İlk kodda sadece "Hatalı" denirken, bu çözümde hatanın kullanıcı adında mı yoksa parolada mı olduğu net bir şekilde belirtilir. 
-> Bu durum, kullanıcının hatasını hızlıca düzeltmesini sağlayarak Kullanıcı Deneyimi (UX) kalitesini artırır.

2.İstisnaları Ayıklama (Guard Clauses):
-> Programlama dünyasında önce hataları if/elif ile ayıklayıp başarıyı en sona (else) bırakmak bir standarttır.
-> Bu sayede hatalar birer "muhafız" gibi kapıda yakalanır ve geçersiz verinin sistemin derinliklerine sızması engellenir.

3.Güvenlik ve Analiz Kapasitesi: 
-> Eğer bir saldırgan sürekli farklı şifrelerle "Ali" ismini deniyorsa, sistem bu durumu parolanın yanlış olduğu elif bloğu üzerinden takip edebilir. 
-> Bu, sisteme bir güvenlik denetimi (logging) katmanı eklemeni sağlar.

4.Esneklik ve Genişletilebilirlik:
-> İleride her hata türü için farklı bir aksiyon almak istersen (örneğin; şifre 3 kez yanlış girilince hesabı kilitle ama kullanıcı adı yanlışsa bir şey yapma), her bir elif bloğuna özel kodlar yazabilirsin. İlk koddaki "ya hep ya hiç" mantığında bu çok zordur.

5.Mantıksal Kesinlik : 
-> Tüm hata senaryolarını (!= durumlarını) tek tek kontrol edip elediğin için, kod else bloğuna ulaştığında artık verinin doğruluğundan %100 emin olunur.
"""


#--------------------------------
# ÖRNEK 7: Basit Atm Uygulaması :
#--------------------------------
print("----------------------- ATM MAKİNESİNE HOŞGELDİNİZ -----------------------")
"""
İşlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basın.
"""
bakiye = 1000

while True:
    islem = input("İşlemi seçiniz (1/2/3/q): ") 

    if islem == "q":
        print("Sistemden çıkılıyor... Yine bekleriz.")
        break
    
    elif islem == "1":
        print(f"Mevcut bakiyeniz: {bakiye} TL")
    
    elif islem == "2":
        miktar = int(input("Yatırılacak miktarı giriniz: "))
        bakiye += miktar
        print(f"İşlem başarılı. Yeni bakiyeniz: {bakiye} TL")
    
    elif islem == "3":
        miktar = int(input("Çekilecek miktarı giriniz: "))
        
        # MÜHENDİSLİK REFLEKSİ: Önce Kontrol
        if miktar > bakiye:
            print(f"Hata: Yetersiz bakiye! (Bakiye: {bakiye} TL)")
        else:
            bakiye -= miktar
            print(f"İşlem başarılı. Kalan bakiye: {bakiye} TL")
            
    else:
        print("Geçersiz işlem! Lütfen 1, 2, 3 veya 'q' tuşlayınız.")


#--------------------------------------------------------------
# ÖRNEK 8: Bir sayının faktöriyelini hesaplayan Python Örneği :
#--------------------------------------------------------------
print("-----------------------Faktöriyel Bulma Programı-----------------------")

while True:
    sayi = input("Faktöriyelini hesaplamak istediğiniz sayıyı girin (Çıkış için 'q'):")
    
    if (sayi == "q"):
        print("Program sonlandırılıyor...")
        break
    
    else:
        sayi = int(sayi)
        faktoriyel = 1
        
        for i in range(2, sayi + 1):
            faktoriyel *= i
            
        print(f"{sayi}! = {faktoriyel}")


#-----------------------------
# ÖRNEK 9 : FİZZ-BUZZ ÖRNEĞİ :
#-----------------------------
"""
Ne zaman çıktı: 2007 yılında yazılımcı 'Imran Ghory' tarafından ortaya atıldı ve Jeff Atwood'un blog yazısıyla tüm dünyaya yayıldı.
Nasıl çıktı: Bilgisayar bilimleri mezunu birçok adayın mülakatlarda en basit algoritmalarda bile zorlandığının fark edilmesi üzerine bir "eleme testi" olarak doğdu.
Ne işe yarıyor: Adayın karmaşık kütüphaneler yerine temel döngü, koşul hiyerarşisi ve problem çözme mantığına sahip olup olmadığını saniyeler içinde ölçmeye yarıyor.

A-) 1-100 arasındaki sayılar için 3'e bölünürse "Fizz" 5'e bölünürse "Buzz" 15'e bölünürse "FizzBuzz" yazdıran kodu yazınız.
"""
for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    

#------------------------------------------------------
# ÖRNEK 10: Mükemmel Sayı Analizi (Mükemmel Sayı mı?) :
#------------------------------------------------------
sayi=int(input("Bir sayı giriniz: "))
toplam = 0

for i in range (1, sayi):
    if sayi % i == 0:
        toplam +=i

if toplam == sayi:
    print(f"{sayi} mükemmel bir sayıdır.")
else :
    print(f"{sayi} mükemmel bir sayı değildir.")

#-------------------------------------
# ÖRNEK 11: Armstrong Sayısı Tespiti :
#-------------------------------------
sayi_str = input("Bir sayı giriniz: ")
basamak_sayisi = len(sayi_str)
sayi_int = int(sayi_str)
toplam = 0

for rakam in sayi_str:
    toplam += int(rakam) ** basamak_sayisi

if toplam == sayi_int:
    print(f"{sayi_int} bir Armstrong sayısıdır.")
else:
    print(f"{sayi_int} bir Armstrong sayısı değildir.")


#------------------------------------------
# ÖRNEK 12: Çarpım Tablosu (Nested Loops) :
#------------------------------------------
for i in range(1, 11):
    print(f"--- {i}'ler Tablosu ---")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)


#---------------------------------------------
# ÖRNEK 13: Dinamik Akümülatör (q ile Çıkış) :
#---------------------------------------------
toplam = 0

while True:
    islem = input("Bir sayı girin (Çıkış için 'q'): ")
    
    if islem == "q":
        print(f"Döngü sonlandırıldı. Toplam değer: {toplam}")
        break
    
    toplam += int(islem)


#-------------------------------------------------------------------
# ÖRNEK 14: Koşullu İlerleme (1-100 Arası 3'ün Katları - Continue) :
#-------------------------------------------------------------------
for i in range(1, 101):
    if i % 3 != 0:
        continue  # 3'e bölünmeyenleri es geç, döngünün başına dön
    print(i)


#----------------------------------------------------------
# ÖRNEK 15: List Comprehension (1-100 Arası Çift Sayılar) :
#----------------------------------------------------------
# Geleneksel döngü yerine modern Pythonic yaklaşım:
cift_sayilar = [i for i in range(1, 101) if i % 2 == 0]
print(cift_sayilar)
"""
-> Tabi dediğim gibi her ne kadar buraya yazsam da PYTHON 201 dersinde List Comprehension kısmı daha detaylıca anlatılacaktır.
"""

#---------------------------------------------------------------
# ÖRNEK 16: Asal Sayı Kontrol Algoritması (Prime Number Check) :
#---------------------------------------------------------------
# Bir sayı sadece 1'e ve kendisine bölünebiliyorsa ASAL'dır.
# Mühendislik Notu: 1 asal sayı değildir. En küçük asal sayı 2'dir.

sayi = int(input("Sorgulamak istediğiniz sayıyı giriniz: "))

if sayi <= 1:
    print(f"{sayi} bir asal sayı değildir.")
elif sayi == 2:
    print("2 en küçük ve tek çift asal sayıdır.")
else:
    asal_mi = True
    
    # 2'den başlayarak sayının kendisine kadar olan bölenleri deniyoruz
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False
            break # Bir tane bile bölen bulursak döngüyü kırmak performansı artırır.

    if asal_mi:
        print(f"{sayi} bir asal sayıdır.")
    else:
        print(f"{sayi} bir asal sayı değildir.")

#-------------------------------
# ÖRNEK 17: Dik Üçgen Tasarımı :
#-------------------------------
# Mantık: Döngünün her adımında karakter sayısı 1 artar.
boyut = int(input("Üçgenin boyutu: "))

for i in range(1, boyut + 1):
    print("*" * i)

"""

ÇIKTI (Output):
---------------
*
**
***
****
*****

"""


#------------------------------------
# ÖRNEK 18: Ters Dik Üçgen Tasarımı :
#------------------------------------
# Mantık: range(başlangıç, bitiş, artış) parametresindeki -1 ile geri sayım yapılır.
boyut = int(input("Ters üçgen boyutu: "))

for i in range(boyut, 0, -1):
    print("*" * i)

"""

ÇIKTI (Output):
---------------
*****
****
***
**
*
---------------
"""


#------------------------------------------------------
# ÖRNEK 19: İkizkenar Piramit İnşası (Simetrik Üçgen) :
#------------------------------------------------------
# Mühendislik Notu: Önce boşlukları (space), sonra yıldızları yazdırmak gerekir.
kat = int(input("Piramit kaç katlı olsun? "))

for i in range(1, kat + 1):
    # Boşluk sayısı azalırken, yıldız sayısı tek sayılar (2n-1) şeklinde artar.
    print(" " * (kat - i) + "*" * (2 * i - 1))


"""

ÇIKTI (Output):
---------------
    *
   ***
  *****
 *******
*********
--------------
"""


#-----------------------------------
# ÖRNEK 20: Elmas (Baklava) Deseni :
#-----------------------------------
# Mantık: Bir düz piramit ve bir ters piramidin birleşimidir.
n = int(input("Elmasın orta genişliği (kat sayısı): "))

# Üst kısım
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Alt kısım (Ters Piramit)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

"""
ÇIKTI (Output):
---------------
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
--------------
"""
#-------------------------------------------------------
# ÖRNEK 21: while Döngüsü ile Haklı Tahmin Mekanizması :
#-------------------------------------------------------
harfler = "adchtx"
hak = 3  # Kullanıcının 3 canı var

while hak > 0:  # Hak bitene kadar çalış
    tahmin = input(f"Bir harf giriniz ({hak} hakkınız kaldı):")
    
    if tahmin in harfler:
        print("Tebrikler, doğru tahmin!")
        break  # Doğru bilince döngüden hemen çık
    else:
        hak -= 1  # Yanlış tahmin, hakkı bir azalt
        if hak > 0:
            print("Yanlış! Tekrar dene.")
        else:
            print("Maalesef hakkınız bitti. Kaybettiniz!")

# Döngü biterse buraya geçer
print("Program sonlandı.")

# ===================================================================================================================================================
""" 
 Bi-iznillah, 7. Bab nihayete erdi; döngülerin sonsuz devr-i daiminde hikmet arandı ve yirmi bir düğümle mühürlendi.
 Gayretin sürekliliği, neticenin selametidir hakikatince; statik kodları dinamik bir akışa, kuru bilgiyi ise tekrar eden bir nizama dönüştürdük. 
 Programın nabzını, iterasyonun disipliniyle bu 21 seçkin örnekte sabitledik.
"""
# ===================================================================================================================================================
#  BAB 7: PYTHON'DA DÖNGÜLER PROJE LİSTESİ :                                                                                                        |
# ===================================================================================================================================================
#  ÖRNEK 1 : Sayısal Menzil Analizi (1-100 Arası Koşullu Filtreleme ve İstatistik)                                                                  |
#  ÖRNEK 2 : Dinamik Sınır Belirleme (Kullanıcı Girdili Artışlı Liste Yönetimi)                                                                     |
#  ÖRNEK 3 : Karakter İndeksleme (String Verinin İteratif Olarak Alt Alta Yazdırılması)                                                             |
#  ÖRNEK 4 : Akümülatör ile Aralık Toplamı (İki Sayı Arası Sayısal Kütle Hesabı)                                                                    |
#  ÖRNEK 5 : Hibrit Algoritma (N'e Kadar Çift Toplamı ve Tek Çarpımı Yönetimi)                                                                      |
#  ÖRNEK 6 : Defansif Giriş Algoritması (Hata Muhafızları ile Kullanıcı Doğrulama)                                                                  |
#  ÖRNEK 7 : Finansal İşlem Motoru (ATM Simülasyonu ve Bakiye Kontrol Mekanizması)                                                                  |
#  ÖRNEK 8 : Faktöriyel Hesaplama Motoru (Döngüsel Çarpım ve Birikim Modeli)                                                                        |
#  ÖRNEK 9 : Fizz-Buzz Eleme Testi (Mantıksal Hiyerarşi ve Modüler Aritmetik Zirvesi)                                                               |
#  ÖRNEK 10: Mükemmel Sayı Analizi (Bölenlerin Harmonisi ve Eşitlik Kontrolü)                                                                       |
#  ÖRNEK 11: Armstrong Sayısı Tespiti (Basamak Kuvvetleri ve Sayısal Sadakat)                                                                       |
#  ÖRNEK 12: Matrisel Düzen: Çarpım Tablosu (İç İçe Döngülerin Senkronizasyonu)                                                                     |
#  ÖRNEK 13: Dinamik Akümülatör (Sonsuz Döngüde 'q' Kontrollü Veri Biriktirme)                                                                      |
#  ÖRNEK 14: Koşullu İlerleme (1-100 Arası 'continue' ile Filtrelenmiş 3'ün Katları)                                                                |
#  ÖRNEK 15: List Comprehension Giriş (Pythonic Yaklaşımla Tek Satırda Veri Listeleme)                                                              |
#  ÖRNEK 16: Asal Sayı Kontrol Algoritması (Prime Number Check)                                                                                     |
#  ÖRNEK 17: Dik Üçgen Tasarımı (Lineer Artışlı Karakter Dizilimi)                                                                                  |
#  ÖRNEK 18: Ters Dik Üçgen Tasarımı (Azalan Döngü ve range Parametrizasyonu)                                                                       |
#  ÖRNEK 19: İkizkenar Piramit İnşası (Boşluk ve Karakter Dengesi Algoritması)                                                                      |
#  ÖRNEK 20: Elmas (Baklava) Deseni (Simetrik İç İçe Döngü Yönetimi)                                                                                | 
#  ÖRNEK 21: while Döngüsü ile Haklı Tahmin Mekanizması                                                                                             |             
# ===================================================================================================================================================

