#╔══════════════════════════════════════════════════════════════════════════╗#
#║             ALGORİTMA VE PROGRAMLAMAYA GİRİŞ-1(PYTHON_101)               ║#
#╚══════════════════════════════════════════════════════════════════════════╝#

#-----------------------------------------------
# BAB 1 (PROBLEM ÇÖZME VE ALGORİTMA TEMELLERİ) : 
#-----------------------------------------------
"""
-> Problem tanımına yer verildi. Bir problemi tanımlamasından çözümüne kadarki olan süreç teorik olarak öğrenildi ve gerçek hayattan uygulamalı bir örnek ile pekiştirildi.
-> Algoritmanın tanımı problem çözüm yönteminden verildi.
-> Algoritmanın kelimesini bulan El-Harezmi'ye değinildi.
-> El-Harezmi'nin diğer disiplinlerdeki çalışmalarına da kısaca değinildi.
-> El-Harezmi'nin bulduğu 2'lik binary sisteminin bilgisayar bilimine  ve elektroniğe katkısının önemi vurgulandı.
-> Algoritmaların genel özelliklerine değinildi.
-> Algoritma işlem adımlarını belirleyen 3 farklı yönteme ( Algoritmik doğal dil, Akış Şeması, Sözde Kod ) değinildi.
-> Algoritmayı ifade etmek için akış şemalarının dışında olan N-S(Nassi-Shneiderman) Şemaları ve W-O(Warnier-Orr) Diyagramlarına da kısaca değinildi.
-> Algoritmik doğal dil işlendi ve birkaç örnek çözüldü.
-> Sözde Kod işlendi ve birkaç örnek çözüldü.
-> Akış Şeması(Flowchart) ve temel elemanları işlendi ve birkaç örnek çözüldü. Özellikle paralelkenar ve dikdörtgen arasındaki fark mukayaese edilip özümsendi.
-> Akış Şeması pratik olarak da draw.io gibi uygulamalarda uygulamalı olarak çözüldü.
-> Sözde kod(Pseudocode) kavramı  ve algoritmik doğal dil ile arasındaki farklar gözetildi.
"""
# 1.BAB, 137 satır ve 1 örnekten oluşmaktadır.


#--------------------------------------------------------------
# BAB 2 (YAZILIM GELİŞTİRME TEMELLERİ VE PROGRAMLAMA DİLLERİ) :
#--------------------------------------------------------------
"""
-> Yazılım, algoritma, program tanımları verildi arasındaki ilişkiye değinildi.
-> Programlama dili kavramına değinildi.
-> Makine Dili kavramına değinildi ve bilgisayar için önemi vurgulandı.
-> Programlama Dilleri Türlerine (Çok Yüksek,Yüksek,Orta,Düşük) değinildi ve sınıflandırıldı.
-> Makine diline değinildi ve anlatıldı. Donanım için öneminden söz edildi.
-> Derleyici ve yorumlayıcı anlatıldı farkları gözetildi. Akılda kalıcı örnekle de durum pekiştirildi.
-> Yorumlayıcıdaki ara kod (Byte kod ) kavramına değinildi.
-> Bytecode'u makine koduna dönüştüren platformlara değinildi.(Sanal Makine)
-> Sanal makinelerden JVM ve PVM'ye değinildi.
"""
# 2.BAB, 182 satır ve 0 örnekten oluşmaktadır.


#------------------------------------------------------------
# BAB 3 (PYTHON PROGRAMLAMA DİLİNE GİRİŞ VE ORTAM KURULUMU) :
#------------------------------------------------------------
"""
-> Python programlama dilinin tarihçesine değinildi.
-> Python 2'de olan raw_input() ve input arasındaki fark açıklandı.
-> Python temel felsefelerinden bahsedildi.(PEP 20)
-> Python kurulumu yapıldı.Stable releases ve Pre-releases farkı anlatıldı.
-> Pre-releases aşamalarından söz edidi.(Alpha,Beta,RC,Stable)
-> Python için editör kurulumu yapıldı.
-> IDE ve IDLE kavramlarına değinildi ve mukayese yapıldı.
-> Python'da en çok kullanılan IDE'lerden olan PyCharm kurulumu yapıldı.
-> En çok kullanılan Python IDE'lerine değinildi.
-> Kütüphane kavramına değinildi ve Pythonda en çok kullanılan kütüphaneler ayrıntıya girmeden bakıldı.
-> Python'ın diğer dillerden ayıran özelliklere değinildi.
-> Python kullanım yerlerine değinildi.
-> Pythonda ("Selamünaleyküm Dünya") yazıldı.
"""
# 3.BAB, 363 satır ve 0 örnekten oluşmaktadır.


#--------------------------------------------
# BAB 4 (TEMEL VERİ TÜRLERİ VE DEĞİŞKENLER) :
#--------------------------------------------

