from datetime import datetime
import random
import keyboard #tuş basışını okumak için
import multiprocessing #birden fazla işlemi paralel yürütmek için

global bf #Burada multiprocessing'i kullandığımdan ve işlemlerin hepsi kendi fonksiyonlarının içinde olduğundan, olası bir hataya karşı herşeyi başlangıçta ve de kullanıldıkları fonksiyonların içinde global olarak kaydetmeye karar verdim
global dummyRep
global ans
global remdum
global remans
global yanlislar
global timeBool

def timeStart(press): #(basılan tuş; hangi tuş olduğu önemli değil)
  global bf
  global timeBool

  if press.event_type == keyboard.KEY_DOWN and timeBool: #if press'in event type'ı klavye tuşuna basışsa, ve...
    bf = datetime.now()
    timeBool=False #main'de başlangıçta (son 7 satır), True olarak define edilip, ilk tuş basılışında False yapılır, yoksa kullanıcı her tuşa bastığında timer resetlenir
    #print("Time started!")  # Debug

def KelimeAyirici(cumle, rem): #(cümlenin geri kalanı, return edilecek kelime)
  for i in cumle: #cümlenin geri kalanından harf harf kelime variable'ına ekler, ta ki boşluğa gelene kadar. Sonrasında loop'dan çıkıp kelimeyi return'ler
    rem+=i
    if i==" ":
      break
  return rem

def everythingStart(): #Bu aslında programın asıl kısmı. Kelime ayırıcı ve timer dışında işlevlerin bütün geri kalan hepsi bunun içinde
  global dummyRep
  global ans
  global bf
  global remdum
  global remans
  global yanlislar

  replikler = ["Sen Bihter Ziyagilsin aptallık etme", "Dön bak arkana yeğen, gitmez dediğin kaç kişi var hayatında", "Hayatın kuralı bu ne kadar uzağa gidersen git, başladığın yere dönersin sonunda", "Aman Ali Rıza Bey ağzımızın tadı kaçmasın", "İki kişinin bildiği sır değildir", "Olay yerine yakınız", "Acele edin çocuklar, fazla zamanımız yok"]
  replik = random.choice(replikler)

  print("Bu repliğin aynısını yazabileceğiniz kadar hızlı yazınız:\n{}".format(replik))

  dummyRep = replik.lower() #karşılaştırılmanın kolaylaşması için seçilen replik de kullanıcı cevabı da küçük harfe çevrilir
  ans = input("\n").lower()

  remdum = "" #Kullanılacak dummy listeler
  remans = "" 
  yanlislar = [] #Typo yapılan kelimelerin kaydedileceği listenin initialize edilmesi

  if dummyRep == ans: #input random repliğe tamı tamına uyduğunda
    af = datetime.now() 
    hiz = af - bf #timeStart'ta ilk alınan global bf, yazının bitiminde tekrar alınan zamandan çıkarılır
    saniye = hiz.total_seconds()
    letter_per_second = round(len(replik) / saniye, 1)
    print("Skorunuz: {} saniye".format(saniye))
    print("Saniyede {} harf".format(letter_per_second))
  else: #eğer inputta yanlışlık varsa
    print("Typo'nuz var")
    while True:
      remdum=KelimeAyirici(dummyRep,remdum) #Boşluğa rast gelene kadar KelimeAyirici fonksiyonumu kullanarak sırayla kelimeleri orijinal replikten ve kullanıcı cümlesinden sırayla dummy stringlere çeker
      remans=KelimeAyirici(ans,remans)
      if remdum!=remans: #Eğer birbirlerine uyuşmazlarsa yanlışlar listesine ekler
        yanlislar.append(remans)
      dummyRep=dummyRep.removeprefix(remdum) #while loop'unun içinde işlemin sonraki kelimelerden devam ederek tekrar edilmesi için orijinal replik ve kullanıcı cevabından çektiğimiz kelimeleri sileriz
      ans=ans.removeprefix(remans)
      remdum="" #sonraki loop iterasyonuna hazırlık için dummy stringleri boşaltırız
      remans=""
      if dummyRep=="": #orjinal replik stringi en sonunda tamamen boş kaldığında bu loop'tan çıkar
        break
    print("Yanlış yazdığınız kelimeler: " + ", ".join(yanlislar)) #sırayla yanlış kelimeler listesindekileri yanına printler

def process1():
  keyboard.on_press(timeStart) #herhangi bir keyboard press'inde timeStart'ı çağırır

def process2():
  everythingStart()
#process1 ve process2, p1 ve p2 variable'larına atanır
timeBool=True
p1 = multiprocessing.Process(target=process1())
p2 = multiprocessing.Process(target=process2())
p1.start()
p2.start()
#start ve joinler sayesinde bu processler daha başlangıçtan yürütülüp paralel çalışabilir
p1.join()
p2.join()
