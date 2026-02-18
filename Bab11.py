# ==================================================
# == BAB 11: MODÜLLER-1 (CHAPTER 11: MODULES-1) : ==
# ==================================================
"""
#---------------
# FONKSİYONLAR :
#---------------
-> Fonksiyon; belirli bir işi veya görevi yerine getirmek için tasarlanmış, ismi olan ve ihtiyaç duyulduğunda tekrar tekrar çağrılabilen kod bloklarıdır.
-> Bir fonksiyon sadece tanımlandığı dosya içerisinde yaşar. (Yereldir)
-> Kapsamı kısıtlıdır.
-> Başka bir programdan o fonksiyonu doğrudan çağıramazsınız. Kodun içine kopyalayıp yapıştırmanız gerekir.

#-----------
# MODÜLLER :
#-----------
-> Modüller birbiri ile ilgili kodların paketlenmesi ile oluşturulan kod kütüphaneleridir.
-> Modüller ise aslında içinde fonksiyonlar, değişkenler veya sınıflar barındıran ayrı dosyalardır.
-> Kapsamı geniştir.
-> Bir kez yazılır ve import komutuyla her yerden çağırılabilir. (Evrenseldir)
-> Daha önceden yazılan modülleri herhangi bir kod dosyasında kullanabilmek için kod dosyasının üzerine modülün bağlanması gerekir.
-> Harici kodları veya modülleri (kütüphaneleri) mevcut programınıza dahil etmek ve bu kodların içerdiği işlevleri, sınıfları veya sabitleri kullanabilir hale getirmek anlamına gelir.
-> Bu iş için 'import' komutu kullanılır. import işlemi modülünü içe aktarılması denir.
-> import math komutuyla modülü programa dahil ettikten sonra, o modülün içindeki herhangi bir öğeye erişmek için her zaman o modülün adını kullanırız.
"""

# Modüller de fonksiyonlarınkine benzer bir mantık taşır yani yazılan kodların yeniden kullanılabilirliğini sağlar.
# Modülerin fonksiyondan farkı yazılan kodun sonra başka program içerisinden çağrılabilir olmasıdır.

#----------------------------------
# 1. YERLEŞİK (BUILT-IN) MODÜLLER :
#----------------------------------
"""
-> Bu modüller Python’un içine C diliyle yazılıp gömülmüştür. 
-> Bunlar Python dilinin çekirdeğine gömülüdür. Python yüklendiği an belleğe hazır gelirler. Çok temel ve hızlı işlemler için kullanılırlar.
-> Bu olay 'Bir Tofaş şasesine BMW motoru entegre etmek' gibidir. 
-> Python yorumlayıcısını (interpreter) başlattığın anda bu fonksiyonlar ve modüller bellekte (RAM) hazırdır.
-> Teknik olarak bilgisayarında bir .py dosyası olarak bulunmazlar, doğrudan Python'un ana çalıştırılabilir dosyasının içindedirler.
-> Normal bir modülü (.py dosyası) import ettiğinde, Python o dosyayı bulur, okur ve derler.
-> Ancak Yerleşik Modüller zaten derlenmiş ve makine diline (C seviyesine) çok yakın bir halde beklerler.
-> Bu modüllere import dersin ve anında çalışır.
"""

"""
#------------------------
# 1.sys (Sistem Modülü) :
#------------------------
-> Python yorumlayıcısının kendisiyle ilgili her şey buradadır.
-> Python'un çalışma yolunu (path), versiyonunu, bellekteki nesne boyutlarını (getsizeof) ve komut satırı argümanlarını (argv) yönetir.
-> Programın işletim sistemiyle ilk temasını bu sağlar.


#-------------------------
# 2. time (Zaman Modülü) :
#-------------------------
-> Zamanı en saf haliyle, yani saniyelerle ölçer.
-> Kodun bir kısmının ne kadar sürede çalıştığını ölçmek (time.time()) veya programı belirli bir süre duraklatmak (time.sleep()) için kullanılır.
-> Farkı: datetime bir .py dosyasıdır (standart kütüphane), ama time yerleşiktir (built-in) ve çok daha hızlıdır.
-> time modülü, işletim sisteminin (Windows, Linux, macOS) çekirdek saatine doğrudan erişir. Bu yüzden çok hassastır. 
-> datetime ise bu saniyeleri alıp bizim okuyabileceğimiz "Yıl/Ay/Gün" formatına çeviren daha ağır bir "çevirmendir".

#--------------------------------------------
# 3. gc (Garbage Collector / Çöp Toplayıcı) :
#--------------------------------------------
-> Python'un temizlik işçisidir.
-> Bellekte artık kullanılmayan verileri takip eder ve onları silerek RAM'i boşaltır.
-> gc sistemi gereksiz yükten kurtarır.


#------------------------------------------
# 4. builtins (Temel Fonksiyonlar Deposu) :
#------------------------------------------
-> Aslında print(), int(), len() gibi her zaman kullandığın her şey bu modülün içindedir. 
-> 'Ana Fonksiyon deposu' gibi bir şey aslında.
-> İlginç bilgi: Sen print("Merhaba") yazdığında, Python aslında arka planda builtins.print("Merhaba") komutunu çalıştırır.

Sen Python'u çalıştırdığında manzara şöyledir:

En Üst Katman: Python Yorumlayıcısı (Interpreter)
                    
Ana Depo: builtins modülü (Sen import etmeden otomatik yüklenir).

İçindekiler :
-------------
1.Fonksiyonlar: print(), len(), abs()...
2.Veri Tipleri/Sınıflar: int, str, list, dict...
3.Hata Tipleri: ValueError, IndexError, KeyError...


#---------------------------------
# 5. marshal (İçsel Serileştirme) :
#--------------------------------- 
-> Bu biraz daha "mutfak" kısmıdır.
-> Python'un kendi .pyc dosyalarını (derlenmiş kodlarını) okumak ve yazmak için kullandığı içsel bir formattır.
-> Normal kullanıcılar pek dokunmaz ama sistemin işlemesi için kritiktir.
-> Çünkü marshal ile serileştirilen veriler Python versiyonları arasında uyumlu değildir. 
-> Yani Python 3.9 ile marshal ettiğin bir veriyi Python 3.11 okuyamayabilir. 
-> Bu yüzden biz "dış dünya" ile veri paylaşırken JSON veya Pickle kullanırız.
"""

import sys       # Sistem ayarları için
import time      # Hassas zaman ölçümü için
import gc        # Çöp toplayıcıyı kontrol etmek için
import builtins  # Normalde otomatik gelir ama import da edilebilir
import marshal   # .pyc dosyalarıyla çalışmak için

# Örnek kullanım:
print(f"Python versiyonu: {sys.version}")               #Çıktı: Python versiyonu: 3.13.7
print(f"Şu anki zaman (timestamp): {time.time()}")      #Çıktı: Şu anki zaman (timestamp): 1768768541.0388203
print(f"Temizlenen obje: {gc.collect()}")               #Çıktı: Temizlenen obje: 0
print(f"Mutlak Uzunluk: {builtins.len([1,2,3])}")       #Çıktı: Mutlak Uzunluk: 3
print(f"Byte hali: {marshal.dumps("Selam")}")           #Çıktı: Byte hali: b'\xda\x05Selam'

"""
NOT :
-> Bilgisayarlar zamanı bizim gibi "18 Ocak 2026, Pazar" şeklinde anlamazlar; çünkü bu format dilden dile ve ülkeden ülkeye değişir. 
-> Karmaşayı önlemek için bilgisayarlar zamanı saniye sayarak tutarlar.
-> Bu sayı, dünya çapında kabul edilen bir başlangıç noktasından (Milat) itibaren geçen toplam saniyedir:
-> Başlangıç: 1 Ocak 1970, Saat 00:00:00 (UTC).
-> Senin Sayın: 1 Ocak 1970'ten şu ana kadar tam 1.768.768.541 saniye geçmiş.

#-------------------------------------------------------
# Neden başka bir tarih değil de 1970 İşte 3 ana sebep :
#-------------------------------------------------------

1. Unix İşletim Sisteminin Doğuşu :
-----------------------------------
-> Modern işletim sistemlerinin atası sayılan Unix, 1960'ların sonunda geliştirilmeye başlandı.
-> Mühendisler sistem saati için bir "başlangıç noktası" seçmek zorundaydı.
-> Unix'in ilk versiyonları 1970'lerin başında tamamlandığı için, o anki "şimdiki zamanı" yuvarlak bir rakamla milat kabul ettiler.

2. 32-Bit Sistemlerin Sınırı :
------------------------------
-> O dönemdeki bilgisayarlar 32-bit idi. Zamanı saniye saniye sayarken, bu 32-bitlik hafıza alanının bize ne kadar süre yeteceğini hesapladılar.
-> Eğer başlangıcı 1900 yapsalardı, sayaç 1970'lere gelmeden dolabilirdi.
-> 1970'i seçerek, sistemin 2038 yılına kadar sorunsuz saniye saymasını sağladılar (Buna meşhur 2038 yılı problemi denir).

3. Keyfi Bir Karar (Standartlaşma) :
------------------------------------
-> Aslında 1971 veya 1969 da seçilebilirdi. Ancak mühendisler (Ken Thompson ve Dennis Ritchie) o dönemde bu tarihi standart olarak belirlediler. 
-> O günden sonra yazılan tüm diller (C, Java, Python, JavaScript) bu geleneği bozmadı.
"""