"""
-> Değişken ve sabit kavramına değinildi. Değişkenin arka planda RAM'de nasıl çalıştığı tafsilatlı anlatıldı.
-> Değişken Adlandırma Kurallarına değinildi.
-> Notasyon kavramına değinildi. En çok kullanılan notasyonlara
değinildi.(Pascal,camelcase,Hungarian,UPPERCASE,snakecase).
-> Değişkenlere değer atama kavramından bahsedildi ve = operatörü anlatıldı.
-> Veri kavramının ne anlama geldiği öğretildi.
-> Pythonda Veri tipi kavramına değinildi ve çeşitleri(int,float,str,bool,list,tuple,dict,set,Nonetype) olarak belirtildi.
-> Dinamik Tipleme (Dynamic Typing) özelliği anlatıldı. Python'ın statik dillerden farkı ve bir değişkenin türünün çalışma anında (runtime) nasıl değişebildiği vurgulandı.
-> Karakter(Char) ile Karakter Dizisi(String) arasındaki fark gözetildi.
-> Pythonda Veri Tipi dönüşümleri anlatıldı. Ve örtülü dönüşüm ile açık dönüşüm çeşitlerine değinilip arasındaki farklar gözetildi.
-> Hatta erken dönüşüm ile geç dönüşüm arasındaki farkların üzerinde duruldu.
-> Pythonda int(),float(),string(),chr(),ord(),bool()tiplerine dönüşüm anlatıldı ve örnekle pekiştirildi.
-> Print() komutu ile karakter dizilerinin kullanımı anlatıldı.
-> sep,end parametreleri anlatıldı.
-> *Yıldız işareti ile karakterleri ayrıştırma kavramı gösterildi.
-> Kaçıs(Escape) karakterleri (\n,\t,\a,\b,\r) anlatıldı.
-> Kaçış karakterlerini etkisiz hale getirme olayı anlatıldı(\\ ve r)
-> Pythonda string birleştirme kavramından bahsedildi ve 4 yöntem(Temel(+)operatörü,f-string, .format() , .join() çeşitlerine değinildi ve örnek yapıldı.
-> input() fonksiyonu ile kullanıcıdan veri alma işlemi anlatıldı ve örnek yapıldı.
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

# 4.BAB, 747 satır ve 9 örnekten oluşmaktadır.


#----------------------------------------------
# BAB 5 (PYTHON'DA OPERATÖRLER VE OPERANDLAR) :
#----------------------------------------------
"""
-> Operatör ve operand kavramları, programlamanın temel yapı taşları olarak ele alındı.
-> Operatör Türlerine(Aritmetik,Karşılaştırma,Mantıksal) detaylıca değinildi ve her biri için özgün örneklerle pekiştirildi.
-> İşlem önceliği konusu, matematiksel disiplinle köprü kurularak anlatıldı; böylece karmaşık ifadelerin çözüm mantığı kavratıldı. 
-> Hatta karşılaştırma ve mantıksal  operatörlerinin işlem önceliğinde neden sonra geldiği de açıklandı.
-> Atama operatörünün (=) matematikteki "eşitlik" anlamından temel farkı vurgulanarak, değişkenlere değer aktarma süreci netleştirildi.
-> İşaret ve Atama Operatörleri değinildi. Hatta = 'in atama için önemini matematikten de farkı vurgulandı.
-> Aritmetik Operatörler Tablo şeklinde gösterildi.
-> Bitsel İşlem Operatörleri anlatıldı.(Bitsel Sola Kaydırma ve Bitsel Sağa Kaydırma)
-> Bitsel operatörler (Bitwise) anlatılırken soyut kalan 0 ve 1 dünyasını somutlaştırmak için bin() fonksiyonu bir "gözlem aracı" olarak dahil edilmiştir.
-> Koleksiyonlar içindeki varlık kontrolünü sağlayan Aitlik Operatörleri (in, not in) pratiklerle gösterildi.
-> Kimlik Operatörleri (is, is not) anlatılırken, sadece işlevselliğe değil, Python'un arka planındaki Bellek Yönetimi mekanizmasına da güçlü bir vurgu yapıldı.
-> Değişkenlerin bellek adresleri (id) üzerinden yapılan bu vurgu ile performans ve bellek tasarrufu mantığı öğretildi.
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

# 5. BAB, 600 satır ve 10 örnekten oluşmaktadır.


