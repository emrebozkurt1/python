kelime = input("Bir Kelime Gir : ")
a = int(input("Başlangıç Sayısını Gir : "))
b = int(input("Bitiş Sayısını Gir : "))
if a > len(kelime) or b > len(kelime):
    print("Kelimeden Büyük Değer Gir!")
else:
    if a <= 0 or b <= 0:
        print("Sıfır Girilemez!")
    else:
        a = a-1
        print("Girdiğiniz Kelime : ", kelime)
        print("Kesilmiş Kelime : {}".format(kelime[:a]+kelime[b:]))
