nama = "ravikwalhidayah" #ini namanya variabel 
pangilan = "ravik"
print(nama)
print("nama saya adalah " + nama)
print("nama pangilan saya " + pangilan)

#tipe data number intenger 
umur = 20 # kalau mau di gabungkan dengan sebuah string ( kalimat ) harus di ubah dulu ke string
print ("umur saya adalah " + str(umur) ) # tambahin str di depan umur lalu tutup kurung

#tipe data number float
tinggi = 170.3 
print("tinggi saya adalah " + str(tinggi) + "cm") #sama harus di bungkus dengan str 

print(type (nama)) # untuk mengetahui tipe data dari sebuah variabel





#operasi matematika
angka1 = 100
angka2 = 200
print (angka1 + angka2) # penjumlahan
print (angka2 - angka1) # pengurangan
print (angka1 * angka2) # perkalian
print (angka2 / angka1)
print (angka2 % angka1) # modulo sisa dari sebuah pembagian 

#tipe data bolean yaitu true dan false ini akan menjadi pondasi dalam membuat sebuah perkondisian di python nantiknya 
isbig = True # biasa digunakan untuk bolean 
has = False



# #statmen
# uangSaya = 7000
# hargaGame = 6000
# waktu = False

# # kondiasional di python, 
# # and untuk menambahkan syart lain, 
# # or cukup 1 syarat satu saja yang terpenuhi
# if uangSaya >= hargaGame or waktu :
#     print("tabungan kamu cukup untuk membeli game")
# else :
#     print("tabungan kamu ngak cukup untuk membeli game")
    
    
uangSaya = 100000
lensaFix = 5000
tripord = 300
memory = 200
if uangSaya >= lensaFix :
    print("bisa beli lensa fix")

elif uangSaya >= tripord :
    print("bisa beli tripord")
elif uangSaya >= memory :
    print("bisa beli memory")
else :
    print("uang kamu ngak cukup untuk beli apa apa")
    

# kondisi dengan mengunakan match & case 
day = 14
match day:
    case 1 :
        print ("senin")
    case 2 :
        print ("selasa")
    case 3 :
        print ("rabu")
    case 4 :
        print ("kamis")
    case 5 :
        print ("jumat")
    case 6 :
        print ("sabtu")
    case 7 :
        print ("minggu")
    case _ : # ini sebagai penutup jika semua kondisi tidak terpenuhi
        print ("hari tidak di ketahui")
        

# list variabel
namaMurid = ["ravik", "dayat", "siti", "budi", "ani", "rani",]
namaMurid.append("dina") # untuk menambahkan data baru dalam list tersebt
print (namaMurid[0])
#cara ganti nilai di dalam variabel 
namaMurid[1]="dion"
print (namaMurid[1])
print (len(namaMurid)) # untuk menghitung panjang dari sebuah list

if len(namaMurid) >= 6 :
    print ("kelas di mulai")
else :
    print ("kelas di tunda dulu")
    
    
    