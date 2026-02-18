
# ==================================================
# == BAB 12: MODÜLLER-2 (CHAPTER 12: MODULES-2) : ==
# ==================================================

#-----------------------------------------------------------------------------------------------------
# 3. ÜÇÜNCÜ TARAF (HARİCİ) KÜTÜPHANELER                                                              |
#-----------------------------------------------------------------------------------------------------
# -> Python ile yüklü gelmezler; "pip install kütüphane_adı" komutuyla dışarıdan yüklenirler.        |
# -> Belirli alanlarda (Yapay Zeka, Web, Veri Analizi) uzmanlaşmış, devasa araç setleridir.          |
# -> Dünyanın her yerindeki yazılımcıların ortak katkısıyla büyüyen bir ekosistemdir.                |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 1. VERİ BİLİMİ, ANALİZ VE GÖRSELLEŞTİRME                                                           |
#-----------------------------------------------------------------------------------------------------
# Sayısal verileri işlemek, tablolar oluşturmak ve grafikler çizmek için kullanılır.                 |
#-----------------------------------------------------------------------------------------------------
# | NumPy        | Yüksek performanslı dizi (array) işlemleri ve matematiksel hesaplamalar yapar.    |
# | Pandas       | Excel/CSV verilerini tablo formatında işler ve analiz eder (DataFrame yapısı).    |
# | Matplotlib   | Verileri çizgi, sütun ve pasta grafiklerine dönüştüren temel görselleştiricidir.  |
# | Seaborn      | Matplotlib tabanlı, daha şık ve gelişmiş istatistiksel grafikler sunar.           |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 2. YAPAY ZEKA VE MAKİNE ÖĞRENMESİ (AI & ML)                                                        |
#-----------------------------------------------------------------------------------------------------
# Bilgisayarlara veriden öğrenme ve tahmin yapma yeteneği kazandırmak için kullanılır.               |
#-----------------------------------------------------------------------------------------------------
# | Scikit-Learn | Temel makine öğrenmesi algoritmaları (Tahmin, Sınıflandırma) için standarttır.    |
# | TensorFlow   | Google imzalı, derin öğrenme ve karmaşık yapay sinir ağları kurma kütüphanesidir. |
# | PyTorch      | Meta (Facebook) imzalı, esnek ve akademik araştırmalarda çok popüler AI aracıdır. |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 3. WEB GELİŞTİRME VE API YÖNETİMİ                                                                  |
#-----------------------------------------------------------------------------------------------------
# İnternet sitelerinin arka planını (Backend) kurmak ve veri alışverişi sağlamak içindir.            |
#-----------------------------------------------------------------------------------------------------
# | Django       | Güvenlik ve veritabanı dahil her şeyi hazır sunan devasa bir web iskeletidir.     |
# | Flask        | Küçük ve esnek projeler için kullanılan hafif, mikro bir web çerçevesidir.        |
# | FastAPI      | Modern, tip korumalı ve Python'un en hızlı API geliştirme kütüphanesidir.         |
# | Requests     | Bir web sitesine kolayca bağlanmak ve oradan veri çekmek (HTTP) için kullanılır.  |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 4. WEB KAZIMA VE OTOMASYON (BOT YAZIMI)                                                            |
#-----------------------------------------------------------------------------------------------------
# İnternetteki bilgileri otomatik toplamak veya tarayıcıyı kontrol etmek içindir.                    |
#-----------------------------------------------------------------------------------------------------
# | BeautifulSoup| Web sitelerinin HTML kodlarını parçalayıp içinden istenen veriyi çekip alır.      |
# | Selenium     | Tarayıcıyı canlı bir robot gibi kullanır (Buton tıklama, form doldurma vb.).      |
# | Scrapy       | Çok büyük çaplı ve hızlı veri kazıma operasyonları için profesyonel bir yapıdır.  |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 5. MASAÜSTÜ ARAYÜZ, OYUN VE RESİM İŞLEME                                                           |
#-----------------------------------------------------------------------------------------------------
# Kullanıcının etkileşime girdiği görsel pencereler ve multimedya içerikler üretir.                  |
#-----------------------------------------------------------------------------------------------------
# | PyQt5        | Windows/Mac için profesyonel pencereli masaüstü uygulamaları tasarlar.            |
# | Pygame       | Python ile 2D oyunlar geliştirmek ve fizik simülasyonları yapmak içindir.         |
# | Kivy         | Hem masaüstü hem de mobil (Android/iOS) cihazlara uygulama geliştirmeyi sağlar.   |
# | Pillow (PIL) | Fotoğrafları boyutlandırma, filtreleme ve format değiştirme işlemlerini yapar.    |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 6. VERİTABANI VE TEST ARAÇLARI                                                                     |
#-----------------------------------------------------------------------------------------------------
# Veriyi güvenli saklamak ve kodun doğruluğunu denetlemek için kullanılır.                           |
#-----------------------------------------------------------------------------------------------------
# | SQLAlchemy   | Python kodlarını doğrudan SQL sorgularına dönüştüren veritabanı köprüsüdür.       |
# | Pytest       | Kodun içindeki hataları (bug) bulmak için kullanılan gelişmiş test kütüphanesidir.|
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 7. SİBER GÜVENLİK VE AĞ YÖNETİMİ (SECURITY & NETWORKING)                                           |
#-----------------------------------------------------------------------------------------------------
# Sistem güvenliğini test etmek ve ağ trafiğini yönetmek için kullanılır.                            |
#-----------------------------------------------------------------------------------------------------
# | Scapy        | Ağ paketlerini yakalar, analiz eder ve manipüle eder (Hacker'ların favorisidir).  |
# | Paramiko     | SSH bağlantıları üzerinden uzak sunuculara güvenli şekilde hükmetmenizi sağlar.   |
# | Cryptography | Verileri şifrelemek ve dijital imzalar oluşturmak için standart kütüphanedir.     |
# | Nmap (python)| Ağ taraması yaparak açık portları ve cihazları tespit etmeye yarar.               |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 8. BULUT SİSTEMLERİ VE DEVOPS (CLOUD & AUTOMATION)                                                 |
#-----------------------------------------------------------------------------------------------------
# Sunucuları yönetmek ve projeleri canlıya taşımak için kullanılır.                                  |
#-----------------------------------------------------------------------------------------------------
# | Boto3        | Amazon Web Services (AWS) servislerini Python ile yönetmenizi sağlar.             |
# | Docker (py)  | Docker konteynerlarını Python koduyla oluşturup kontrol etmeyi sağlar.            |
# | Ansible      | Sunucu kurulumlarını ve yapılandırmalarını otomatize eden dev bir araçtır.        |
# | Celery       | Arka planda çalışan zamanlanmış görevleri ve iş kuyruklarını yönetir.             |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 9. SES, GÖRÜNTÜ VE DOĞAL DİL İŞLEME (NLP & MULTIMEDIA)                                             |
#-----------------------------------------------------------------------------------------------------
# İnsan dilini anlamak ve medya dosyaları üzerinde işlem yapmak içindir.                             |
#-----------------------------------------------------------------------------------------------------
# | OpenCV       | Bilgisayarlı görü (Görüntü işleme, yüz tanıma, nesne takibi) kütüphanesidir.      |
# | NLTK         | Metin analizi ve doğal dil işleme için en köklü kütüphanelerden biridir.          |
# | SpaCy        | Modern, aşırı hızlı ve endüstriyel seviyede doğal dil işleme yapar.               |
# | Librosa      | Ses dosyalarını analiz etmek, ritim ve nota bulmak için kullanılır.               |
# | MoviePy      | Videoları kesmek, birleştirmek ve efekt eklemek için kullanılan video editörüdür. |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 10. FİNANS, EKONOMİ VE TARİHSEL VERİ ANALİZİ                                                       |
#-----------------------------------------------------------------------------------------------------
# Borsa verileri, kripto paralar ve istatistiksel modeller için kullanılır.                          |
#-----------------------------------------------------------------------------------------------------
# | Yfinance     | Yahoo Finance üzerinden canlı ve geçmiş borsa verilerini çeker.                   |
# | Statsmodels  | Çok derin istatistiksel testler ve ekonomik tahmin modelleri kurmayı sağlar.      |
# | Prophet      | Facebook tarafından geliştirilen, zaman serisi tahmini (Gelecek tahmini) yapar.   |
# | CCXT         | Yüzlerce kripto para borsasına tek bir kütüphane üzerinden bağlanmayı sağlar.     |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 11. DÖKÜMANTASYON, EXCEL VE RAPORLAMA                                                              |
#-----------------------------------------------------------------------------------------------------
# Ofis işlerini otomatize etmek ve profesyonel raporlar sunmak içindir.                              |
#-----------------------------------------------------------------------------------------------------
# | Openpyxl     | Excel dosyalarını (.xlsx) okumak ve hücre hücre yazmak için kullanılır.           |
# | Python-docx  | Microsoft Word belgeleri oluşturmak ve düzenlemek için kullanılır.                |
# | ReportLab    | Karmaşık ve profesyonel PDF dökümanları oluşturmanızı sağlar.                     |
# | Plotly       | İnternet tarayıcısında çalışan, etkileşimli ve hareketli grafikler üretir.        |
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# 12. PERFORMANS VE YARDIMCI ARAÇLAR                                                                 |
#-----------------------------------------------------------------------------------------------------
# Kodunuzun hızını artırmak ve geliştirme sürecini kolaylaştırmak içindir.                           |
#-----------------------------------------------------------------------------------------------------
# | Cython       | Python kodunu C diline çevirerek inanılmaz hız artışları sağlar.                  |
# | Rich         | Terminal ekranını renklendirmek, tablolar ve ilerleme çubukları eklemek içindir.  |
# | Click        | Harika görünen komut satırı arayüzleri (CLI) oluşturmanızı sağlar.                |
#-----------------------------------------------------------------------------------------------------

