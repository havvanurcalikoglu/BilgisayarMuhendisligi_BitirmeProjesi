# Bilgisayar-Muhendisligi-Bitirme-Projesi 1.Rapor
## Araçların Çevresinde Tehlike Oluşturabilecek Varlıkların Görüntü İşleme ile Tespit Edilmesi

**1- PROJE ÖZETİ**

Bu projede hedef, kameralardan elde edilen araç görüntüleri izlenerek, araç etrafında bulunan insan, hayvan veya nesnelerin Görüntü İşleme yöntemleri ile tespit edilmesidir. Dijital görüntüler alınarak, nesne tanıma ile yazılım tabanlı olarak çalışır. Nesne tespit ve tanıma süreçleri veri girişi, veri ön işleme ve aşamaları, öznitelik çıkarımı ve öz nitelik seçimi, tanımlama aşamaları altında farklı algoritmalar yardımıyla çözüm bulmaktadır. Projeye göre değişik uygulamaları olup, uygulamaya özel algoritma ve donanım yapısının bir araya getirilmesi ile oluşturulan bir sistemdir.Aynı zamanda araçların tespiti ve sınıflandırılması yapılır.

Araçların etrafında  tehlike oluşturabilecek varlıkların görüntülerden tespitiyle de aslında aracın ve çevresinin güvenliği sağlanmış olur.Sürücüye, aracın çevresi fark ettirilir. <br/>

Ülkemizde her geçen gün saatte 27 trafik kazası meydana geliyor. Bu kazalarda günde ortalama 5 - 20 kişi ölüyor, 200’e yakın kişi de yaralanıyor. 
Yıl bazında yaşanan kazaların oranlarını aşağıda görebilirsiniz: <br/>
•	Araca yandan çarpma ya da çarpışma (%29,67) <br/>
•	Yayaya çarpma (%16,64)   <br/>
•	Araca arkadan çarpma (%9,86)  <br/>
•	Sabit cisme çarpma (%9,32)     <br/>
•	Duran araca çarpma (%2,49)    <br/>
•	Aracın hayvana çarpması (%0,47)   <br/>

Sürücü dikkatsizliği, biliçsizlik, aşırı hız vs. gibi sebeplerden kaynaklanan ölümleri göz ardı etmeyerek, canlı yaşamını korumak ve sürücüye güvenli, kazasız bir yolculuk sağlamak amaçlanır.

**2- PROJE ARKA PLANI**

Birebir aynı ürünü görmesem de benzer çalışmaları inceledim. Nesne tanıma, araç tespiti, plaka tanıması gibi çalışmaları benzer ürünlere örnek verebilirim.
Araçların renk tespiti, hız tespiti, sayımı, sınıflandırılması; Nesne tespiti, nesne tanıması,yüz tanıması gibi yapılmış projeler bulunmaktadır.

Benim projemin yapılan projelerden farklılığı ise; ele alınan konunun amacı, aracın sadece renginin, tipinin belirlenmesi, aracın tanınması değil; aynı zamanda etrafta bulunan canlı veya cansız varlıkların da tespitinin yapılması ve bunun sürücüye fark ettirilmesidir.Burada hem araçlar hem de araçların etrafındaki nesneler üzerinde çalışacağım.
<br/>
<br/>

