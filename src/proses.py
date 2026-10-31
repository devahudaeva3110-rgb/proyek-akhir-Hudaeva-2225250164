def hitung_rata_rata(nilai_list):
    if len(nilai_list) == 0:
        return 0
    return sum(nilai_list) / len(nilai_list)

def status_lulus(nilai_list, batas=60):
    return [x for x in nilai_list if x >= batas]

def ringkasan_statistik(data_siswa, batas_kkm):
    if not data_siswa:
        return None
    nilai_list = [siswa['nilai'] for siswa in data_siswa]
    nilai_lulus = status_lulus(nilai_list, batas_kkm)
    return {
        "jumlah": len(nilai_list),
        "rata_rata": hitung_rata_rata(nilai_list),
        "minimum": min(nilai_list) if nilai_list else None,
        "maksimum": max(nilai_list) if nilai_list else None,
        "lulus": len(nilai_lulus),
        "remedial": len(nilai_list) - len(nilai_lulus)
    }
