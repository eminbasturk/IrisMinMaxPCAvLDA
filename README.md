# IrisMinMaxPCAvLDA
Iris veri setine min-max normalizasyonu ve normalizasyon üzerinden PCA ve LDA yöntemlerinin uygulanıp karşılaştırılması.

## Iris Veri Seti
Iris veri seti, İngiliz istatistikçi, öjenikçi ve biyolog Ronald Fisher’ın 1936 tarihli makalesinde kullandığı çok değişkenli bir veri kümesidir. Iris veri seti, üç Iris türünün (Iris setosa, Iris virginica ve Iris versicolor) her birinden 50 gözlem birimi olmak üzere toplamda 150 gözlem birimi içerir. Her gözlem birimi için dört farklı özellik ölçülmüştür: çanak yaprak uzunluğu (sepal length), çanak yaprak genişliği (sepal width), taç yaprak uzunluğu (petal length) ve taç yaprak genişliği (petal width). Özellikler santimetre cinsinden ölçülmüştür. 

## Iris Veri Setinin Elde Edilmesi
![y1](https://user-images.githubusercontent.com/52385702/92302835-08bdec80-ef78-11ea-96d0-636ed01bb83f.png)

## Min – Max Normalizasyonu
Değişkenlerin ortalaması (μ = 0) ve standart sapması (σ = 1) üzerinden ölçeklendirilen değişkenleri [0,1] aralığına getirilen, minimum ve maksimum değerin sırasıyla 0 ve 1 olduğu normalizasyon yöntemidir. Birbirinden farklı pek çok verinin, normalize edilerek kendi içinde karşılaştırılmasını sağlar. 

## Min – Max Normalizasyonunun Matematiksel Formülü
![Screenshot_7](https://user-images.githubusercontent.com/52385702/92302922-e4aedb00-ef78-11ea-8897-55e6835a3f37.png)

## Min – Max Normalizasyonunun Veri Setine Uygulanması
![y2](https://user-images.githubusercontent.com/52385702/92302974-7c142e00-ef79-11ea-8b93-cf92b77ebd7f.png)

## Gerçek Veri ve Min – Max Normalizasyonu Uygulanan Veri
* ![y3](https://user-images.githubusercontent.com/52385702/92302989-9b12c000-ef79-11ea-9585-a7ea002d3279.png)
* ![c](https://user-images.githubusercontent.com/52385702/92303002-be3d6f80-ef79-11ea-82ad-19e1ba330381.png)

## PCA (Principal Component Analysis)
Çok değişkenli verinin ana özelliklerini daha az sayıda değişken/bileşen ile temsil etmektedir. Başka bir deyişle PCA’nın amacı küçük miktarda bir bilgi kaybını göze alıp değişken boyutunu azaltmaktır.

## Varyans
* Verilerin dağılımının belirler.
* ![Screenshot_7](https://user-images.githubusercontent.com/52385702/92303022-f17ffe80-ef79-11ea-9f6b-ab433bc0792a.png)

## Kovaryans Matrisi
* İki değişkenin birlikte değiştiği seviyeyi gösterir.
* ![Screenshot_8](https://user-images.githubusercontent.com/52385702/92303044-13798100-ef7a-11ea-903e-56381a1c0407.png)

## Özvektör ve Özdeğerler
* Özvektörler maksimum varyans yönünü gösterir. Ona karşılık gelen özdeğerler ise karşılık gelen özvektörün önemini gösterir.
* ![Screenshot_9](https://user-images.githubusercontent.com/52385702/92303063-3015b900-ef7a-11ea-9030-640a7c840cbd.png)

## PCA Yöntemininin Uygulanma Adımları
* Ortalamanın X’ten çıkarılması.
* Cov (X, X) değerinin hesaplanması.
* Kovaryans matrisinin özvektörlerinin ve özdeğerlerinin hesaplanması.
* Özvektörlerin, özdeğerlerine göre büyükten küçüğe sıralanması.
* İlk k özvektörünün seçilmesi ve orijinal n boyutlu veri noktalarının k boyutlarına dönüştürülmesi

## PCA Modülünün Oluşturulması
![y4](https://user-images.githubusercontent.com/52385702/92303098-74a15480-ef7a-11ea-8941-c1b8aac19d03.png)

## LDA (Linear Discriminant Analysis)
Amaç, bir veri kümesinin özelliklerinin bir doğrusal birleşimini bularak veriyi sınıflara ayırmaktır. 

## Matematiksel Model
* **Sınıf içi dağılım matrisi**
* ![Screenshot_10](https://user-images.githubusercontent.com/52385702/92303123-af0af180-ef7a-11ea-99e5-fb174514704e.png)
* **Sınıflar arası dağılım matrisi**
* ![Screenshot_11](https://user-images.githubusercontent.com/52385702/92303136-d3ff6480-ef7a-11ea-96da-2260f69c5467.png)

## Özdeğer ve Özvektör
* Aşağıdaki denklem için özdeğer ve özvektör hesaplanmalı
* ![Screenshot_12](https://user-images.githubusercontent.com/52385702/92303153-f3968d00-ef7a-11ea-8a8d-ca3cbba211c5.png)

## LDA Yöntemininin Uygulanma Adımları
* S_B ve S_W değerinin hesaplanması.
* S_w^(-1) S_B denkleminin özdeğerlerinin hesaplanması.
* Özvektörlerin, özdeğerlerine göre büyükten küçüğe sıralanması.
* İlk k özvektörünün seçilmesi ve orijinal n boyutlu veri noktalarının k boyutlarına dönüştürülmesi

## LDA Modülünün Oluşturulması
![Screenshot_5](https://user-images.githubusercontent.com/52385702/92303183-36f0fb80-ef7b-11ea-9ba9-fd254ff1f0da.png)

## PCA Yöntemi Uygulanan Min-Max Normalizasyonlu Verinin Gösterilmesi
* ![y7](https://user-images.githubusercontent.com/52385702/92303205-5f78f580-ef7b-11ea-8c5d-cf146f9e0763.png)
* ![Screenshot_2](https://user-images.githubusercontent.com/52385702/92303207-60118c00-ef7b-11ea-85a7-9fb80d31511a.png)

## LDA Yöntemi Uygulanan Min-Max Normalizasyonlu Verinin Gösterilmesi
* ![Screenshot_3](https://user-images.githubusercontent.com/52385702/92303236-95b67500-ef7b-11ea-8d40-a4db34fbf8ea.png)
* ![Screenshot_4](https://user-images.githubusercontent.com/52385702/92303238-964f0b80-ef7b-11ea-8a68-17191f885579.png)

## PCA ve LDA Yöntemleriyle Elde Edilen Sonuçların Karşılaştırılması
* LDA: İki sınıf arasındaki farkı en üst düzeye çıkaran yönü bulur.
* PCA: Verilerdeki varyansı en üst düzeye çıkaran yönü bulur.
* LDA, Bağımsız ve bağımlı değişken arasındaki ilişkinin gücüne dayalı olarak değişken azaltma için kullanılır.
* PCA, Bağımsız değişkenlerin doğrusallığına bağlı olarak değişkenleri azaltmak için kullanılır.
* PCA gözetimsiz öğrenme algoritmasıdır. LDA gözetimli öğrenme algoritmasıdır. Gözetimsiz öğrenme, gözetimli öğrenmeden farklı olarak, verileri sebep-sonuç ya da giriş-çıkış şeklinde etiketlenmeden, veri içerisinde var olan ilişkilerin ve yapıların öğrenmesidir.
* PCA kümeleme problemlerinde kullanılırken, LDA sınıflandırma problemlerinde görülür.
* Öncesinde minimum maximum yöntemi ile normalize edilen verinin üzerine uygulanan bu yöntemler [0,1] arasına yerleştirilmektedir. 
* Grafiklerde görüldüğü üzere her iki yöntem de başarılı bir şekilde uygulanmıştır. Verileri gözlemlediğimizde setosa ve virginica iris çiçeklerinde görülen veriler ile versicolor iris çiçeğinde görülen veriler arasında bir zıtlık bulunmaktadır. Aynı şekilde iki yöntem arasında da bu veriler üzerinden karşılaştırma yaptığımızda bir zıtlık görülmektedir. Bu zıtlığın sebebi PCA’nın veri noktaları arasındaki mesafeyi maksimize etmeye çalışırken LDA’nın sınıflar arasındaki mesafeyi maksimize etmeye çalışmasındandır.
