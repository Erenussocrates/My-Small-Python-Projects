import PyPDF2 #pdf dosyalarını okumak için gerekli bir kütüphane

#Bu projeyle aynı klasöre "input.pdf" adlı bir pdf yerleştirmeniz kullanmanız için yeterli

file=open("input.pdf", "rb") #r read için, b ise binary için, b gerekli çünkü pdf dosyasını binary'ye çevirmeden okuyamıyor

filereader=PyPDF2.PdfReader(file) #pdf dosyasının okunmuş halini kodda bir objeye atıyor

word=input("Arayacağınız kelimeyi giriniz (iki kelime veya boşluk olabilir):\n").lower()
count=0

for sayfa in filereader.pages: #pages[] aslında bir pdf objesinin içindeki sayfaların listesidir
#burda sayfa sayfa filereader.pages'in içinden geçecek
  count+=sayfa.extract_text().lower().count(word) #extract_text() fonksiyonu burda otomatikman her sayfanın içinde bulunan her boyutta yazıyı string formatına çeviriyor, lower ile küçültüp, count ile de bizim girdiğimiz sözcük dizisinin kaç kere geçtiğini alıyoruz
#extract_text() methodu sadece sayfa objesinin içinde işleyebilir

print("Aradığınız kelime verilen pdf'te {} kere geçiyor.".format(count))
file.close()