#----------------------------------
# 2. STANDART KÜTÜPHANE MODÜLLERİ :
#----------------------------------
"""
ÖZET OLARAK MODÜLLER -> AŞAĞIDA AYRINTILISI DA GÖSTERİLECEK.
#---------------------------------
# 1. os (İşletim Sistemi Modülü) :
#---------------------------------
-> Bilgisayarındaki dosya ve klasörlere hükmetmeni sağlar.
-> Klasör oluşturur, siler, dosyaların yerini değiştirir.
Örnek: os.getcwd() (Şu an hangi klasördeyim?)

#---------------------------------
# 2. random (Rastgelelik Modülü) :
#---------------------------------
-> Şans faktörü gereken her yerde kullanılır.
-> Rastgele sayılar üretir, bir liste içinden rastgele seçim yapar.
Örnek: random.randint(1, 100) (1 ile 100 arası sayı seç.)

#-----------------------------
# 3. math (Matematik Modülü) :
#-----------------------------
-> Temel operatörlerin (+, -) yetmediği karmaşık hesaplar içindir.
-> Pi sayısı, karekök, trigonometri gibi ileri hesapları yapar.
Örnek: math.sqrt(16) (16'nın karekökünü alır.)

#--------------------------------------
# 4. datetime (Tarih ve Zaman Modülü) :
#--------------------------------------
-> time modülünden farkı, veriyi bizim anlayacağımız "Gün/Ay/Yıl" formatında işlemesidir.
-> Bugünü verir, iki tarih arasındaki gün farkını hesaplar.
Örnek: datetime.datetime.now() (Şu anki tam tarih ve saat.)

#--------------------------------
# 5. json (Veri Değişim Modülü) :
#--------------------------------
-> İnternet dünyasının ortak dilidir.
-> Python sözlüklerini (dict) internette taşınabilir metin formatına çevirir.
Örnek: json.dumps(veri) (Veriyi JSON formatına paketle.)

#--------------------------------------------
# 6. shutil (Yüksek Seviye Dosya İşlemleri) :
#--------------------------------------------
-> os modülünün daha yetenekli kardeşidir.
-> Sadece tek bir dosyayı değil, koca bir klasörü içindekilerle birlikte kopyalamayı, taşımayı veya silmeyi sağlar.
Örnek: shutil.copy("kaynak.txt", "hedef/") # Dosyayı kopyalar.

#-------------------------------
# 7. csv (Tablolu Veri Modülü) :
#-------------------------------
-> Excel benzeri verilerle çalışmanın en basit yoludur.
-> Virgülle ayrılmış verileri (CSV) okur ve yazar. Veri analizi için ilk adımdır.
Örnek: csv.writer(dosya) # Verileri tablo formatında kaydeder.

#-------------------------------------------------
# 8. re (Regular Expressions / Düzenli İfadeler) :
#-------------------------------------------------
-> Metinlerin içindeki gizli dedektifindir.
-> Çok karmaşık metin aramaları yapar. Örneğin bir metindeki tüm e-postaları veya telefon numaralarını bir saniyede bulup çıkarır.
Örnek: re.findall(r"\d+", metin) # Metindeki tüm sayıları bulur.

#------------------------------------
# 9. statistics (İstatistik Modülü) :
#------------------------------------
-> Verilerin analizinde temel matematiksel özetler sunar.
-> Ortalamayı, medyanı veya standart sapmayı hesaplar.
Örnek: statistics.mean([1, 5, 8]) # Sayıların ortalamasını alır.

#-------------------------------------------
# 10. collections (Gelişmiş Veri Yapıları) :
#-------------------------------------------
-> Standart listelerin ve sözlüklerin (dict) "süper kahraman" versiyonlarıdır.
-> Örneğin bir listede hangi elemanın kaç kez geçtiğini anında sayan Counter gibi yapılar sunar.
Örnek: collections.Counter("abracadabra") # Hangi harften kaç tane olduğunu sayar.
"""


#---------------------------------
# 1. os (İŞLETİM SİSTEMİ MODÜLÜ) :
#---------------------------------
import os
"""
-> os modülü, yazdığın programın üzerinde çalıştığı İşletim Sistemi (Operating System) ile konuşmasını sağlayan bir köprüdür.
-> Genellikle dosya işlemleri, klasör yönetimi ve sistem bilgilerine ulaşmak için kullanılır.
-> Windows, Linux veya macOS fark etmeksizin kodunun işletim sistemiyle etkileşime girmesine olanak tanır.
-> İşletim sistemin ne olursa olsun (Windows, Linux, Mac) her Python dosyasının başına import os yazmak zorunda değilsin.
-> Sadece kodunun içinde işletim sistemiyle ilgili os modülüne ait özel fonksiyonları (klasör oluşturma, dosya silme, yol bulma gibi) kullanacaksan bu satırı eklemelisin.

-> Yeni klasörler oluşturabilirsin ve mevcut olanları silebilirsin.
-> Bir dosyanın adını değiştirebilirsin.
-> Bilgisayarın o an hangi klasörde çalıştığını öğrenebilirsin.
-> İşletim sistemindeki çevre değişkenlerine (Environment Variables) ulaşabilirsin.
"""

#-----------------------------------------------------------------------------------------------------
# 1. DİZİN VE KONUM YÖNETİMİ                                                                         |
#-----------------------------------------------------------------------------------------------------
# Bilgisayarın dosya hiyerarşisinde yol bulmak ve hareket etmek için kullanılır.                     |
#-----------------------------------------------------------------------------------------------------
# | os.getcwd()          | Mevcut çalışma dizinini (klasör yolunu) verir.                            |      
# | os.chdir(yol)        | Çalışma dizinini belirtilen yola değiştirir.                              |
# | os.listdir()         | Bulunulan dizindeki dosya ve klasörleri liste olarak döner.               |
# | os.mkdir(ad)         | Belirtilen isimde yeni bir klasör oluşturur.                              |
# | os.makedirs()        | İç içe geçmiş klasör yolları oluşturur (Örn: Sınavlar/Matematik/Notlar).  |
# | os.rmdir(ad)         | Sadece içi boş olan bir klasörü siler.                                    |
# | os.removedirs()      | İç içe geçmiş boş klasör zincirini temizler.                              |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 2. DOSYA VE SİSTEM OPERASYONLARI                                                                   |
#-----------------------------------------------------------------------------------------------------
# Dosyaların fiziksel varlıkları ve işletim sistemi ayarları üzerinde işlem yapar.                   |
#-----------------------------------------------------------------------------------------------------
# | os.rename(e, y)     | Dosya veya klasörün ismini değiştirir.                                     |
# | os.remove(yol)      | Belirtilen dosyayı kalıcı olarak siler (Dikkat: Geri dönüşü yoktur!).      |
# | os.stat(yol)        | Dosya boyutu, erişim tarihi gibi teknik verileri getirir.                  |
# | os.name             | İşletim sistemi ailesini verir (nt: Windows, posix: Linux/Mac).            |
# | os.environ          | Sistem çevre değişkenlerini (Path vb.) bir sözlük olarak sunar.            |
# | os.system()         | Terminale/CMD'ye doğrudan komut gönderir (Örn: os.system("cls")).          |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 3. OS.PATH: AKILLI YOL YÖNETİMİ                                                                    |
#-----------------------------------------------------------------------------------------------------
# Dosya yollarını (Path) analiz etmek ve kontrol etmek için kullanılan alt modüldür.                 |
#-----------------------------------------------------------------------------------------------------
# | os.path.exists()    | Belirtilen yol (dosya/klasör) var mı? (True/False).                        |
# | os.path.join()      | İşletim sistemine uygun şekilde yolları birleştirir (/ veya \).            |
# | os.path.isfile()    | İşaret edilen konumun bir 'dosya' olup olmadığını kontrol eder.            |
# | os.path.isdir()     | İşaret edilen konumun bir 'klasör' olup olmadığını kontrol eder.           |
# | os.path.abspath()   | Göreli (relative) yolu tam (absolute) yola çevirir.                        |
# | os.path.split()     | Yolu, dizin ve dosya adı olarak iki parçaya böler.                         |
# | os.path.splitext()  | Dosya adı ile uzantısını (.txt, .py) birbirinden ayırır.                   |
#-----------------------------------------------------------------------------------------------------


#---------------------------------
# 2. random (RASTGELELİK MODÜLÜ) :
#---------------------------------
import random
"""
-> random modülü, Python'da rastgele sayılar üretmek, listelerden rastgele seçimler yapmak ve verileri karıştırmak için kullanılan standart bir kütüphanedir.
-> Bilgisayar dünyasında tam bir "rastgelelik" (true randomness) zordur; bu modül "sözde rastgele" (pseudo-random) algoritmalar kullanır.

-> Ne İşe Yarar?
----------------
1. Oyunlardaki zar atma, kritik vuruş (crit) şansı gibi mekanikleri kurar.
2. Güvenli şifreler veya doğrulama kodları üretir.
3. Elindeki veri setini (örneğin bir deste kartı) karıştırır.
4. Büyük veriler arasından tarafsız örneklemler seçer.
"""

