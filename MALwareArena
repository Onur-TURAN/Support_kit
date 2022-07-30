Proje



Amaç : Bir Zararlı yazılım tespit edildikten sonra bunun analiz edilip ortan kaldırılması ve raporlanması sürezini kısaltıp otomatikleştirmek .

1. Aşama (Zararlı Yazılımı RasberyPI a atılması)
Bir RasberyPı içinde bir fronthend sayfası oluşturularak bir portta onun göstreimi yapılabilir . Kaydır bırak yoluyla bu zaralı yazılım index.html sayfasındaki alana bırakılacak . Bu işlemlerin hepsi gerçekleşirken her iki cihazda da internet kapalı olacak . Bİr tane Çalıştır butonu olacak . Buna bastığımızda ilgili dosya rasberyPı a atılacak .



2. Aşama(Database'i Taraması)
İlk başta atılan zaralı dosyanın hash değeri alınır. Python kullanarak database de taram yapılacak. Bu database'in oluşturulması daha sonra bahsedilecektir. 
---Eğer Bu hash değeri datbase de bulunuyorsa , zaralı yazılım ile ilgili bilgileri index.html de görüntülecekdir. Görüntülenme detayları daha sonra konuşulmalıdır.
---Eğer bu hash değeri veri tabanında bulunamazsa bir tane docker sistemi oluşturulacaktır . Bu doscker'ın işletim sistemi ilk baştaki bilgisayarın işletim sistemi ile aynı olmalıdır . Bu bilginin manuel değil de otomatik olarak çekilmesi gerekmektedir.


3. Aşama(Eğer veri tabanında hash bulunamazsa gerçekleşecek işlemler)
dockerın içine zaralı yazılım atılır ve orada çalıştırılması sağlanır.
Belirli bir süre bekledikten sonra dockerdaki log kayıtlarının tutulduğu dosyalar dockerın içinden rasberyPI a çekilir ve docker kapatılır .
Ilk seviye olarak bu log kayıtları ilgili bir siber güvenlik uzmanın incelenmesi için otomatik olark oluşturulmuş olur.






Problemler 

1 )
Veri tabanının içinde yer alan bilgiler neler olaracak. Demo versiyonu için veriler amele gibi elle girilebilir ama sonra bu işlemin otomatikleştirilmesi gerekmektedir . 



2 )
2. ve 3. aşamadaki işlemlerin gerşekleştirilmesi için bence önceden iyi bir çalışma yapılmalıdır . Yarışma anında tüm işlerin yapılması zor olacaktır.






Görev Dağılımı

Görevler yukarıdaki aşamalarca 3 e bölünerek dağıtılabilir .
 Bir kişi ağırlık olarak portta yayınlacak index.html in düzenlenmesinde kaydırıp bırakma mekanizmasının ayarlanmasında ve bu dosyanın rasbery pi a iletimi ve sonuçların hepsinin görüntülenmesi  aşamalarında çalışmalıdır
 İkinci kişi birinci kişi ile birlikte bu yazılımın rasbery e iletiminde , zararlı yazılımlarının hashlerinin ve o yazılım ile ilgi bilgilerin bulunduğu veri tabanın ayarlanmasında , python kullanarak hash değerlerinin veri tabanından kontrolünün sağlanmasında , eğer zararlı yazılım bulunursa sonuçların index.html e iletiminden  eğer bulunamzsa zararlı yazılımı docker içerisinde iletiminden sorumludur.
 Üçüncü kişi ikinci ile zaralı yazılımı docker içine iletiminden , kısaca dockera giriş içindeki işlemler ve docker dan çıkış ve log sonuçlarının görüntülenmesi ile ilgili her şeydejn sorumludur.
 
 
 
 
 
 
 
 
 
 Yazarın Notu:
 Bence 3. kişinin yapacağı işlere  daha sonra ağırlık verilebilir. 1. 2 aşama bir seviyeye geldikten sonra başlanabilir. 3. aşmadaki işlerle uğraçacak olan 1 ve 2 deki kişilere yardım edebilir.
 
 
EK :
Görev dağılımı ile ilgili geri dönüş bekliyorum .



