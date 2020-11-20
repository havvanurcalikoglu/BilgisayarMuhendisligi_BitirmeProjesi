# Bilgisayar-Muhendisligi-Bitirme-Projesi
## Araçların Çevresinde Tehlike Oluşturabilecek Varlıkların Görüntü İşleme ile Tespit Edilmesi

**1- PROJE ÖZETİ**

Bu projede hedef, kameralardan elde edilen araç görüntüleri izlenerek, araç etrafında bulunan insan, hayvan veya nesnelerin Görüntü İşleme yöntemleri ile tespit edilmesidir. Dijital görüntüler alınarak, nesne tanıma ile yazılım tabanlı olarak çalışır. Nesne tespit ve tanıma süreçleri veri girişi, veri ön işleme ve aşamaları, öznitelik çıkarımı ve öz nitelik seçimi, tanımlama aşamaları altında farklı algoritmalar yardımıyla çözüm bulmaktadır. Projeye göre değişik uygulamaları olup, uygulamaya özel algoritma ve donanım yapısının bir araya getirilmesi ile oluşturulan bir sistemdir.Aynı zamanda araçların tespiti ve sınıflandırılması yapılır.

Araçların etrafında  tehlike oluşturabilecek varlıkların görüntülerden tespitiyle de aslında aracın ve çevresinin güvenliği sağlanmış olur.Sürücüye, aracın çevresi fark ettirilir.
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

**3- İŞ BÖLÜMÜ PLANLAMA**

Projeyi tek başıma yürüteceğimden tüm iş paketlerinden (  literatür taramasi, metodoloji, deneme ve sonuç ) ben sorumluyum.



**4- HEDEFLENEN ÇIKTILAR**

Hedeflenen proje, araç ve araç çevresini tespit eden bir masaüstü uygulamasıdır. <br/>
Anaconda Python ile geliştirip; Tensorflow, OpenCV, Numpy kütüphanelerinden faydalanacağım.Projeyi Windows işletim sistemi üzerinde çalıştıracağım. 
(Linux ile de yürütülebilir.) <br/>
Nesne tanıma, görüntülerdeki veya videolardaki nesneleri tanımlamak için bir bilgisayarlı görü tekniğidir. Nesne tanıma, derin öğrenme ve makine öğrenme algoritmalarının önemli bir çıktısıdır. Tensorflow , veri akış grafiklerini kullanarak sayısal hesaplama için açık defter bir yazılım kitaplığıdır. Grafikteki düğümler matematiksel temsil sırasında, grafik kenarları aralarında iletişim kuran çok boyutlu veri dizilerini temsil eder.OpenCV, açık kaynak bir bilgisayarla görme ve makine öğrenimi yazılım kitaplığıdır. OpenCV, bilgisayarla görme uygulamaları için ortak bir altyapı sağlamak ve ticari ürünlerde makine algısının sağlanması hızlandırmak için kullanılır.
Projenin olmazsa olmazları nesne tanıma, sınıflandırma, makine öğrenmesi algoritmaları ve OpenCV, Tenserflow gibi kütüphanelerdir.Bu teknolojiler ile istenen çıktılara ulaşılacaktır. <br/>
Araç ve nesne tespiti görüntü işleme algoritmaları ile elde edilir. <br/>
•	Görüntü işleme, aracın son derece güvenilir bir şekilde yolculuğunu sağlar. <br/>
•	Görüntü işleme, canlı veya cansız varlıkların güvenliğini sağlar. <br/>
•	Görüntü işleme ile  kaza oranı azaltılır. <br/>
•	Görüntü işleme, sürücüye bilinçli yolculuk bir sağlar. <br/>
Bu sayede açıklanan tüm sistem gereksinimleri sağlanır. Projenin ilerleyen aşamalarında gelişmeye açık olduğunu da belitirmek isterim.













