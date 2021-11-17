inputibu = str (input ( "Ibu : "))
print ("Anak : ok")
print ("*Anak Pergi ke Toko")

inputanak = str (input("Anak ke Toko : Apakah ada susu? (ada/tidak) : "))
if inputanak == "ada":
    hasila = print ("*Anak mengecek Harganya Cukup")

else :
    print ("*Anak pulang ke rumah")
    print("*Menyerahkan hasil belanjanya kepada ibu")

hasilbarua = hasila
hasilbarua = str (input("Anak ke Toko : Apakah ada telur? (ada/tidak)  :  "))
if hasilbarua == "ada":
    hasilbaruaa = print ("*Anak membeli susu dan telur")

elif hasilbarua == "tidak":
    hasiltdk = print("*Anak hanya membeli susu")

print ("*Anak pulang ke rumah")
print ("*Menyerahkan hasil belanjanya kepada ibu")

