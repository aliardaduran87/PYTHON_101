# =================================================
# == BAB 14: DOSYA İŞLEMLERİ (FILE OPERATIONS) : ==
# =================================================

"""
Dosya işlemleri, bir programın kalıcı depolama (sabit disk, SSD) ile veri alışverişi yapmasını sağlar.
Bellek (RAM) geçicidir; bilgisayar kapanınca içindeki veriler kaybolur. Dosyalar ise verileri kalıcı olarak saklamamıza yarar.

Bu bölümde:
- Dosya açma, okuma, yazma, kapama
- Farklı dosya modları (okuma, yazma, ekleme)
- Metin (text) ve ikili (binary) dosyalar
- 'with' anahtar kelimesi ile otomatik kaynak yönetimi
- Dosya konumlandırma (seek, tell)
- Dizin işlemleri (os modülü ile dosya yönetimi)
"""

# ----------------------------------------
# 1. DOSYA AÇMA VE KAPAMA (OPEN / CLOSE) :
# ----------------------------------------

# open() fonksiyonu ile dosya açılır. İlk parametre dosya yolu, ikinci parametre mod'dur.
# Modlar:
# "r"  : Okuma (varsayılan) - dosya yoksa hata verir.
# "w"  : Yazma - dosya varsa içeriği silinir, yoksa oluşturulur.
# "a"  : Ekleme - dosya sonuna ekleme yapar, yoksa oluşturulur.
# "x"  : Oluşturma - dosya zaten varsa hata verir.
# "b"  : Binary (ikili) mod - resim, video gibi dosyalar için (rb, wb, ab)
# "t"  : Metin modu (varsayılan) - rt, wt, at

# Örnek: Yazma modunda dosya açma
dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("Merhaba dosya!\n")
dosya.write("İkinci satır.")
dosya.close()  # Dosyayı kapatmak önemlidir (kaynakları serbest bırakır)

