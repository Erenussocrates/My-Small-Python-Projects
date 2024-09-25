import random

#Text dosyaları açılıp variable'lara atanır
erkekisim=open("maleNames.txt","r")
kizisim=open("femaleNames.txt","r")
soyisim=open("surnames.txt","r")

erkekliste=[]
kizliste=[]
soyliste=[]
#Kullanılacak listeleri initialize eder
sec_ilk_list=[]
sec_iki_list=[]
sec_soy_list=[]

def kapat(): #Dosya kapatmalarını (sonda zorunlu) tek satıra indirir
  erkekisim.close()
  kizisim.close()
  soyisim.close()
  exit()

def listInit (file, liste):
  for i in file:
    liste.append(i.strip())
#Sırayla text dosyalarındaki her satırı kendi listelerine atıyor
listInit(erkekisim,erkekliste)
listInit(kizisim,kizliste)
listInit(soyisim,soyliste)

def firstDraw(liste, sec_list): #(Erkek veya kız isimleri listesi, seçilen isimler listesi)
  sec=random.choice(liste) #Bir isim listeden seçilir
  sec_list.append(sec) #Seçilen isim, seçilen isimler listesine eklenir
  liste.remove(sec) #Seçilen isim, ilk listeden kaldırılır

def secondDraw(liste, sec_list): #(Erkek veya kız isimleri listesi, seçilen isimler listesi)
  nullrand=random.randint(1,2)
  if nullrand==1: #50% şansla seçilen kişinin 1 veya 2 ismi olur
    sec=""
  else:
    sec=random.choice(liste)
  sec_list.append(sec)
  if sec!="": #Eğer kişinin 2 ismi olmazsa bu sefer isim listesinden birşey kaldırılmaz
    liste.remove(sec)

def famDraw(sec_ilk_list, sec_iki_list, sec_soy_list, i):
#(Seçilen ilk isim, seçilen ikinci isim, seçilen soyisimler listesi, sayıcı)
  global soyliste #Soyisimler erkek ve kızlar için ortak olabildiğinden, global kullanılabilir
  while True:
    sec=random.choice(soyliste)
    if sec!=sec_ilk_list[i] and sec!=sec_iki_list[i]:
#Seçilen soyismin ilk veya ikinci adla aynı olmamasına dikkat edilir
      sec_soy_list.append(sec)
      soyliste.remove(sec)
      break

def allDraw(liste, sec_ilk_list, sec_iki_list, sec_soy_list, i):
#3 fonksiyon bir araya getirilir
  firstDraw(liste, sec_ilk_list)
  secondDraw(liste, sec_iki_list)
  famDraw(sec_ilk_list, sec_iki_list, sec_soy_list, i)

gend=input("Erkek mi seçmek istiyorsunuz, kız mı, yoksa karma mı? (e/k/i)\n").lower()
numb=int(input("Kaç kişi seçmek istiyorsunuz?\n"))

if numb<=0:
  print("Lütfen pozitif bir sayı giriniz.")
  kapat()
elif numb>len(erkekliste) or numb>len(kizliste) or numb>len(soyliste):
  print("Listedeki isim sayısından fazla bir sayı girdiniz.")
  kapat()
if gend=="e":
  for i in range(numb):
    allDraw(erkekliste, sec_ilk_list, sec_iki_list, sec_soy_list, i)
elif gend=="k":
  for i in range(numb):
    allDraw(kizliste, sec_ilk_list, sec_iki_list, sec_soy_list, i)
elif gend=="i":
    for i in range(numb):
      gendrand=random.randint(1,2) #Karma seçenekte erkek veya kız çekilme ihtimali aynıdır
      if gendrand==1:
        allDraw(erkekliste, sec_ilk_list, sec_iki_list, sec_soy_list, i)
      else:
        allDraw(kizliste, sec_ilk_list, sec_iki_list, sec_soy_list, i)
else:
  print("Yanlış buton basışı")
  kapat()

#Seçilen isimler ve soyisimler sırayla kendi listelerinin içindedir
#Index'i aynı olan isim ve soyisim, aynı kişiye aittir ve böylece sırayla ekrana yazılır

for i in range(numb):
  print(sec_ilk_list[i]+ " " + sec_iki_list[i], end="")
  if sec_iki_list[i] == "": #Kişinin ikinci ismi boşluksa (yoksa), ekstra boşluk yazılmaz
    print(sec_soy_list[i])
  else:
    print(" " + sec_soy_list[i])

kapat()
