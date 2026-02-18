# ============================================================================================================
# == BAB 3: PYTHON PROGRAMLAMA DİLİNE GİRİŞ VE ORTAM KURULUMU (INTRODUCTION TO PYTHON LANGUAGE AND SETUP) : ==
# ============================================================================================================

#--------------------------------------
# 1. PYTHON TARİHÇESİ (BRIEF HISTORY) :
#--------------------------------------
"""
-> 1989: Hollanda'daki CWI'da çalışan ve ABC programlama dilinin yerini alacak ve eksikleri kapatmayı düşünen Guido van Rossum adındaki programcı çalışmalara başladı.
-> İsmini sevdiği "Monty Python" isimli komedi filminden almıştır.
-> 1991: Python'un ilk sürümü 0.9.0 yayınlandı.
-> 1994: Python'un 1.0 sürümü yayınlandı.
-> 2000: Python 2.0 sürümü yayınlandı. Unicode desteği, Çöp toplama (Garbage Collection), liste üreticileri (list comprehensions) özellikleri geldi.
-> 2008: Python 3.0 sürümü yayınlandı. Python 2'de 'print' bir ifade iken Python 3'te bir fonksiyondur.
   - Python 2 -> print "Merhaba"
   - Python 3 -> print("Merhaba")
-> Kısacası: Guido van Rossum sadeliği ve okunabilirliği arttırmak için Python dilini geliştirdi.
-> Şu an Python'un en son sürümü 3.13 lakin 3.14 sürümü hakkında çalışmalar devam ediyor (Yıl 2026)
"""

"""
-> Python 2'de kullanıcıdan veri almak için iki farklı fonksiyon vardı:
   - raw_input(): Kullanıcının girdiği her şeyi "string" (metin) olarak alır.
   - input(): Kullanıcının girdiği ifadeyi Python kodu olarak değerlendirir (örneğin 5+3 girilirse 8 döndürür). Bu davranış güvenlik riskleri oluşturabildiği için Python 3'te kaldırıldı.
-> Python 3'te ise sadece input() fonksiyonu vardır ve Python 2'deki raw_input() gibi çalışır: Kullanıcının girdiği her şeyi string olarak döndürür.
-> Yani Python 3'te:
   isim = input("Adınız: ")   # Kullanıcı "Ali" yazarsa isim değişkeni "Ali" olur (string).

# NOT: Python 2'den Python 3'e geçerken input() fonksiyonu değişti.
# Python 2'de input() tehlikeliydi (girilen kodu çalıştırırdı), raw_input() ise güvenliydi.
# Python 3'te raw_input() kaldırıldı, input() güvenli hale getirildi ve her zaman string döndürür.
"""

#---------------------------------------
# PYTHON'UN TEMEL FELSEFELERİ (PEP 20) :
#---------------------------------------
"""
1. Güzel, çirkinden iyidir. (Beautiful is better than ugly.)
   -> Kodun estetik ve düzenli olması, sadece çalışan ama karmaşık olan koda tercih edilir.

2. Açık, kapalıdan iyidir. (Explicit is better than implicit.)
   -> Bir kodun ne yaptığı gizli saklı olmamalı, her şey "kabak gibi" ortada olmalıdır.

3. Basit, karmaşıktan iyidir. (Simple is better than complex.)
   -> Bir işi en basit yolla çözmek varken, gereksiz ve karmaşık mühendislik oyunlarına girilmemelidir.

4. Okunabilirlik önemlidir. (Readability counts.)
   -> Kod yazmaktan çok, o kodun başkaları (veya gelecekteki siz) tarafından okunacağı unutulmamalıdır.

5. Hatalar asla sessizce geçiştirilmemelidir. (Errors should never pass silently.)
   -> Bir hata oluştuğunda program "çaktırmadan" devam etmemeli, hatayı net bir şekilde bildirmelidir.

6. Bir işi yapmanın bir -ve tercihen sadece bir- belirgin yolu olmalıdır. 
   (There should be one-- and preferably only one --obvious way to do it.)
   -> Python'da kafa karışıklığını önlemek için her zaman standart ve kabul görmüş yollar tercih edilir.
"""