# ------------------------------------------------------------------
# 2. 'with' ANAHTAR KELİMESİ (BAĞLAM YÖNETİCİSİ - CONTEXT MANAGER) :
# ------------------------------------------------------------------
"""
with bloğu kullanıldığında, dosya otomatik olarak kapatılır (hata olsa bile).
Bu yöntem daha güvenli ve Pythonic'tir.
"""
with open("deneme.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)
# Bloktan çıkınca dosya otomatik kapanır.

# ---------------------------
# 3. DOSYA OKUMA YÖNTEMLERİ :
# ---------------------------

# read()         -> Tüm dosyayı tek bir string olarak okur
# read(n)        -> n karakter okur (binary modda n byte)
# readline()     -> Bir satır okur (bir sonraki çağrıda sonraki satır)
# readlines()    -> Tüm satırları bir liste olarak okur

with open("deneme.txt", "r", encoding="utf-8") as f:
    # 1. Tüm içerik
    icerik = f.read()
    print("--- Tüm içerik ---")
    print(icerik)

with open("deneme.txt", "r", encoding="utf-8") as f:
    # 2. Satır satır okuma (hafif büyük dosyalar için idealdir)
    print("--- Satır satır ---")
    for satir in f:
        print(satir, end="")  # Her satır zaten \n içerir

with open("deneme.txt", "r", encoding="utf-8") as f:
    # 3. readlines() ile liste
    satirlar = f.readlines()
    print("--- readlines ile ---")
    print(satirlar)

# ---------------------------
# 4. DOSYA YAZMA YÖNTEMLERİ :
# ---------------------------

# write(metin)        -> Metni dosyaya yazar (kaç karakter yazıldığını döndürür)
# writelines(liste)   -> Listeyi dosyaya yazar (satır sonları otomatik eklenmez)

with open("yeni_dosya.txt", "w", encoding="utf-8") as f:
    f.write("Birinci satır\n")
    f.write("İkinci satır\n")
    f.writelines(["Üçüncü satır\n", "Dördüncü satır"])

# Ekleme modu (append)
with open("yeni_dosya.txt", "a", encoding="utf-8") as f:
    f.write("\nBu satır sonradan eklendi.")

# ------------------------
# 5. DOSYA KONUMLANDIRMA :
# ------------------------

# tell() -> Dosya içinde bulunulan konumu (byte cinsinden) döndürür.
# seek(offset, from) -> Konumu değiştirir. from=0: başlangıç, 1: bulunduğun yer, 2: son

with open("deneme.txt", "r", encoding="utf-8") as f:
    print(f.tell())        # 0 (başlangıç)
    f.seek(5)              # 5. byte'a git
    print(f.read(10))      # 10 karakter oku
    print(f.tell())        # okuduktan sonraki konum

# -----------------------------------
# 6. İKİLİ (BINARY) DOSYA İŞLEMLERİ :
# -----------------------------------
"""
Resim, ses, video gibi dosyalar binary modda açılır.
Okuma ve yazma byte dizileri (bytes) ile yapılır.
"""

# Örnek: Bir resim dosyasını kopyalama
with open("resim.jpg", "rb") as kaynak:
    with open("resim_kopya.jpg", "wb") as hedef:
        hedef.write(kaynak.read())  # Dikkat: Büyük dosyalarda bellek sorunu olabilir
        # Daha iyisi: parça parça kopyalamak
        # while True:
        #     parca = kaynak.read(4096)  # 4KB'lık parçalar
        #     if not parca:
        #         break
        #     hedef.write(parca)

# -----------------------------------------
# 7. DOSYA VE DİZİN İŞLEMLERİ (OS MODÜLÜ) :
# -----------------------------------------

import os

# Dosya var mı kontrolü
if os.path.exists("deneme.txt"):
    print("Dosya mevcut.")
else:
    print("Dosya yok.")

# Dosya silme
os.remove("yeni_dosya.txt")   # Dosya yoksa hata verir

# Dosya adı değiştirme / taşıma
os.rename("deneme.txt", "eski_deneme.txt")

# Dizin oluşturma
os.makedirs("klasor/alt_klasor", exist_ok=True)

# Dizin içindekileri listeleme
print(os.listdir("."))

# Dizin silme (boş olmalı)
os.rmdir("klasor/alt_klasor")   # Sadece alt klasörü siler

# Dizin ve içindeki her şeyi silme (shutil kullanılır)
import shutil
shutil.rmtree("klasor")   # Dikkatli kullanın!

# --------------------
# 8. PRATİK ÖRNEKLER :
# --------------------

# ÖRNEK 1: Kullanıcıdan alınan bilgileri dosyaya kaydetme
def kullanici_kaydet():
    with open("kullanicilar.txt", "a", encoding="utf-8") as f:
        ad = input("Adınız: ")
        soyad = input("Soyadınız: ")
        f.write(f"{ad},{soyad}\n")
    print("Kullanıcı kaydedildi.")

# ÖRNEK 2: CSV benzeri bir dosyayı okuyup işleme
def kullanicilari_listele():
    try:
        with open("kullanicilar.txt", "r", encoding="utf-8") as f:
            for satir in f:
                satir = satir.strip()
                if satir:
                    ad, soyad = satir.split(",")
                    print(f"Ad: {ad}, Soyad: {soyad}")
    except FileNotFoundError:
        print("Henüz kayıtlı kullanıcı yok.")

# ÖRNEK 3: Büyük bir dosyayı satır satır işleme (log analizi gibi)
def log_analiz(dosya_adi, aranan_kelime):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            for satir in f:
                if aranan_kelime in satir:
                    print(satir, end="")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

# -----------------
# 9. ÖZET TABLOSU :
# -----------------
"""
-------------------------------------------------------------------
| Mod              | Açıklama                                     |
-------------------------------------------------------------------
| "r"              | Okuma (varsayılan). Dosya yoksa hata.        |
| "w"              | Yazma. Dosya varsa içeriği silinir.          |
| "a"              | Ekleme. Dosya sonuna yazar.                  |
| "x"              | Oluşturma. Dosya varsa hata.                 |
| "rb", "wb", ...  | Binary mod (resim, video).                   |
| "r+", "w+"       | Okuma + yazma (dikkatli kullanılmalı).       |
-------------------------------------------------------------------

-------------------------------------------------------------------
| Fonksiyon        | Açıklama                                     |
-------------------------------------------------------------------
| read()           | Tüm dosyayı okur.                            |
| readline()       | Bir satır okur.                              |
| readlines()      | Tüm satırları liste olarak okur.             |
| write()          | String yazar.                                |
| writelines()     | Liste yazar (satır sonları eklenmez).        |
| tell()           | Mevcut konumu verir.                         |
| seek(offset)     | Konumu değiştirir.                           |
| close()          | Dosyayı kapatır (with ile otomatik).         |
-------------------------------------------------------------------
"""

# --------------------
# 10. ALTIN KURALLAR :
# --------------------
"""
1.  Dosyayı açtıktan sonra mutlaka kapatın. (with kullanarak garantiye alın.)
2.  Dosya yolu yazarken işletim sistemine dikkat edin: Windows'ta '\' kullanılır, ama Python'da r"..." veya "/" tercih edin.
3.  Encoding (karakter kodlaması) belirtmeyi unutmayın (özellikle Türkçe karakterler için 'utf-8').
4.  Büyük dosyaları okurken read() yerine satır satır veya parça parça okuyun (bellek tasarrufu).
5.  Dosya işlemleri sırasında hata oluşabileceğini unutmayın; try-except ile koruyun.
6.  Geçici dosyalar için tempfile modülünü araştırın.
7.  Dizin işlemlerinde os ve shutil modüllerini kullanın.
8.  Dosya silme ve taşıma işlemlerini dikkatli yapın; geri dönüşü olmayabilir.
9.  with bloğu dışında dosya nesnesi kullanmayın; kapalı dosyaya erişim hata verir.
10. Farklı modları (r+, w+) karıştırmayın; basit işler için ayrı ayrı kullanın.
"""

# ==========================================================
# == BAB 14: DOSYA İŞLEMLERİ PROJELERİ (FILE OPERATIONS): ==
# ==========================================================

# -----------------------------------------------------
# ÖRNEK 1: Öğrenci Bilgilerini Dosyaya Yazma ve Okuma :
# -----------------------------------------------------
# Amaç: Kullanıcıdan alınan öğrenci bilgilerini (isim, not)
#        "ogrenciler.txt" dosyasına satır satır yazmak ve
#        ardından dosyayı okuyup ekrana listelemek.

def ogrenci_kaydet_ve_oku():
    dosya_adi = "ogrenciler.txt"
    
    # Yazma işlemi (append modu - ekleme)
    with open(dosya_adi, "a", encoding="utf-8") as f:
        while True:
            isim = input("Öğrenci adı (çıkmak için 'q' girin): ")
            if isim.lower() == 'q':
                break
            notu = input("Notu: ")
            f.write(f"{isim},{notu}\n")
    
    # Okuma işlemi
    print("\n--- Kayıtlı Öğrenciler ---")
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            isim, notu = satir.strip().split(',')
            print(f"Öğrenci: {isim}, Notu: {notu}")

# ogrenci_kaydet_ve_oku()  # Çalıştırmak için yorumu kaldır


# ---------------------------------------------------------
# ÖRNEK 2: Büyük Dosyayı Satır Satır Okuma (Bellek Dostu) :
# ---------------------------------------------------------
# Amaç: Çok büyük bir log dosyasını satır satır okuyarak
#        içinde "ERROR" geçen satırları ayrı bir dosyaya yazmak.

def hata_satirlarini_ayikla(kaynak_dosya, hedef_dosya):
    try:
        with open(kaynak_dosya, "r", encoding="utf-8") as kaynak, \
             open(hedef_dosya, "w", encoding="utf-8") as hedef:
            
            for satir_no, satir in enumerate(kaynak, 1):
                if "ERROR" in satir:
                    hedef.write(f"{satir_no}: {satir}")
        print(f"Hata satırları {hedef_dosya} dosyasına yazıldı.")
    except FileNotFoundError:
        print(f"{kaynak_dosya} bulunamadı!")

# hata_satirlarini_ayikla("buyuk_log.txt", "hatalar.txt")


# ------------------------------------------------------------
# ÖRNEK 3: Dosya İçinde Belirli Bir Konuma Gitme (seek/tell) :
# ------------------------------------------------------------
# Amaç: Bir dosyanın 10. baytından itibaren 20 baytlık kısmını okumak.

def dosyadan_bolum_oku(dosya_adi, baslangic=10, uzunluk=20):
    try:
        with open(dosya_adi, "rb") as f:  # ikili mod
            f.seek(baslangic)
            veri = f.read(uzunluk)
            print(f"Okunan veri (bayt {baslangic}-{baslangic+uzunluk}):")
            print(veri)
            print(f"Şu anki konum: {f.tell()}")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

# dosyadan_bolum_oku("test.bin", 10, 20)


# -----------------------------------------------------------------
# ÖRNEK 4: os Modülü ile Klasör Gezintisi ve Dosya İstatistikleri :
# -----------------------------------------------------------------
# Amaç: Belirtilen bir klasördeki tüm .txt dosyalarını bulup
#        her birinin boyutunu ve son değiştirilme tarihini listelemek.

import os
import time

def txt_dosyalarini_listele(klasor_yolu):
    if not os.path.exists(klasor_yolu):
        print("Klasör bulunamadı!")
        return
    
    print(f"\n{klasor_yolu} içindeki .txt dosyaları:")
    for dosya in os.listdir(klasor_yolu):
        if dosya.endswith(".txt"):
            tam_yol = os.path.join(klasor_yolu, dosya)
            boyut = os.path.getsize(tam_yol)
            mtime = os.path.getmtime(tam_yol)
            tarih = time.ctime(mtime)
            print(f"{dosya} - {boyut} bayt - Son değişiklik: {tarih}")

# txt_dosyalarini_listele(".")  # Bulunulan klasör


# ---------------------------------------------
# ÖRNEK 5: pathlib ile Modern Dosya İşlemleri :
# ---------------------------------------------
# Amaç: pathlib kullanarak "veri" klasörü oluşturmak, içine bir metin dosyası
#        yazmak, dosyayı okuyup ekrana basmak ve sonunda dosyayı silmek.

from pathlib import Path

def pathlib_ornek():
    # Klasör oluştur
    klasor = Path("veri")
    klasor.mkdir(exist_ok=True)
    
    # Dosya yolu
    dosya = klasor / "notlar.txt"
    
    # Yazma
    dosya.write_text("Python dosya işlemleri\npathlib çok kullanışlı!", encoding="utf-8")
    
    # Okuma
    icerik = dosya.read_text(encoding="utf-8")
    print("Dosya içeriği:")
    print(icerik)
    
    # Dosyayı sil
    dosya.unlink()
    print(f"{dosya} silindi.")
    
    # Klasörü sil (içi boşsa)
    klasor.rmdir()
    print(f"{klasor} silindi.")

# pathlib_ornek()


# ==============================================================================================================
#  BAB 14: DOSYA İŞLEMLERİ - PROJE LİSTESİ (PROJECTS ON FILE OPERATIONS)                                       |
# ==============================================================================================================
#  ÖRNEK 1 : Öğrenci Bilgilerini Dosyaya Yazma ve Okuma (Temel Dosya G/Ç)                                      |
#  ÖRNEK 2 : Büyük Dosyayı Satır Satır Okuma (Bellek Dostu Log Analizi)                                        |
#  ÖRNEK 3 : seek/tell ile Dosya İçinde Gezinme (Rastgele Erişim)                                              |
#  ÖRNEK 4 : os Modülü ile Klasör Gezintisi ve Dosya İstatistikleri (Dizin Tarama)                             |
#  ÖRNEK 5 : pathlib ile Modern Dosya İşlemleri (Nesne Tabanlı Yaklaşım)                                       |
# ==============================================================================================================

# ==============================================================================================================================
""" 
 Elhamdülillah, 14. Bab ile dosya işlemlerinin ilmine vakıf olduk; veriyi kalıcı kılmanın, diske hükmetmenin yollarını öğrendik.
 Böylece Python 101 yolculuğumuzun sonuna geldik. Bu on dört bab boyunca:
 
 -------------------------------------------------
 ALGORİTMA VE PROGRAMLAMAYA GİRİŞ-1 (PYTHON_101) :
 -------------------------------------------------

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

 Her bir bab, ilmin amele dönüşmesi için çaba gösterdiğimiz birer durak oldu. 
 Şimdi elde ettiğimiz bu birikimle, daha büyük projelere, daha karmaşık problemlere yelken açabiliriz.
 
 Unutmayalım: "İlim ilim bilmektir, ilim kendin bilmektir." Öğrenmek bitmeyen bir yolculuktur.
 Python 101'i tamamladık ama yazılım dünyasında keşfedilecek daha nice okyanuslar var.
 
 Tüm babların sonunda yaptığımız gibi, bu son babı da bir dua ile taçlandıralım:
 
 Rabbimiz, ilmimizi artır, bizleri faydalı ilimle amel edenlerden eyle. 
 Bu mütevazı çalışmayı, öğrenmeye gönül vermiş tüm kardeşlerimize faydalı kıl.

 Daha iyi öğrenmek eksikleri kapatmak için Python'un ana sitesinden bakabilirsiniz. 
 # https://docs.python.org/3/tutorial/index.html

 PYTHON_101 Projesi 9470 satırdan  ve 102 tane örnekten oluşmaktadır.
 
 # PYTHON_101 serisi tamamlanmıştır.
 # Tarih:  17 Şubat 2026
"""
# ==============================================================================================================================