#-----------------------------
# MODÜLLERE TAKMA İSİM VERME :
#-----------------------------
"""
-> Modüller içe aktarılırken, kod dosyası  içerisinde daha pratik bir şekilde kullanabilmek için modül ismine takma ad verilebilir.
-> Takma ad verme işlemi as anahtar sözcüğü ile yapılır.

"""
#import OrijinalAd as KeyfiAd

import random as rastgele  # rastgele sayılarla ilgili random modülüne rastgele isim ver.
x = rastgele.randint(1,50)   # rastgele takma adı ile radiant ()özelliğine eriş ve 1 ile 50 arası rastgele sayı üret.
# rastgele sayı üret 
print(x)

#----------------------------------------
# MODÜLÜN BELLİ BİR KISMINI İÇE AKTARMA :
#----------------------------------------
"""
-> Bir modülü import etmekle içerisinde yer alan tüm özellikler dosyaya eklenmiş olur.
-> Fakat modülün içerisinde sadece belirli bir özelliğe ihtiyaç duyuluyorsa tümünü import etmek yerine sadece ilgili isim özelliğinin import edilmesi şu şekilde sağlanır.
"""

from os import name
print(name)
# Burada işletim sistemi özellikleri içeren os modülü içinden sadece name özelliği dosyaya eklenmiş olur.
# Diğer veriler eklenmediği için sisteme ek yük getirmez.

