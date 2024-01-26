'''
    isalpha() bu fonksiyon ne işe yarar ?

    isalpha(), Python'da bir karakter dizisinin (string) tamamen alfabetik karakterlerden oluşup oluşmadığını 
    kontrol eden bir metoddur. Bu metodun döndürdüğü değer True veya False olur.
İşlevi şu şekildedir:
Eğer karakter dizisi tamamen alfabetik karakterlerden oluşuyorsa, True döndürür.
Eğer karakter dizisi içinde alfabetik olmayan bir karakter (rakam, boşluk, noktalama işareti, sembol vb.) bulunuyorsa, False döndürür.
    '''

'''
    liste = ["a", "b", "c", "d"]
for indeks, eleman in enumerate(liste, start=1):
    print(f"Index: {indeks}, Değer: {eleman}")
    
    
    '''

'''
Tk    --> pencere


Label --> tkinter'da metin veya resim içeren bir etiket oluşturmanızı sağlar. Bu etiketler genellikle kullanıcı
arayüzünde bilgi göstermek veya belirli bir öğenin adını tanımlamak için kullanılır. Label'lar, genellikle kullanıcıya
bir açıklama, bilgi veya talimat sunmak için kullanılır.


Entry --> Tkinter'daki Entry widget'ı, kullanıcıdan metin veya veri girişi almak için kullanılır. Bu widget genellikle
kullanıcıya bir metin kutusu sağlamak ve bu metin kutusundan veri almak amacıyla kullanılır.Kullanıcıdan Bilgi Almak,Parola Girişi
Sayısal Girişler, de kullanılır yani sen klavyeden bir değer almalısın aslında.


Button


Text --> Text widget'ı, çok satırlı metin girişi veya görüntüleme için kullanılır ve Entry widget'ına kıyasla daha büyük
metin miktarlarını işleyebilir. Text widget'ı, kullanıcıdan bir paragraf veya daha uzun metin almak, çok satırlı girişlerle
çalışmak, veya büyük metin verilerini göstermek için kullanışlıdır.


Scale --> Scale, Tkinter kütüphanesinde bulunan bir widget'tır ve genellikle bir kaydırma çubuğu (slider) olarak bilinir.
Bu widget, bir sayısal değeri belirli bir aralık içinde seçmek için kullanılır. Kullanıcı, kaydırma çubuğunu sürükleyerek
veya doğrudan değeri girerek bir değeri seçebilir.


Spinbox --> Spinbox, kullanıcının belirli bir sayı aralığında bir değeri seçmesine olanak tanıyan bir Tkinter widget'ıdır.
Genellikle sayısal değerlerin seçilmesi için kullanılır. Kullanıcı, artırma ve azaltma düğmelerini kullanarak değeri seçebilir
veya doğrudan Spinbox'a sayıyı girebilir.


CheckButton --> (onay kutusu) Tkinter kütüphanesinde bir widget'tir ve genellikle kullanıcının bir seçeneği açma veya
 kapatma yeteneğini sunan bir kutucuk olarak kullanılır. Kullanıcı, bu kutucuğu işaretleyerek (seçerek) veya işareti
 kaldırarak (seçmeyerek) bir durumu temsil eden bir değeri kontrol edebilir.Aslında bir var mı yok mu sorusu gibi düşün
 kullanıcının bu işaretlemesine karşılık bende ona göre şekil alıyorum.


Radiobutton --> Tkinter kütüphanesinde bir widget'tir ve genellikle kullanıcının bir seçenek grubundan sadece bir
seçeneği seçmesine izin vermek için kullanılır. Örneğin, bir kullanıcının bir dizi renk arasından sadece bir rengi
seçmesini sağlamak için kullanılabilir.



sözlük iterable yapısında .items() ne işe yarar ?

Python'da, bir sözlük üzerinde iterasyon yaparken, sözlüğün hem anahtarlarını hem de değerlerini almak istiyorsanız
 .items() metodunu kullanabilirsiniz. Bu metodun kullanımı aşağıdaki gibidir:
 
 sozluk = {'anahtar1': 'deger1', 'anahtar2': 'deger2', 'anahtar3': 'deger3'}

for anahtar, deger in sozluk.items():
    print(f"Anahtar: {anahtar}, Değer: {deger}")

'''

