# =========================================================================================================
# == BAB 1: PROBLEM ÇÖZME VE ALGORİTMA TEMELLERİ (CHAPTER 1: BASICS OF PROBLEM SOLVING AND ALGORITHMS) : ==
# =========================================================================================================

"""
-> Problem: Karşılaşılabilecek sorun veya çözülmesi gereken bir duruma denir.
-> Bir problemi çözmek için iki temel yol vardır: Deneme-yanılma veya Algoritma.
-> Algoritma: Bir problemi çözmek için izlenen adım adım mantıksal yol haritasıdır.
-> Problemin ortaya koyulmasından çözümün tamamlanmasına kadar geçen sürece "problem çözme süreci" denir.
-> Algoritma, bir problemi çözmeye giden yolun basit, net ve belirli bir sıraya göre tasarlanmış halidir.
-> Algoritma kelimesi, İslam bilgini El-Harezmi'nin (780-850) isminin Latince karşılığından türetilmiştir.
-> El-Harezmi; matematik, gök bilimi ve coğrafya alanlarında çalışmış, cebrin temelini atmıştır.
-> Bilgisayar biliminin temeli olan 2'lik (Binary) sistemi ve sıfırı (0) bulan önemli bir bilim insanıdır.
 
"Algoritma belirli bir işi, önceden tanımlanmış işlem adımlarını kullanarak adım adım ortaya koymaktır ve bu adımları bilgisayar ortamında herhangi bir dil ile kodlamaktır."[ÇÖLKESEN-2002]
"""

#--------------------------------
# ALGORİTMANIN GENEL ÖZELLİKLERİ:
#--------------------------------
"""
1) Her algoritmanın giriş ve çıkış değerleri olmalı.
2) Sonlu ve uygulanabilir olmalı.
3) Algoritma adımları kesin ve net olmalı.
4) Algoritma belirli bir mantık sırasında (sıralı) olmalı.
5) Algoritma etkin ve genel olmalı.
"""

#-----------------------------
# ALGORİTMA İFADE YÖNTEMLERİ :
#-----------------------------
"""
İşlem adımlarını belirlerken 3 farklı yöntem kullanılır:

--------------------------
 1. Algoritmik Doğal Dil :
--------------------------
-> Problemin çözümünü günlük dil kullanarak, herkesin anlayabileceği şekilde anlatmaktır.
-> Basit, teknik olmayan, herkesin anlayabileceği sıralı bir yapıya sahiptir.
-> Başla komutuyla başlar, Bitir komutuyla sonlanır.

---------------------------------------
 2. Akış Şeması/Diyagramı (Flowchart) :
---------------------------------------
-> İşlem adımlarının grafiksel sembollerle gösterilmesidir.
-> Görsel yapısı sayesinde mantık takibi kolaydır.

------------------------------------------------------
 3. Pseudocode (Sözde Kod / Yalancı Kod / Sahte Kod) :
------------------------------------------------------
-> Konuşma dili ile programlama dili arasındaki yapay kodlardır.
-> Dilden Bağımsızdır: Belirli bir dilin kurallarını bilmenize gerek yoktur.
-> Anlaşılırdır: Teknik olmayan kişilerin bile algoritmanın akışını anlamasını sağlar.
-> Hata Ayıklamayı Kolaylaştırır: Karmaşık bir problemi kodlamadan önce mantık hatalarını görmenize yardımcı olur.
-> Standart Değildir: Herkes kendine özgü bir şekilde yazabilir, ancak genellikle "EĞER", "DÖNGÜ", "BAŞLAT" gibi temel anahtar kelimeler kullanılır.

-> Bir algoritmayı ifade etmek için akış şemaları dışında N-S(Nassi-Shneiderman) Şemaları ve W-O(Warnier-Orr) Diyagramları vardır.
-> N-S şemalarının akış şemasından farkı, tüm işlemlerin/akışının bir dikdörtgen içerisinde gösterilmesidir.
-> W-O diyagramları ise, şekilsel bir yöntem olmayıp bir çeşit kaba kod benzeri yöntemdir.
"""