from math import sin,radians
print(sin(radians(30)))
#Bu kod ile math modülü altındadaki sin ve radians fonksiyonları dosyaya dahil edilmiş olur.

#-------------------------------------------------
# MODÜL ADI ÖNEKİ KULLANMADAN ÖZELLİKLERE ERİŞİM :
#------------------------------------------------- 
"""
-> Bir modül import edildikten sonra altındaki yer alan özelliklere "modül.özellik" şeklinde modül adı ön eki ile özelliklere erişilebilir.
-> Modül adı ön ekini kullanmaya gerek kalmadan özelliklere erişebilmeyi sağlamak için şu yöntem kullanılır.

"""
from math import*
print(cos(radians(30)))
#Yukarıdaki kodda import* ifadesi ile math modülünün altında yer alan her şeyin bu kod dosyası içerisinde math ön eki yazılmadan kullanabileceği belirtilmektedir.

#----------------------------
# MODÜL İÇERİĞİNİ LİSTELEME :
#----------------------------
"""
-> Bir modül altında yer alan özelliklerin  listelenmesi için dir() fonksiyonu kullanılır.
"""

import math
icerik=dir(math)
print(icerik)

# math modülü altında yer alan içerik şu şekilde listelenir.
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 
# 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
#  'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor',
#  'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
#  'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
#  'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']



"""
 "Elhamdülillah, 12. Bab ile Python’un kendi öz mülkünden (Standart Kütüphane) çıkıp, tüm dünyadaki yazılımcıların (alimlerin) ortak birikimi olan o devasa 'İlim Okyanusu'na (3. Taraf Kütüphaneler) yelken açtık."
 "Bu kütüphanelerin her birini, fethe hazır birer kale gibi önümüze serdik. dir() fonksiyonuyla bu kalelerin en gizli odalarını, her bir detayını ve mühimmatını listeleyerek her ayrıntıya vakıf olma şerefine nail olduk."
 "Bu Bab, sadece bir keşif ve niyet makamı olduğundan, örneklerle bizzat kılıç kuşanmak yerine, hangi ordunun (kütüphanenin) hangi fetihte (projede) kullanılacağının ilmini tahsil ettik."
"""