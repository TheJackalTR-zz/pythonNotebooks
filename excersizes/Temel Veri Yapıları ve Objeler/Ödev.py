# %% PROBLEM 1 - KULLANICIDAN ALINAN ÜÇ SAYIYI ÇARAPRAK FORMAT İLE YAZMA

a = int(input("Birinci sayıyı griiniz: "))
b = int(input("İkinci sayıyı giriniz: "))
c = int(input("Üçüncü sayıyı giriniz: "))

result = a * b * c

print("{} x {} x {} = {}".format(a, b, c, result))

# %% PROBLEM 2 - Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

boy = float(input("Boyunuzu giriniz(örnek: 1.77): "))
kilo = float(input("Kilonuuzu giriniz: "))

bmi = kilo / (boy * boy)

print("Your Height is: {}\nYour Weight is: {}\nYour BMI is: {}\n".format(boy, kilo, bmi))

#%% PROBLEM 3 - bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
# sürücünün toplam ne kadar ödemesini gerektiğini hesaplayın

amountOfMoneyBurnedPerKilometer = float(input("Aracın Kilometre başına kaç kuruş yaktığı: "))
totalKilometer = int(input("Aracın kat ettiği kilometre miktarı: "))

total = amountOfMoneyBurnedPerKilometer * totalKilometer

print("\nYour car cost's: {} per kilometer\nYour car goes: {} kilometer\nYou have to pay: {}\n"
      .format(amountOfMoneyBurnedPerKilometer, totalKilometer, total))

#%% PROBLEM 4 = Kullanıcıdan ad, soyad, ve numara bilgisini bunları alt alta yazdırmak

name = input("Enter your first name: ")
surname = input("Enter your last name: ")
phone = input("Enter your phone number: ")

print("\nYour name is: {}\nYour surname is: {}\nYour phone number is: {}".format(name, surname, phone))

# %% PROBLEM 5 - Kullanıcıdan alınan iki sayıyı birbirleri ile değişitir

a = input("a sayısını giriniz: ")
b = input("b sayısını giriniz: ")

print("\na sayısı: {}\nb sayısı: {}\n".format(a, b))

a, b = b, a
print("SWAP İŞLEMİNDEN SONRA")
print("\na sayısı: {}\nb sayısı: {}".format(a, b))

#%% PROBLEM 6 - Kullanıcıdan bir dik üçgenin dik olan iki kenarını alıp hipotenüs bulmak

a = int(input("Please enter the first side: "))
b = int(input("Please enter the second side: "))

c = (a ** 2 + b ** 2) ** 0.5

print("Hypotenuse: ", c)