#----------------------------------
# 1. Sayısal Üretim Fonksiyonları :
#----------------------------------

# 0.0 ile 1.0 arasında ondalık sayı üretir
print(f"Rastgele ondalık (0-1): {random.random()}")   # random modülüne git ve onun içindeki random() isimli metodu çalıştır."

# Belirlenen aralıkta ondalık sayı üretir (Örn: 5.5 ile 10.5 arası)
print(f"Aralıklı ondalık: {random.uniform(5.5, 10.5)}")

# Belirlenen aralıkta TAM SAYI üretir (Sınırlar DAHİLDİR)
print(f"Rastgele tam sayı (1-100): {random.randint(1, 100)}")

# Belirli bir adım miktarına göre tam sayı üretir (Örn: 0'dan 100'e kadar 5'in katları)
print(f"5'in katı rastgele: {random.randrange(0, 101, 5)}")


#---------------------------------------
# 2. Liste ve Koleksiyon Operasyonları :
#---------------------------------------
arkadaslar = ["Ali", "Emre", "Qusay", "Ümit", "Baran", "Erol"]

# Listeden rastgele TEK BİR eleman seçer
secilen = random.choice(arkadaslar)
print(f"Günün şanslısı: {secilen}")

# Listeden TEKRARSIZ k adet eleman seçer (Çekiliş sistemi için en iyisi) . Orijinal listeyi bozmaz.
kazananlar = random.sample(arkadaslar, k=2)
print(f"Çekiliş Kazananları: {kazananlar}")

# Listeden eleman tekrarına izin vererek seçim yapar (choices) . Ağırlıklı seçim yapmaya da olanak tanır.
print(f"Çoklu seçim: {random.choices(arkadaslar, k=3)}")

# Listeyi yerinde karıştırır (shuffle)
# DİKKAT: Bu fonksiyon bir şey döndürmez, listenin kendisini kalıcı olarak değiştirir.
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(sayilar)
print(f"Karıştırılmış liste: {sayilar}")


#------------------------------
# 3. Gelişmiş Komutlar (Seed) :
#------------------------------

# random.seed(deger): Üretilen rastgele sayıları sabitlemek için kullanılır.
# Eğer aynı seed değerini verirseniz, her zaman aynı "rastgele" sayıları alırsınız.
# Bu özellik, hata ayıklama (debug) ve test süreçlerinde hayati önem taşır.

# 1. DURUM: Seed Belirleyerek Sabitleme :
#----------------------------------------
random.seed(42) # 42 sayısını bir kilit gibi düşünün
print(f"1. Deneme (Seed 42): {random.randint(1, 100)}")
print(f"2. Deneme (Seed 42): {random.randint(1, 100)}")

print("-" * 30)

# Şimdi kilidi tekrar 42'ye kuruyoruz (Sayılar en baştan aynı sırayla gelecek)
random.seed(42)
print(f"3. Deneme (Seed 42): {random.randint(1, 100)}") # 1. deneme ile AYNI sayı çıkar
print(f"4. Deneme (Seed 42): {random.randint(1, 100)}") # 2. deneme ile AYNI sayı çıkar

print("-" * 30)

# 2. DURUM: Seed Belirlemeden (Tamamen Rastgele) :
#-------------------------------------------------
# Eğer seed vermezseniz Python arka planda sistem saatini (timestamp) seed olarak kullanır.
# Bu yüzden her saniye farklı bir sonuç alırsınız.
print(f"Seed'siz Rastgele: {random.random()}")


#-----------------------------
# 3. math (MATEMATİK MODÜLÜ) :
#-----------------------------
import math
"""
-> Python programlama dilinde  karmaşık matematiksel işlemler ve fonksiyonlar içeren math modülünü programa dahil etmek için kullanılan bir ifadedir.
-> Bu modül, Python'un standart kütüphanesinin bir parçasıdır ve ek kurulum gerektirmez.

-> Ne İşe Yarar ?:
------------------
1. Sık kullanılan matematiksel sabitlere (π, e, tau, infinity, nan vb.) kolayca erişim sağlar.
2. Trigonometrik Fonksiyonlar (Sinüs, kosinüs, tanjant) gibi trigonometrik ve bunların ters (arc) fonksiyonlar üzerinde işlem yapmamıza olanak tanır.
3. Doğal logaritma (log), 10 ve 2 tabanlı logaritmalar (log10, log2) ile üstel fonksiyon (exp) hesaplamaları yapmamıza olanak tanır."
4. Faktöriyel (factorial), karekök (sqrt), mutlak değer (fabs), ebob (gcd) ve yuvarlama (ceil, floor) gibi spesifik matematiksel işlemleri gerçekleştirmek için kullanılır."
"""

# Bu modül eklendikten sonra yer alan matematiksel değer ve komutlara erişilebilir.
# math modülü, Python'ın yerleşik matematiksel işlevlerinin ötesine geçerek daha gelişmiş matematiksel işlemler ve sabitler sağlar.

#---------------------------
# 1. MATEMATİKSEL SABİTLER :
#---------------------------
print(f"Pi sayısı :{math.pi}")           #Çıktı: Pi sayısı:3.141592653589793  , # math.pi kullanımı, programın açıkça "math modülündeki pi değeri" anlamına geldiğini bilmesini sağlar.
print(f"Euler sayısı :{math.e}")         #Çıktı: Euler sayısı:2.718281828459045
print(f"Tau(2π) sayısı :{math.tau}")     #Çıktı: Tau(2π) sayısı:6.283185307179586
print(f"Sonsuzluk :{math.inf}")          #Çıktı: Sonsuzluk:inf
print(f"Sayı Olmayan Değer:{math.nan} ") #Çıktı: Sayı Olmayan Değer:nan 

# Ama biz bunu formating yerine değişken atayarak da yazabiliriz. 
pi_sayisi = math.pi                        #Çıktı: 3.141592653589793
print(pi_sayisi)

euler_sayisi = math.e                      #Çıktı: 2.718281828459045
print(euler_sayisi)

tau_sayisi = math.tau                      #Çıktı: 6.283185307179586
print(tau_sayisi)

sonsuzluk_sayisi = math.inf                #Çıktı: inf
print(sonsuzluk_sayisi)

sayi_degil = math.nan                      #Çıktı: nan 
print(sayi_degil)

# Bu şekilde yazılabilir. Aslında burada göstermek istediğimiz şey tek bir  yazım şeklinin olmayışı ve yazım şeklinin kullanıca bağlı olmasını göstermektir.
import math
                                       
print("Pi:", math.pi)                    #Çıktı: Pi: 3.141592653589793
print("Euler sayısı:", math.e)           #Çıktı: Euler sayısı: 2.718281828459045
print("Tau:", math.tau)                  #Çıktı: Tau: 6.283185307179586
print("Sonsuzluk:", math.inf)            #Çıktı: Sonsuzluk: inf
print("Tanımsız:", math.nan)             #Çıktı: Tanımsız: nan


#--------------------------------
# 2. TRİGONOMETRİK FONKSİYONLAR :
#--------------------------------

# Sinüs, Kosinüs, Tanjant
print(f"sin(π/6):{math.sin(math.pi/6)}")  #Çıktı: sin(π/6):0.49999999999999994 (0.5)
print(f"cos(π/3):{math.cos(math.pi/3)}")  #Çıktı: cos(π/3):0.5000000000000001 (0.5)
print(f"tan(π/4):{math.tan(math.pi/4)}")  #Çıktı: tan(π/4):0.9999999999999999 (1.0)

"""
-> Fark ettiyseniz math.cot yok. Bunun sebebi performans ve minimum kaynakla maksimum iş prensibine dayanıyor.
-> cotx=1/tanx olduğu için ayrıyeten tanımlanma ihtiyacı duyulmamıştır. math.tan yeterli görünmüştür.
-> Kotanjant fonksiyonu 0,180,360 gibi pi’nin katlarında tanımsızdır (sonsuza gider).
-> Eğer kütüphaneye math.cot eklenseydi, bu "tanımsızlık" durumlarında programın çökmemesi için arka planda sürekli ekstra kontrol mekanizmaları (if-else blokları) çalışacaktı.
-> Ama cot kullanılacaksa bu şekilde kullanabilirsin.
"""
aci = math.pi/3
cot_degeri = 1/math.tan(aci)
print(f"cot(π/4):{cot_degeri}")           #Çıktı: cot(π/3):0.577350269189626


# Ters trigonometrik fonksiyonlar
print(f"arcsin(0.5): {math.asin(0.5)}")        # π/6 ≈ 0.5236 radyan
print(f"arccos(0.5): {math.acos(0.5)}")        # π/3 ≈ 1.0472 radyan
print(f"arctan(1): {math.atan(1)}")            # π/4 ≈ 0.7854 radyan

# Derece-radyan dönüşümü
print(f"30 derece = {math.radians(30)} radyan")             #Çıktı: 30 derece = 0.5235987755982988 radyan
print(f"π/4 radyan = {math.degrees(math.pi/4)} derece")     #Çıktı: π/4 radyan = 45.0 derece


# -------------------------------------
# 3. LOGARİTMİK VE ÜSTEL FONKSİYONLAR :
# -------------------------------------

