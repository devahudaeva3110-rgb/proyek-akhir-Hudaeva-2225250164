import os

def format_laporan_akhir(data_siswa, statistik, batas_kkm):
    laporan =  "=" * 55 + "\n"
    laporan += "         LAPORAN RESMI HASIL EVALUASI MATEMATIKA       \n"
    laporan += "=" * 55 + "\n"
    laporan += f" Total Siswa Dinilai: {statistik['jumlah']}\n"
    laporan += f" Rata-rata Kelas    : {statistik['rata_rata']:.2f}\n"
    laporan += f" Nilai Tertinggi    : {statistik['maksimum']:.2f}\n"
    laporan += f" Nilai Terendah     : {statistik['minimum']:.2f}\n"
    laporan += f" Jumlah Tuntas KKM  : {statistik['lulus']}\n"
    laporan += f" Wajib Remedial     : {statistik['remedial']}\n"
    laporan += "-" * 55 + "\n"
    laporan += "Detail Status Kelulusan Siswa:\n"
    for siswa in data_siswa:
        status = "TUNTAS" if siswa['nilai'] >= batas_kkm else "REMEDIAL"
        laporan += f"- {siswa['nama']}: {siswa['nilai']} -> STATUS: {status}\n"
    laporan += "=" * 55 + "\n"
    return laporan

def cetak_dan_simpan(laporan_teks, path_output):
    print("\n" + laporan_teks)
    os.makedirs(os.path.dirname(path_output), exist_ok=True)
    with open(path_output, 'w', encoding='utf-8') as file:
        file.write(laporan_teks)
    print(f"[Sistem] File laporan sukses diekspor ke '{path_output}'")
