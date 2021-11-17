a=10
b=5

hasil = a+b

print ("Hasil", a, "+", b, "=", hasil)

print ("======Kalkulator Sederhana Sekali======")

adata = float (input ("Masukan angka : "))
bdata = float (input ("Masukan angka : "))

print ("===Pilih Operasi===")
print ("+")
print ("-")
print ("*")
print ("/")

opr = (input("masukan operasi : "))

if opr == "+":
    hasil = adata + bdata
    print ("Hasil", adata, "+", bdata, "=", hasil)
elif opr == "-":
    hasil = adata - bdata
    print ("Hasil", adata, "-", bdata, "=", hasil)
elif opr == "*":
    hasil = adata * bdata
    print ("Hasil", adata, "*", bdata, "=", hasil)
elif opr == "/":
    hasil = adata / bdata
    print ("Hasil", adata, "/", bdata, "=", hasil)
else :
    print ("harap masukan operasi (+ - * /)")