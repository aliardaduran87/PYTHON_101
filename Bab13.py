
# ========================================================================================
# == BAB 13: HATA YÖNETİMİ VE İSTİSNALAR (CHAPTER 13: ERROR HANDLING AND EXCEPTIONS) : ==
# ========================================================================================

"""
-> Program yazarken iki tür hata ile karşılaşırız. Bunları iyi ayırt etmek gerekir.
"""

# ------------------------------------------
# 1. SÖZ DİZİMSEL HATALAR (SYNTAX ERRORS) :
# ------------------------------------------
"""
-> Kodun Python dil kurallarına (gramer) uygun yazılmamasından kaynaklanır.
-> Python yorumlayıcısı (interpreter) kodu çalıştırmadan önce analiz eder; eğer kural ihlali varsa kod hiç başlatılmaz.
-> Çözüm: Yazım hatalarını düzeltmek (iki nokta unutmak, parantez kapatmamak, yanlış girintileme gibi).
"""
# Örnek (çalışmaz):
# if True print("Merhaba")   # SyntaxError: invalid syntax

# ----------------------------------------------------------
# 2. İSTİSNALAR (ÇALIŞMA ZAMANI HATALARI) - RUNTIME ERRORS :
# ----------------------------------------------------------
"""
-> Kodun söz dizimi doğrudur, ancak çalışma esnasında beklenmedik bir durum oluşur.
-> Bu hatalar yakalanmazsa programı durdurur (crash).
-> try-except mekanizması işte bu hataları yönetmek için kullanılır.
"""

# ------------------------------------------
# 2.1. EN SIK KARŞILAŞILAN İSTİSNA TÜRLERİ :
# ------------------------------------------
"""
-------------------------------------------------------------------------------
| İstisna Adı        | Açıklama                                               |
|--------------------|---------------------------------------------------------
| ValueError         | Uygun olmayan değer (int("abc") gibi)                  |
| ZeroDivisionError  | Bir sayının 0'a bölünmesi                              |
| IndexError         | Liste/demet sınırları dışına çıkma                     |
| TypeError          | Uyumsuz veri türleri arasında işlem                    |
| NameError          | Tanımlanmamış değişken kullanımı                       |
| KeyError           | Sözlükte olmayan anahtar çağrılması                    |
| FileNotFoundError  | Var olmayan dosya açılmaya çalışılması                 |
-------------------------------------------------------------------------------

-> Eğer daha fazla hata türüne bakmak isterseniz https://docs.python.org/3/library/exceptions.html sitesine gidebilirsiniz.
"""
# Örnek hatalar (açıklama satırındayken çalışmaz):
# int("abc")          -> ValueError
# 10 / 0              -> ZeroDivisionError
# ["a"][5]            -> IndexError
# "yaş" + 30          -> TypeError
# print(bilinmeyen)   -> NameError
# {"ad":"Ali"}["yas"] -> KeyError

# --------------------------------------------------------------
# 3. HATA YAKALAMA MEKANİZMASI (TRY - EXCEPT - ELSE - FINALLY) :
# --------------------------------------------------------------
"""
------------------------------------------------------------------------------
| try     : Riskli kod buraya yazılır.                                        |
| except  : Hata oluşursa burası çalışır.                                     |
| else    : Hata oluşmazsa burası çalışır (opsiyonel).                        |
| finally : Hata olsa da olmasa da her zaman çalışır (opsiyonel).             |
------------------------------------------------------------------------------
"""

# ÖRNEK: Gelişmiş Hesap Makinesi
def gelismis_hesap_makinesi():
    try:
        sayi_1 = int(input("İlk sayıyı giriniz: "))
        sayi_2 = int(input("İkinci sayıyı giriniz: "))
        bolum_sonucu = sayi_1 / sayi_2

    except ValueError:
        print("Hata: Lütfen sadece tam sayı giriniz!")
    except ZeroDivisionError:
        print("Hata: Bir sayı sıfıra bölünemez!")
    except Exception as genel_hata:
        print(f"Beklenmedik bir hata oluştu: {genel_hata}")
    else:
        print(f"İşlem başarılı! Sonuç: {bolum_sonucu}")
    finally:
        print("Hata yönetimi bloğu tamamlandı.")

