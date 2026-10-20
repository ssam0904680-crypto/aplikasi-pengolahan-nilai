
# ==================================================
# APLIKASI PENGOLAHAN NILAI MAHASISWA
# Bahasa Pemrograman: Python
# ==================================================

daftar_mahasiswa = []


# 1. FUNGSI MENGHITUNG NILAI AKHIR
def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    return nilai_akhir


# 2. FUNGSI MENENTUKAN GRADE
def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 75:
        return "B"
    elif nilai_akhir >= 65:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


# 3. FUNGSI MENENTUKAN STATUS KELULUSAN
def tentukan_status(nilai_akhir):
    if nilai_akhir >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"


# 4. FUNGSI INPUT DAN VALIDASI NILAI
def input_nilai(jenis_nilai):
    while True:
        try:
            nilai = float(input(f"Masukkan nilai {jenis_nilai} (0-100): "))

            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Kesalahan: nilai harus antara 0 sampai 100.")

        except ValueError:
            print("Kesalahan: masukkan angka yang valid.")


# 5. PROSEDUR MENAMBAH DATA MAHASISWA
def tambah_mahasiswa():
    print("\n========== TAMBAH DATA MAHASISWA ==========")

    nama = input("Masukkan nama mahasiswa: ").strip()

    while nama == "":
        print("Nama tidak boleh kosong!")
        nama = input("Masukkan nama mahasiswa: ").strip()

    tugas = input_nilai("Tugas")
    uts = input_nilai("UTS")
    uas = input_nilai("UAS")

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    grade = tentukan_grade(nilai_akhir)
    status = tentukan_status(nilai_akhir)

    mahasiswa = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir,
        "grade": grade,
        "status": status
    }

    daftar_mahasiswa.append(mahasiswa)

    print("\nData mahasiswa berhasil ditambahkan!")
    print("------------------------------------------")
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {tugas:.2f}")
    print(f"Nilai UTS      : {uts:.2f}")
    print(f"Nilai UAS      : {uas:.2f}")
    print(f"Nilai Akhir    : {nilai_akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")
    print("------------------------------------------")


# 6. PROSEDUR MENAMPILKAN REKAP NILAI
def tampilkan_rekap():
    print("\n========== REKAP NILAI MAHASISWA ==========")

    if len(daftar_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return

    for nomor, mahasiswa in enumerate(daftar_mahasiswa, start=1):
        print(f"\nData Mahasiswa ke-{nomor}")
        print(f"Nama         : {mahasiswa['nama']}")
        print(f"Nilai Tugas  : {mahasiswa['tugas']:.2f}")
        print(f"Nilai UTS    : {mahasiswa['uts']:.2f}")
        print(f"Nilai UAS    : {mahasiswa['uas']:.2f}")
        print(f"Nilai Akhir  : {mahasiswa['nilai_akhir']:.2f}")
        print(f"Grade        : {mahasiswa['grade']}")
        print(f"Status       : {mahasiswa['status']}")

    jumlah = len(daftar_mahasiswa)

    total_nilai = sum(
        mahasiswa["nilai_akhir"]
        for mahasiswa in daftar_mahasiswa
    )

    rata_rata = total_nilai / jumlah

    print("\n========== RINGKASAN ==========")
    print(f"Jumlah Mahasiswa : {jumlah}")
    print(f"Rata-rata Nilai  : {rata_rata:.2f}")


# 7. PROSEDUR MENCARI MAHASISWA
def cari_mahasiswa():
    print("\n========== CARI MAHASISWA ==========")

    if len(daftar_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return

    kata_kunci = input("Masukkan nama mahasiswa: ").strip().lower()

    if kata_kunci == "":
        print("Nama pencarian tidak boleh kosong.")
        return

    ditemukan = False

    for mahasiswa in daftar_mahasiswa:
        if kata_kunci in mahasiswa["nama"].lower():
            print("\nData mahasiswa ditemukan!")
            print(f"Nama        : {mahasiswa['nama']}")
            print(f"Nilai Tugas : {mahasiswa['tugas']:.2f}")
            print(f"Nilai UTS   : {mahasiswa['uts']:.2f}")
            print(f"Nilai UAS   : {mahasiswa['uas']:.2f}")
            print(f"Nilai Akhir : {mahasiswa['nilai_akhir']:.2f}")
            print(f"Grade       : {mahasiswa['grade']}")
            print(f"Status      : {mahasiswa['status']}")
            ditemukan = True

    if not ditemukan:
        print("Mahasiswa tidak ditemukan.")


# 8. PROSEDUR MENAMPILKAN MENU
def tampilkan_menu():
    print("\n==============================================")
    print("       APLIKASI PENGOLAHAN NILAI MAHASISWA")
    print("==============================================")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Rekap Nilai")
    print("3. Cari Mahasiswa")
    print("4. Keluar")
    print("==============================================")


# 9. PROGRAM UTAMA
def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tambah_mahasiswa()

        elif pilihan == "2":
            tampilkan_rekap()

        elif pilihan == "3":
            cari_mahasiswa()

        elif pilihan == "4":
            print("\nProgram selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-4.")


# 10. MENJALANKAN PROGRAM
if __name__ == "__main__":
    main()
