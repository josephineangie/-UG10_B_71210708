angka = int(input("Masukkan angka: "))

if ((angka % 2) == 0) and((angka % 3) != 0):
    jawab = "YA"
elif ((angka % 2) != 0) and ((angka % 3) == 0):
    print ("Bilangan tersebut habis dibagi 2 dan habis dibagi 3. Program dihentikan")
    finished ();
    
print ("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: ", jawab)

if ((angka % 5) != 0) or ((angka % 10) == 0):
    jawab = "IYA DONG"
elif ((angka % 5) == 0) or ((angka % 10) != 0):
    jawab = "TIDAK"

print ("Apakah bilangan tersebut juga tidak habis dibagi 5 atau dibagi 10? Jawab: ", jawab)