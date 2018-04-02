for i in range(0,3) :
    birincisayi = int(input("Birinci sayıyı gir:"))
    ikincisayi = int(input("İkinci sayiyi gir:"))
    islem = input("Yapacağınız işlemi seç(+,-,/,*):")
    if islem == "+" :
        print (birincisayi+ikincisayi)
    elif islem == "-" :
        print (birincisayi-ikincisayi)
    elif islem == "*" :
        print (birincisayi*ikincisayi)
    elif islem =="/" :
        print (birincisayi/ikincisayi)
    elif islem == "exit":
        break
    else:
        print("Lütfen belirtilen operatörlerden birini gir")  