# Hata yakalarken özelden genele doğru sıralama yapılması gerekir. Örneğin önce ValueError, sonra Exception yazılmalı. Aksi halde genel except özel olanı gölgeler.

# -------------------------------------
# 4. KENDİ HATAMIZI FIRLATMAK (RAISE) :
# -------------------------------------
"""
-> Bazen Python için hata olmayan bir durumu, kendi iş mantığımız gereği hata olarak değerlendirmek isteriz. Bunun için 'raise' kullanırız.
"""

# Örnek 1: Bakiye kontrolü
def bakiye_kontrol(miktar):
    mevcut_bakiye = 500
    if miktar > mevcut_bakiye:
        raise Exception(f"Yetersiz bakiye! Mevcut: {mevcut_bakiye}, İstenen: {miktar}")
    else:
        print("Ödeme başarılı.")

# Örnek 2: Yaş doğrulama (özel hata türü ile)
def yas_dogrula(yas):
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")
    elif yas > 120:
        raise OverflowError("Bu yaş bir insan için çok büyük!")
    return True

# ----------------------------
# 5. İDDİA ETMEK (ASSERTION) :
# ----------------------------
"""
-> assert ifadesi, bir koşulun doğru olduğunu iddia eder.
-> Koşul yanlışsa AssertionError fırlatır. Genelde test amaçlı kullanılır.
"""
def maas_hesapla(saat, ucret):
    assert saat > 0, "Çalışma saati 0 veya negatif olamaz!"
    return saat * ucret

# ------------------------------------------
# 6. ÖZET: HATA YÖNETİMİNDE ALTIN KURALLAR :
# ------------------------------------------
"""
1.  Hata oluşabilecek kodları try içine al.
2.  Genel except: kullanma; mümkünse özel hata türlerini yakala.
3.  'Exception as e' ile hatanın orijinal mesajını okuyabilirsin.
4.  Programı çökertme ama hatayı da gizleme; mutlaka kullanıcıya anlaşılır mesaj ver.
5.  finally'i dosya, veritabanı bağlantısı gibi kaynakları kapatmak için kullan.
6.  raise ile kendi iş kurallarını hata olarak tanımla.
7.  Kullanıcıya teknik hata mesajı gösterme; onun anlayacağı dille uyar.
8.  Boş except (pass) kullanma; hatayı bilmiyorsan en azından log tut.
9.  İç içe try-except'leri karmaşık işlemler için kullanabilirsin.
10. Hata yönetimi performansı az da olsa etkiler; sadece gerekli yerlerde kullan.
"""

# ---------------------------------
# 7. TEKNİK KARŞILAŞTIRMA TABLOSU :
# ---------------------------------
"""
---------------------------------------------------------------------
| Blok/Anahtar | Ne Zaman Çalışır?                    | Zorunlu mu? |
|--------------|--------------------------------------|-------------|
| try          | Her zaman ilk olarak çalışır         | Evet        |
| except       | Sadece try'da hata oluşursa          | Evet*       |
| else         | Sadece try'da hata oluşmazsa         | Hayır       |
| finally      | Hata olsa da olmasa da her zaman     | Hayır       |
| raise        | Kodun istediğimiz yerinde            | Hayır       |
---------------------------------------------------------------------
* En az bir except bloğu olmalıdır.
"""

#--------------------------------------------------------
# Örnek 1: Liste İçindeki Numerik Verilerin Ayıklanması :
#--------------------------------------------------------
liste = ["345","sadas","324a","14","kemal"]
for eleman in liste:
    try:
        eleman = int (eleman)
        print(eleman)
    except:
        pass

    