#------------------------------------------
# YAZIM STANDARTLARI (CLEAN CODE & PEP 8) :
#------------------------------------------
"""
-> Python'da fonksiyon isimleri ile parantez arasına boşluk KONULMAZ.
-> Boşluk bırakmak kodun çalışmasını engellemez (Syntax Error vermez) ancak profesyonel standartlara aykırıdır.
"""

# Senior Developer Gözüyle Karşılaştırma:

# DOĞRU (Standart):
for i in range(1, 101):
    print(i)

# YANLIŞ (Amatör görünüm):
for i in range (1, 101): 
    print (i)

"""
NEDEN BİTİŞİK?
--------------
1. Semantik Bütünlük: Fonksiyon ismi ve parantez bir bütündür; parantez o fonksiyonun 'çalıştırılacağını' temsil eder.
2. Tool Uyumluluğu: Linterlar (Hata denetleyiciler) ve otomatik formatlayıcılar (Black, Prettier) bu boşluğu otomatik olarak siler.
3. Karmaşıklığı Önleme: İç içe fonksiyonlarda boşluk bırakmak, kodun görsel hiyerarşisini bozar.
"""

# ----------------------------------------------------------------------------------------------------------
#  Kullanım Alanı      : Boşluk Durumu           : Örnek                                                   |
#  --------------------:-------------------------:---------------------------------------------------------|
#  Fonksiyon Çağrısı   : Bitişik (Boşluksuz)     : print("Merhaba"), range(10)                             |
#  Operatörler         : Boşluklu                : x = 5 + 3, y == 10                                      |
#  Virgül Sonrası      : 1 Boşluk                : [1, 2, 3], func(a, b)                                   |
#  Anahtar Kelimeler   : 1 Boşluk                : if x:, for i in:, while True:                           |
# ----------------------------------------------------------------------------------------------------------

#---------------------------------
# 1. PYTHON.ORG VE SÜRÜM SEÇİMİ :
#---------------------------------
"""
-> Web Sitesi: python.org/downloads.
-> Kategoriler: Stable Releases (Kararlı) ve Pre-releases (Ön Sürüm).

Pre-releases Aşamaları:
-----------------------
- Alpha: En erken sürüm, hatalar boldur, geliştiriciler içindir.
- Beta: Daha kararlı, genel kullanıcılar test edebilir.
- RC (Release Candidate): Kararlı sürüme çok yakın, son testler.
- Stable: Tam sürüm, genel kullanıma hazırdır.
"""

#-----------------------------------
# 2. YÜKLEYİCİ (INSTALLER) TİPLERİ :
#-----------------------------------
"""
A) Windows Installer: Bilgisayarınıza Python'u kurmak için en yaygın seçenektir.
   - 64-bit: Modern bilgisayarların çoğu için uygundur.
   - 32-bit: Çok eski bilgisayarlar için gerekebilir.
   - ARM64: Surface Pro X gibi ARM işlemcili cihazlar içindir.

B) Windows Embeddable Package: Bir projenin veya uygulamanın içine gömmek için tasarlanmış özel pakettir.
   - Avantajları: Çevre kirliliğini önler, çakışmaları azaltır ve taşınabilirdir.
   - Kişisel kullanım için "Windows Installer" tercih edilmelidir.
"""

#-----------------------------
# 3. KRİTİK KURULUM ADIMLARI :
#-----------------------------
"""
Ekran Seçenekleri:
------------------
1. Install Now: En kolay seçenektir, her şeyi otomatik kurar.
2. Customize Installation: Kurulacak bileşenleri kendiniz seçersiniz.

EN ÖNEMLİ KUTUCUKLAR:
---------------------
-> Use admin privileges when installing py.exe: Yönetici ayrıcalıkları sağlar.
-> Add python.exe to PATH: Bu kutucuğu işaretlemek ŞİDDETLE tavsiye edilir. 
   Terminalden (cmd/powershell) 'python' komutuyla kod çalıştırmanızı sağlar.
"""


