
#üçgen alanı

tabanUzunlugu= input("Taban uzunluğunu girin:")
yukseklik= input("Yüksekliği girin:")

tabanUzunlugu = float(tabanUzunlugu)
yukseklik = float(yukseklik)

ucgenAlani = (tabanUzunlugu * yukseklik)/2

print("ucgenin alanı: ", ucgenAlani,"\n")


#okula kaç yaşında gittiğini bulma

isim = input("İsminizi girin: ")
soyisim = input("Soy isminizi girin: ")
yas = input("Yaşınızı girin: ")
okul = input("İlkokulunuzu girin: ")

yas = int(yas)

ilkokulyili = 2021 - (yas - 7)
print(okul, "'na ", ilkokulyili, " yılında gitmeye başladınız.\n" )


#tekerleme

tekerleme = "***Tekerleme*** \n Şu tarlaya bi şinik kekere mekere ekmişler.Bu tarlaya da bi şinik kekere mekere ekmişler. Şu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuk, bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğa demiş ki; 'ben bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum' demiş. Öteki tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsukta; ben de; 'bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum' demiş.\n"

print(tekerleme)
tekerleme = tekerleme.split()

kelime = input("Tekerlemede aramak istediğiniz kelimeyi yazın:")

result = tekerleme.count(kelime)
print("Tekerlemede ", result," adet ", kelime, " kelimesi bulunmaktadır.")