#-----------------------------------------------------
# Örnek 2: Çift Sayı Sorgusu ve Şartlı Hata Fırlatma :
#-----------------------------------------------------
def cift_mi(sayi):
    if (sayi % 2 == 0):
        return sayi
    else: 
        raise ValueError
liste = [34,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass


#---------------------------------------------------
# Örnek 3: Gelişmiş Hata Ayıklayan Hesap Makinesi  :
#---------------------------------------------------

def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölme hatası!")
    return a / b

def debug_yaz(debug_aktif, mesaj, seviye="BİLGİ"):
    """Debug modu açıksa mesajı yazdır."""
    if debug_aktif:
        print(f"[DEBUG - {seviye}] {mesaj}")

def hesap_makinesi(debug_modu=False):
    """
    Ana hesap makinesi fonksiyonu.
    debug_modu = True ise işlem adımları ayrıntılı gösterilir.
    """
    print("Basit Hesap Makinesi (çıkmak için 'çıkış' yazın)")
    print("İşlemler: + (toplama), - (çıkarma), * (çarpma), / (bölme)")

    while True:
        try:
            # Kullanıcıdan işlem seçimi
            islem = input("\nİşlem seçin (+, -, *, / veya 'çıkış'): ").strip()
            if islem.lower() == 'çıkış':
                debug_yaz(debug_modu, "Kullanıcı çıkış yaptı.", "ÇIKIŞ")
                break

            if islem not in ('+', '-', '*', '/'):
                print("Geçersiz işlem! Lütfen +, -, *, / veya 'çıkış' yazın.")
                debug_yaz(debug_modu, f"Geçersiz işlem girildi: {islem}", "UYARI")
                continue

            # İki sayı al
            try:
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Hata: Geçerli bir sayı girmediniz!")
                debug_yaz(debug_modu, "Sayısal dönüşüm hatası (ValueError)", "HATA")
                continue

            debug_yaz(debug_modu, f"İşlem: {sayi1} {islem} {sayi2}", "İŞLEM")

            # İşlemi gerçekleştir
            if islem == '+':
                sonuc = topla(sayi1, sayi2)
            elif islem == '-':
                sonuc = cikar(sayi1, sayi2)
            elif islem == '*':
                sonuc = carp(sayi1, sayi2)
            elif islem == '/':
                try:
                    sonuc = bol(sayi1, sayi2)
                except ZeroDivisionError as e:
                    print(f"Hata: {e}")
                    debug_yaz(debug_modu, f"Sıfıra bölme denemesi: {sayi1} / {sayi2}", "HATA")
                    continue

            print(f"Sonuç: {sonuc}")
            debug_yaz(debug_modu, f"Sonuç hesaplandı: {sonuc}", "SONUÇ")

        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")
            debug_yaz(debug_modu, f"Genel hata: {e}", "HATA")

# ============================================================================================================
"""
 "Elhamdülillah, 13. Bab ile kodumuzun beklenmedik çıkmazlarını (hata ve istisnaları) ilimle kuşattık.
 'Hatasız kod olmaz' düsturunca, bu çıkmazları birer rahmete dönüştürmenin yollarını tahsil ettik.
 Try-except kalkanlarıyla kodumuzu muhafaza altına aldık; raise ile kendi sınırlarımızı çizdik.
 Bu bab, programın selametle yoluna devam etmesi için bir sigortadır.
"""
# ============================================================================================================
#  BAB 13 (HATA YÖNETİMİ VE İSTİSNALAR) PROJE LİSTESİ :                                                      |
# ============================================================================================================
#  ÖRNEK 1 : Liste İçindeki Numerik Verilerin Ayıklanması (pass ile hata yutma)                              |
#  ÖRNEK 2 : Çift Sayı Sorgusu ve Şartlı Hata Fırlatma (raise kullanımı)                                     |
#  ÖRNEK 3 : Gelişmiş Hata Ayıklayan Hesap Makinesi (try-except-else-finally ve özel hata yakalama)          |
# ============================================================================================================