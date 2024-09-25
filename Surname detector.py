EnteredName = input("Lütfen isminizi ve soyisminizi girin:")
surnameBuffer=""
singularNameCheck = False

for i in EnteredName:
  surnameBuffer+=i
  if i == " ":
    surnameBuffer=""
    singularNameCheck=True
    
if(singularNameCheck==False):
  print("Yazdığınız soy isimsiz tek bir isim.")
else:
  print("İsim: " + EnteredName.removesuffix(surnameBuffer))
  print("Soyisim: " +surnameBuffer)
