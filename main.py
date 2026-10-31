from src.input_data import baca_data_nilai
from src.proses import ringkasan_statistik
from src.output import format_laporan_akhir, cetak_dan_simpan

def main():
    print("=" * 60)
    print("APLIKASI MODULAR REKAPITULASI NILAI MATEMATIKA - P15")
    print("=" * 60)
    
    while True:
        try:
            kkm = float(input("Masukkan nilai batas kelulusan KKM (0-100): "))
            if 0 <= kkm <= 100:
                break
            print("[Peringatan] Nilai KKM harus berada di rentang 0-100!")
        except ValueError:
            print("[Error] Masukkan format angka numerik yang valid!")

    path_input = "data/contoh_data.txt"
    data_mentah = baca_data_nilai(path_input)
    
    data_valid = []
    for siswa in data_mentah:
        if 0 <= siswa['nilai'] <= 100:
            data_valid.append(siswa)
        else:
            print(f"[Validasi Gagal] Nilai {siswa['nama']} ({siswa['nilai']}) di luar rentang 0-100! (Diabaikan)")

    if not data_valid:
        print("[Sistem Error] Tidak ada data nilai valid yang bisa diproses.")
        return

    statistik = ringkasan_statistik(data_valid, kkm)
    laporan_final = format_laporan_akhir(data_valid, statistik, kkm)
    cetak_dan_simpan(laporan_final, "docs/laporan_akhir.txt")

if __name__ == "__main__":
    main()