#-----------------------------------------------
# BAB 6 (PYTHON'DA AKIŞ KONTROL MEKANİZMALARI) :
#-----------------------------------------------
"""
-> Akış Kontrol Mekanizmaları (Flow Control) kavramı ve programın dallanma mantığı genel hatlarıyla anlatıldı.
-> Karar Yapıları (Decision Structures) kavramına değinildi ve programın çalışma esnasında nasıl seçim yaptığı açıklandı.
-> Python'da girintileme (indentation) sisteminin önemi, blok başlatma işareti olan iki nokta (: ) kullanımı ve kodun görsel hiyerarşisi tafsilatlı anlatıldı.
-> Değerlendirme (Evaluation) ile Yürütme (Execution) arasındaki farklar gözetildi; bir koşulun sorgulanması ile o bloğun çalıştırılması ayrımı yapıldı.
-> if Yapısı anlatıldı; bir koşulun doğruluğuna (True) bağlı olarak eylem gerçekleştirme mantığı öğretildi.
-> else Yapısı anlatıldı. Tüm koşulların yanlış (False) olduğu durumlarda devreye giren "varsayılan yol" mantığı açıklandı.
-> elif Yapısı anlatıldı. Birbiriyle ilişkili çoklu koşul hiyerarşisi ve if-else-if zincirinin çalışma prensibi örneklerle pekiştirildi.
-> Sıralama Hatası (Ordering Matters) uyarısı yapıldı; koşulların "özelden genele" doğru sıralanmasının önemi vurgulandı.
-> Python'da "Boşluk Kontrolü" için kullanılan pass komutunun işlevi ve kullanım alanları anlatıldı.
-> Mantıksal Operatörler (and, or) ile birden fazla koşulu birleştirerek karmaşık karar mekanizmaları kurgulama yetisi kazandırıldı.
-> Chained Comparison (Zincirleme Karşılaştırma) kavramından bahsedildi ve Python'a özgü bir durum olduğu vurgulandı.
-> İç İçe if (Nested if) yapıları anlatıldı; hiyerarşik kararların nasıl verildiği ve karar ağacı mantığı açıklandı.
-> Inline Conditional Expressions (Tek satırlık if) yapısı anlatıldı ve Ternary Operator mantığına değinildi. Lakin List Comprehension kısmına girilmedi.
-> Savunmacı Programlama (Defensive Programming) kavramına değinilerek, matematiksel hataları (sıfıra bölme vb.) daha oluşmadan mantık süzgeciyle engelleme yöntemleri gösterildi.(Try-exceptsiz)
-> DRY prensibi üzerinde duruldu ve neden 
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

# 6.BAB, 726 satır ve 12 örnekten oluşmaktadır.

#-----------------------------
# BAB 7 (PYTHON'DA DÖNGÜLER) :
#-----------------------------
"""
-> Döngü tanımına yer verilmekle birlikte döngünün ne işe yaradığı nerelerde kullanıldığına değinildi.
-> Python'daki döngülere (while,for) değinildi.
-> Döngülerin çalışma prensibi vurgulandı.
-> while döngüsü tafsilatlı anlatılıp önemi vurgulandı.Çalışma adımları tek tek gösterildi. Basit örneklerle pekiştirildi.
-> while ile sonsuz döngü kavramına değinildi. Program açısından önemi vurgulandı.
-> while True ile basit bir hesap makinesi kodlaması yapıldı.
-> for döngüsü tafsilatlı anlatılıp önemi vurgulandı. Çalışma adımları tek tek gösterildi. Basit örneklerle pekiştirildi.
-> while , for döngüsü kullanım alanları ve farklarının mukayesesi yapıldı.
-> for döngüsü ile liste demetlerde gezinme kavramı gösterildi. Listeler yerine neden bunun kullanıldığını önemle vurgulandı.
-> range fonksiyonu  anlatıldı. (ilk_deger,son_deger,artış_miktarı) örnekle pekiştirildi.
-> Atlama ifadeleri anlatıldı ve döngüler üzerinde önemi vurgulandı.
-> break,continue,pass kavramlarına değinildi. Kodlamada aktif bir şekilde kullanıldı. Farkları gözetilip mukayesesi yapıldı.
-> case yapısına değinildi. Diğer dillerde switch-case olan ama Python'da match-case yapısı olduğu vurgulandı.
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

# 7.BAB, 1072 satırdan ve 21 örnekten oluşmaktadır.


