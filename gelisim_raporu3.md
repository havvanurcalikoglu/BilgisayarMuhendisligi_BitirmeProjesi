# BİLGİSAYAR MÜHENDİSLİĞİ BİTİRME PROJESİ 3. RAPORU

### Araçların Çevresinde Tehlike Oluşturabilecek Varlıkların Görüntü İşleme ile Tespit Edilmesi


**1- DÜZELTMELER**

Güncel Gantt Chart: 

![takvim](https://user-images.githubusercontent.com/56633000/115921433-26e34900-a484-11eb-9483-cf882b541cea.PNG)


Bu kısım, 21 Ocak 2021 tarihinde Bitirme Projesi'nin ilk sunumu gerçekleştikten sonraki aşamaları barındırmaktadır.Genel olarak iş bölümlerine ayrılan zamanlamalar, üniversitenin bitiş takvimine göre arttırılmıştır.  


1. Yapılan Çalışma:

![detection](https://user-images.githubusercontent.com/56633000/115875900-6131f380-a44e-11eb-8534-b9d7d456e7eb.PNG)

Burada insan yüzü ve gözü tespit edilmektedir.Test için Steve Jobs fotoğrafı kullanılarak, doğru bir tespit yapılmıştır.Gerekli kod ve medyayı src/proje klasörü altında bulabilirsiniz.  

#### Öğrenilen Kavramlar    
Yüz tanıma algoritmaları çalışma şekline göre 3 farlı başlık altında incelenebilir, farklı kaynaklarda 4 veya 5 başlık altında ele alındığını da görebilirsiniz.Bunlar:

1)Bütünsel Eşleme (Holistic Matching): Bu yöntemde girdi olarak kullanılacak yüz verisi tek bir bütün parça halinde algoritmaya girdi verisi olarak sunulur. 2D (iki boyutlu) görüntüler üzerinde yüz tanıma için oldukça popüler bir yöntemdir. Opencv içerisinde de yer alan Eigenface bu yönteme bir örnektir.

2)Öznitelik Tabanlı (Feature Based): Öznitelik tabanlı algoritmalar, öznitelik çıkarımı kullanarak yüzün önemli noktalarını referans alarak çalışır. Bu önemli noktalar göz, ağız, burun, yüz genişliği, ağız genişliği, alın genişliği veya göz bebekleri arası mesafe olabilir. Bu algoritmalar yüz tespiti için bilinen öz nitelikleri kullanır. OpenCV içerisinde yer alan ve nesne tanıma bölümünde işlenilen Haar-Cascade algoritması buna bir örnektir, bu algoritma ile görüntü içerisindeki yüzler tespit edilebilir, yine OpenCV içerisinde yeralan SIFT bu yönteme örnek gösterilebilir.  

3)Hibrit Yaklaşım: Hibrit algoritmalar adında anlaşılacağı üzere bütünsel eşleme ve öznitelik çıkarımını birlikte kullanarak daha iyi sonuçlar elde etmeyi amaçlar.  

OpenCV içerisinde yer alan bazı yüz tanıma algoritmaları aşağıdaki gibidir;

-Eigenfaces: EigenFaces algoritması, eğitim için kullanılan tüm yüzler ile girdi olarak verilen yüzü karşılaştırır. Bu eşleştirme de eleme yöntemi kullanarak veri seti içerisindeki yüzler ile girdi yüzü arasında eşleşmeyen yerleri atarak sona kalan yüzü bulur.   

-Fisherfaces: Fisherfaces algoritması, girdi olarak verilen yüz üzerindeki öznitelikleri belirler ve eğitim için kullanılan yüzler ile sırasıyla öznitelik yönünden karşılaştırır, en çok benzeyeni bulana kadar devam eder.   