#----------------------------------------------
# 4. PROFESYONEL GELİŞTİRME: PYCHARM KURULUMU :
#----------------------------------------------
"""
-> Web: jetbrains.com/pycharm.
-> Pycharm: Profesyonel anlamda Python uygulamaları geliştirmek için ideal bir IDE'dir.

Kurulum Seçenekleri ve Anlamları:
---------------------------------
1. Create Desktop Shortcut: Masaüstünde hızlı erişim sağlar.
2. Update PATH Variable: Terminalden 'pycharm' yazarak programı başlatmanızı sağlar (Yeniden başlatma gerektirir).
3. Update Context Menu: Klasöre sağ tıklayıp "Proje Olarak Aç" seçeneğini ekler.
4. Create Associations (.py): .py dosyalarının otomatik Pycharm ile açılmasını sağlar.

-> Kritik Uyarı: "Add python.exe to PATH" kutucuğunun önemini vurgulaman hayat kurtarır.
-> PATH, işletim sisteminin hangi komutun hangi klasördeki dosyayı çalıştıracağını bildiği bir adres defteridir.
"""


#------------------------
# 5. KURULUMU TAMAMLAMA :
#------------------------
"""
-> JetBrains Install seçeneğine tıklanır.
-> Kurulum bittikten sonra "Finish" (Bitir) butonuna tıklanarak süreç tamamlanır.
"""

#------------------------------------
# GELİŞTİRME ORTAMLARI (IDLE & IDE) :
#------------------------------------
"""
----------------------------------------------------------
# IDLE (Integrated Development and Learning Environment) :
----------------------------------------------------------
-> Entegre Geliştirme ve Düzenleme Ortamı anlamına gelir.
-> Python ile birlikte gelen basit, minimal, temel bir geliştirme ortamıdır.
-> Tek dosya şeklinde çalışır. Elinizdeki tek bir yaprak sayfaya benzetebilirsiniz.
-> Python'ın resmi web sitesinden indirilen Python dağıtımı ile birlikte gelir.
-> Temel bir metin düzenleyici, Python kabuğu (interaktif ortam), hata ayıklayıcı içerir.
-> Özellikle yeni başlayanlar için basit ve anlaşılırdır.
-> Çoklu dosya düzenleme için uygun değildir, genelde tek dosya üzerinde çalışır.
-> Sözdizimi vurgulama, otomatik tamamlama gibi özellikleri sınırlıdır.


--------------------------------------------
# IDE (Integrated Development Environment) :
--------------------------------------------
-> Entegre Geliştirme Ortamı anlamına gelir.
-> Kod yazmak, düzenlemek, çalıştırmak, hata ayıklamak için kullanılan bir yazılım ortamıdır.
-> Kodlamayı kolaylaştıran araçları tek bir çatı altında toplar.
-> Profesyonel yazılım geliştirme için kullanılır.
-> Kod tamamlama, akıllı imleç, sürüm kontrol entegrasyonu, veritabanı araçları gibi birçok özellik sunar.
-> Birden fazla programlama dili ve büyük projeleri destekler.
-> Örnekler: PyCharm, Visual Studio Code, Eclipse, IntelliJ IDEA.
"""

"""
-> IDE (Integrated Development Environment): Kod yazmak, düzenlemek, çalıştırmak ve 
   hata ayıklamak için kullanılan profesyonel bir yazılım ortamıdır.
-> Kodlamayı kolaylaştıran araçları (hata ayıklayıcı, terminal, dosya yöneticisi) 
   tek bir çatı altında toplar.
"""

#------------------------------------------
# 1. PYCHARM: PROFESYONEL VE TAM KAPSAMLI :
#------------------------------------------
"""
-> Geliştirici: JetBrains şirketi tarafından geliştirilmiştir.
-> Sürümler: Community Edition (Ücretsiz) ve Professional Edition (Ücretli) sürümleri bulunur.
-> Özellikler: 
   - Akıllı kod tamamlama, gelişmiş hata ayıklama (debugging) ve entegre test araçları sunar.
   - Web geliştirme, veri bilimi ve makine öğrenimi için özelleştirilmiş araçlara sahiptir.
-> Not: Profesyonel anlamda Python uygulamaları geliştirmek için idealdir.
"""

