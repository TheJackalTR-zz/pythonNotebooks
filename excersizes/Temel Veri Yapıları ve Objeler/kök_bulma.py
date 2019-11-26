print("2.dereceden bir bilinmeyenli denklemin köklerini bulma")

# Denklem : ax^2 + bx + c

a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
c = int(input("c sayısını giriniz: "))

delta = b ** 2 - 4 * a * c

firstRoot = (-b - delta ** 0.5) / 2 * a
secondRoot = (-b + delta ** 0.5) / 2 * a

print("\nBirinci Kök: {}\nİkinci Kök: {}\n".format(firstRoot, secondRoot))
