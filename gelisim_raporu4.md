# BİLGİSAYAR MÜHENDİSLİĞİ BİTİRME PROJESİ 4. RAPORU

### Araçların Çevresinde Tehlike Oluşturabilecek Varlıkların Görüntü İşleme ile Tespit Edilmesi



**1- DÜZELTMELER**

Güncel Gantt Chart: 

![GuncelAkis](https://user-images.githubusercontent.com/56633000/121725831-6debd300-caf2-11eb-8aa6-f359be0a57a4.png)


Projenin son aşaması olan tehlike oluşturabilecek mesafenin ölçümü ve uyarı sistemi de tamamlanmıştır.Ancak araçlar ksımında hatalı tespitler olduğundan,
proje dönem sonuna kadar geliştirilmeye devam edilecektir.Aynı zamanda raporlama bitmiş olup, tez aşaması devam etmektedir.
İlerleme tabloda güncellenmiştir.Teslim tarihine kadar tezin sonlanması ve proje gelişiminin tamamlanması hedeflenmiştir.

1. Yapılan Çalışma:

Projemin önemli kısmı olan tehlike oluşturabilecek mesafenin hesaplanması için; ilk olarak statik bir noktaya göre hareket eden bir cismin,
merkezi noktasının uzaklığını ölçmeye çalıştım.Bu kısım src/proje klasöründe bulunan MesafeHesaplama içerisindeki Python kodudur.Test aşamasında bir kalem kullandım ve 
çıktıdan alınmış bir görseli rapora ekledim.

![mesafeHesap](https://user-images.githubusercontent.com/56633000/121722712-4eeb4200-caee-11eb-95ea-3871206a8a0d.PNG)
       
      
      
2. Yapılan Çalışma:

Test videoları üzerinde çalıştığım; insanların arasındaki mesafeye göre, birbirlerine fazla yakın olanların kırmızı dikdörtgen ile tespit ettiğim,
src/proje klasöründe bulunan SosyalMesafeHesaplama içerisindeki Python kodudur.Projede insanlar tespit edildikçe aralarındaki mesafe uyumu analizi yapılacaktır. 
Çıktıdan aldığım görselleri de yine hazırladığım rapora ekledim.

1.Video Çıktısı

![Test](https://user-images.githubusercontent.com/56633000/121727194-41d15180-caf4-11eb-9b07-7c03c01fc3f1.PNG)

2.Video Çıktısı

![sosyalMesafe](https://user-images.githubusercontent.com/56633000/121720718-18acc300-caec-11eb-9abc-4ff12a9488b5.PNG)



#### Öğrenilen Kavramlar    

HOG(Histogram of Oriented Gradients): İmge işleme ve örüntü tanıma ile alakalı çalışmalar literatürde yoğun olarak verilmekte ve mevcut algoritma ve sınıflandırıcıların
performansını artırıcı yönde çeşitli öneri ve yöntemler araştırmacılar tarafından sunulmaktadır. Son yıllarda Shashua ve Dalal ve Triggs tarafından önerilen HOG algoritması
bu yönde yapılan başarılı çalışmalara örnek olarak verilebilir.Nesne ve örüntü tanıma için yaygın olarak kullanılmaya başlanan Histogram of Oriented Gradient (HOG), bir çok
konuda ve farklı şartlar altında çok yüksek bir başarımla çalışabilmektedir. HOG, ilk olarak Shashua ve diğerleritarafından yaya tanıma sistemlerinde kullanılabilecek
tanımlayıcılar olarak önerilmiştir. Dalal ve Triggs, bu tanımlayıcıları başarı ile kompleks ortamlarda insan tanıma problemine uyarladılar. Bu basit fakat etkin tanımlayıcı,
başarılı uygulamalarından dolayı, literatürde yoğun bir ilgi kazanmış ve birçok uygulamada kullanılmaya başlanmıştır.Son yıllarda imgedeki piksellerin yönelim (θ) ve büyüklük
değerlerinin karakteristiği olarak da adlandırılabilecek olan HOG algoritmasının kullanımı bir çok alanda oldukça ilgi görmektedir.

![112](https://user-images.githubusercontent.com/56633000/121725200-a0490080-caf1-11eb-812d-cc45036e5ba2.PNG)

Bir çok araştırmacı tarafından oldukça ilgi gören HOG yöntemindeki temel amaç imgeyi bir grup lokal histogramlar olarak tanımlamaktır. Bu gruplar, imgenin lokal bir bölgesindeki
gradyanların yönelimlerinde, gradyanların büyüklüklerinin toplandığı histogramlardır.Yönlendirilmiş gradyanların histogramı, nesne algılama amacıyla bilgisayarla görme ve 
görüntü işlemede kullanılan bir özellik tanımlayıcıdır.Teknik, bir görüntünün lokalize kısımlarındaki gradyan yönelim oluşumlarını sayar.

![111](https://user-images.githubusercontent.com/56633000/121724261-45fb7000-caf0-11eb-897c-d1de6dc68c88.png)


**2- KAYNAKLAR**

Mesafe ölçümü ve analizi çalışmaları için faydalandığım kaynaklar:

1. AI,Landing. "Landing AI Social Distancing Detector Demo", Youtube, 15 Nisan 2020, https://youtu.be/15iIV1Lff-M .
  
2. Cogneethi. "C34 | HOG Feature Vector Calculation | Computer Vision | Object Detection | EvODN", Youtube, 11 Ağustos 2019, https://youtu.be/28xk5i1_7Zc .
  
3. N. Dalal and B. Triggs., “Histograms of oriented gradients for human detection”, In C. Schmid, S. Soatto, and C. Tomasi, editors, International Conference on Computer Vision and Pattern
Recognition, volume 2, pages 886–893, June 2005.
  
4. Ghosh,Priyanjit. "How AI can be used to detect social distance in public | Codevector Labs", Youtube, 20 Nisan 2020, https://youtu.be/Q4gQ4v-fy04 .

5. Açıl,Sıddık. "Python: Nokta Doğru Mesafesi Hesaplama", Medium, 11 Şubat 2018, https://medium.com/@sddkal/python-nokta-do%C4%9Fru-mesafesi-hesaplama-979e40b34fa1 .

6. Kane,Frank with Education Sundog. "Computer Vision with OpenCV: HOG Feature Extraction", Youtube, 6 Ekim 2018, https://youtu.be/4ESLTAd3IOM .

7. Team Detection Object, TF. "TensorFlow Object Detection API", Github, 1 Haziran 2020, https://github.com/tensorflow/models/tree/master/research/object_detection .

8. Delibaşoğlu,İbrahim. "Python - OPENCV Yaya Tespiti (Görüntü İşleme)", Blogger, 23 Ocak 2017, http://ibrahimdelibasoglu.blogspot.com/2017/01/python-yaya-tespiti-goruntu-isleme.html .

9. Russell Dicker Director of Product, Google Maps. "A smoother ride and a more detailed Map thanks to AI", Google Blog, 18 Mayıs 2021, https://blog-google.cdn.ampproject.org/c/s/blog.google/products/maps/google-maps-101-ai-power-new-features-io-2021/amp/ .


**3- İLERLEME**

İkinci dönemin ilk raporunda belirttiğim gibi video içerisindeki hareketli insanları tespit etmeye çalışmış ve kodunu yazmıştım.İlk dönem ise araçların tespiti ve 
hareketini algılama kısmını çözmüştüm.İlk rapor tesliminden sonra; insan, araç takibi ve sayımı üzerine projedeki son kısım olan insanlar ve araçlar tespit edildikçe 
aralarındaki mesafe analizini yapmaya çalıştım.Bunun için öncelikle videoda geçen insanların ve araçların ortalama en genişliğini bulmaya çalıştım.
Ardından, insanların araçlar ile arası uzaklığın ortalama en genişliğinin 2 katı olmadığı durumlarda mesafe ihlali olarak görüntünün üzerine bilgi mesajı yazdırmayı düşündüm. 
Merkezler arasındaki mesafeyi ,iki nokta arasındaki uzaklık formülü ile buldum.Kod çalıştırıldığında da mesafeyi ihlal eden araç veya insanların kırmızı dikdörtgen,
bir sorun teşkil etmeyen araç ve insanları ise yeşil diktörtgen içinde göstererek, çıktı vermeye çalıştım.
  
Böylece; proje sonuna yaklaşarak, hareket içinde olan insan ve araçlar arasında mesafe korunmuş, kazaların önüne geçilerek can kaybının azalması sağlanmıştır.


**4- ARAÇLAR**

Projede kullandığım araçlar: 

1. Jupyter Notebook : Python dilinde projemi geliştirdiğim, etkileşimli bir ortam sağlayan açık kaynak kodlu bir programdır.  

2. OpenCV : Görüntü işleme uygulamalarında kullandığım açık kaynaklı kütüphanedir.

3. Youtube : Test için kullandığım gerekli video kaynaklarını ve faydalandığım eğitim videolarını içinde barındıran web sitesidir.

4. Github : Görüntü işleme gibi birçok farklı konuda proje geliştirmiş insanların repolarını incelediğim, projeme yön vermemi sağlayan web tabanlı bir depolama servisidir.

5. Numpy : NumPy, Python programlama dili için bir kütüphane olup, büyük, çok boyutlu diziler ve matrisler için destek eklerken, bu dizilerde çalışmak için yüksek düzeyli matematiksel fonksiyonların geniş bir koleksiyonudur.  

6. TensorFlow : TensorFlow, bir dizi görev arasında veri akışı ve türevlenebilir programlama için kullanılan ücretsiz ve açık kaynaklı bir yazılım kütüphanesidir. Sembolik bir matematik kütüphanesidir ve sinir ağları gibi makine öğrenimi uygulamaları için de kullanılır.    

7. Stack Overflow : Aldığım kod hatalarını düzeltmek için başvurduğum kullanıcı odaklı soru cevap sitesidir.

8. Imutils : Çevirme, döndürme, yeniden boyutlandırma, iskeletleştirme, Matplotlib görüntülerini görüntüleme, konturları sıralama, kenarları algılama gibi temel görüntü işleme işlevlerini çok daha kolay hale getiren kütüphanedir. 