#--------------------------------------------------
# 2. VISUAL STUDIO CODE (VS CODE): HAFİF VE GÜÇLÜ :
#--------------------------------------------------
"""
-> Geliştirici: Microsoft tarafından geliştirilen, açık kaynaklı ve ücretsiz bir editördür.
-> Özellikler:
   - "Python" uzantısı (extension) yüklendiğinde tam teşekküllü bir IDE'ye dönüşür.
   - Entegre terminal, Git sürüm kontrolü ve debugging desteği sağlar.
   - Çok sayıda eklenti (market) ile her türlü ihtiyaca göre genişletilebilir.
"""

#----------------------------------------------
# 3. JUPYTER NOTEBOOK / LAB: VERİ BİLİMİ ÜSTÜ :
#----------------------------------------------
"""
-> Kullanım Alanı: Özellikle veri bilimi, araştırma ve akademik çalışmalar için popülerdir.
-> Yapısı: Hücre tabanlıdır (Cell-based). Kod, görselleştirme (grafik) ve metin (Markdown) bir arada bulunur.
-> Avantajı: Canlı kod denemeleri, matematiksel denklemler ve sunumlar için ideal bir ortam sunar.
"""

#----------------------------------------
# 4. SPYDER: BİLİMSEL GELİŞTİRME ODAĞI :
#----------------------------------------
"""
-> Hedef: Bilimsel Python geliştirme için tasarlanmıştır.
-> Entegrasyon: NumPy, SciPy ve Matplotlib gibi kütüphanelerle yerleşik olarak çalışır.
-> Araçlar: Değişken gezgini (Variable Explorer) ve kod profilleri ile MATLAB kullanıcılarına tanıdık bir deneyim sunar.
"""

#-------------------------------
# 5. IDLE: VARSAYILAN VE BASİT :
#-------------------------------
"""
-> Tanım: Python ile birlikte gelen varsayılan ve en temel geliştirme ortamıdır.
-> Yapısı: Basit ve hafif bir editördür; tek bir yaprak sayfaya benzer.
-> Hedef Kitle: Yeni başlayanlar için uygundur; sözdizimi vurgulama ve temel debugging içerir.
"""

#---------------------------------
# 6. DİĞER POPÜLER ALTERNATİFLER :
#---------------------------------
"""
-> Atom: GitHub tarafından geliştirilen ancak artık bakım modunda olan bir editör.
-> Sublime Text: Çok hızlı ve hafif olmasıyla bilinir (Ücretli lisans seçeneği vardır).
-> Eclipse + PyDev: Java dünyasından gelenler için güçlü bir eklenti tabanlı çözüm.
-> Vim / Emacs: Terminal tabanlı çalışan, uzman ve ileri düzey kullanıcılar için tasarlanmış sistemler.
"""

#----------------------------------------------------------------
# 2. KÜTÜPHANE (LIBRARY) KAVRAMI VE SIK KULLANILAN KÜTÜPHANELER :
#----------------------------------------------------------------
"""
-> Kütüphane Nedir?
   - Belirli işlevleri yerine getirmek için önceden yazılmış kod koleksiyonudur.
   - Geliştiricilerin "tekerleği yeniden icat etmesini" önler ve zaman kazandırır.
   - Python'da kütüphaneler genellikle `import` anahtar kelimesiyle projeye dahil edilir.

------------------------------------------------------   
 En Çok Kullanılan Python Kütüphaneleri (Özet Liste) :
------------------------------------------------------
A) Veri Analizi ve Bilimsel Hesaplama:
   import numpy as np    # Sayısal işlemler ve matrisler
   import pandas as pd   # Veri manipülasyonu ve analizi
   import scipy          # Bilimsel hesaplamalar

B) Makine Öğrenimi ve Yapay Zeka (AI & ML):
   import tensorflow as tf   # Derin öğrenme framework'ü
   import torch              # Facebook'un (Meta) derin öğrenme kütüphanesi
   import scikit-learn       # Geleneksel makine öğrenimi algoritmaları

C) Veri Görselleştirme:
   import matplotlib.pyplot as plt   # 2D grafik çizimleri
   import seaborn as sns             # İstatistiksel görselleştirme

D) Web Geliştirme:
   import django   # Yüksek seviye (High-level) web framework'ü
   import flask    # Mikro (Lightweight) web framework'ü

E) Diğer Alanlar:
   - Web Scraping: BeautifulSoup, Selenium, Scrapy
   - Sistem & Otomasyon: os, sys, requests
   - GUI (Arayüz): Tkinter, PyQt5, Kivy 
"""


