# Bilgisayar-Muhendisligi-Bitirme-Projesi 2.Rapor
## Araçların Çevresinde Tehlike Oluşturabilecek Varlıkların Görüntü İşleme ile Tespit Edilmesi


**1- DÜZELTMELER**  

Gantt Chart : İş bölümünün zamanlaması Mayıs 2021’de bitmek üzerine yeniden planlanmıştır.

![Gantt Chart](https://user-images.githubusercontent.com/56633000/103461113-d9a06780-4d2c-11eb-9fb5-d78ce84d941e.PNG)  


**2- KAYNAKLAR**  

Görüntü İşleme ve Nesne Tespiti çalışmaları için faydalandığım kaynaklar:

1. Kızrak,Ayyüce,Merve. "Derin Öğrenmeye Giriş", Udemy, https://www.udemy.com/course/derin-ogrenmeye-giris/  
   
2. Kurt,Özge. "Python ile Görüntü İşleme - OpenCV Giriş", Youtube, 15 Nisan 2020, https://youtu.be/hRzBtQh6wuU

3. Mekatronik,Mert. "Haarcascade Araba,Beden Tespiti", Youtube, 15 Ocak 2019, https://youtu.be/UwdKG0m1I8s

4. Informatic,Falcon. "Vehicle Detection And Counting", Youtube, 13 Temmuz 2020, https://youtu.be/IdBnsNttXq0  
   
5. Yücel,Enes,M. "Görüntü İşleme Araç Takibi", Github, 12 Ocak 2019, https://github.com/mmenesyucel/Goruntu-Isleme-Arac-Takibi 
   
6. Informatic,Falcon. "Realtime Face Recognition Using Python", Youtube, 11 Nisan 2020, https://youtu.be/Ip79Q9dFbG8  
   
7. Yurdakul,Mustafa. "Görüntü İşleme", Github, 2 Ocak 2020, https://github.com/mustafayurdakul/goruntu-isleme   
   
8. Pişkin,Mesut. "Opencv Eğitim Serisi", 24 Ekim 2016, https://mesutpiskin.com/blog/opencv-egitim-serisi    
   
9. Sarai,Rebeca. "Vehicle Recognition", Towards Data Science, 8 Nisan 2017, https://towardsdatascience.com/vehicle-recognition-in-external-environments-through-image-processing-87dd00237dc8    

10. "Digital Image Processing", Wikipedia, https://en.wikipedia.org/wiki/Digital_image_processing   
      
11. Görüntü İşleme Ders Notları  
    İstanbul Üniversitesi Cerrahpaşa, 2019-2020 Bilgisayar Mühendisliği Bölümü , Doç. Dr. Selçuk SEVGEN  
    
12. "Opencv Kurulumu", https://opencv.org/    
      
13. "Hata Çözümlemeleri", https://stackoverflow.com/  
      
14. Kızrak,Ayyüce,Merve. "Derin Öğrenmeye Giriş", Github, 16 Ağustos 2020, https://github.com/ayyucekizrak



**3- ZORLUKLAR**  

Projeye başlamadan önce OpenCV gibi gerekli kütüphane kurulumlarını gerçekleştirdim.Kurulumdan sonra literatür taraması aşamasındaki nesne tespiti üzerine bulduğum faydalı eğitimleri izledim.Eğitimden sonra hem kütüphanelerin kullanılması hem de görüntü işleme aşamasına geçtim.Bu aşamada Rakam Tanıma, Kenar Belirleme gibi çeşitli uygulamaları gerçekleştirdim ve kodlarını Github repoma ekledim.

![edge](https://user-images.githubusercontent.com/56633000/103484967-e774ec00-4e03-11eb-80c1-694d10badd56.png) 

Projem için gerekli hazırlığı yaptıktan sonra araç tespiti ve sayımı şeklinde projenin ilk kısmına başladım.Veri seti olarak bulduğum örnek bir kaynağı kodlarım üzerinde çalıştırıp, sonuçlarını inceledim.

![Arac_Tespit_Sayimi](https://user-images.githubusercontent.com/56633000/103484979-fc517f80-4e03-11eb-8f4c-27444d5b97d7.PNG)

##### Öğrenilen Kavramlar

Görüntü İşleme, görüntüyü dijital form haline getirmek ve bazı işlemleri gerçekleştirmek için geliştirilmiş, spesifik görüntü elde etmek veya ondan bazı yararlı bilgiler çıkarmak için kullanılan bir yöntemdir. Bu yöntemin girdisi video kesiti veya fotoğraf gibi bir görüntüdür. Çıktısı ise görüntünün istenilen ya da dikkat edilmesi gereken bölümüne karşılık gelir.   
Görüntü işleme temel olarak üç adımda incelenmektedir:  

– Gerekli araçlar ile imajı aktarılması  
– Görüntünün analiz edilerek istenilen doğrultuda işlenmesi  
– Analiz edilip işlenen veri raporu ve çıktısının, sonucunun alınması  

![sema](https://user-images.githubusercontent.com/56633000/103483399-1c7b4180-4df8-11eb-98f8-27e429141b5d.jpg)  


Nesne tanıma, görüntü işlemede büyük önem taşımaktadır. Bu ihtiyaç üzerine OpenCV de geliştirilmiş bir çok yöntem bulunmaktadır. 

Nesne tespiti için 4 farklı yöntem mevcuttur. Bu yöntemler;  

1.Template Matching (Şablon Eşleştirme):  
Şablon eşleme, bir görüntünün şablon görüntüsüyle eşleşen küçük kısımlarını bulmak için dijital görüntü işlemede kullanılan bir tekniktir. Görüntülerdeki kenarları algılamanın bir yolu olarak da kullanılabilir.Kaynak görüntü üzerinde nesneyi tüm piksellerde dolaşarak aramaktadır. Buda görüntünün birebir aynısı olarak aranması demektir. Bu yüzden nesneyi ayırt etmede çok fazla başarılı değildir.

![template-matching-sonuc](https://user-images.githubusercontent.com/56633000/103485949-35d9b900-4e0b-11eb-96e5-2db57c751a30.jpg)

2.HAAR Cascade:  
Haarcascade sınıflandırıcısında, nesnenin bulunduğu resimler üzerinden geçirilerek değerler oluşturulur. Örneğin yüz taramasında ağız, burun, alın, saç gibi bölgelerde birçok karanlık aydınlık özellikleri oluşturulacaktır. Bunların her birinden hedef değerler oluşturulmaktadır. Ve bu işlem çerçeve büyüklükleri değiştirilerek diğer aşamalarda tekrar edilmektedir.Bu çerçeveler(zayıf sınıflandırıcılar) her resim boyutu için düşünüldüğünde yüz binlerce çekirdek oluşacaktır. Negatif resimler üzerinde tarama yapılarak içinde nesne bulunmadığı için kullanılmayacak olan çerçevelerin büyük çoğunluğu elenecektir. Pozitif resimlerde nesne seçilerek nesnedeki kullanılacak çerçeveler belirlenecektir. Bunun için eğitim sırasında pozitif resimlerde nesnenin milimetrik seçimine dikkat edilmelidir.  Pozitif ve negatif resim örneklerinin çok olması istenilen nesnede daha iyi sonuçlar almak için önemlidir.  
Bu işlemlerin hem eğitimde hem de nesnelerin bulunmasında bilgisayarı çok yoracağı ve işlemlerin uzun süreceği düşünülebilir. Real time görüntü işlemede hız çok önemlidir. Haarcascade sınıflandırıcısında öncelikle resimlerin integralleri alınır. Böylelikle piksel değerlerinin tek tek toplamları hesaplanmak yerine integralle hesaplanmış olmaktadır. Böylelikle bilgisayardan büyük bir işlem gücü kaldırılacaktır.    

![haarcascade-siniflandirici](https://user-images.githubusercontent.com/56633000/103486277-bb5e6880-4e0d-11eb-935f-3f748def457c.jpg)

3.LBP – Local Binary Pattern  (Yerel İkili Örüntü Tabanli Veri Gizleme Algoritması):
Bu yöntem kaynak görüntüde aranan nesneyi piksel yoğunluğuna(intensity) göre bulmaktadır. Daha teknik olarak, bir noktanın etrafındaki piksellerin yoğunluk değerlerine göre oluşan ikili(binary) örüntülerden yaratılır ve bu örüntüler üzerinde işlemler gerçekleştirerek nesneyi aramaktadır.  

![lbp](https://user-images.githubusercontent.com/56633000/103486364-5a836000-4e0e-11eb-8a7d-89ddcf77fd80.png)

4.HOG – Histogram of Oriented Gradients:
Yönlendirilmiş gradyanların histogramı, nesne algılama amacıyla bilgisayarla görme ve görüntü işlemede kullanılan bir özellik tanımlayıcıdır. Teknik, bir görüntünün lokalize kısımlarındaki gradyan yönelim oluşumlarını sayar.

![histogram_og](https://user-images.githubusercontent.com/56633000/103486403-b2ba6200-4e0e-11eb-82a7-995f1941cbe2.png)


Template Matching yöntemi dışındaki yöntemler “Sınıflandırıcı” olarak tanımlanan Machine Learning algoritmalarıdır.

##### Karşılaşılan Sorunlar ve Çözümleri  





**4- ARAÇLAR**  

Projenin ilk aşamasında kullanılan araçlar:

1. Anaconda Navigator : Anaconda Navigator, uygulamalarınızı başlatmamıza ve komut satırı komutlarını kullanmanıza gerek kalmadan Anaconda paketlerini, ortamları ve kanalları kolayca yönetmenizi sağlayan Anaconda'da bulunan bir masaüstü grafik kullanıcı arabirimidir.  

2. Jupyter Notebook : Jupyter Notebook, çeşitli programlama dilleri için etkileşimli bir ortam sağlayan açık kaynak kodlu bir programdır.  

3. Spyder : Spyder, Python dilinde bilimsel programlama için açık kaynaklı bir platformlar arası entegre geliştirme ortamıdır.  

4. OpenCV : Gerçek-zamanlı bilgisayar görüsü uygulamalarında kullanılan açık kaynaklı kütüphanedir.  

5. Numpy : NumPy, Python programlama dili için bir kütüphane olup, büyük, çok boyutlu diziler ve matrisler için destek eklerken, bu dizilerde çalışmak için yüksek düzeyli matematiksel fonksiyonların geniş bir koleksiyonudur.  

6. TensorFlow : TensorFlow, bir dizi görev arasında veri akışı ve türevlenebilir programlama için kullanılan ücretsiz ve açık kaynaklı bir yazılım kütüphanesidir. Sembolik bir matematik kütüphanesidir ve sinir ağları gibi makine öğrenimi uygulamaları için de kullanılır.  

7. Udemy : Udemy.com profesyonel yetişkinlere ve öğrencilere yönelik eğitim teknolojisi, kitlesel çevrimiçi açık ders ve bir çevrimiçi öğrenme platformudur.   

8. Stack Overflow : Stack Overflow, bilgisayar programcılığı ile ilgili kullanıcı odaklı soru cevap sitesidir.      

9. Github   
  
10. Youtube  


**5- İŞ DAĞILIMI** 

03.01.2021 tarihine kadar yapılan çalışma, saat cinsinden yüzdesel olarak tabloda gösterilmektedir.Projeyi tek yürüttüğümden çalışmanın tamamı bana aittir.

                      
| İş Tanımı | Yüzdesel Saat | Proje Sorumlusu                      |                   
|--------:|----------------------------|:--------------------:|
| Cihazların ve yazılımın hazırlanması        |       10                     |           Havvanur ÇALIKOĞLU           |                 
| Proje için literatür taraması ve gerekli eğitimlerin alınması        |      50                      |      Havvanur ÇALIKOĞLU                  | 
| Görüntü İşleme ve Kütüphaneler üzerine çalışılması        |         35                   |           Havvanur ÇALIKOĞLU             |                   
| Veri seti toplanması ve Metedoloji        |                  5          |  Havvanur ÇALIKOĞLU  | 
                



