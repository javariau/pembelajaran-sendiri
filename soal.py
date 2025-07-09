kendaraan  = input("jenis kendaraan : ").lower()
darurat = "ambulance,pemadam kebakaran , truck tentara"

print(f"jenis kenadaraan : {kendaraan}")

if kendaraan == "mobil" :
    print("tarif 12 rp")

elif kendaraan == "motor":
    print("tarif 5 rp")

elif kendaraan == "truck":
    print("tarif 15")

elif kendaraan  in darurat:
    print("GRATIS")