from datetime import *
#Nedense sırf "import date" kullanınca .strptime fonksiyonu kullanılamıyor

#Replit output'u Greenwich Mean Time'ı esas alırken, IDLE output'u sizin bilgisayarınızın
#Timezone'unu esas alır

dogumgunu=datetime.strptime(input("Ne zaman doğdun? (Gün.Ay.Yıl) \n"),"%d.%m.%Y")
#Takes as date format with dots inbetween
yas=datetime.now()-dogumgunu

minutes=int(yas.total_seconds()/60)
hours=int(minutes/60)
weeks=int(yas.days/7)
months=int(yas.days/30)
years=int(yas.days/365)

print("\n{} saniyedir = {} dakikadır = {} saattir = {} gündür = {} haftadır = {} aydır = {} yıldır hayattasınız.\n".format(int(yas.total_seconds()), minutes, hours, int(yas.days), weeks, months, years)) 

remainder=yas.total_seconds()

def convert_post(factor, unit): #(Çevrilirken kaça bölüneceği, printte bahsedilen birim)
  global remainder
  
  remainder=(remainder-int(remainder))*factor #Bir alt birimin hesabı gerçekleşir
  print(int(remainder), end=unit) #Hesaplanan birim tamsayı olarak gösterilir

remainder=remainder/(60*60*24*365) #Toplam saniyeden toplam yıl hesaplanır
print("Toplamda; " + str(int(remainder)), end=" yıl, ") #int olarak yıl print edilir
convert_post(12, " ay, ")
convert_post(4, " hafta, ")
convert_post(7, " gün, ")
convert_post(24, " saat, ")
convert_post(60, " dakika, ")
convert_post(60, " saniye yaşadınız.")
