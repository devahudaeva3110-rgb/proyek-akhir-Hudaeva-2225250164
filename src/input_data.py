import os

def baca_data_nilai(path):
    if not os.path.exists(path):
        print(f"[Error] File data '{path}' tidak ditemukan!")
        return []
    data_mentah = []
    with open(path, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            if not baris or "," not in baris:
                continue
            nama, nilai_str = baris.split(",", 1)
            try:
                nilai = float(nilai_str)
                data_mentah.append({'nama': nama.strip(), 'nilai': nilai})
            except ValueError:
                print(f"[Warning] Mengabaikan data tidak valid: {baris}")
    return data_mentah