# Logaritma fonksiyonları
print(f"ln(e):{math.log(math.e)}")                  #Çıktı: ln(e):1.0
print(f"log10(1000):{math.log(1000)}")              #Çıktı: log10(1000):6.907755278982137
print(f"log2(8):{math.log2(8)}")                    #Çıktı: log2(8):3.0

# İstediğimiz tabanda logaritma
print(f"log_5(25): {math.log(25, 5)}")              #Çıktı: log_5(25): 2.0

# Üstel fonksiyon
print(f"e^2:{math.exp(2)}")                         #Çıktı: e^2:7.38905609893065
print(f"2^3:{math.pow(2,3)}")                       #Çıktı: 2^3:8.0

#-----------------------
# 4. ÖZEL FONKSİYONLAR :
#-----------------------

# Faktöriyel
print(f"5!={math.factorial(5)}")                    #Çıktı: 5!=120
print(f"3!={math.factorial(3)}")                    #Çıktı: 3!=6

# Karekök
print(f"√25 ={math.sqrt(25)}")                      #Çıtkı: √25 =5.0
print(f"√900={math.sqrt(900)}")                     #Çıktı: √900=30.0

# Mutlak Değer
print(f"|-3.14|={math.fabs(-3.14)}")                #Çıktı: |-3.14|=3.14
print(f"|6.89|={math.fabs(6.89)}")                  #Çıktı: |6.89|=6.89

# En büyük ortak bölen (GCD(Greatest Common Divisor))
print(f"EBOB(36,48)={math.gcd(36,48)}")             #Çıktı: EBOB(36,48)=12
print(f"EBOB(20,60)={math.gcd(20,60)}")             #Çıktı: EBOB(20,60)=20

# En küçük ortak kat (LCM (Least Common Multiple))-> (Python 3.9+) 
print(f"EKOK(15,20)={math.lcm(15,20)}")             #Çıktı: EKOK(15,20)=60
print(f"EKOK(20,60)={math.lcm(20,60)}")             #Çıktı: EKOK(20,60)=60

# Mod alma (float için)
print(f"10.5 mod 3.2={math.fmod(10.5,3.2)}")        #Çıktı: 10.5 mod 3.2=0.8999999999999995
print(f"14.5 mod 3.67={math.fmod(14.5,3.67)}")      #Çıktı: 14.5 mod 3.67=3.49

#-------------------------
# 5. YUVARLAMA İŞLEMLERİ :
#-------------------------

# Yukarı yuvarla
print(f"ceil(4.2): {math.ceil(4.2)}")            #Çıktı: ceil(4.2): 5
print(f"ceil(99.34):{math.ceil(99.34)}")         #Çıktı: ceil(99.34):100 

# Her zaman kendinden büyük veya kendisine eşit olan en yakın tam sayıya yuvarlar. Yani yuvarlama işlemi her zaman yukarıya doğru yapılır.
# Bu şekilde de değer değişkeni atayarak yapılabilir.
tavan_deger=math.ceil(2.95)
print(tavan_deger)

# Aşağı yuvarla
print(f"floor(4.8): {math.floor(4.8)}")          #Çıktı: floor(4.8): 4
print(f"floor(92.23):{math.floor(92.23)}")       #Çıktı: floor(92.23):92

# Tam kısmını al
print(f"trunc(-3.7): {math.trunc(-3.7)}")        #Çıktı: trunc(-3.7): -3 
print(f"trunc(78.345):{math.trunc(78.345)}")     #Çıktı: trunc(78.345): 78

# En yakın tam sayıya yuvarla
print(f"round(3.5): {round(3.5)}")               #Çıktı: round(3.5): 4
print(f"round(-3.5):{round(-3.5)}")              #Çıktı: round(-3.5):-4


#-----------------------------
# 6. HİPERBOLİK FONKSİYONLAR :
#-----------------------------
print(f"sinh(1): {math.sinh(1)}")               # Çıktı: sinh(1): 1.1752011936438014 ≈ 1.175
print(f"cosh(1): {math.cosh(1)}")               # Çıktı: cosh(1): 1.5430806348152437 ≈ 1.543
print(f"tanh(1): {math.tanh(1)}")               # Çıktı: tanh(1): 0.7615941559557649 ≈ 0.762


#------------------------------------
# 7. UZAKLIK VE HİPOTENÜS HESAPLAMA :
#------------------------------------

# İki nokta arasındaki mesafe
mesafe = math.dist([1, 2], [4, 6])
print(f"(1,2) ile (4,6) arası mesafe: {mesafe}")  #Çıktı: (1,2) ile (4,6) arası mesafe: 5.0

mesafe=math.dist([1,3],[7,14])                    #Çıktı: Mesafe: 12.529964086141668
print("Mesafe:",mesafe)

# Hipotenüs hesaplama
hipotenus = math.hypot(3, 4)
print(f"Dik kenarları 3 ve 4 olan üçgenin hipotenüsü: {hipotenus}")  #Çıktı: Dik kenarları 3 ve 4 olan üçgenin hipotenüsü: 5.0

hipotenus=math.hypot(5,12)
print("Hipotenüs:",hipotenus)                      #Çıktı: Hipotenüs: 13.0

#----------------------------------------------
# 8. KOMBİNASYON VE PERMÜTASYON (Python 3.8+) :
#----------------------------------------------

# Kombinasyon
print(f"5'in 2'li kombinasyonu: {math.comb(5, 2)}")  #Çıktı: 5'in 2'li kombinasyonu :10
print(f"7'nin 4'lü kombinasyonu:{math.comb(7,4)}")   #Çıktı: 7'nin 4'lü kombinasyonu:35

print(f"5'in 2'li permütasyonu: {math.perm(5,2)}")   #Çıktı: 5'in 2'li permütasyonu :20
print(f"7'in 4'li permütasyonu: {math.perm(7,4)}")   #Çıktı: 7'nin 4'lü permütasyonu:840

#----------------------------------
# 9. GAMMA VE FAKTÖRİYEL İLİŞKİSİ :
#----------------------------------

# Gamma fonksiyonu: Γ(n) = (n-1)!
print(f"Gamma(5) = {math.gamma(5)}")            # 24.0 (yani 4!)
print(f"4! = {math.factorial(4)}")              # 24

# Gamma fonksiyonu: Γ(n) = (n-1)!
# Doğal sayılar için:
# Γ(n) = (n-1)!  (n pozitif tam sayı)

print("Γ(1) = 0! =", math.gamma(1))      # 1.0
print("Γ(2) = 1! =", math.gamma(2))      # 1.0
print("Γ(3) = 2! =", math.gamma(3))      # 2.0
print("Γ(4) = 3! =", math.gamma(4))      # 6.0
print("Γ(5) = 4! =", math.gamma(5))      # 24.0
print("Γ(6) = 5! =", math.gamma(6))      # 120.0

# Gamma fonksiyonu faktöriyelin GENİŞLETİLMİŞ HALİDİR
# Faktöriyel sadece tam sayılar için tanımlıyken
# Gamma fonksiyonu reel ve kompleks sayılar için tanımlıdır


"""
-> Tarih ve zaman işlemleri; zamanın akışını (saniye), takvimin düzenini ve nizamı yöneten araçlardır.    
-> time modülü: Zamanı 1 Ocak 1970'ten (Epoch) geçen saniyeler (tick) olarak görür (Sistem odaklı).       
-> datetime modülü: Zamanı yıl, ay, gün gibi anlaşılır nesneler olarak yönetir (İşlem odaklı).            
-> calendar modülü: Takvim görünümleri ve artık yıl (leap year) hesaplamaları için kullanılır.  
"""

#----------------
# 4.time MODÜLÜ :
#----------------
"""
#-------------
# 1. NEDİR ? :
#-------------
-> Tarih ve zaman işlemleri, Python’da zamanın akışını (saniye), takvimin düzenini (gün/ay/yıl) ve astronomik nizamı (artık yıl) yöneten araçlar bütünüdür.

#------------------------
# 2. NEDEN KULLANILIR ? :
#------------------------
-> Logging: Sistemsel işlemlerin "ne zaman" gerçekleştiğini mühürlemek için.
-> Performans: Kodun ne kadar sürede çalıştığını (hızını) ölçmek için.
-> Hesaplama: İki tarih arasındaki mesafeyi (Örn: Kaç gün kaldı?) bulmak için. -> Nizam: Takvim görünümleri oluşturmak ve artık yılları tespit etmek için.
-> Python dilinde tarih ve zaman işlemleri için "calendar" ve "time" modülleri kullanılır.

#----------------------------------------
# 3. NASIL KULLANILIR? (HOW TO USE IT?) :
# ---------------------------------------
-> Farklı formlarda zaman bilgilerine ulaşmak için time modülü kullanılır.
-> Bu modül içerisinde yer alan yine aynı isimli time() fonksiyonu zamanı tick formunda verir.
-> tick bir saniyeyi oluşturan birimler, en küçük zaman parçalarıdır.
-> Ondalıklı sayı türünde bir veridir.
"""

import time
print(time.time())
# Bu komut, time modülü içerisindeki time adlı nesneyi (bir fonksiyonu) ekrana yazdırmaya çalışır.
# time()fonksiyonu ile elde edilen tick formundaki zaman bilgisi farklı formlara dönüştürülerek güncel zaman bilgisi görüntülenebilir.

