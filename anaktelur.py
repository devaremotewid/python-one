inputibu = str (input ( "Ibu : "))
print ("Anak : ok")
print ("*Anak Pergi ke Toko")

inputanak = str (input("Anak ke Toko : Apakah ada susu? (ada/tidak) : "))
if inputanak == "ada":
    hasila = print ("*Anak mengecek Harganya Cukup")

elif inputanak == "tidak":
    hasilt = print("*Anak Tidak jadi membeli susu")


hasilbaru = str (input("Anak ke Toko : Apakah ada telur? (ada/tidak)  :  "))
if hasilbaru == "ada":
    hasilbarua = print ("*Anak membeli susu dan telur")

elif hasilbaru == "tidak":
    hasiltdk = print("*Anak hanya membeli susu")

print ("*Anak pulang ke rumah")
print ("*Menyerahkan hasil belanjanya kepada ibu")

