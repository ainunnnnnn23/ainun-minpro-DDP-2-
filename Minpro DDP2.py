from datetime import datetime

print("=================================================")
print("      MINI PROJECT DASAR DASAR PEMROGRAMAN       ")
print("=================================================")
print("Nama     : Asriah Ainun Fazah                    ")
print("NIM      : 2409116068                            ")
print("Kelas    : SISTEM INFORMASI - B                  ")
print("=================================================")

pengguna = {
    "admin": {"password": "admin123", "peran": "admin"},
    "pelanggan": {"password": "pelanggan123", "peran": "pelanggan"}
}

paket_foto = {
    1: {"nama": "Paket Hemat ", "harga": 250000,  "durasi": 1, "background": ["putih", "hitam"]},
    2: {"nama": "Paket Reguler", "harga": 400000,  "durasi": 2, "background": ["putih", "hitam", "biru"]},
    3: {"nama": "Paket Spesial", "harga": 600000, "durasi": 3, "background": ["putih", "hitam", "biru", "hijau", "merah"]}
}


jadwal_booking = {}

def masuk():
    while True:
        nama_pengguna = input("Saya adalah: ")
        kata_sandi = input("Masukkan kata sandi: ")
        if nama_pengguna in pengguna and pengguna[nama_pengguna]["password"] == kata_sandi:
            return pengguna[nama_pengguna]["peran"], nama_pengguna
        else:
            print("Maaf data yang dimasukkan tidak valid atau kata sandi salah. Silakan coba lagi.")

def tampilkan_paket_foto():
    print("=== DAFTAR PAKET STUDIO ===")
    for id, paket in paket_foto.items():
        print(f"{id}. {paket['nama']} - Harga: Rp{paket['harga']} - Durasi: {paket['durasi']} jam")
        print(f"background tersedia: {', '.join(paket['background'])}")
    input("Tekan Enter...")

def tambah_paket_foto():
    print("=== TAMBAH PAKET STUDIO ===")
    nama = input("Nama paket: ")
    harga = int(input("Harga paket: "))
    durasi = int(input("Durasi paket (jam): "))
    background = input("Masukkan pilihan background, :").split(',')
    background = [bg.strip() for bg in background]
    
    id_baru = max(paket_foto.keys()) + 1
    paket_foto[id_baru] = {"nama": nama, "harga": harga, "durasi": durasi, "background": background}
    print("Paket studio berhasil ditambahkan.")
    input("Tekan Enter untuk kembali...")

def update_paket_foto():
    tampilkan_paket_foto()
    id_paket = int(input("Masukkan paket studio yang akan diupdate: "))
    if id_paket in paket_foto:
        print("Masukkan informasi baru (biarkan kosong jika tidak ingin mengubah):")
        nama = input(f"Nama ({paket_foto[id_paket]['nama']}): ") or paket_foto[id_paket]['nama']
        harga = input(f"Harga ({paket_foto[id_paket]['harga']}): ") or paket_foto[id_paket]['harga']
        durasi = input(f"Durasi ({paket_foto[id_paket]['durasi']}): ") or paket_foto[id_paket]['durasi']
        background = input(f"Background saat ini: {', '.join(paket_foto[id_paket]['background'])}: ") or ', '.join(paket_foto[id_paket]['background'])

        paket_foto[id_paket]['nama'] = nama
        paket_foto[id_paket]['harga'] = int(harga)
        paket_foto[id_paket]['durasi'] = int(durasi)
        paket_foto[id_paket]['background'] = [bg.strip() for bg in background.split(',')]
        print("Paket foto berhasil diupdate.")
    else:
        print("ID paket tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def hapus_paket_foto():
    tampilkan_paket_foto()
    id_paket = int(input("Masukkan ID paket yang akan dihapus: "))
    if id_paket in paket_foto:
        del paket_foto[id_paket]
        print("Paket foto berhasil dihapus.")
    else:
        print("ID paket tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def lihat_jadwal_booking():
    print("=== JADWAL BOOKING ===")
    for tanggal, bookings in sorted(jadwal_booking.items()):
        print(f"Tanggal: {tanggal}")
        for booking in bookings:
            print(f"  - {booking['nama_pelanggan']}: {booking['paket']} (Background: {booking['background']}, ({booking['waktu']})")
    input("Tekan Enter untuk kembali...")

def lakukan_booking(pelanggan):
    tampilkan_paket_foto()
    id_paket = int(input("Masukkan paket yang ingin di-booking: "))
    if id_paket in paket_foto:
        nama_pelanggan = input("Masukkan nama anda: ")
        tanggal = input("Masukkan tanggal booking (YYYY-MM-DD): ")
        waktu = input("Masukkan waktu booking (HH:MM): ")

        print("Pilihan background:")
        for i in range (len(paket_foto[id_paket]['background'])):
            print(f"{i+1}. {paket_foto[id_paket]['background'][i]}")
        pilihan_bg = int(input("Pilih nomor background: "))
        background = paket_foto[id_paket]['background'][pilihan_bg - 1]
        
        if tanggal not in jadwal_booking:
            jadwal_booking[tanggal] = []
        
        jadwal_booking[tanggal].append({
            "nama_pelanggan": nama_pelanggan,
            "paket": paket_foto[id_paket]['nama'],
            "waktu": waktu,
            "background" : background
        })
        
        print(f"Booking berhasil untuk {nama_pelanggan} - {paket_foto[id_paket]['nama']} dengan background {background} pada {tanggal} {waktu}")
    else:
        print("ID paket tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def menu_admin():
    while True:
        print("======================================")
        print("===           MENU ADMIN           ===")
        print("======================================")
        print("         1. Lihat Paket Foto          ")
        print("         2. Tambah Paket Foto         ")
        print("         3. Update Paket Foto         ")
        print("         4. Hapus Paket Foto          ")
        print("         5. Lihat Jadwal Booking      ")
        print("         0. Keluar                    ")
        print("======================================")

        pilihan = input("Pilih menu (0-5): ")
        
        if pilihan == "1":
            tampilkan_paket_foto()
        elif pilihan == "2":
            tambah_paket_foto()
        elif pilihan == "3":
            update_paket_foto()
        elif pilihan == "4":
            hapus_paket_foto()
        elif pilihan == "5":
            lihat_jadwal_booking()
        elif pilihan == "0":
            break
        else:
            input("Pilihan tidak valid. Tekan Enter untuk melanjutkan...")

def menu_pelanggan(pelanggan):
    while True:
        print("======================================")
        print(f"===        MENU PELANGGAN         ===")
        print("======================================")
        print("         1. Lihat Paket Foto          ")
        print("         2. Booking Foto              ")
        print("         0. Keluar                    ")
        print("======================================")
        
        pilihan = input("Pilih menu (0-2): ")
        
        if pilihan == "1":
            tampilkan_paket_foto()
        elif pilihan == "2":
            lakukan_booking(pelanggan)
        elif pilihan == "0":
            break
        else:
            input("Pilihan tidak valid. Tekan Enter")

def main():
    while True:
        print("=== SISTEM BOOKING FOTO STUDIO ===")
        peran, nama_pengguna = masuk()
        if peran == "admin":
            menu_admin()
        elif peran == "pelanggan":
            menu_pelanggan(nama_pengguna)

if __name__ == "__main__":
    main()