-Local Binary Patterns Histograms LBPH: LBPH algoritması diğer algoritmalarda çok büyük bir sorun olan ışık ve çevre koşullarından en az oranda etkilenmeyi sağlamak amacıyla geliştirilmiştir. LBPH adından da anlaşılacağı üzere yerel pikselleri bir biriyle komşuluklarına göre inceleyerek sonuç çıkarmaya çalışır. Komşu piksel gruplarından yararlanarak yerel bir yapı bulmayı amaçlar, bu yöntemi girdi ve veri tabanındaki yüzler üzerinde uygulayarak en çok benzeyen yüzü bulmaya çalışır.  

-Sinir Ağları ile Yüz Tanıma: Bu yöntemi kullanmak için çok fazla veriye ihtiyaç duyulur. Tanınmasını istenen kişilerin yüzleri sinir ağına eğitim verisi olarak girilir ve sinir ağı (genellikle CNN) verisetinde yer alan yüzler üzerinde baskın öz nitlikleri belirleyerek bir sınıflandırma yapar. Girdi olarak verilen yüz sinir ağına girdiğinde bakılması gereken öz nitelikler eğitim ile belirlendiği için hızlı bir şekilde yüzün hangi sınıta olduğu belirlenir. Veri tabanına eklenen her kişinin yüzü artık ayrı bir sınıf olmuştur geriye kalan ise girdi olarak verilen yüzün hangi sınıfta olduğudur.    

Bu algoritmaları denediğinizde hızlı fakat başarı oranı düşük sonuç alabilirsiniz, bu durumlarda daha yüksek doğruluk oranı sağlayan sinir ağı tabanlı sınıflandırma algoritmaları kullanılır.Projenin önemli bir kısmı da insan tespiti olduğundan, doğru bir tespit yapmak amaca daha fazla ulaştıracaktır.


2. Yapılan Çalışma:

![insanTespit](https://user-images.githubusercontent.com/56633000/115900535-b8dd5880-a468-11eb-88b2-ee9e7cb65dc5.PNG)

![Ekran Görüntüsü (350)](https://user-images.githubusercontent.com/56633000/115900579-c692de00-a468-11eb-9b04-c482b98a5097.png)

İnsanların, diğer canlı ve nesnelerden ayrıştırılması sağlanarak, doğruluk oranları alınmıştır.Gerekli kod ve medyayı src/proje klasörü altında bulabilirsiniz.

Proje kapsamında gereksinim duyulan insan tespiti probleminin çözümü bir görüntüde insan olup olmadığının tespit edilmesi ve insan var ise konumunun bulunması işlemlerini kapsamaktadır. Video tabanlı bir sistem oluşturulduğu için hareketli nesnelerin bulunması ve bu nesnelerin insan olup olmadığının tespit edilmesi problemin çözümü olacaktır. Bu bağlamda bir görüntü üzerinden insan tespiti iki temel aşamadan oluşmaktadır. İlk aşama video üzerinden hareket eden nesnelerin bulunmasını sağlayan ön işlemlerden oluşmaktadır. İkinci aşama ise bu nesnelerin insan olup olmadığının tespit edilmesini kapsayan ikili sınıflandırma modelidir.
Bu aşamadan sonra video içerisindeki hareketli insanlar tespit edilmiştir.


3. Yapılan Çalışma:

![Ekran Alıntısı](https://user-images.githubusercontent.com/56633000/115817147-f0b1b500-a402-11eb-90d1-e42992ce86e7.PNG)  

Video içerisinde hareketli insanlar tespit edilmeye çalışılmıştır.Gerekli kod ve medyayı src/proje klasörü altında bulabilirsiniz.

#### Öğrenilen Kavramlar  
Nesne takibi genel olarak bir video veya sıralı gelengörüntü dizisinde bulunan nesnenin takip edilmesidir. Nesnetakibi yöntemleri temel olarak 3 kategoriye ayrılır. Bunlar
sırasıyla nokta tabanlı, çekirdek tabanlı ve siluet tabanlı yöntemlerdir.Nokta takip yönteminde takip edilecek nesne noktalar ile ifade edilir. Bu noktaların bir sonraki imgedeki konumları vebirbirlerine olan uzaklıkları gibi verilerin sonraki gelen video çerçevesinde de birbirine paralel olması beklenir. Bu bilgilerden yola çıkılarak nesne takibi sağlanır. Bu yöntemde temel amaç nesnenin video çerçevesi içinde tespit edilmesi ve bir önceki çerçevede kullanılan nokta benzerliklerin hesaplamasıdır. Bu yöntem deterministik ve istatistiksel yöntemler olarak ta kendi içinde alt sınıflandırmalar içermektedir.

Nokta takibi yöntemlerinde en yaygın kullanılan yöntemlerden birisi kalman filtresidir. Bu yöntem nesnenin Gaussian dağılıma sahip durum değişkenleri yardımıyla videodaki bir sonraki gelen çerçevede nesne konumunu tahmin etmektedir. Kalman filtresi basit ve hızlı olma açısından gerçek zamanlı nesne takip uygulamalarında kullanıma uygundur. Durum değişkenleri Gaussian dağılımına sahip olmayan sistemlerde kalman filtresi başarısız olabilmektedir. Bu tür problemlerin giderilmesi için parçacık filtresi yöntemi geliştirilmiştir. Parçacık filtresi olasılıksal yönteme dayanmaktadır. Bu yöntemin en büyük avantajı doğrusal olmayan ve çoklu dağılıma sahip sistemlerde çalışabilmesidir.
Çekirdek tabanlı yöntemlerde bir geometrik şekil yardımıyla takip edilecek nesne çerçevelenir. Bu çerçeve içerisinde bulunan nesne parçasının anlamlı bilgileri hesaplanarak başlangıçtaki şekil yardımıyla nesne takip edilir. Bu yöntemde nesnenin şeklinden ziyade kullanılan geometrik şeklin içerisinde bulunan nesne bilgilerinin çıkarılması yeterli olabilmektedir. Bu şekil içinde bulunan piksellerin hesaplanan olasılık yoğunluk bilgileri veya histogram özellikleri gibi bilgileri sonraki video çerçevelerinde takip edilebilmektedir. 

![Ekran Alıntısı2](https://user-images.githubusercontent.com/56633000/115927046-82b1d000-a48c-11eb-9ef7-082aff783a65.PNG)

Siluet tabanlı yöntemler genellikle takip edilen nesnenin insan ya da hayvan gibi belli bir geometrik şekille ifade edilemediği durumlarda kullanılır. Bu yöntemin temel amacı
nesneyi tanımlayacak kenar bilgisi ya da şekil bilgisi çıkartılarak sonraki imgelerde bu bilgiyi aramaktır. Bu yöntem şekil değişikliğine karşı oldukça hassas olmaktadır.
Çekirdek ve siluet tabanlı yöntemler kıyaslandığında, çekirdek tabanlı yöntemlerin daha düşük işlem zamanına ve daha yüksek başarı oranlarına sahip oldukları görülmektedir.
Bu sebepten dolayı çalışmalarda çekirdek tabanı yöntemler geniş bir kullanım alanına sahiptir. Nokta tabanlı yöntemler diğer yöntemlere oranla daha düşük işlem zamanına sahip
olmakla birlikte daha düşük başarı oranına sahiptirler.  


4. Yapılan Çalışma:

![aracSayim](https://user-images.githubusercontent.com/56633000/115905352-a9610e00-a46e-11eb-84f9-e82745717ca9.PNG)

Araçların hareketleri incelenerek, daha fazla doğruluk oranlı sayım yapılmıştır.Gerekli kod ve medyayı src/proje klasörü altında bulabilirsiniz.


5. Yapılan Çalışma:

![Ekran Alıntısı2](https://user-images.githubusercontent.com/56633000/115817415-79c8ec00-a403-11eb-945f-407446071612.PNG)


![Ekran Alıntısı3](https://user-images.githubusercontent.com/56633000/115817438-83525400-a403-11eb-9697-10f803c378db.PNG)

Bu çalışmada gömülü bir platform üzerinde çalışan gerçek zamanlı bir şerit takip sistemi önerilmiştir. Sürücülerin sürüş sırasında uykuya dalmaları nedeniyle araçlarının kontrolünü kaybederek şerit değiştirdikleri bilinmektedir.Araçların kendi şeritlerinde hareket ettiğini tespit edebilmek için kenar (şerit) tespiti yapılmıştır.Gerekli kod ve medyayı src/proje klasörü altında bulabilirsiniz.



**2- KAYNAKLAR**

Görüntü İşleme ve Nesne Tespiti çalışmaları için faydalandığım kaynaklar:

1. G,Kittipong. "Lane detection and steering module with OpenCV & Arduino",Youtube, 11 Haziran 2016, https://youtu.be/8h9vU1pnNZA .

2. freeCodeCamp.org. "OpenCV Course - Full Tutorial with Python",Youtube, 3 Kasım 2020, https://youtu.be/oXlwWbU8l2o .

3. Y. Freund and R. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting,
   Journal of Computer and System Sciences, 55 (1997), https://www.sciencedirect.com/science/article/pii/S002200009791504X?via%3Dihub .

4. ProgrammingKnowledge. "OpenCV Python Tutorial - Find Lanes for Self-Driving Cars (Computer Vision Basics Tutorial)",Youtube, 7 Ekim 2018, https://youtu.be/eLTLtUVuuy4 .

5. Luvizon,Diogo. "A Video-Based System for Vehicle Speed Measurement in Urban Roadways",Youtube, 1 Eylül 2015, https://youtu.be/3IaKJuZN55k .

6. USA,BMW. "Daytime Pedestrian Detection",Youtube, 22 Eylül 2017, https://youtu.be/Pxv0TKO75rk .

7. Developer,NVIDIA. "Real-Time Object Detection in 10 Lines of Python Code on Jetson Nano",Youtube, https://youtu.be/bcM5AQSAzUY .

8. Sturdevant,Mark. "Object tracking in video with OpenCV and Deep Learning",Youtube, 6 Eylül 2018, https://youtu.be/19vaot75JCY .

9. Bastien F., Lamblin P., Pascanu R., Bergstra J., Goodfel-low I. J., Bergeron A., Bouchard N., Bengio Y.: Theano:new features and speed improvements.
   Deep Learning and Unsu-pervised Feature Learning NIPS 2012 Workshop, 2012, https://arxiv.org/pdf/1211.5590.pdf .
   
10. Ramsri. "Viola Jones face detection and tracking explained",Youtube, 16 Eylül 2012, https://youtu.be/WfdYYNamHZ8 .

11. Workshop Murtaza's -Robotics and AI. "LEARN OPENCV in 3 HOURS with Python | Including 3x Example Projects",Youtube, 25 Mart 2020, https://youtu.be/WQeoO7MI0Bs .

12. "Face Detection using Haar Cascade". OpenCV. Web. 10.03.2021. https://docs.opencv.org/4.0.0/d7/d8b/tutorial_py_face_detection.html .

13. "Hata Çözümleri". StackOverflow. Web. https://stackoverflow.com/ .

14. humandecoded,TOM. "People-Detector",Github, 16 Ocak 2020, https://github.com/humandecoded/People-Detector .

15. Engineering,of,School,University,Stanford. "Lecture 1 | Introduction to Convolutional Neural Networks for Visual Recognition",Youtube, 11 Ağustos 2017, https://youtu.be/vT1JzLTH4G4 .

16. "Python Project – Auto-capture Selfie by Detecting Smile". Data Flair. Web. https://data-flair.training/blogs/python-project-capture-selfie-by-detecting-smile/ .

17. Kharwal,Aman. "Computer Vision Projects with Python". Medium. Web. https://becominghuman.ai/computer-vision-projects-with-python-ecfac58ded18 .

18. Luvizon,Diogo. "vehicle-dsm",Github, 12 Şubat 2019, https://github.com/dluvizon/vehicle-dsm .

19. ATALLA,RAMY. "Car_lane_sign_detection",Github, 13 Ocak 2017, https://github.com/ramitix/Car_lane_sign_detection .

20. Çelik, U., Oral, M. (2003). Motorlu Araçlar İçin Plaka Tanıma Sistemi, Elektrik-Elektronik Bilgisayar Mühendisliği 10. Ulusal Kongresi, (pp. 499-502), İTÜ : İstanbul.

 
 
**3- ZORLUKLAR**

İmplementasyon safhasında, yanlış tespitler yapılmış ve kod hataları alınmıştır.Stackoverflow, Youtube, Github gibi platformlar sayesinde düzeltmeler yapılarak, kod hataları giderilmiştir.

Yanlış Tespitler:

![z1](https://user-images.githubusercontent.com/56633000/115929407-716ac280-a490-11eb-9648-1e0c6625a3b4.PNG)

Video çekilen kamera hareket halinde olduğundan sanki nesneler de hareket ediyor gibi algılanmıştı.

![z2](https://user-images.githubusercontent.com/56633000/115929623-c8709780-a490-11eb-933e-8cdac3a172b1.PNG)

Birbirine daha yakın insanların sayımında hatalar çıkmıştı.

Kod Hataları:

1. IndentationError: unindent does not match any outer indentation level

2. error: OpenCV(4.5.1) C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-oduouqig\opencv\modules\core\src\arithm.cpp:669: error: (-209:Sizes of input arguments do not match) The operation is neither 'array op array' (where arrays have the same size and the same number of channels), nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'

Bu sorun, bir iddianın başarısız olduğunu söylüyor. Dosya verilen yolda yoksa, cv2 bu hatayı döndürür. Bu nedenle, dosyanın verilen yolda olup olmadığını kontrol edin.


#### Öğrenilen Kavramlar 
DNN (Derin Sinir Ağı): Canlıların davranışlarını inceleyip, matematiksel olarak modelleyip, benzer yapay modellerin üretilmesine sibernetik denir. Eğitilebilir, adaptif ve kendi kendine organize olup öğrenebilen ve değerlendirme yapabilen yapay sinir ağları ile insan beyninin öğrenme yapısı modellenmeye çalışılmaktadır. Aynı insanda olduğu gibi yapay sinir ağları vasıtasıyla makinelerin eğitilmesi, öğrenmesi ve karar vermesi amaçlanmaktadır.  
  
Tek Katmanlı Algılayıcılar: Tek katmanlı yapay sinir ağları sadece girdi ve çıktı (Ç) katmanlarından oluşur. Çıktı üniteleri bütün girdi ünitelerine (X) bağlanmaktadır ve her bağlantının bir ağırlığı (W) vardır. İki girdi ve bir çıktıdan oluşan tek katmanlı bir yapay sinir ağıdır. 

Bu ağlarda süreç elemanlarının değerlerinin ve dolayısıyla ağın çıktısının sıfır olmasını önleyen bir de eşik değeri (Φ) vardır ve değeri daima 1’dir. Ağın çıktısı ağırlıklandırılmış girdi değerlerinin eşik değeri ile toplanması sonucu bulunur. Bu girdi ile bir aktivasyon fonksiyonundan geçirilerek ağın çıktısı hesaplanır. Tek katmanlı algılayıcılarda çıktı fonksiyonu doğrusal bir fonksiyondur ve 1 veya -1 değerlerini almaktadır. Eğer çıktı 1 ise birinci sınıfa -1 ise ikinci sınıfa kabul edilmektedir.  

Çok Katlı Algılayıcılar: Algılayıcı ve Adaline yöntemleri doğrusal olmayan çözümler üretemediği için hem mimari hem de eğitim algoritması açısından iyileştirilmiş Çok Katmanlı Algılayıcı (MLP) ağı önerilmiştir. Mimari açıdan doğrusal olmayan aktivasyon fonksiyonuna sahip birçok nöronun birbirine hiyerarşik olarak bağlandığı bir yapıya sahip olan MLP, Algılayıcı ve Adaline yöntemlerinin avantajları yanı sıra geri-yayılım adındaki öğrenme sistemini kullanmaktadır ve genel olarak yapay sinir ağları ileri beslemeli ve geri beslemeli ağlar olarak ikiye ayrılmaktadır.  

-İleri Beslemeli Ağlar: 

![b](https://user-images.githubusercontent.com/56633000/115928215-70389600-a48e-11eb-8b8b-2b115c8296e3.PNG)

İleri beslemeli sinir ağları tek yönlü sinyal akışı için izin verir. Ayrıca, ileri beslemeli sinir ağları çoğu katmanlar halinde organize edilmektedir.İleri beslemeli yapay sinir ağında, hücreler katmanlar şeklinde düzenlenir ve bir katmandaki hücrelerin çıkışları bir sonraki katmana ağırlıklar üzerinden giriş olarak verilir. Giriş katmanı, dış ortamlardan aldığı bilgileri hiçbir değişikliğe uğratmadan ara (gizli) katmandaki hücrelere iletir. Bilgi, ara ve çıkış katmanında işlenerek ağ çıkışı belirlenir.  

-Geri Beslemeli Yapay Sinir Ağları:

![ab](https://user-images.githubusercontent.com/56633000/115928324-965e3600-a48e-11eb-9b92-3c460f58b76d.PNG)

Geri beslemeli Yapay Sinir Ağları (YSA)’ da, en az bir hücrenin çıkışı kendisine ya da diğer hücrelere giriş olarak verilir ve genellikle geri besleme bir geciktirme elemanı üzerinden yapılır. Geri besleme, bir katmandaki hücreler arasında olduğu gibi katmanlar arasındaki hücreler arasında da olabilir. Bu yapısı ile geri beslemeli YSA, doğrusal olmayan dinamik bir davranış gösterir. 


#### Şu anda implementasyon ve test aşaması birlikte yürütülmektedir.Araçlar, insanlar ve yol şeritleri ayrı şekilde tespit edilmiş; kodu yazılmıştır.Bundan sonraki kısımda araç ve insanlar arasında ilişki kodu yazılarak, kaza olma olasılıkları üzerine çalışılacaktır.Kodlama kısmı ise tamamen bittikten sonra, yapılan araştırmalar ve detaylı proje rapora yazılıp, sunumu yapılacaktır.



**4- ARAÇLAR**

Projede kullandığım araçlar: 

1. Jupyter Notebook : Python dilinde projemi geliştirdiğim, etkileşimli bir ortam sağlayan açık kaynak kodlu bir programdır.  

2. Spyder : Python dilinde projemi geliştirdiğim, açık kaynaklı platformlar arası entegre geliştirme ortamıdır.  

3. OpenCV : Görüntü işleme uygulamalarında kullandığım açık kaynaklı kütüphanedir.

4. Youtube : Test için kullandığım gerekli video kaynaklarını ve faydalandığım eğitim videolarını içinde barındıran web sitesidir.

5. Github : Görüntü işleme gibi birçok farklı konuda proje geliştirmiş insanların repolarını incelediğim, projeme yön vermemi sağlayan web tabanlı bir depolama servisidir.

6. Numpy : NumPy, Python programlama dili için bir kütüphane olup, büyük, çok boyutlu diziler ve matrisler için destek eklerken, bu dizilerde çalışmak için yüksek düzeyli matematiksel fonksiyonların geniş bir koleksiyonudur.  

7. TensorFlow : TensorFlow, bir dizi görev arasında veri akışı ve türevlenebilir programlama için kullanılan ücretsiz ve açık kaynaklı bir yazılım kütüphanesidir. Sembolik bir matematik kütüphanesidir ve sinir ağları gibi makine öğrenimi uygulamaları için de kullanılır.  

8. Udemy : Udemy.com üzerinden faydalandığım kursları içinde barındıran, kitlesel çevrimiçi açık ders ve bir çevrimiçi öğrenme platformudur.   

9. Stack Overflow : Aldığım kod hatalarını düzeltmek için başvurduğum kullanıcı odaklı soru cevap sitesidir.      

  
  
