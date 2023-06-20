import os
def clear_console():
    # Clear console for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

#untuk tampilin Jadwal
def tampilkan_Jadwal() : 
    clear_console()
    print("----------------------------------------------------------------")
    print('Senin   : {: <15}{: <8}'.format(daftarJadwal['Senin']['Name'], daftarJadwal['Senin']['Time']))
    print('Selasa  : {: <15}{: <8}'.format(daftarJadwal['Selasa']['Name'], daftarJadwal['Selasa']['Time']))
    print('Rabu    : {: <15}{: <8}'.format(daftarJadwal['Rabu']['Name'], daftarJadwal['Rabu']['Time']))
    print('Kamis   : {: <15}{: <8}'.format(daftarJadwal['Kamis']['Name'], daftarJadwal['Kamis']['Time']))
    print('Jumat   : {: <15}{: <8}'.format(daftarJadwal['Jumat']['Name'], daftarJadwal['Jumat']['Time']))
    print("----------------------------------------------------------------")

daftarJadwal = {
    'Senin' : {
        'id' : 1,
        'Name' : 'Sena',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Selasa' : {
        'id' : 2,
        'Name' : 'Selia',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Rabu' : {
        'id' : 3,
        'Name' : 'Rabita',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Kamis' : {
        'id' : 4,
        'Name' : 'Kamila',
        'Time' : '08:00 - 15:00',
        'Status' : 'Available'
    },
    'Jumat' : {
        'id' : 5,
        'Name' : 'Jumarni',
        'Time' : '08:00 - 12:00',
        'Status' : 'Available'
    },
}

def menu():
     while True:
        print("Selamat datang di aplikasi konseling")
        print("1. Masukan biodata")
        print("2. Jadwal yang sudah di booking")
        print("3. Keluar aplikasi")
        pilihan_menu = int(input("Silahkan memilih menu anda: "))

        if pilihan_menu == 1:
            # menu 1
            print("Masukan biodata anda:")
            nama = input("Nama: ")
            nim = input("NIM: ")
            # Lakukan proses input biodata lainnya sesuai kebutuhan

            print("Biodata telah berhasil dimasukkan.")

            tampilkan_Jadwal()

            # Jika tersedia konselor (nah kalo bagian ini gw gatau nih
            konselor = input("Apakah tersedia konselor?   (ya/tidak): ")
            if konselor.lower() == "ya":
                print("Jadwal booking telah ditambahkan.")

            # Kembali ke menu utama
            input("Tekan Enter untuk kembali ke menu utama.")

        elif pilihan_menu == 2:
            # menu 2
            print("Berikut jadwal yang sudah di booking")
        elif pilihan_menu == 3:
            # keluar aplikasi
            print("Terima kasih telah menggunakan aplikasi ini")
            break  
        else:
            print("Input tidak valid")


ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""

print(ascii_art)

Username = input("Masukan username anda: ")
print("Selamat datang,"+Username)
tampilkan_Jadwal()
menu()