#--------------------------------------------------------------
# BAB 8: KOLEKSİYONLAR-1(COLLECTIONS-1)(LİSTELER VE DEMETLER) :
#--------------------------------------------------------------
"""
-> Koleksiyon tanımına yer verildi ve Koleksiyonların temel amaçlarından bahsedildi.
-> Pythondaki 4 ana yerleşik koleksiyon türü (Liste,Demet,Sözlük,Küme) kısaca bahsedildi.
-> Teorik olarak listenin tanımına yer verilmekle birlikte liste tanımlama yöntemleri pratik olarak gösterildi.
-> Listelerin farklı türlerde oluşabildiğini vurgulayıp bunun Python'ın diğer dillerden farklı olduğu da vurgulanmış oldu.
-> Listelerin yapısı ve esneklik özelliğinden bahsedildi ve bu yapının kullanılma amacına değinildi.
-> Listelerin genel özelliklerinden bahsedildi.
-> Liste [] tanımlama ile list() fonksiyonu anlatılıp arasındaki fark mukayese edilip öğrenciye kavratıldı.
-> Liste elemanlarına erişim (İndex) günlük hayattan örnek verilerek anlatıldı.
-> Pozitif-Negatif indeksleme gösterildi .
-> Negatif indekslemenin avantajları ve C, C++, Java dillerinde neden bulunmadığı bahsedildi.
-> Liste eleman sayısını bulan len() fonksiyonu ve kullanım alanları gösterildi.
-> Listeye eleman ekleme metotları (append, extend, insert) arasındaki nüanslar ve "ev sahibi" kuralı anlatıldı.
-> Listeden eleman silme yöntemleri (remove, pop, clear, del) kullanım amaçlarına göre (değer vs. indeks) sınıflandırıldı.
-> Liste içinde arama ve sayma yapan index() ve count() metotları pratik örneklerle işlendi.
-> Sıralama işlemleri için sort() ve reverse() metotları, ASCII/Unicode değer öncelikleri (Türkçe karakter hassasiyeti) vurgulanarak anlatıldı.
-> Bellek yönetiminde kritik öneme sahip olan copy() metodu ile "yüzeysel kopyalama" ve "referans ataması" farkı açıklandı.
-> Matematiksel analizler için max(), min() ve sum() fonksiyonlarının hem sayısal hem de karakter tabanlı listelerdeki davranışı gösterildi.
-> Liste Üreteçleri (List Comprehensions) konusuna giriş yapılarak, Pythonic kod yazım tarzının temeli atıldı.
-> Demetler (Tuples) konusu; "Değişmezlik (Immutable)" ve "Veri Güvenliği" temasıyla, Listelerle mukayese edilerek tamamlandı.
-> Tek elemanlı demet tanımlama ve demetlerin hangi durumlarda (sabit veriler, sözlük anahtarları) tercih edilmesi gerektiği vurgulandı.
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

# 8.BAB, 912 satırdan ve 5 örnekten oluşmaktadır.


#--------------------------------------------------------------
# BAB 9: KOLEKSİYONLAR-2(COLLECTIONS-2)(SÖZLÜKLER VE KÜMELER) :
#--------------------------------------------------------------
"""
-> Sözlük (Dictionary) kavramı; gerçek hayat analojisiyle (kelime-anlam ilişkisi) teorik olarak tanımlandı.
-> Veri erişiminde devrim yaratan Anahtar (Key) - Değer (Value) çifti mantığı ve benzersiz anahtar kuralı işlendi.
-> Python versiyonları arasındaki (3.6 öncesi ve sonrası) sıralama (order) farklarına ve erişim performansına değinildi.
-> Sözlük oluşturmada kullanılan Literal ({}) yöntem ile dict() fonksiyonu arasındaki söz dizimi farkları mukayese edildi.
-> Veri güvenliği açısından hayati önem taşıyan, hata döndürmeyen .get() metodu ile standart erişim yöntemi karşılaştırıldı.
-> Sözlükler üzerinde Ekleme, Düzenleme, Silme (del) ve Temizleme (clear) operasyonları pratik örneklerle gösterildi.
-> Sözlük içeriğini analiz etmek için kullanılan .keys(), .values() ve .items() metotlarının döngülerle kullanımı öğretildi.
-> Sözlükte Anahtar Varlığını kontrol etmeye sağlayan "in" ve "not in" ifadelerine değinildi. 
-> Sözlüklerin bellek yönetimi; Referans Ataması ile .copy() (bağımsız kopyalama) arasındaki farklarla açıklandı.
-> Matematiksel temellere dayanan Küme (Set) yapısı; Benzersizlik (Unique) ve Sırasızlık (Unordered) özellikleri üzerinden tanımlandı.
-> Kümeleri kullanma nedenleri ve diğer veri yapıları arasındaki farklar üzerinden anlatıldı.
-> Küme tanımlama için set() komutundan bahsedildi ve bunun built-in bir fonksiyon olduğu üzerinde duruldu.
-> Listeyi kümeye dönüştürme işlemi gösterildi.
-> Kümeye veri ekleme (add) ve veri silmede hata yönetimi farkı olan remove vs discard yöntemleri anlatıldı.
-> remove ve discard komutları arasındaki fark değinildi. Kümede olmayan elemanı çıkarmaya çalıştığımızda remove'un hata verdiğini ve discard komutunun hata vermediği gösterildi.
-> İki küme arasındaki ilişkileri belirleyen Fark (difference), Kesişim (intersection) ve Birleşim (union) işlemleri hem metot hem operatör bazında gösterildi ve örneklerle pekiştirildi.
-> Kümeler arası hiyerarşiyi sorgulayan Ayrık Küme (isdisjoint), Alt Küme (issubset) ve Kapsayan Küme (issuperset) kontrolleri işlendi ve örneklerle pekiştirildi.
-> İç içe sözlük (Nested Dict) kavramına değinildi. Json formatına benzediği vurgulandı.
"""

# ===============================================================================================================================================
# ÖRNEK 1: Koleksiyonlar Üzerinde Veri Analizi ve Koşullu Transformasyon (Listeler ve Sözlüklerin İç İçe Kullanımı)                             |
# ÖRNEK 2: Sözlükler Üzerinde Temel Gezinti (Implicit Loop Yöntemi)                                                                             |
# ÖRNEK 3: Sözlük Metotları ile Profesyonel Veri İşleme (Keys, Values, Items ve Unpacking Teknikleri)                                           |
# ÖRNEK 4: Kümeler (Sets) ile Karakter Denetimi ve Ayrık Küme Analizi (isdisjoint Metodu Uygulaması)                                            |   
# ÖRNEK 5: Dinamik Dijital Kütüphane ve İlim Dalları Sorgulama Sistemi (Kapsamlı Veri Tasnifi ve Güvenli Erişim Uygulaması)                     |
# ===============================================================================================================================================

# 9.BAB 917 satır ve 5 örnekten oluşmaktadır.


#------------------------
# BAB 10 (FONKSİYONLAR) :
#------------------------
"""
-> Fonksiyon kavramı anlatıldı ve modüler programlama için önemi vurgulandı.
-> Fonksiyonların aslında alt programlar gibi çalıştığı izah edildi.
-> Fonksiyonların temel amaçları anlatıldı. Kodun tekrar kullanılabilirliği, karmaşıklığı bölmek, soyutlama, okunabilirlik ve düzen gibi ifadelere değinildi.
-> Örnek hazır fonksiyon olan print() ve input() fonksiyonu soyutlama mantığı ile anlatıldı.
-> Fonksiyonların çalışma mantığı anlatıldı.
-> Fonksyion tanımlama anlatıldı. 'def' anahtar sözcüğüne değinildi.
-> Parametre kavramına değinildi ve parametreli fonksiyonlar anlatıldı.
-> Fonksiyon çağrımı nasıl olduğu izah edildi.
-> Parametresiz fonksiyon anlatıldı ve parametreli fonksiyon ile mukayese edildi.
-> Fonksiyonun geriye değer döndürmesi (return) kavramı anlatıldı ve önemine değinildi.
-> Varsayılan değerli parametreler anlatıldı.
-> İsimli ve isimsiz parametreler anlatıldı. Farkları mukayese edildi.
-> Değişken sayıda parametre alan fonksiyonlardan *args kavramından bahsedildi.
-> Fonksiyonlarla alakalı 10 Genel özellikten bahsedildi.
-> Özyineli Fonksiyonlardan bahsedildi. Fibonacci, Faktöriyel örnekleri ile pekiştirildi.
-> Matematiksel ve Karakter tabanlı fonksiyonlardan bahsedildi.
"""

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

# 10.BAB 1145 Satır ve 20 örnekten oluşmaktadır.


#--------------------
# BAB 11 (MODÜLLER) :
#--------------------
"""
-> Belirli bir dosya ile sınırlı olan fonksiyonların yerelliği ile import komutuyla her yerden çağrılabilen modüllerin evrenselliği arasındaki mimari farklar işlendi.
-> Modüllerin yeniden kullanılabilirliği, nizamlı bir paketleme ve projenin farklı dosyalara bölünerek yönetilebilir kılınması prensibleri açıklandı.
-> Modüller 3 ana kategoriye ayrıldı. Built-in, Standart Kütüphane Modülleri, Üçüncü Taraf Modülleri diye kısaca bahsedildi.
-> Python'ın çekirdeğine (C seviyesinde) gömülü olan, kurulum gerektirmeyen ve çalışma anında RAM'de hazır bulunan yüksek performanslı modüller tanımlandı. Built-in (Yerleşik) Modüllerin özelliklerinden bahsedildi. 
-> sys (Sistem Modülü): Python yorumlayıcısının çalışma yolu (path), versiyonu ve sistem argümanlarını yöneten mekanizmalar incelendi.
-> time (Zaman Modülü): Bilgisayarların zaman miladı (Epoch - 1 Ocak 1970) kavramı açıklandı. Hassas zaman ölçümü ve time.sleep() ile program akışının yönetimi gösterildi.
-> gc (Garbage Collector): Python'ın bellek temizlik işçisi olan çöp toplayıcı mekanizmasının RAM üzerindeki otomatik temizlik mantığına değinildi.
-> builtins Modülü: Her zaman hazır bulunan temel fonksiyonların (print, len vb.) aslında bu görünmez kütüphaneye bağlı olduğu teknik olarak gösterildi.
-> marshal (İçsel Serileştirme): Python'ın kendi kaynak kodlarını derlerken kullandığı (.pyc dosyaları), veriyi makine diline yakın bayt dizilerine dönüştüren en alt seviye modül incelendi.
-> Bilgisayarlar için zaman kavramının neden 1970'de başladığı anlatıldı.
-> Hatta 2038 problemine değinildi.
-> Standart Kütüphane Modüllerine ve özelliklerine değinildi.
-> os (İşletim Sistemi Modülü): Yazılımın donanım ve dosya sistemiyle kurduğu köprü incelendi. Dizin oluşturma, dosya silme ve sistem çevre değişkenlerine (Environment Variables) hükmetme yöntemleri gösterildi.
-> random (Rastgelelik Mekanizması): Bilgisayar bilimindeki "Psödo-Rastgelelik" kavramı açıklandı. seed() fonksiyonu ile rastgeleliğin nasıl kontrol altına alınabileceği ve kilitlenebileceği (debugging için önemi) teknik olarak işlendi.
-> math (Matematiksel Sabitler ve Fonksiyonlar): Temel operatörlerin yetmediği yerde Pi, Euler ve Tau gibi evrensel sabitlere erişim sağlandı. Trigonometrik, logaritmik ve ileri seviye (Gamma, Faktöriyel) hesaplamaların kütüphane nizamıyla çözümü gösterildi.
-> datetime (Nesne Tabanlı Zaman Yönetimi): Zamanın sadece bir "tick" (saniye) değil, yıl/ay/gün olarak bir nesne (object) şeklinde nasıl modellendiği ve tarihler arası aritmetik işlemlerin (timedelta) mantığı anlatıldı.
-> calendar (Takvim ve Astronomik Nizam): Takvimsel verilerin görselleştirilmesi ve Şubat'ın 29 çektiği "Artık Yıl" (Leap Year) hesaplamalarının yazılımsal karşılığı incelendi.
-> json (Evrensel Veri Takas Lisanı): Python'daki zahirî veri yapılarının (dict, list), dış dünya ile konuşabilmesi için metin tabanlı evrensel bir formata dönüştürülmesi (Serialization/Deserialization) süreci işlendi.
-> shutil (Yüksek Seviye Dosya Operasyonları): os modülünün kaba işleri bıraktığı yerden devralan, bütünsel klasör kopyalama, taşıma ve arşivleme (zip) gibi "ağır iş makinesi" fonksiyonları tanımlandı.
-> csv (Tablolu Veri Yönetimi): Veri biliminin temeli olan virgülle ayrılmış dosyaların (.csv) okunması ve yazılması süreçleri; indeks bazlı (reader) ve anahtar bazlı (DictReader) erişim yöntemleriyle açıklandı.
-> re (Düzenli İfadeler - Giriş): Metinler içindeki karmaşık kalıpların (e-posta, telefon vb.) saniyeler içinde tespit edilmesini sağlayan dedektiflik mekanizmasına kısaca değinildi.
-> statistics (Merkezi Eğilim Analizi): Veri setlerinin ham halinden anlamlı özetler (ortalama, medyan, mod ve standart sapma) çıkarma yöntemleri mühendislik bakış açısıyla gösterildi.
-> collections (Gelişmiş Veri Yapıları): Standart listelerin ve sözlüklerin yetmediği senaryolarda; Counter ile hızlı sayım, deque ile iki uçlu hızlı işlem ve namedtuple ile isimli erişim gibi "süper kahraman" veri yapıları pekiştirildi.
"""

# =============================================================================================================================================
#  BAB 11: MODÜLLER PROJE LİSTESİ :                                                                                                           |
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
#  ÖRNEK 11: Algoritmik Strateji: Sayı Tahmin Oyunu (Random & Loop Control)                                                                   |                                                                        |
# =============================================================================================================================================

# 11.BAB 1377 satırdan ve 11 örnekten oluşmaktadır.

#----------------------
# BAB 12 (MODÜLLER-2) :
#----------------------
"""
-> Taraf Kütüphanelerin ne olduğu ve neden kullanıldığı detaylıca izah edildi.
-> Veri Bilimi, Analiz ve Görselleştirme kütüphanelerinin mahiyetine değinildi.
-> Yapay Zeka ve Makine Öğrenmesi kütüphanelerinin temel işlevlerine değinildi.
-> Web Geliştirme ve API Yönetimi kütüphanelerinin sunduğu imkanlara değinildi.
-> Web Kazıma ve otomasyon kütüphanelerinin kullanım alanlarına değinildi.
-> Masaüstü, Arayüz, Oyun ve Resim işleme kütüphanelerinin gücü vurgulandı.
-> Veritabanı ve test araçları kütüphanelerinin güvenli kod yazımındaki yeri anlatıldı.
-> Siber güvenlik ve ağ yönetimi kütüphanelerinin koruyucu etkisine değinildi.
-> Bulut sistemleri ve DevOps kütüphanelerinin operasyonel faydaları zikredildi.
-> Ses, görüntü ve doğal dil işleme kütüphanelerinin derinliklerine değinildi.
-> Finans, ekonomi, borsa ve tarihsel veri analizi kütüphaneleri incelendi.
-> Dökümantasyon, excel ve raporlama kütüphanelerinin otomasyon gücü belirtildi.
-> Performans ve yardımcı araçlar kütüphanelerinin sağladığı hız artışına değinildi.
"""

# 12.BAB 211 satırdan ve 0 örnekten oluşmaktadır.



#---------------------------------------
# BAB 13 (HATA YÖNETİMİ VE İSTİSNALAR) :
#---------------------------------------
"""
-> Hata türlerinin iki ana başlıkta sınıflandırıldığı izah edildi: Söz Dizimsel Hatalar (Syntax Errors) ve Çalışma Zamanı Hataları (Exceptions / Runtime Errors).
-> Söz Dizimsel Hataların (SyntaxError) ne olduğu, neden oluştuğu ve nasıl düzeltileceği öğrenildi.
-> Çalışma Zamanı Hatalarının (İstisnalar) syntax doğru olsa bile program çalışırken ortaya çıkabileceği izah edildi.
-> En sık karşılaşılan istisna türleri ve açıklamaları tablo halinde sunuldu: ValueError, ZeroDivisionError, IndexError, TypeError, NameError, KeyError, FileNotFoundError.
-> Her bir istisna türü için örnek kod parçacıklarıyla hangi durumlarda ortaya çıktığı gösterildi.
-> Hata oluşabilecek kod bloklarının try bloğu içine alınması gerektiği izah edildi.
-> except bloğunun, try bloğunda hata oluştuğunda çalıştığı öğrenildi.
-> Genel except: kullanımından kaçınılması, mümkünse özel hata türlerinin yakalanması gerektiği vurgulandı.
-> Birden fazla except bloğu ile farklı hata türlerine özel tepkiler verilebileceği uygulamalı olarak gösterildi.
-> except Exception as e kullanarak hatanın orijinal mesajına erişilebileceği izah edildi.
-> else bloğunun, try bloğunda hiç hata oluşmazsa çalıştığı öğrenildi.
-> finally bloğunun, hata olsun veya olmasın her durumda çalıştığı ve genellikle kaynak temizliği (dosya kapatma, bağlantı kesme) için kullanıldığı izah edildi.
-> Örnek bir hesap makinesi fonksiyonu üzerinden tüm blokların (try-except-else-finally) birlikte nasıl kullanıldığı uygulamalı olarak gösterildi.
-> Python için hata olmayan ancak iş mantığına göre hata sayılan durumlarda raise deyimi ile istisna fırlatılabileceği öğrenildi.
-> Genel Exception ile özel hata türlerinin (ValueError, OverflowError vb.) nasıl fırlatılacağı örneklerle gösterildi.
-> raise kullanarak programın akışını kontrol etme ve kullanıcıyı bilinçlendirme becerisi kazanıldı.
-> assert ifadesinin bir koşulun doğruluğunu test etmek için kullanıldığı izah edildi.
-> Koşul yanlış olduğunda AssertionError fırlatıldığı ve genellikle test / hata ayıklama amaçlı kullanıldığı öğrenildi.
-> Hata yönetimi yaparken dikkat edilmesi gereken 10 altın kural listelendi.
-> Her kuralın neden önemli olduğu kısaca izah edildi.
-> try, except, else, finally ve raise anahtar kelimelerinin ne zaman çalıştığını özetleyen bir karşılaştırma tablosu oluşturuldu.
-> En az bir except bloğunun zorunlu olduğu bilgisi pekiştirildi.
"""

# ============================================================================================================
#  BAB 13 (HATA YÖNETİMİ VE İSTİSNALAR) PROJE LİSTESİ :                                                      |
# ============================================================================================================
#  ÖRNEK 1 : Liste İçindeki Numerik Verilerin Ayıklanması (pass ile hata yutma)                              |
#  ÖRNEK 2 : Çift Sayı Sorgusu ve Şartlı Hata Fırlatma (raise kullanımı)                                     |
#  ÖRNEK 3 : Gelişmiş Hata Ayıklayan Hesap Makinesi (try-except-else-finally ve özel hata yakalama)          |
# ============================================================================================================

# 13. BAB 273 satır ve 3 örnekten oluşmaktadır.


#--------------------------
# BAB 14 (DOSYA YÖNETİMİ) :
#--------------------------
"""
-> Dosya kavramı ve programlama dünyasındaki önemi anlatıldı.
-> Kalıcı veri saklama (persistence) ile geçici bellek (RAM) arasındaki fark vurgulandı.
-> Python'da dosya işlemleri için yerleşik open() fonksiyonunun temel görevi açıklandı.