#--------------------------------------
# AKIŞ ŞEMASI SEMBOLLERİ VE GÖREVLERİ :
#--------------------------------------
"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|   | AKIŞ ŞEMASI SEMBOLLERİ |                                      | GÖREVLERİ |                                                                                                                                                 |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1 | Oval (Elips):                                                 | 1 |  Algoritmanın başladığını ve bittiğini gösterir.                                                                                                        |                                           
| 2 | Paralelkenar (Input/Output):                                  | 2 |  Veri girişi ve veri Sunumu (Girdi/Çıktı) sembolüdür.                                                                                                   |
| 3 | Dikdörtgen (Processing):                                      | 3 |  Aritmetik işlemler ve değişkene değer atama (İşlem) sembolüdür.                                                                                        |
| 4 | Eşkenar Dörtgen (Decision):                                   | 4 |  Karar verme mekanizması (Karar verme işlemi).                                                                                                          |
| 5 | Altıgen (Preparation):                                        | 5 |  Tekrarlanacak işlemler (Döngü) için kullanılır.                                                                                                        | 
| 6 | Dalgalı Dörtgen (Document):                                   | 6 |  Ekrana veya yazıcıya bilgi çıkışı için kullanılır.                                                                                                     |
| 7 | Daire (Connector):                                            | 7 |  Birleştirici veya bağlantı noktalarını temsil eder.                                                                                                    |
| 8 | Oklar (Flow Lines / Akış Yönü):                               | 8 |  İşlemlerin hangi yöne doğru ilerlediğini gösteren en temel unsurdur. Mantıksal akışın yönünü (yukarıdan aşağıya, soldan sağa) belirler.                |
| 9 | Kesik Kesik Oklar (Annotation / Açıklama Hattı):              | 9 |  Belirli bir sembol hakkında ek bilgi veya not eklemek için kullanılan, ana akışa dahil olmayan bağlantı çizgisidir.                                    |
| 10 | Çift Çizgili Dikdörtgen (Predefined Process / Alt Program):  | 10 |  Daha önceden tanımlanmış bir fonksiyonu veya başka bir akış şemasında detaylandırılmış bir alt süreci (sub-routine) çağırmak için kullanılır.         |
| 11 | Silindir (Database / Veri Deposu):                           | 11 |  Bilginin kalıcı olarak saklandığı bir veritabanını veya depolama birimini temsil eder.                                                                |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
NOT: 
 Paralelkenar -> Girdi / Çıktı (Sadece Almak ve Sunmak,Veri Alımı ve çıktı işlemleri için kullanılır.)
 Dikdörtgen   -> İşlem (Alınan Bilgiyi İşlemek ve Eyleme Dökmek)

-> Veri veya durum, akış şemasına dışarıdan alınır ya da dışarıya verilir; paralelkenar içinde işlenmez veya değiştirilmez.
-> Alınan bilgiyi işlemek ve eyleme dökmek için Dikdörtgen (İşlem) kullanılır.
"""


# ========================================================================================
# == BAB 1: PROBLEM ÇÖZME VE ALGORİTMA TEMELLERİ PROJELERİ (TEK-ÇİFT ANALİZİ PROJESİ) : ==
# ========================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ÖRNEK 1: Klavyeden girilen n sayısına kadar çiftleri toplayan, tekleri çarpan algoritmayı hem Algoritmik Doğal Dil ile hem de Pseudocode ile yazınız ve Akış Şeması şeklinde gösteriniz :
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
-------------------------------------------------------------------------------------------------------------------------------
| Adım No | Algoritmik Doğal Dil                                                    | Pseudocode (Sözde Kod)                  |
-------------------------------------------------------------------------------------------------------------------------------
|    1    | Başla                                                                   | Başla                                   | 
|    2    | Kullanıcıdan n sayısını al (n)                                          | Oku(n)                                  |
|    3    | Toplam=0, Carpim=1 değerlerini alalım                                   | Toplam=0, Carpim=1 olsun                |
|    4    | i = 1 olsun                                                             | i = 1 olsun                             |
|    5    | Eğer i > n ise 9. adıma git                                             | Eğer i > n ise git 9. adıma             |
|    6    | Eğer i'nin 2 ile bölümünden kalan 0 ise toplamın üstüne i sayısını ekle | Eğer i % 2 == 0 ise toplam = toplam + i |
|    7    | Değilse carpim = carpim * i                                             | Değilse carpim = carpim * i             |
|    8    | i'yi arttıralım (i++) ve 5. adıma dön                                   | Arttır i (i++) ve git 5. adıma          |
|    9    | Toplam ve carpim değerlerini ekrana yaz                                 | Yaz toplam, carpim                      |
|    10   | Bitir                                                                   | Bitir                                   |
-------------------------------------------------------------------------------------------------------------------------------

#----------------------
# AKIŞ ŞEMASI MANTIĞI :
#----------------------

-> Başla (Oval)
-> n (Paralelkenar - Giriş)
-> toplam=0, carpim=1, i=1 (Dikdörtgen - Başlatma)
-> Döngü Kontrolü: i <= n? (Eşkenar Dörtgen)
- HAYIR: (Döngü bitti) -> toplam ve carpim değerlerini yaz (Dalgalı Dörtgen/Paralelkenar) -> BİTİR (Oval).
- EVET: (İçeri gir) -> Alt adıma geç:
-> Karar: i % 2 == 0? (Eşkenar Dörtgen)
- EVET: toplam = toplam + i (Dikdörtgen)
- HAYIR: carpim = carpim * i (Dikdörtgen)
-> Artırım: i = i + 1 (Dikdörtgen)
-> Başa Dön: 4. adıma (Döngü kontrolüne) geri dön.
"""

# ===========================================================================================================================================================
"""                                                                                                                                                          
 Besmele ile, ilmin ilk kapısı olan 1. Bab’a besmeleyle kadem bastık.                                                                                          
 Zihni bulandıran karmaşayı (problemi) tefekkür süzgecinden geçirip, selametle amele ulaştıracak o müstakim yolu (algoritmayı) inşa etmeye niyet ettik.      
 Ve ilk örneğimizle başladık."                                                                                                                               
"""                                                                                                                                                             
# ===========================================================================================================================================================
