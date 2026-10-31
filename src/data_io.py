import os

def baca_data(path):
    """Membaca berkas teks mentah dan mengembalikan list data."""
    if not os.path.exists(path):
        print(f"[Error] Berkas basis data '{path}' tidak ditemukan!")
        return []

    data_siswa = []
    with open(path, 'r') as file:
        for baris in file:
            baris = baris.strip()
            if not baris or "," not in baris:
                continue
            nama, nilai_str = baris.split(",", 1)
            try:
                nilai = float(nilai_str)
                data_siswa.append({'nama': nama.strip(), 'nilai': nilai})
            except ValueError:
                print(f"[Warning] Baris data '{baris}' memiliki format nilai tidak valid (diabaikan).")
    return data_siswa

def simpan_laporan(hasil_teks, path):
    """Menulis laporan ringkas hasil analisis ke berkas eksternal."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(hasil_teks)
    print(f"[Sistem] Laporan akhir berhasil diekspor ke '{path}'")