##### Örnek bir nesne tespiti çalışması
![Örnek bir nesne tespiti çalışması](https://github.com/OlafenwaMoses/ImageAI/raw/master/data-images/video1.jpg)  

<br/>
<br/>

##### Örnek bir plaka tanıma sistemi
![Örnek bir plaka tanıma sistemi](https://www.desialarmi.com/wp-content/uploads/2016/08/plaka-tan%C4%B1ma-sistemleri-1024x576.jpg)


<br/>
<br/>

##### Örnek bir araç takibi, sayımı ve renk tespiti
![Örnek bir araç takibi, sayımı ve renk tespiti](https://user-images.githubusercontent.com/22610163/36344830-095cc4ec-1431-11e8-8e57-976c40d87cf9.gif)


<br/>
<br/>

**3- KULLANILACAK TEKNOLOJİLER**

Projemi Python Jupyter Notebook ortamında geliştirip; Tensorflow, OpenCV, Scikit-learn, Numpy,Keras kütüphanelerinden faydalanacağım. <br/>
Veri seti için hazır kaynak kullanmayı planlıyorum.Ancak test aşamasında, İstanbul'da trafiğe açık alanlardan da çektiğim görüntüleri kullanabilirim. <br/>
Yapay zeka programlama için herhangi bir dil kullanılabilir fakat burada bir tek dilden veya herhangi bir dilden bahsetmek yerine, geliştirilmek istenen yazılım özelinde karşılaşılacak sorunlara uygun dil seçmek en mantıklısı olacaktır.Python kullanmamın sebebi de, diğer dillere göre oldukça kolay yazımı olması, bunun yanında diğer dillere kıyasla daha kısa sürede yazılması, literatür taramasında oldukça fazla açık kaynak kod bulunması ve güncel yapay zeka projelerinin yine Python'da yazılmasından dolayıdır.Ayrıca Python’un kullanıcılarına sunduğu geniş kütüphanesi de tercih sebeplerinden bir tanesidir. <br/>
Projemi kodlarken Python bilgisi yanında, görüntü işleme ve python kütüphaneleri kullanacağımdan Udemy, Coursera, Youtube, Github gibi platformlardan faydalanacağım.Ayrıca lisansta aldığım Makine Öğrenmesi ve Görüntü İşleme derslerinin yanı sıra Stanford Üniversitesi gibi üniversitelerin online derslerini takip etmeyi planlıyorum.



**4- İŞ BÖLÜMÜ PLANLAMA**

Projeyi tek başıma yürüteceğimden tüm iş paketlerinden ben sorumluyum. <br/>
İş bölümünün zamanlaması Mayıs 2021’de bitmek üzerine planlanmıştır.

![Proje planlama](https://user-images.githubusercontent.com/56633000/99888902-5c7bd000-2c61-11eb-80c7-67592ef40f8b.PNG)


<br/>
<br/>

![Proje planlama](https://user-images.githubusercontent.com/56633000/99888936-a5cc1f80-2c61-11eb-934a-10528a2ed078.PNG)

<br/>
<br/>

**5- HEDEFLENEN ÇIKTILAR**

Hedeflenen proje, araç ve araç çevresini tespit eden bir masaüstü uygulamasıdır. <br/>
Projeyi Windows işletim sistemi üzerinde çalıştıracağım. 
(Daha sonradan Linux ile de yürütülebilir.) <br/>
Nesne tanıma, görüntülerdeki veya videolardaki nesneleri tanımlamak için bir bilgisayarlı görü tekniğidir. Nesne tanıma, derin öğrenme ve makine öğrenme algoritmalarının önemli bir çıktısıdır. Tensorflow , veri akış grafiklerini kullanarak sayısal hesaplama için açık defter bir yazılım kitaplığıdır. Grafikteki düğümler matematiksel temsil sırasında, grafik kenarları aralarında iletişim kuran çok boyutlu veri dizilerini temsil eder.OpenCV, açık kaynak bir bilgisayarla görme ve makine öğrenimi yazılım kitaplığıdır. OpenCV, bilgisayarla görme uygulamaları için ortak bir altyapı sağlamak ve ticari ürünlerde makine algısının sağlanması hızlandırmak için kullanılır. <br/>
Araç ve nesne tespiti görüntü işleme algoritmaları ile elde edilir.Projenin olmazsa olmazları: <br/>
•	Proje, aracın son derece güvenilir bir şekilde yolculuğunu sağlar. <br/>
•	Canlı veya cansız varlıkların güvenliğini sağlar. <br/>
•	Görüntü işleme ile  kaza oranı azaltılır. <br/>
•	Sürücüye bilinçli bir yolculuk sağlanır. <br/>
Nesne tanıma, sınıflandırma, makine öğrenmesi algoritmaları ve OpenCV, Tenserflow gibi kütüphaneler ile istenen çıktılara ulaşılacaktır. Bu sayede açıklanan tüm sistem gereksinimleri sağlanır.<br/>
Projenin ilerleyen aşamalarında gelişmeye açık olduğunu da belitirmek isterim.













