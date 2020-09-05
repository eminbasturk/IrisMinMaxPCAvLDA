# IrisMinMaxPCAvLDA
Iris veri setine min-max normalizasyonu ve normalizasyon üzerinden PCA ve LDA yöntemlerinin uygulanıp karşılaştırılması.

Iris Veri Seti
Iris veri seti, İngiliz istatistikçi, öjenikçi ve biyolog Ronald Fisher’ın 1936 tarihli makalesinde kullandığı çok değişkenli bir veri kümesidir. Iris veri seti, üç Iris türünün (Iris setosa, Iris virginica ve Iris versicolor) her birinden 50 gözlem birimi olmak üzere toplamda 150 gözlem birimi içerir. Her gözlem birimi için dört farklı özellik ölçülmüştür: çanak yaprak uzunluğu (sepal length), çanak yaprak genişliği (sepal width), taç yaprak uzunluğu (petal length) ve taç yaprak genişliği (petal width). Özellikler santimetre cinsinden ölçülmüştür. 

Min – Max Normalizasyonu
Değişkenlerin ortalaması (μ = 0) ve standart sapması (σ = 1) üzerinden ölçeklendirilen değişkenleri [0,1] aralığına getirilen, minimum ve maksimum değerin sırasıyla 0 ve 1 olduğu normalizasyon yöntemidir. Birbirinden farklı pek çok verinin, normalize edilerek kendi içinde karşılaştırılmasını sağlar. 
Min – Max Normalizasyonunun Matematiksel Formülü
x^'=  (x-min⁡(x))/(max⁡(x)-min⁡(x) )

PCA (Principal Component Analysis)
	Çok değişkenli verinin ana özelliklerini daha az sayıda değişken/bileşen ile temsil etmektedir. Başka bir deyişle PCA’nın amacı küçük miktarda bir bilgi kaybını göze alıp değişken boyutunu azaltmaktır.
Varyans
Verilerin dağılımının belirler.
Var(X)=1/n ∑▒〖(X_i-X ̅)〗^2 
Kovaryans Matrisi
İki değişkenin birlikte değiştiği seviyeyi gösterir.
Cov(X,Y)=1/n ∑▒〖(X_i-X ̅)〖(Y_i-Y ̅)〗^T 〗
Cov(X,X)=1/n ∑▒〖(X_i-X ̅)〖(X_i-X ̅)〗^T 〗
Özvektör ve Özdeğerler
Özvektörler maksimum varyans yönünü gösterir. Ona karşılık gelen özdeğerler ise karşılık gelen özvektörün önemini gösterir.
Av^→=λv^→
	PCA Yöntemininin Uygulanma Adımları
	Ortalamanın X’ten çıkarılması.
	Cov (X, X) değerinin hesaplanması.
	Kovaryans matrisinin özvektörlerinin ve özdeğerlerinin hesaplanması.
	Özvektörlerin, özdeğerlerine göre büyükten küçüğe sıralanması.
	İlk k özvektörünün seçilmesi ve orijinal n boyutlu veri noktalarının k boyutlarına dönüştürülmesi

PCA (Principal Component Analysis)
	Çok değişkenli verinin ana özelliklerini daha az sayıda değişken/bileşen ile temsil etmektedir. Başka bir deyişle PCA’nın amacı küçük miktarda bir bilgi kaybını göze alıp değişken boyutunu azaltmaktır.
Varyans
Verilerin dağılımının belirler.
Var(X)=1/n ∑▒〖(X_i-X ̅)〗^2 
Kovaryans Matrisi
İki değişkenin birlikte değiştiği seviyeyi gösterir.
Cov(X,Y)=1/n ∑▒〖(X_i-X ̅)〖(Y_i-Y ̅)〗^T 〗
Cov(X,X)=1/n ∑▒〖(X_i-X ̅)〖(X_i-X ̅)〗^T 〗
Özvektör ve Özdeğerler
Özvektörler maksimum varyans yönünü gösterir. Ona karşılık gelen özdeğerler ise karşılık gelen özvektörün önemini gösterir.
Av^→=λv^→
	PCA Yöntemininin Uygulanma Adımları
	Ortalamanın X’ten çıkarılması.
	Cov (X, X) değerinin hesaplanması.
	Kovaryans matrisinin özvektörlerinin ve özdeğerlerinin hesaplanması.
	Özvektörlerin, özdeğerlerine göre büyükten küçüğe sıralanması.
	İlk k özvektörünün seçilmesi ve orijinal n boyutlu veri noktalarının k boyutlarına dönüştürülmesi

PCA ve LDA Yöntemleriyle Elde Edilen Sonuçların Karşılaştırılması
LDA: İki sınıf arasındaki farkı en üst düzeye çıkaran yönü bulur.
PCA: Verilerdeki varyansı en üst düzeye çıkaran yönü bulur.
LDA, Bağımsız ve bağımlı değişken arasındaki ilişkinin gücüne dayalı olarak değişken azaltma için kullanılır.
PCA, Bağımsız değişkenlerin doğrusallığına bağlı olarak değişkenleri azaltmak için kullanılır.
PCA gözetimsiz öğrenme algoritmasıdır. LDA gözetimli öğrenme algoritmasıdır. Gözetimsiz öğrenme, gözetimli öğrenmeden farklı olarak, verileri sebep-sonuç ya da giriş-çıkış şeklinde etiketlenmeden, veri içerisinde var olan ilişkilerin ve yapıların öğrenmesidir.
PCA kümeleme problemlerinde kullanılırken, LDA sınıflandırma problemlerinde görülür.
Öncesinde minimum maximum yöntemi ile normalize edilen verinin üzerine uygulanan bu yöntemler [0,1] arasına yerleştirilmektedir. 
Grafiklerde görüldüğü üzere her iki yöntem de başarılı bir şekilde uygulanmıştır. Verileri gözlemlediğimizde setosa ve virginica iris çiçeklerinde görülen veriler ile versicolor iris çiçeğinde görülen veriler arasında bir zıtlık bulunmaktadır. Aynı şekilde iki yöntem arasında da bu veriler üzerinden karşılaştırma yaptığımızda bir zıtlık görülmektedir. Bu zıtlığın sebebi PCA’nın veri noktaları arasındaki mesafeyi maksimize etmeye çalışırken LDA’nın sınıflar arasındaki mesafeyi maksimize etmeye çalışmasındandır.