#---------------------------
# YEREL ZAMANI GÖRÜNTÜLEME :
#---------------------------
import time
guncel_zaman=time.localtime()
print(guncel_zaman)

#Çıktı: time.struct_time(tm_year=2025, tm_mon=12, tm_mday=3, tm_hour=14, tm_min=34, tm_sec=24, tm_wday=2, tm_yday=337, tm_isdst=0) 

# Bu yapı içerisinde yer alan her bir özellik sıfırdan başlayan bir sıra numarasına sahiptir ve istenen özelliğe sıra numarası ile erişmek mümkündür.
# Bu sırayı bilmek gerekir. Ve numaralar değişmemektedir.
# Python'daki time.localtime() fonksiyonu bize bir nesne döndürür ama bu nesne aynı zamanda bir tuple (demet) gibi davranır. 

"""
------------------------------------------------------------------------------------------------------
| İNDEKS SIRA NUMARALARI (BU SIRA DEĞİŞMEZ):                                                         |
------------------------------------------------------------------------------------------------------
| [0] tm_year  -> 4 haneli yıl bilgisi                                                               |
| [1] tm_mon   -> 0-12 arası rakam ile belirtilen ay bilgisi                                         |
| [2] tm_mday  -> 1 ile 31 arası değer alan gün bilgisi                                              |
| [3] tm_hour  -> 0 ile 23 arası değer alan saat bilgisi                                             |
| [4] tm_min   -> 0 ile 59 arası değer alan dakika bilgisi                                           |
| [5] tm_sec   -> 0 ile 60 arası değer alan saniye bilgisi                                           |
| [6] tm_wday  -> 0 ile 6 arası  değer alan haftanın günü bilgisi (0  Pazartesi)                     |
| [7] tm_yday  -> 1 ile 366 arası yılın günü bilgisi (366 artık yıl olması halinde)                  |
| [8] tm_isdst -> Yaz saati uygulaması 0 değeri yaz saati uygulaması yok , 1 var anlamına gelir.     |
------------------------------------------------------------------------------------------------------
""" 
"""
Bu indeksler Neden Değişmez ? :
-------------------------------
-> Eğer bu numaralar değişseydi, dünya üzerindeki milyonlarca yazılım (bankacılık sistemleri, uçuş kontrol sistemleri vb.) anında çökerdi. 
-> Yazılımcılar olarak biz bu "sabitliğe" güveniriz.
"""
import time
guncel_zaman=time.localtime()

# 0- YIL BİLGİSİ
guncel_yil = guncel_zaman[0]
print(f"Yıl: {guncel_yil}")
# Çıktı: 2026

# 1- AY BİLGİSİ (1-12)
guncel_ay = guncel_zaman[1]
print(f"Ay: {guncel_ay}")
#Çıktı: 1

# 2- GÜN BİLGİSİ (Ayın kaçıncı günü)
guncel_gun = guncel_zaman[2]
print(f"Gün: {guncel_gun}")
#Çıktı: 18

# 3- SAAT BİLGİSİ (0-23)
guncel_saat = guncel_zaman[3]
print(f"Saat: {guncel_saat}")
#Çıktı: 22

# 4- DAKİKA BİLGİSİ (0-59)
guncel_dakika = guncel_zaman[4]
print(f"Dakika: {guncel_dakika}")
#Çıktı: 37

# 5- SANİYE BİLGİSİ (0-59)
guncel_saniye = guncel_zaman[5]
print(f"Saniye: {guncel_saniye}")
#Çıktı: 29

# 6- HAFTANIN GÜNÜ (0=Pazartesi, 6=Pazar)
haftanin_gunu = guncel_zaman[6]
print(f"Haftanın Günü (0-6): {haftanin_gunu}")
#Çıktı: 6 (Pazar)

# 7- YILIN GÜNÜ (1-366)
yilin_gunu = guncel_zaman[7]
print(f"Yılın Kaçıncı Günü: {yilin_gunu}")
#Çıktı: 18

# 8- YAZ SAATİ DURUMU (0: Yok, 1: Var)
yaz_saati_durumu = guncel_zaman[8]
print(f"Yaz Saati Uygulaması: {yaz_saati_durumu}")
#Çıktı: 0

#-------------------------------------
# ZAMANI BİÇİMLENDİREREK GÖRÜNTÜLEME :
#-------------------------------------
import time 
formatlizaman=time.asctime()
print(formatlizaman)
# Çıktı : Wed Dec  3 14:46:52 2025

import time
formatlizaman=time.strftime("%d %m %y %H %M %S")
print(formatlizaman)
# Zamanı istenen herhangi bir formatta görüntülemek için strftime()fonksiyonu kullanılabilir.

#Format içerisinde % ile başlayan her bir harf ,bir zaman birimini temsil eder.Bazılarının anlamları şöyledir.
"""
-----------------------------------------------------    
| %d -> Rakam olarak gün bilgisi                    |
| %m -> İki haneli rakam olarak ay bilgisi          |
| %b -> Üç haneli yazı olarak ay bilgisi            |
| %y -> İki haneli rakam olarak yıl bilgisi         |
| %Y -> Dört haneli rakam olarak yıl bilgisi        |
| %M -> Dakika bilgisi                              |
| %S -> Saniye bilgisi                              |
| %a -> Üç haneli yazı ile gün adı                  |
| %A -> Günün tam adı                               |
| %D -> Ay/Gün/Yıl                                  |
-----------------------------------------------------
"""

#----------------------------------------------------
# 2. datetime MODÜLÜ (NESNE TABANLI ZAMAN YÖNETİMİ) :                                                 
#----------------------------------------------------

#--------------------
# A. NEDİR? (WHAT?) :
#--------------------
"""
-> datetime, zamanı "saniye yığını" (tick) olarak değil; Yıl, Ay, Gün, Saat gibi birer "Nesne" olarak temsil eden bir modüldür. 
-> İçinde tarih (date), zaman (time) ve her ikisinin birleşimi (datetime) olan sınıflar barındırır.
"""
#------------------------------
# B. NEDEN KULLANILIR? (WHY?) :
#------------------------------
"""
# 1. Okunabilirlik: Saniyeleri (1705678234) okumak imkansızdır, "2026-01-19" demek çok daha kolaydır.
# 2. Aritmetik İşlemler: "Bugünden 45 gün sonrası ne zamana denk gelir?" gibi takvim hesaplarını yapar.
# 3. Kıyaslama: "Bu sipariş mi daha önce verildi, yoksa şu mu?" sorusuna (t1 > t2) şeklinde cevap verir.
# 4. Veritabanı Uyumu: SQL ve modern veritabanları tarihleri datetime formatında saklar ve bekler.
"""

#---------------------------------
# C. MODÜLÜN TEMEL YAPI TAŞLARI  :                                          
#---------------------------------
from datetime import datetime, date, time, timedelta

# 1. datetime Sınıfı: Hem tarih hem saat bilgisini tutar.
su_an = datetime.now()
print(f"Tam Zaman Nesnesi: {su_an}")

# 2. date Sınıfı: Saatle işimiz yoksa, sadece takvim bilgisini tutar.
bugun = date.today()
print(f"Sadece Tarih: {bugun}")

# 3. time Sınıfı: Tarihle işimiz yoksa, sadece gün içindeki saati (00:00 - 23:59) tutar.
saat = time(15, 30, 45)         # 15:30:45 nesnesini oluşturur.
print(f"Sadece Saat: {saat}")

# 4. timedelta Sınıfı: ZAMANDAKİ "MESAFE" (En önemli fark buradadır!)
# İki tarih arasındaki 'süre miktarını' (gün, saat, dakika) ifade eder.
# Bir tarihe süre eklemek veya çıkarmak için kullanılır.

simdi = datetime.now()

# Bir süreyi değişkene atayalım:
bes_gun = timedelta(days=5)
on_saat = timedelta(hours=10)

# Gelecek ve Geçmiş Hesaplama:
bes_gun_sonra = simdi + bes_gun
on_saat_once = simdi - on_saat

print(f"Bugün: {simdi.strftime('%d %B %Y')}")
print(f"5 Gün Sonra: {bes_gun_sonra.strftime('%d %B %Y')}")
print(f"10 Saat Önceki Zaman: {on_saat_once}")

# İki tarih arasındaki toplam saniye veya günü bulma:
dogum_gunu = datetime(2026, 12, 31)
kalan_sure = dogum_gunu - simdi
print(f"Yılbaşına kalan toplam saniye: {kalan_sure.total_seconds()}")


#--------------------------------------------------
# 3. calendar MODÜLÜ (Takvim ve Astronomik Nizam) :                                                   
#--------------------------------------------------

#--------------------
# A. NEDİR? (WHAT?) :
#--------------------
"""
-> Takvimsel verileri görsel (text-based) tablolar halinde sunan modüldür.
-> Haftanın hangi günden başlayacağı, belirli bir ayın kaç gün sürdüğü ve 
-> "Artık Yıl" (Leap Year) gibi astronomik hesaplamaları yapmak için kullanılır.
"""

