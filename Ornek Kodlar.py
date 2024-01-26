'''
grup3 = ['c','ç','l','u']
grup2 = ['b','k']
grup1 = ['j']


gruplar = {
    1: grup1, 2: grup2, 3: grup3
}

print(gruplar.keys())    # keyleri yani anahtarları çağırırken bunları alıp bir liste formatına tutuyor.
print(gruplar.values())  # valueları çağırırkende hepsinin bir liste içine alıyor ayrıca her bir value değerlerinide liste içine alıyor.
print(gruplar.items())   # topluca bunları bir liste şekline alıyor.ve her bir key-value değerini tuple içine alıyor.
print(gruplar.get(1))
'''

import tkinter

mywindow = tkinter.Tk()
mywindow.title("İsim Analizi")
mywindow.config(width=600,height=600,bg="black")

mylabel = tkinter.Label(mywindow,text="İsim Analizine Hoş Geldiniz\n"
                             "İsim ve Soy ismi boşluk BIRAKMADAN yazınız")
mylabelwrite=("Calibri",14)
mylabel.config(bg="black",fg="white",font=mylabelwrite)
mylabel.place(relx=0.5,rely=0.1,anchor="center")


myentry = tkinter.Entry(mywindow)
myentry.config(width=30)
myentry.place(relx=0.3,rely=0.2)



def isimisleme():
    isim = myentry.get()
    grup9 = ['ı', 'i', 'r', 'I', 'İ', 'R']
    grup8 = ['h', 'z', 'q', 'H', 'Z', 'Q']  # ben bunları herhangi bir yerden alamam çünkü bunlar özel gruplar
    grup7 = ['g', 'ğ', 'p', 'y', 'G', 'Ğ', 'P', 'Y']  # o yüzden aklıma bunları tanımlamaktan başka hiçbirşey gelmedi.
    grup6 = ['o', 'ö', 'f', 'O', 'Ö', 'F']
    grup5 = ['e', 'n', 'w', 'E', 'N', 'W']
    grup4 = ['d', 'm', 'v', 'D', 'M', 'V']
    grup3 = ['c', 'ç', 'l', 'u', 'ü', 'C', 'Ç', 'L', 'U', 'Ü']
    grup2 = ['b', 'k', 't', 'B', 'K', 'T']
    grup1 = ['a', 'j', 's', 'ş', 'A', 'J', 'Ş', 'S']

    # Harf gruplarını bir sözlükte(dictionary) topla
    gruplar = {
        1: grup1, 2: grup2, 3: grup3,  # iyice artık benim ana veri yapımı elimin içine aldım
        4: grup4, 5: grup5, 6: grup6,
        7: grup7, 8: grup8, 9: grup9
    }

    # Her grup için başlangıçta sayıyı sıfıra ayarla
    grup_sayilari = {i: 0 for i in range(1, 10)}  # grup_sayilari = {1: 0, 2: 0, 3: 0, ..., 9: 0}  bu şekilde bir
    # dictionary oluşturdu burada.

    # İsimdeki harfleri kontrol et
    for harf in isim:  # alitoker
        for grup, harfler in gruplar.items():
            if harf in harfler:
               global grup_sayilari[grup] = grup_sayilari[grup] + 1

def sonuçyazdır():
    # Sonuçları yazdır
    for grup, sayi in grup_sayilari.items():
        if sayi > 0:
            print(f"{grup}.Çakradan : {sayi} adet var.")

    # Çakradan eksik harfleri kontrol et
    eksik_cakralar = [grup for grup, sayi in grup_sayilari.items() if sayi == 0]

    # Eksik çakraları yazdır
    if eksik_cakralar:
        for eksik in eksik_cakralar:
            print(f"{eksik}. çakradan eksik harf bulunmamaktadır.")
    else:
        print("Girilen isimde tüm çakralar bulunmaktadır.")

mybutton = tkinter.Button(text="Hesaplayalım",command=isimisleme)
mybutton.place(relx=0.4,rely=0.3,anchor="center")

mylabelSonuç = tkinter.Label(text=sonuçyazdır)
mylabelSonuç.place(relx=0.4,rely=0.4,anchor="center")

mywindow.resizable(False, False) # ben buradada penceremin değişmemesini sağladım aslında.
mywindow.mainloop()            # ben bir pencere açmış isem zaten bunu koymak zorundayım çünkü bu olmadan benim pencerem
# ayakta kalamaz.