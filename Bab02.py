# ============================================================================================================================================
# == BAB 2: YAZILIM GELİŞTİRME TEMELLERİ VE PROGRAMLAMA DİLLERİ (CHAPTER 2: SOFTWARE DEVELOPMENT FUNDAMENTALS AND PROGRAMMING LANGUAGES ) : ==
# ============================================================================================================================================

"""
-> Algoritma: Belirli bir sorunu veya problemi çözmek için izlenen adım adım mantıksal yol. (Zihinsel yol haritası gibi).
-> Program: Herhangi bir elektronik cihaza (Akıllı saat, Bilgisayar, Cep Telefonu, Televizyon) işlem yaptırmak için yazılan komutlar dizisidir.
-> Program: Bir veya birkaç algoritma bir araya getirilerek bir gereksinimi karşılayan, programlama dili kullanılarak elde edilen çözüme "program" denir.
-> Programlama Dili: İnsanların bilgisayarlara ne yapacaklarını anlatmak için kullandığı yapay bir dildir.
-> Yazılım: Programların bir araya getirilerek bir bilişim tabanlı  otomasyon gerçekleştirmesine "yazılım" denir.
"""

#-----------------------------
# MAKİNE DİLİ (MACHINE CODE) :
#-----------------------------
"""
---------------------------
 Özellikleri ve Detayları :
---------------------------
-> Bir bilgisayarın merkezi işlem birimi (CPU) tarafından doğrudan yürütülen, ikili (binary) formattaki komutlar kümesidir.
-> İkili (Binary) Yapı: Sadece 0 ve 1’lerden oluşur. Bu rakamlar işlemci içindeki devrelerin "açık" veya "kapalı" olma durumunu temsil eder.
-> 0 ve 1'lerden oluşan bu sistem, aslında George Boole'ün cebirsel mantık sistemine ve Claude Shannon'un bu mantığı elektrik devrelerine uygulamasına dayanır.
-> 0 ve 1, aslında belirli voltaj aralıklarını temsil eder (Örn: 0V - 0.5V arası '0', 2.5V - 3.3V arası '1').
-> Tüm modern dijital elektroniğin ve yazılımın teorik temelidir.
-> En Düşük Seviye: Yazılım dünyasındaki hiyerarşinin en temelidir. İnsan dilinden en uzak, donanıma en yakın noktadır.
-> Donanım Bağımlılığı: Her işlemci mimarisinin (Örn: Intel x86, Apple M1 ARM) kendine has bir makine dili vardır. Bir işlemci için yazılan makine kodu diğeriyle çalışmayabilir.
-> Maksimum Performans: Herhangi bir yorumlama veya derleme süreci gerektirmediği için donanım üzerinde en yüksek hızda çalışır.
-> Zorluk Seviyesi: İnsanlar için okunması, yazılması ve hataların ayıklanması (debug) imkansıza yakındır.
-> Soyutlama Yoktur: Bellek adresleri ve işlemci kayıtçıları (registers) ile doğrudan çalışılır; hiçbir karmaşıklık gizlenmez.
-> Bugün yazdığımız tüm yüksek seviyeli diller (Python, C++, Java vb.), bilgisayarın çalıştırabilmesi için en nihayetinde Makine Diline dönüştürülmek zorundadır.

-> Donanım sadece 0 ve 1 anlar çünkü:
1-) Fiziksel olarak en kolay uygulanabilir sistemdir (açık/kapalı transistörler)
2-) Elektriksel gürültüye en dayanıklı sistemdir
3-) Boole cebiri ile mükemmel uyumludur

"""

