#Mini project dasar pemograman
print("--------------------------")
print("Nama: Elmy Fadillah       ") 
print("NIM:2409116075            ")
print("Kelas: Sistem informasi B ")
print("--------------------------")

while True:
    nama =str(input("nama: "))
    jam_kerja =int(input("jumlah jam kerja: "))
    tarif_kerja_per_jam = int(input("tarif kerja per jam: "))
    total_gaji = jam_kerja * tarif_kerja_per_jam
    print(total_gaji)
    if jam_kerja > 160:
        total_gaji = total_gaji * (0.1) + total_gaji
    print(total_gaji)

    print('anda menerima gaji sebesar Rp.', total_gaji)
    print()

    pilihan = input("Apakah anda ingin menghitung gaji kryawan lagi?(ya/tidak):")
    if pilihan == "ya": 
        print("silahkan")
    if pilihan == "tidak": 
        print("program berhenti,Terima kasih")
        break
