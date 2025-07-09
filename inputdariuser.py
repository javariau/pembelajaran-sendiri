# # mengambil input dari user
# # data yang di masukan pasti string

# # disini kita bisa menggunakan operator casting

data = input("masukan data :" )

print("data = ", data, " type=", type(data))


 # jika ingin mengambil int, maka 
angka = float(input("masukan angka :" ))
angka = int(input("masukan angka :" ))

print("data = ", angka, " type=", type(angka))
print("data = ", angka, " type=", type(angka))

data_bool = bool(int(input("masukan data boolean : "))) # kalau boolean dia agak susah kita harus memindahkan dulu ke integer baru keboolean ini salah satu cata paling gampang

print("data = ", data_bool, " type=", type(data_bool))