-> open() fonksiyonu ile dosya nesnesi oluşturma gösterildi.
-> "r" (okuma), "w" (yazma), "a" (ekleme), "x" (oluşturma), "b" (binary), "t" (text), "+" (okuma+yazma) modları tanıtıldı.
-> Her modun ne zaman kullanılacağı ve davranışları örneklendirildi.

-> close() ile dosyayı kapama ve kaynakların serbest bırakılması gerekliliği vurgulandı.
-> with open(...) as ... yapısının avantajları (otomatik kapatma, hata durumunda bile kaynakların serbest bırakılması) gösterildi.
-> Geleneksel try-finally ile karşılaştırma yapıldı.

-> read() ile dosyanın tamamını okuma.
-> read(n) ile belirli sayıda karakter/byte okuma.
-> readline() ile bir satır okuma.
-> readlines() ile tüm satırları liste olarak okuma.
-> for döngüsü ile dosya nesnesi üzerinde satır satır iterasyon yapma gösterildi.

-> write() ile string yazma.
-> writelines() ile bir liste içindeki stringleri yazma.
-> Yazma işlemlerinde karakter kodlaması (encoding parametresi) ve utf-8 kullanımı anlatıldı.
-> Liste içindeki metinleri dosyaya yazma örnekleri verildi.