#--------------------------------------------
# DİL SEVİYELERİ VE SOYUTLAMA (ABSTRACTION) :
#--------------------------------------------
"""
Hiyerarşi: Makine Dili -> Düşük Seviyeli Diller -> Orta Seviyeli Diller -> Yüksek Seviyeli Diller -> Çok Yüksek Seviyeli Diller

A) Makine Dilinden Uzaklaştıkça (Yüksek Seviyeli Diller):
---------------------------------------------------------
-> Soyutlama artar.
-> İnsan okunabilirliği artar.
-> Geliştirme hızı artar.
-> Kodun anlam katmanları artar.
-> Derleyiciye bağımlılık artar.
-> Donanım kontrolü azalır.
-> Hata yapma riski azalır.
-> Performans / Kaynak verimi azalır.
-> Kodun şeffaflığı azalır (Yani arkaplanda çok şey gizlenir).

B) Makine Diline Yaklaştıkça (Düşük Seviyeli Diller):
-----------------------------------------------------
-> Soyutlama azalır.
-> İnsan okunabilirliği azalır.
-> Geliştirme hızı azalır.
-> Kodun anlam katmanları azalır.
-> Derleyiciye bağımlılık azalır.
-> Donanım kontrolü artar.
-> Hata yapma riski artar.
-> Performans / Kaynak verimi artar.
-> Kodun şeffaflığı artar.
"""


#----------------------------------------------------
# DERLEYİCİ (COMPILER) VS YORUMLAYICI (INTERPRETER) :
#----------------------------------------------------
"""
--------------------------
 1. Derleyici (Compiler) :
--------------------------
-> Tüm kodu tek bir seferde makine diline çevirir.
-> Genelde daha hızlı çalışır (Önceden çevrilmiş olur).
-> Tüm hataları derleme aşamasında (Kod çalışmadan önce) gösterir.
-> Makine kodu üretir.
-> Platforma bağımlılık vardır.
-> C++, C, Rust, Go örnek dillerdir.

-------------------------------
 2. Yorumlayıcı (Interpreter) :
-------------------------------
-> Kodu satır satır okur ve anında çalıştırır.
-> Daha yavaş çalışır (Her satırı anlık yorumlar).
-> Hatalar çalışırken, satır satır ortaya çıkar.
-> Makine kodu üretmez. Doğrudan çalıştırır.
-> Platformdan bağımsızdır.
-> Python, JS, Ruby örnek dillerdir.

NOT:
-> Derleyici Hataları kod çalışmadan önce bulurken yorumlayıcı kod çalışırken buluyor. Bu detay önemli.
-> Önce bytecode'a derleme sonra yorumlama işlemi olur.
-> Yorumlayıcı (Interpreter): "Makine kodu üretmez" ifadesi 101 seviyesi için doğrudur.
-> Ancak teknik olarak modern yorumlayıcılar (JIT - Just-In-Time) çalışma anında kodun bazı kısımlarını makine koduna çevirebilir.


------------------------------------------
 ANLATIM REHBERİ: "AŞÇI VE TARİF" ÖRNEĞİ :
------------------------------------------
Diyelim ki elinizde yabancı dilde yazılmış bir yemek tarifi var:

-> Derleyici (Compiler): Tüm tarifin önceden Türkçeye çevrilip size verilmesi gibidir. 
   Mutfağa girdiğinizde sadece yemeği yapmaya odaklanırsınız (Hızlı çalışır), 
   ancak çeviride bir hata varsa mutfağa girmeden önce çevirmenin düzeltmesi gerekir.

-> Yorumlayıcı (Interpreter): Yanınızda bir çevirmenle mutfağa girmek gibidir. 
   Siz bir adım atarsınız, çevirmen o satırı o an çevirir. 
   Yemek yaparken çevirmeni beklemek zorunda kalırsınız (Daha yavaş), 
   ancak  mesela 5. adımda bir hata çıkarsa hatayı o an fark edip hemen düzeltebilirsiniz.
"""