#------------------------------
# B. NEDEN KULLANILIR? (WHY?) :
#------------------------------
"""
-> 1. Görselleştirme: Terminal ekranına bir ajanda veya takvim basmak için en kolay yoldur.
-> 2. Nizam: Yazılımın "Şubat bu yıl 29 mu çekiyor?" sorusuna kesin cevap vermesini sağlar.
-> 3. Haftalık Planlama: Bir tarihin haftanın hangi gününe (Pazartesi, Salı...) denk geldiğini bulur.
"""
#--------------------------------------------------------
# C. ÖNEMLİ FONKSİYONLAR VE AYRINTILAR (Core Functions) :                                            
#--------------------------------------------------------

import calendar

# 1. calendar(yıl) -> Tüm Yılı Yazdırır
# Belirtilen yılın 12 ayını yan yana ve alt alta bir tablo olarak döner.
yillik_takvim = calendar.calendar(2026)
print(yillik_takvim)

# 2. month(yıl, ay) -> Tek Bir Ayı Yazdırır
# Sadece istediğin ayın günlerini haftalık düzende gösterir.
kasim_takvimi = calendar.month(2025, 11)
print(f"2025 Kasım Ayı:\n{kasim_takvimi}")

# 3. isleap(yıl) -> Artık Yıl Kontrolü
# Dünya güneş etrafında 365 gün 6 saatte döner. Bu 6 saat, 4 yılda bir (4x6=24) 1 tam gün eder.
# Bu gün Şubat'a eklenir (29 Şubat). Buna 'Artık Yıl' denir.
print(f"2024 Artık yıl mı?: {calendar.isleap(2024)}") # True
print(f"2026 Artık yıl mı?: {calendar.isleap(2026)}") # False

# 4. leapdays(yıl1, yıl2) -> Aralıkta Kaç Artık Yıl Var?
# Belirtilen iki yıl arasında toplam kaç tane 366 çeken gün olduğunu hesaplar.
artik_gun_sayisi = calendar.leapdays(2000, 2026)
print(f"2000-2026 arası toplam {artik_gun_sayisi} kez Şubat 29 çekti.")

# 5. weekday(yıl, ay, gün) -> Günün Adını Bulma
# Verilen tarihin haftanın kaçıncı günü olduğunu döner (0: Pazartesi ... 6: Pazar).
gun_no = calendar.weekday(2026, 1, 19)
print(f"19 Ocak 2026 haftanın {gun_no}. günüdür (Pazartesi).")


#-----------------
# 5. json MODÜLÜ :
#-----------------
"""
-> JSON (JavaScript Object Notation), hafif, metin tabanlı ve evrensel bir veri değişim formatıdır.  
-> Makinelerin kolayca ayrıştırdığı, insanların ise rahatça okuyabildiği bir yapıdadır.             
-> Python'daki Sözlük (dict) ve Liste (list) yapılarına çok benzer ancak dil bağımsızdır.           
"""

#-----------------------------------------------------------------------------------------------------
# A. TEMEL KAVRAMLAR: PYTHON DICT VS JSON                                                            |
#-----------------------------------------------------------------------------------------------------
# | ÖZELLİK         | PYTHON SÖZLÜĞÜ (dict)           | JSON FORMATI (.json)                         |
# |-----------------|---------------------------------|----------------------------------------------|
# | Yaşam Alanı     | Bilgisayarın RAM belleği        | Hard disk (Dosya) veya İnternet trafiği      |
# | Dil Desteği     | Sadece Python anlar             | Tüm programlama dilleri (Java, C#, JS...)    |
# | Tırnak Yapısı   | Tek (') veya Çift (") tırnak    | Sadece Çift Tırnak (") zorunludur            |
# | Boolean/Null    | True, False, None               | true, false, null                            |
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# B. json MODÜLÜ FONKSİYONLARI                                                                       |
#-----------------------------------------------------------------------------------------------------
# | FONKSİYON       | İŞLEM YÖNÜ                      | AÇIKLAMA                                     |
# |-----------------|---------------------------------|----------------------------------------------|
# | json.dumps()    | Python Objesi -> Metin (str)    | Veriyi metin olarak paketler (S: String)     |
# | json.loads()    | Metin (str) -> Python Objesi    | Metni Python sözlüğüne çözer (L: Load)       |
# | json.dump()     | Python Objesi -> Dosya (.json)  | Veriyi doğrudan dosyaya kaydeder             |
# | json.load()     | Dosya (.json) -> Python Objesi  | Dosyayı okuyup Python nesnesine çevirir      |
#-----------------------------------------------------------------------------------------------------

import json

# Örnek Veri Yapısı (Python Dict)
kullanici = {
    "ad": "Ali",
    "yas": 20,
    "yazilimci_mi": True,
    "notlar": None,
    "diller": ["Python", "C++"]
}

#-----------------------------------------------------------------------------------------------------
# C. UYGULAMA ÖRNEKLERİ (PRACTICAL EXAMPLES)                                                         |
#-----------------------------------------------------------------------------------------------------

# A. SERİLEŞTİRME (Serialization): Python -> JSON String
# indent=4: Okunabilirliği artırır. ensure_ascii=False: Türkçe karakterleri korur.
json_metni = json.dumps(kullanici, indent=4, ensure_ascii=False)
print(f"JSON Çıktısı:\n{json_metni}")

# B. DESERİLEŞTİRME (Deserialization): JSON String -> Python Dict
python_verisi = json.loads(json_metni)
print(f"\nKullanıcının Adı: {python_verisi['ad']}") # Dict gibi erişim sağlanır.