-> tell() ile dosya içindeki mevcut bayt konumunu öğrenme gösterildi.
-> seek(offset, whence) ile dosya işaretçisini belirtilen konuma taşıma anlatıldı.
-> whence=0 (dosya başı), whence=1 (mevcut konum), whence=2 (dosya sonu) parametreleri açıklandı.
-> İkili dosyalarda ('b' modu) seek kullanımı örneklendirildi.
-> Belirli bir konumdan veri okuma kodu gösterildi.

-> Dosya bulunamama (FileNotFoundError), izin hatası (PermissionError) gibi istisnalar tanıtıldı.
-> try-except-finally yapısı ile dosya işlemlerini sarmalama gösterildi.
-> Hata yakalayarak dosya açma ve kapama garantisi sağlayan kod örnekleri verildi.

os modülü ile:
-> os.getcwd() ile çalışma dizinini öğrenme.
-> os.listdir() ile dizin içeriğini listeleme.
-> os.mkdir(), os.makedirs() ile klasör oluşturma.
-> os.rmdir(), shutil.rmtree() ile klasör silme.
-> os.rename() ile dosya/klasör adı değiştirme.
-> os.path alt modülü ile exists(), isfile(), isdir(), join(), getsize(), getmtime() fonksiyonları gösterildi.

