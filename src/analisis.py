def hitung_statistik(data_siswa):
    """Menghitung rata-rata, nilai tertinggi, dan nilai terendah kelas."""
    if not data_siswa:
        return {'rata_rata': 0.0, 'max': 0.0, 'min': 0.0}

    nilai_list = [siswa['nilai'] for siswa in data_siswa]
    return {
        'rata_rata': sum(nilai_list) / len(nilai_list),
        'max': max(nilai_list),
        'min': min(nilai_list)
    }

def tentukan_status(nilai, kkm):
    """Menentukan ketuntasan individu berdasarkan nilai batas KKM."""
    return "Tuntas" if nilai >= kkm else "Belum Tuntas (Remedial)"