#------------------------------------------------
# 3. PYTHON'I DİĞER DİLLERDEN AYIRAN ÖZELLİKLER :
#------------------------------------------------
"""
1. Sadelik ve Okunabilirlik: İngilizceye yakın sözdizimi ve girintileme (indentation) yapısı ile 
   okunabilirliği en yüksek dildir.
   
2. Yorumlanan (Interpreted) Dil: Kod derleme gerektirmez, satır satır çalıştırılır. 
   Ancak arkaplanda önce ByteCode'a derlenip sonra yorumlanır.

3. Dinamik Tipli (Dynamically Typed): Değişken türünü (int, str vb.) belirtmeye gerek yoktur .
   Python türü çalışma anında otomatik belirler.

4. Çok Paradigmalı: Nesne yönelimli, fonksiyonel ve yapısal programlamayı aynı anda destekler.

5. "Piller Dahil" (Batteries Included): Standart kütüphanesinde 200'den fazla modül 
   kurulu olarak gelir; dosya işlemeden ağ programlamaya kadar her şey hazırdır.

6. Bellek Yönetimi: "Garbage Collection" (Çöp Toplayıcı) sayesinde kullanılmayan bellek 
   otomatik olarak temizlenir, geliştirici bellek yönetimiyle uğraşmaz.

7. Hızlı Öğrenme Eğrisi: Yazılım dünyasına giriş yapanlar için en ideal "öğrenci dostu" dildir.

NOT: 
-> Profesyonel İpucu: Python dinamik tiplidir ama aynı zamanda "Strongly Typed" (Güçlü Tipli) bir dildir.
Örnek: JavaScript'te "5" + 5 işlemi 55 sonucunu verirken, Python'da bu bir TypeError döndürür. Bu, Python'un güvenli bir liman olmasını sağlar.
"""

#-----------------------------------------
# 4. PYTHON KULLANIM YERLERİ (USE CASES) :
#-----------------------------------------
"""
-> Python 2026 yılı itibarıyla neredeyse her sektörün kalbinde yer almaktadır:

1. Veri Bilimi ve Analitik: Büyük veri işleme ve istatistiksel modelleme.
2. Yapay Zeka (AI): Doğal dil işleme (NLP), bilgisayarlı görü ve derin öğrenme.
3. Web Geliştirme: Güçlü ve güvenli backend (sunucu tarafı) sistemleri.
4. Otomasyon ve Scripting: Tekrarlayan görevlerin ve sistem yönetiminin otomatikleştirilmesi.
5. Siber Güvenlik: Ağ araçları, sızma testi araçları ve soket programlama.
6. Gömülü Sistemler ve IoT: Raspberry Pi ve MicroPython ile cihaz yönetimi.
7. Eğitim: Algoritma ve temel bilgisayar bilimleri öğretimi.
"""


#------------------------------------------
# 5. İLK KOD: MERHABA DÜNYA (HELLO WORLD) :
#------------------------------------------
"""
-> Python 3 ile birlikte gelen parantez zorunluluğunu unutmayalım:

print("Merhaba Dünya")

-> Neden print()?: Ekrana veri yazdırmak için kullanılan temel fonksiyondur.
-> Python 2 (Eski): print "Merhaba"
-> Python 3 (Güncel): print("Merhaba")
"""
print("Selamünaleyküm Dünya")

# ==========================================================================================================================================
"""
 Elhamdülillah, 3. Bab ile Python dünyasına adım attık. 
 Kodlarımızı yazacağımız ortamı (zemin) hazırladık; niyetimiz, bu yeni dille öğrendiğimiz her bilgiyi  doğru birer eyleme dönüştürmektir.
 Ayrıyeten "Selamünaleyküm Dünya" diyerek de PYTHON dünyasına giriş yapmış bulunmaktayız.
"""
# ==========================================================================================================================================


