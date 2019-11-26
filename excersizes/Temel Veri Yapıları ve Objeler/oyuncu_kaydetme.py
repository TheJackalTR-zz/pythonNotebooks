print("Oyuncu Kaydetme")

ad = input("oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

bilgiler = [ad, soyad, takım]

print("\nBilgiler Kaydediliyor...\n")

print("Oyuncunun Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı: {}\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Bilgiler Kaydedildi")