pathlib modülü (modern yaklaşım) ile:
-> Path nesneleri oluşturma ve işlemler.
-> Path.mkdir(), Path.rmdir(), Path.rename().
-> Path.exists(), Path.is_file(), Path.is_dir().
-> Path.read_text(), Path.write_text(), Path.read_bytes(), Path.write_bytes().
-> Path.iterdir() ile dizin gezintisi.
-> Hem os hem pathlib ile klasör oluşturma, dosya bilgisi alma örnekleri verildi.

-> CSV (Comma Separated Values) formatı tanıtıldı.
-> csv.reader ve csv.writer ile basit okuma/yazma gösterildi.
-> csv.DictReader ve csv.DictWriter ile sözlük tabanlı işlemler anlatıldı.
-> Öğrenci bilgilerini CSV dosyasına yazma ve geri okuma örneği yapıldı.

-> JSON (JavaScript Object Notation) formatı tanıtıldı.
-> json.dump() ve json.load() ile dosyaya yazma/okuma gösterildi.
-> ensure_ascii=False ve indent parametrelerinin kullanımı açıklandı.
-> Sözlük verisini JSON dosyasına kaydetme ve geri yükleme örneği yapıldı.

-> Metin dosyası ile ikili dosya arasındaki fark anlatıldı.
-> Resim, ses, video gibi dosyaların ikili modda açılması gerektiği vurgulandı.
-> read() ve write() ile byte dizileri işleme gösterildi.
-> Bir resim dosyasını ikili modda okuyup kopyalama örneği yapıldı.

