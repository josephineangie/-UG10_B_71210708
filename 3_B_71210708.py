bil1 = float(input("Bil1: "))
bil2 = float(input("Bil2: "))
kalimat = str(input("Masukkan kalimat: "))

if ("tambah" in kalimat): 
    hasil = bil1 + bil2
    print ("Hasil penjumlahan ", bil1, "dengan", bil2, "adalah", hasil)
elif ("kurang" in kalimat): 
    hasil = bil1 - bil2
    print ("Hasil pengurangan ", bil1, "dengan", bil2, "adalah", hasil)
elif ("bagi" in kalimat): 
    hasil = bil1 / bil2
    print ("Hasil pembagian ", bil1, "dengan", bil2, "adalah", hasil)
elif ("kali" in kalimat): 
    hasil = bil1 * bil2
    print ("Hasil perkalian ", bil1, "dengan", bil2, "adalah", hasil)
    