#----------------------------------------
# NEDEN ÖNCE DERLEME, SONRA YORUMLAMA ? :
#----------------------------------------
"""
Python gibi diller "Hibrit" (Karma) bir yöntem kullanır. Bu sürecin iki temel sebebi vardır:

1. Platform Bağımsızlığı (Taşınabilirlik):
------------------------------------------
-> Eğer kod doğrudan makine diline derlenseydi, sadece o işlemci (Örn: Intel) için çalışırdı.
-> Önce Bytecode'a derlenir; bu sayede aynı kod Windows, Linux veya Mac fark etmeksizin 
   her yerde çalışabilir. "Bir kere yaz, her yerde çalıştır" mantığı budur.

2. Performans ve Güvenlik:
--------------------------
-> Kodun tamamını satır satır ham metin olarak okumak çok yavaştır.
-> Derleme aşaması kodu temizler, optimize eder ve hataları kontrol eder. 
-> Oluşan Bytecode, işlemcinin anlayabileceği formata çok yakındır ancak hala güvenli bir 
   sanal makine (PVM) içinde çalışır.

----------------------------------------------
 ANLATIM REHBERİ: "NOTER VE TERCÜMAN" ÖRNEĞİ :
----------------------------------------------
-> Derleme Aşaması (Noter Onayı): Yazdığınız dilekçeyi (kodunuzu) önce notere götürürsünüz. 
   Noter kağıdı inceler, hataları bulur ve "Resmi Ara Format" haline getirir. 
   Bu belge artık her devlet dairesinde (her işletim sisteminde) geçerlidir.

-> Yorumlama Aşaması (Gümrük Tercümanı): Noter onaylı bu belge gümrüğe gittiğinde, 
   oradaki görevli (Sanal Makine) belgeyi adım adım okur ve işlemi yapar. 
   Belge zaten onaylı ve optimize olduğu için işlem çok daha hızlı ve güvenli biter.
"""


#-------------------------------------
# ARA KOD (BYTECODE) VE SANAL MAKİNE :
#-------------------------------------
"""
-> Python, Java gibi dillerde önce bir "Ara Kod" (ByteCode) oluşur.
-> Bu ara kod, Sanal Makine (Python için PVM, Java için JVM) tarafından yorumlanarak çalıştırılır.
-> Bytecode'u makine koduna dönüştüren platformlara "Sanal Makine" (Virtual Machine) denir.
-> Sanal Makine: Yazılım aracılığıyla yaratılan, fiziksel bilgisayar gibi çalışan bir ortamdır.
-> Amaç: Bir programın farklı donanım ve işletim sistemlerinde sorunsuz çalışmasını sağlamaktır.
-> NOT: Önce Bytecode'a derleme, sonra yorumlama işlemi olur.

-> NOT: Akademideki klasik derleyici/yorumlayıcı ayrımı günümüzde tamamen keskin değildir. 
   Modern diller (Java, C#, Python gibi) genellikle önce bir ara koda (bytecode) derlenir, 
   ardından bu ara kod bir sanal makine üzerinde yorumlanır veya tam zamanında (JIT - Just In Time) 
   derlenerek makine koduna çevrilir. Bu hibrit yaklaşım, hem taşınabilirliği hem de performansı artırır.
"""


#-----------------------------------------
# TEMEL KAVRAMLAR (KÜTÜPHANE, SOYUTLAMA) :
#-----------------------------------------
"""
Kütüphane: Önceden yazılmış ve çok sık kullanılan kod parçacıklarını programın içine dahil ederek, o kod parçacıklarını kendiniz yazmışsınız gibi kullanabildiğiniz bir yapıdır.
Soyutlama: Karmaşık detayları gizleyerek ve yalnızca işlevselliği göstererek bir sistemin kullanımını basitleştirme sürecidir. (Nasıl çalıştığını değil, ne yaptığını göstermek).

-> Soyutlama detayları gizler ancak bir mühendis olarak alttaki detayları (bellek, CPU) tamamen unutmamalıyız; bazen sızıntılar (hatalar) oradan gelir.
"""

# =================================================================================================================================================================================
"""
"Elhamdülillah, 2. Bab’ın kapısını ilmin usulüne riayet ederek araladık; zihnimizdeki ham tefekkürü bir 'lisan' (programlama dili) ile ifade etmenin yollarını aradık.              
 Hakikati kodlara nakşetmek için gerekli olan temel kaideleri (yazılım temelleri), selim bir iradeyle amele dökülsün diye ilim defterimize kaydettik."      
"""
# =================================================================================================================================================================================