-> Geçici dosya oluşturma ihtiyacı açıklandı.
-> tempfile.TemporaryFile() ve tempfile.NamedTemporaryFile() kullanımı gösterildi.
-> Geçici dosyaya yazıp okuma örneği yapıldı.

-> Dosya işlemlerinde with kullanımının önemi vurgulandı.
-> Karakter kodlamasına dikkat edilmesi (encoding="utf-8") gerektiği belirtildi.
-> Hata yönetimini ihmal etmeme gerekliliği hatırlatıldı.
-> Büyük dosyaları satır satır okuma (bellek yönetimi) tavsiye edildi.
-> Modern pathlib kullanımının teşviki yapıldı.
-> os vs pathlib karşılaştırma tablosu (eski/yeni yaklaşım) sunuldu.
"""

# ==============================================================================================================
#  BAB 14: DOSYA İŞLEMLERİ - PROJE LİSTESİ (PROJECTS ON FILE OPERATIONS)                                       |
# ==============================================================================================================
#  ÖRNEK 1 : Öğrenci Bilgilerini Dosyaya Yazma ve Okuma (Temel Dosya G/Ç)                                      |
#  ÖRNEK 2 : Büyük Dosyayı Satır Satır Okuma (Bellek Dostu Log Analizi)                                        |
#  ÖRNEK 3 : seek/tell ile Dosya İçinde Gezinme (Rastgele Erişim)                                              |
#  ÖRNEK 4 : os Modülü ile Klasör Gezintisi ve Dosya İstatistikleri (Dizin Tarama)                             |
#  ÖRNEK 5 : pathlib ile Modern Dosya İşlemleri (Nesne Tabanlı Yaklaşım)                                       |
# ==============================================================================================================

# 14. BAB 431 satır ve 5 örnekten oluşmaktadır.


"""
--------------------------------------------------------------------------
| 1.BAB   -> PROBLEM ÇÖZME VE ALGORİTMA TEMELLERİ                        |
--------------------------------------------------------------------------
| 2.BAB   -> YAZILIM GELİŞTİRME TEMELLERİ VE PROGRAMLAMA DİLLERİ         |
--------------------------------------------------------------------------
| 3.BAB   -> PYTHON PROGRAMLAMA DİLİNE GİRİŞ VE ORTAM KURULUMU           |
--------------------------------------------------------------------------
| 4.BAB   -> PYTHON'DA TEMEL VERİ TÜRLERİ VE DEĞİŞKENLER                 |
--------------------------------------------------------------------------
| 5.BAB   -> PYTHON'DA OPERATÖRLER                                       |
--------------------------------------------------------------------------
| 6.BAB   -> PYTHON'DA AKIŞ KONTROLÜ                                     |
--------------------------------------------------------------------------
| 7.BAB   -> PYTHON'DA DÖNGÜLER                                          |
--------------------------------------------------------------------------
| 8.BAB   -> KOLEKSİYONLAR-1 (LİSTELER-DEMETLER)                         |
--------------------------------------------------------------------------
| 9.BAB   -> KOLEKSİYONLAR-2 (SÖZLÜKLER VE DEMETLER)                     |
--------------------------------------------------------------------------
| 10.BAB  -> FONKSİYONLAR                                                |
--------------------------------------------------------------------------
| 11.BAB  -> MODÜLLER-1                                                  |
--------------------------------------------------------------------------
| 12.BAB  -> MODÜLLER-2                                                  |
--------------------------------------------------------------------------
| 13.BAB  -> HATA YÖNETİMİ VE İSTİSNALAR                                 |
--------------------------------------------------------------------------
| 14.BAB  -> DOSYA İŞLEMLERİ                                             |
 -------------------------------------------------------------------------
"""