# C. DOSYA İŞLEMLERİ: Dosyaya Yazma ve Okuma
# Yazma (dump)
with open("kullanici_verisi.json", "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya, indent=4, ensure_ascii=False)

# Okuma (load)
with open("kullanici_verisi.json", "r", encoding="utf-8") as dosya:
    yuklenen_veri = json.load(dosya)
    print(f"Dosyadan okunan yaş: {yuklenen_veri['yas']}")

#------------------------------------------------------------------------------------------------------
# D. KULLANIM ALANLARI VE AVANTAJLARI                                                                 |
#------------------------------------------------------------------------------------------------------
# -> API İletişimi: Web siteleri arasındaki veri trafiğini yönetir.                                   |
# -> Konfigürasyon: Program ayarlarını (örneğin 'karanlık_mod': true) saklamak için idealdir.         |
# -> Hafiflik: XML'e göre çok daha az yer kaplar ve daha hızlı işlenir.                               |
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
# 6. shutil MODÜLÜ (YÜKSEK SEVİYE DOSYA İŞLEMLERİ)                                                    |
#------------------------------------------------------------------------------------------------------
# -> os modülünün "ağır iş makinesi" kardeşidir.                                                      |
# -> Sadece tek tek dosyalarla değil, bütün halindeki klasör yapılarıyla ilgilenir.                   |
# -> Kopyalama, taşıma ve kökten silme işlemleri için standarttır.                                    |
#------------------------------------------------------------------------------------------------------
# | shutil.copy(kaynak, hedef)     | Dosyayı kopyalar (Metadatalar hariç).                            |
# | shutil.copy2(kaynak, hedef)    | Dosyayı kopyalar (Oluşturulma tarihi gibi tüm verileri korur).   |
# | shutil.move(kaynak, hedef)     | Dosya veya klasörü taşır (Kes-Yapıştır mantığı).                 |
# | shutil.rmtree(yol)             | Bir klasörü içindeki her şeyle birlikte kalıcı olarak siler.     |
# | shutil.make_archive(ad, 'zip') | Belirtilen klasörü tek komutla .zip dosyası haline getirir.      |
#------------------------------------------------------------------------------------------------------

import shutil
import os

# "Proje" klasörünü her şeyiyle birlikte "Proje_Yedek" adıyla kopyalayalım
if os.path.exists("Proje"):
    shutil.copytree("Proje", "Proje_Yedek") 
    print("Tüm klasör başarıyla yedeklendi.")

# Bir dosyayı başka bir klasöre taşıyalım
# shutil.move("rapor.pdf", "Belgelerim/")


#------------------------------------------------------------------------------------------------------
# 7. csv MODÜLÜ (TABLOLU VERİ YÖNETİMİ)                                                               |
#------------------------------------------------------------------------------------------------------
# -> Excel dosyalarının en sade hali olan .csv (Comma Separated Values) dosyalarını işler.            |
# -> Veri biliminde dev kütüphanelere (Pandas gibi) geçmeden önceki temel veri okuma aracıdır.        |
#------------------------------------------------------------------------------------------------------
# | csv.reader(dosya)              | CSV dosyasındaki satırları bir liste olarak okur.                |
# | csv.writer(dosya)              | Verileri CSV formatında (virgülle ayrılmış) dosyaya yazar.       |
# | csv.DictReader(dosya)          | Her satırı bir sözlük (dict) olarak okur (Sütun adıyla erişim).  |
#------------------------------------------------------------------------------------------------------

import csv

#--------------------------------------------
# 1. csv.writer(dosya) -> Veri Yazma Örneği :
#--------------------------------------------
# Bir liste kümesini alıp virgülle ayrılmış bir tablo (CSV) dosyasına dönüştürür.
personel_listesi = [
    ['Ad', 'Departman', 'Maas'],    # Başlık satırı
    ['Ahmet', 'Yazilim', '45000'],
    ['Ayşe', 'Tasarim', '42000'],
    ['Mehmet', 'Pazarlama', '38000']
]

with open('sirket_verisi.csv', 'w', newline='', encoding='utf-8') as dosya:
    yazici = csv.writer(dosya)
    yazici.writerows(personel_listesi) # Tüm listeyi tek seferde yazar
    print("Veriler 'sirket_verisi.csv' dosyasına kaydedildi.")


#-----------------------------------------------------------
# 2. csv.reader(dosya) -> Veri Okuma Örneği (Liste Olarak) :
#-----------------------------------------------------------
# Dosyadaki her satırı bir Python listesi ['Veri1', 'Veri2'] olarak getirir.
with open('sirket_verisi.csv', 'r', encoding='utf-8') as dosya:
    okuyucu = csv.reader(dosya)
    print("\n--- csv.reader Çıktısı ---")
    for satir in okuyucu:
        # satir[0] Adı, satir[1] Departmanı temsil eder (İndeks ile erişim)
        print(f"Personel: {satir[0]} | Bölüm: {satir[1]}")


#----------------------------------------------------------------
# 3. csv.DictReader(dosya) -> Veri Okuma Örneği (Sözlük Olarak) :
#----------------------------------------------------------------
# En profesyonel yöntemdir. İlk satırı başlık kabul eder ve verilere başlık adıyla erişmenizi sağlar.
with open('sirket_verisi.csv', 'r', encoding='utf-8') as dosya:
    sozluk_okuyucu = csv.DictReader(dosya)
    print("\n--- csv.DictReader Çıktısı ---")
    for satir in sozluk_okuyucu:
        # İndeks (0,1,2) yerine direkt sütun adıyla (Ad, Maas) çağırıyoruz.
        print(f"İsim: {satir['Ad']} -> Maaş: {satir['Maas']} TL")


#------------------------------------------------------------------------------------------------------
# 8. re MODÜLÜ (Regular Expressions / Düzenli İfadeler)                                               |
#------------------------------------------------------------------------------------------------------
# -> Metinlerin içindeki kalıpları (pattern) bulan profesyonel bir arama motorudur.                   |
# -> "Sonu .com ile biten tüm kelimeleri bul" gibi karmaşık komutları anlar.                          |
#------------------------------------------------------------------------------------------------------
# | re.search(kalıp, metin)        | Metin içinde kalıbı arar, ilk bulduğunu döndürür.                |
# | re.findall(kalıp, metin)       | Kalıba uyan tüm sonuçları bir liste olarak döndürür.             |
# | re.sub(kalıp, yeni, metin)     | Belirli bir kalıba uyan yerleri yeni metinle değiştirir.         |
# | [Kalıp Örneği: r"\d+"]         | Metin içindeki tüm sayıları (digit) temsil eder.                 |
#-----------------------------------------------------------------------------------------------------
import re
"""
-> Bu modül biraz karışık olduğundan ve sibere kaçtığından bu derste örneği verilmeyecektir.
"""

#------------------------------------------------------------------------------------------------------
# 9. statistics MODÜLÜ (Temel İstatistik)                                                             |
#------------------------------------------------------------------------------------------------------
# -> Veri setleri üzerinde matematiksel özetler ve analizler yapar.                                   |
# -> karmaşık formüller yazmadan verinin "merkezini" ve "dağılımını" bulmanı sağlar.                  |
#------------------------------------------------------------------------------------------------------
# | statistics.mean(liste)         | Aritmetik ortalamayı hesaplar.                                   |
# | statistics.median(liste)       | Verileri küçükten büyüğe dizer ve tam ortadaki sayıyı bulur.     |
# | statistics.mode(liste)         | Veri setinde en çok tekrar eden (popüler) elemanı bulur.         |
# | statistics.stdev(liste)        | Standart sapmayı (Verilerin ne kadar yayıldığını) hesaplar.      |
#------------------------------------------------------------------------------------------------------

import statistics

# Örnek Veri Setimiz (Bir sınıftaki öğrencilerin sınav notları olsun)
notlar = [85, 90, 70, 85, 100, 60, 85, 40]

#--------------------------------------------------
# 1. statistics.mean(liste) -> Aritmetik Ortalama :
#--------------------------------------------------
# Tüm sayıları toplar ve sayı adedine böler. Sınıfın genel başarı düzeyini gösterir.
ortalama = statistics.mean(notlar)
print(f"Sınıf Ortalaması: {ortalama}") #Çıktı: 84.375


#--------------------------------------------------------
# 2. statistics.median(liste) -> Ortanca Değer (Medyan) :
#--------------------------------------------------------
# Verileri küçükten büyüğe dizer: [40, 60, 70, 85, 85, 85, 90, 100]
# Tam ortadaki değeri seçer. Uç değerlerden (çok düşük veya çok yüksek) etkilenmez.
ortanca = statistics.median(notlar)
print(f"Medyan (Tam ortadaki not): {ortanca}") #Çıktı: 85.0


#--------------------------------------------------------
# 3. statistics.mode(liste) -> En Çok Tekrar Eden (Mod) :
#--------------------------------------------------------
# Veri setinde en "popüler" olan, yani en sık rastlanan değeri bulur.
en_cok_tekrar = statistics.mode(notlar)
print(f"En çok alınan not (Mod): {en_cok_tekrar}") #Çıktı: 85


#-----------------------------------------------
# 4. statistics.stdev(liste) -> Standart Sapma :
#-----------------------------------------------
# Verilerin ortalamadan ne kadar uzaklaştığını söyler.
# Düşük sapma: Herkes birbirine yakın not almış.
# Yüksek sapma: Biriler çok yüksek, birileri çok düşük almış (uçurum var).
sapma = statistics.stdev(notlar)
print(f"Notların Dağılımı (Standart Sapma): {sapma:.2f}") #Çıktı: 18.52


#------------------------------------------------------------------------------------------------------
# 10. collections MODÜLÜ (Gelişmiş Veri Yapıları)                                                     |
#------------------------------------------------------------------------------------------------------
# -> Standart dict, list ve tuple yapılarının "modifiye edilmiş" güçlü versiyonlarıdır.               |
#------------------------------------------------------------------------------------------------------
# | collections.Counter(dizi)      | Elemanların kaçar kez tekrarlandığını sayan bir sözlük döner.    |
# | collections.namedtuple()       | Elemanlarına isimle erişilebilen (nokta notasyonu) tuple yaratır.|
# | collections.deque()            | İki uçtan da hızlı eleman ekleme/çıkarma yapabilen liste türüdür.|
# | collections.defaultdict()      | Anahtar yoksa hata vermek yerine varsayılan değer atayan sözlük. |
#------------------------------------------------------------------------------------------------------

from collections import Counter, namedtuple, deque, defaultdict

#------------------------------------
# 1. Counter(dizi) -> Eleman Sayacı :
#------------------------------------
# Bir liste veya metin içindeki her elemanın kaç kez geçtiğini saniyeler içinde sayar.
kelimeler = ["elma", "muz", "elma", "çilek", "muz", "elma"]
sayac = Counter(kelimeler)

print(f"Meyve Sayıları: {sayac}") 
# Çıktı: Counter({'elma': 3, 'muz': 2, 'çilek': 1})
print(f"En çok tekrar eden: {sayac.most_common(1)}") # En popüleri verir.


#-------------------------------------
# 2. namedtuple() -> İsimli Demetler :
#-------------------------------------
# Normalde tuple'lara indeks (0, 1) ile erişilir. namedtuple ile isimle erişebilirsin.
# "Ogrenci" tipinde; "ad" ve "no" alanları olan bir yapı kuralım:
Ogrenci = namedtuple("Ogrenci", ["ad", "no"])
ogr1 = Ogrenci(ad="Ali", no=123)

print(f"Öğrenci Adı: {ogr1.ad}, Numarası: {ogr1.no}") 
# İndeksle uğraşmak yerine (ogr1[0]) nokta notasyonu (ogr1.ad) kullanıyoruz.


#-------------------------------------
# 3. deque() -> İki Uçlu Hızlı Liste :
#-------------------------------------
# Standart listelerde başa eleman eklemek yavaştır. deque ile her iki uçta da ışık hızında işlem yapılır.
kuyruk = deque(["Mehmet", "Ayşe", "Fatma"])

kuyruk.append("Veli")      # En sağa (sona) ekler
kuyruk.appendleft("Ali")  # En sola (başa) ekler

print(f"Sıralama: {kuyruk}") # Çıktı: deque(['Ali', 'Mehmet', 'Ayşe', 'Fatma', 'Veli'])
kuyruk.popleft()            # En baştakini (Ali) çıkarır.


#------------------------------------------------
# 4. defaultdict() -> Varsayılan Değerli Sözlük :
#------------------------------------------------
# Normal sözlükte olmayan bir anahtarı çağırsan hata alırsın. 
# defaultdict ise hata yerine senin belirlediğin başlangıç değerini (örn: 0) otomatik atar.
sayilar = defaultdict(int) # int başlangıç değeri 0'dır.

sayilar["puan"] += 10 # "puan" anahtarı yoktu ama hata vermedi, 0 kabul edip 10 ekledi.
print(f"Puan Durumu: {sayilar['puan']}") # Çıktı: 10


# ===========================================================================
# == BAB 11: MODÜLLER-1 PROJELERİ (CHAPTER 7: PYTHON MODULES-1 PROJECTS) : ==
# ===========================================================================

# ------------------------------------------------------------
# ÖRNEK 1: os modülü ile klasör oluşturma ve dosya işlemleri :
# ------------------------------------------------------------
import os

# 1. "Denemeler" klasörünü oluştur (varsa hata vermemesi için exist_ok=True)
os.makedirs("Denemeler", exist_ok=True)

# 2. Klasörün içine geçelim
os.chdir("Denemeler")

# 3. "metin.txt" dosyasını oluşturup yazalım
with open("metin.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba Dünya")

# 4. Bulunduğumuz dizindeki dosyaları listeleyelim
dosyalar = os.listdir()
print("Denemeler klasöründeki dosyalar:", dosyalar)


# --------------------------------------------------
# ÖRNEK 2: random modülü ile rastgele şifre üretme :
# --------------------------------------------------
import random
import string

def sifre_uret(uzunluk=8):
    # Kullanılacak karakter havuzu
    karakterler = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

print("Üretilen şifre:", sifre_uret())
print("10 karakterli şifre:", sifre_uret(10))


# ----------------------------------------------
# ÖRNEK 3: math modülü ile hipotenüs hesaplama :
# ----------------------------------------------
import math

a = float(input("Birinci dik kenar uzunluğu: "))
b = float(input("İkinci dik kenar uzunluğu: "))

hipotenus = math.hypot(a, b)
print(f"Hipotenüs: {hipotenus:.2f}")


# ------------------------------------------------------------
# ÖRNEK 4: time modülü ile faktöriyel hesaplama süresi ölçme :
# ------------------------------------------------------------
import time
import math

def faktoriyel_hesapla(n):
    baslangic = time.time()
    sonuc = math.factorial(n)
    bitis = time.time()
    gecen_sure = bitis - baslangic
    print(f"{n}! = {sonuc}")
    print(f"Hesaplama süresi: {gecen_sure:.6f} saniye")

sayi = int(input("Faktöriyeli hesaplanacak sayı: "))
faktoriyel_hesapla(sayi)


# --------------------------------------------
# ÖRNEK 5: datetime modülü ile yaş hesaplama :
# --------------------------------------------
from datetime import date

yil = int(input("Doğum yılınız: "))
ay = int(input("Doğum ayınız: "))
gun = int(input("Doğum gününüz: "))

dogum_tarihi = date(yil, ay, gun)
bugun = date.today()

# Yaş hesapla: yıl farkı, ancak doğum günü henüz gelmemişse bir çıkar
yas = bugun.year - dogum_tarihi.year
if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
    yas -= 1

print(f"Bugün itibarıyla yaşınız: {yas}")


# --------------------------------------------------------------------
# ÖRNEK 6: json modülü ile öğrenci verilerini dosyaya yazma ve okuma :
# --------------------------------------------------------------------
import json

# Sözlük oluştur
ogrenciler = {
    101: "Ali Yılmaz",
    102: "Ayşe Demir",
    103: "Mehmet Kaya"
}

# Dosyaya yaz (dump)
with open("ogrenciler.json", "w", encoding="utf-8") as f:
    json.dump(ogrenciler, f, indent=4, ensure_ascii=False)

# Dosyadan oku (load)
with open("ogrenciler.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print("Dosyadan okunan veri:")
    for no, ad in data.items():
        print(f"{no}: {ad}")


# ---------------------------------------------
# ÖRNEK 7: shutil modülü ile klasör yedekleme :
# ---------------------------------------------
import shutil
import os

kaynak = "Proje"
hedef = "Proje_Yedek"

# Kaynak klasör var mı kontrol et
if not os.path.exists(kaynak):
    print("Kaynak klasör bulunamadı!")
else:
    # Hedef varsa silip yeniden kopyala
    if os.path.exists(hedef):
        shutil.rmtree(hedef)   # Önce sil
        print("Eski yedek silindi.")
    shutil.copytree(kaynak, hedef)
    print(f"{kaynak} klasörü {hedef} olarak yedeklendi.")


# ---------------------------------------------------------------------
# ÖRNEK 8: csv modülü ile maaş verilerini okuma ve ortalama hesaplama :
# ---------------------------------------------------------------------
import csv

toplam = 0
sayac = 0

with open("maaslar.csv", "r", encoding="utf-8") as f:
    okuyucu = csv.DictReader(f)   # Başlıkları otomatik alır
    for satir in okuyucu:
        maas = int(satir["Maaş"])
        toplam += maas
        sayac += 1

if sayac > 0:
    ortalama = toplam / sayac
    print(f"Toplam {sayac} çalışan. Ortalama maaş: {ortalama:.2f}")
else:
    print("Veri bulunamadı.")


# --------------------------------------------
# ÖRNEK 9: statistics modülü ile not analizi :
# --------------------------------------------
import statistics

notlar = [65, 80, 70, 85, 90, 70, 75, 80, 95, 70]

ortalama = statistics.mean(notlar)
medyan = statistics.median(notlar)
mod = statistics.mode(notlar)
st_sapma = statistics.stdev(notlar)

print(f"Notlar: {notlar}")
print(f"Ortalama: {ortalama:.2f}")
print(f"Medyan: {medyan}")
print(f"Mod (en sık): {mod}")
print(f"Standart sapma: {st_sapma:.2f}")


# ------------------------------------------------
# ÖRNEK 10: collections.Counter ile kelime sayma :
# ------------------------------------------------
from collections import Counter
import string

metin = "Python çok güzel bir dil. Python ile veri analizi yapmak çok keyifli. Güzel kod yazmak güzel."
# Noktalama işaretlerini temizle ve küçük harfe çevir
metin = metin.lower()
# Noktalama işaretlerini boşlukla değiştir
for karakter in string.punctuation:
    metin = metin.replace(karakter, " ")
# Kelimelere ayır
kelimeler = metin.split()
# Sayacı oluştur
sayac = Counter(kelimeler)
# En çok geçen 3 kelime
en_cok = sayac.most_common(3)

print("En sık geçen 3 kelime:")
for kelime, adet in en_cok:
    print(f"{kelime}: {adet}")


#---------------------------------------------------------------------------
# ÖRNEK 11: Algoritmik Strateji: Sayı Tahmin Oyunu (Random & Loop Control) :
#---------------------------------------------------------------------------
import random

gizli_sayi = random.randint(1, 100) 
tahmin_hakki = 7

print("--- 1 ile 100 arasında bir sayı tuttum. 7 hakkın var! ---")

while tahmin_hakki > 0:
    tahmin = int(input(f"Tahminini gir (Kalan Hak: {tahmin_hakki}): "))
    
    if tahmin == gizli_sayi:
        print(f"TEBRİKLER! {gizli_sayi} sayısını bildin. Hikmet basamağına ulaştın.")
        break
    elif tahmin < gizli_sayi:
        print("Daha YÜKSEK bir sayı söyle.")
    else:
        print("Daha DÜŞÜK bir sayı söyle.")
    
    tahmin_hakki -= 1

if tahmin_hakki == 0:
    print(f"Hakkın bitti! Maalesef kaybettin. Tuttuğum sayı: {gizli_sayi}")


# =============================================================================================================================================
"""
 "Elhamdülillah, 11. Bab ile kodun birliğini bozmadan, onu 'Cüzlere' (Modüllere) taksim ederek her bir hakikati kendi makamına yerleştirdik."
 " Bu, zihni dağınıklıktan, kodu ise 'faydasız kalabalıktan' kurtarma amelidir." 
 " 11 tane örneğimizle de pekiştirdik. Lakin bu modüller kısmı ayrıntılı bir bölüm olmasından dolayı BAB 11 zorlayıcı olabilir."
"""
# =============================================================================================================================================
#  BAB 11: MODÜLLER-1 PROJE LİSTESİ :                                                                                                         |
# =============================================================================================================================================
#  ÖRNEK 1 : os Modülü ile Klasör Oluşturma ve Dosya İşlemleri                                                                                |
#  ÖRNEK 2 : random Modülü ile Rastgele Şifre Üretme                                                                                          |
#  ÖRNEK 3 : math Modülü ile Hipotenüs Hesaplama                                                                                              |
#  ÖRNEK 4 : time Modülü ile Faktöriyel Hesaplama Süresi Ölçme                                                                                |
#  ÖRNEK 5 : datetime Modülü ile Yaş Hesaplama                                                                                                |
#  ÖRNEK 6 : json Modülü ile Öğrenci Verilerini Dosyaya Yazma ve Okuma                                                                        |
#  ÖRNEK 7 : shutil Modülü ile Klasör Yedekleme                                                                                               |
#  ÖRNEK 8 : csv Modülü ile Maaş Verilerini Okuma ve Ortalama Hesaplama                                                                       |
#  ÖRNEK 9 : statistics Modülü ile Not Analizi                                                                                                |
#  ÖRNEK 10: collections.Counter ile Kelime Sayma                                                                                             |
#  ÖRNEK 11: Algoritmik Strateji: Sayı Tahmin Oyunu (Random & Loop Control)                                                                   |
# =============================================================================================================================================



