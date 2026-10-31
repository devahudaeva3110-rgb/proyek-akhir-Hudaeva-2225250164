# PROPOSAL PROYEK AKHIR PROGRAM SEDERHANA
**Mata Kuliah:** Algoritma dan Pemrograman (Pertemuan 14)  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.  

---

## 1. Judul Proyek
**Aplikasi Rekapitulasi, Analisis Statistik Deskriptif, dan Manajemen Remedial Nilai Matematika Kelas**

## 2. Latar Belakang Masalah
Guru matematika di sekolah sering kali memerlukan waktu yang cukup lama untuk melakukan rekapitulasi nilai ujian siswa pasca-evaluasi. Pengolahan data secara manual seperti menghitung rata-rata kelas, mencari nilai pencapaian tertinggi, nilai terendah, serta pengelompokkan manual siswa yang belum mencapai Kriteria Ketercapaian Tujuan Pembelajaran (KKTP/KKM) rentan terhadap kesalahan hitung logika manusia (*human error*). Diperlukan sebuah alat bantu berbasis pemrograman console terstruktur yang mampu memvalidasi data nilai, mengotomatisasi perhitungan statistik, serta menghasilkan laporan siap cetak secara cepat, valid, dan konsisten.

## 3. Pengguna dan Tujuan
*   **Pengguna Utama:** Guru Mata Pelajaran Matematika.
*   **Tujuan:** Mengotomatisasi sistem rekapitulasi nilai ujian, meminimalkan kesalahan pengolahan data statistik, serta mengidentifikasi siswa yang membutuhkan penanganan program remedial secara langsung.

## 4. Ruang Lingkup dan Batasan Proyek
*   Program dibangun berbasis *Terminal / Console Interface* menggunakan bahasa Python 3.
*   Program membaca input data nilai mentah mahasiswa dari berkas teks eksternal (`data/nilai_contoh.txt`).
*   Program melakukan pengolahan data kolektif terbatas pada analisis statistik deskriptif dasar (*mean*, *max*, *min*), persentase ketuntasan kelas, dan klasifikasi kelulusan berdasarkan nilai KKM.
*   Program menghasilkan file keluaran laporan akhir berupa teks (`output/laporan_akhir.txt`).

## 5. Kebutuhan Sistem
### Kebutuhan Fungsional (F01 - F05):
*   **F01:** Program mampu membaca berkas eksternal berisi daftar nama dan nilai siswa.
*   **F02:** Program wajib memvalidasi data input agar berada pada rentang batas objektif 0–100.
*   **F03:** Program mampu menghitung parameter statistik kelas (Rata-rata, Nilai Tertinggi, Nilai Terendah).
*   **F04:** Program mampu memisahkan dan mengklasifikasikan siswa berdasarkan status tuntas dan tidak tuntas KKM.
*   **F05:** Program mampu mengekspor dan menyimpan hasil rekap analisis ke file dokumen baru.

### Kebutuhan Nonfungsional:
*   Program dapat dijalankan secara lancar melalui terminal integrasi VS Code.
*   Pesan peringatan atau kesalahan penulisan (*exception handling*) disajikan dengan bahasa yang mudah dipahami guru.

## 6. Input, Proses, dan Output (IPO)
*   **Input:** File basis data teks `data/nilai_contoh.txt` berisi baris data berformat `Nama,Nilai` dan nilai standar KKM dari input guru.
*   **Proses:** 
    1. Membaca baris file teks menggunakan *File I/O* Python.
    2. Memisahkan teks string nama dan mengonversi nilai menjadi tipe data float.
    3. Memvalidasi batasan nilai `0 <= nilai <= 100`.
    4. Mengakumulasikan total data untuk mencari nilai *Mean*, *Max*, dan *Min*.
    5. Menyeleksi status menggunakan logika `if nilai >= KKM`.
*   **Output:** Tampilan ringkasan tabel analisis statistik deskriptif pada console terminal dan dokumen laporan eksternal `output/laporan_akhir.txt`.

## 7. Algoritma (Pseudocode Alur Utama)
```text
MULAI
  DEKLARASI daftar_siswa SEBAGAI List Of Dictionary
  INPUT path_file = "data/nilai_contoh.txt"
  INPUT kkm
  
  BACA file berdasarkan path_file
  JIKA file tidak ditemukan THEN
    TAMPILKAN "Error: File basis data tidak tersedia!"
    SELESAI
  ENDIF

  UNTUK setiap baris DI DALAM file DO
    PISAHKAN baris MENJADI nama DAN nilai
    VALIDASI nilai APAKAH angka float 0 SAMPAI 100
    JIKA tidak valid THEN
      LEWATI baris_data
      CONTINUE
    ENDIF
    SIMPAN {nama: nama, nilai: nilai} KE DALAM daftar_siswa
  ENDFOR

  JIKA daftar_siswa KOSONG THEN
    TAMPILKAN "Error: Tidak ada data nilai valid yang dapat diolah."
    SELESAI
  ENDIF

  HITUNG rata_rata = TOTAL nilai / JUMLAH daftar_siswa
  CARI nilai_tertinggi DAN nilai_terendah
  
  TAMPILKAN rekap statistik kelas ke terminal
  UNTUK setiap data DI daftar_siswa DO
    JIKA data.nilai < kkm THEN
      TAMPILKAN data.nama SEBAGAI siswa remedial
    ENDIF
  ENDFOR

  SIMPAN semua rekap data dan daftar siswa remedial KE "output/laporan_akhir.txt"
SELESAI
```

## 8. Struktur Program dan Modularisasi
Program dirancang secara modular menggunakan fungsi-fungsi dengan tanggung jawab tunggal (*Single Responsibility Principle*) yang terbagi dalam file src terpisah:
1.  **`src/data_io.py`**: Berisi fungsi `baca_data(path)` untuk membaca file mentah dan `simpan_laporan(hasil, path)` untuk menulis laporan akhir.
2.  **`src/analisis.py`**: Berisi fungsi `hitung_statistik(data)` untuk kalkulasi rata-rata, nilai tertinggi, terendah dan fungsi `tentukan_status(nilai, kkm)` untuk klasifikasi ketuntasan belajar.
3.  **`src/main.py`**: Berisi fungsi utama `main()` untuk mengatur alur interaksi pengguna, pemanggilan modul, dan kontrol utama program.

## 9. Pemilihan Struktur Data
*   **List of Dictionaries (`[{'nama': str, 'nilai': float}]`)**: Digunakan untuk menyimpan seluruh record siswa terpopulasi karena sangat fleksibel untuk diiterasi pada fungsi perhitungan statistik deskriptif.
*   **Dictionary (`{'rata_rata': float, 'max': float, 'min': float}`)**: Digunakan untuk mengemas ringkasan parameter objek statistik dari fungsi kalkulator agar mudah diakses oleh fungsi pelapor data.

## 10. Perancangan Rencana Test Case Awal (Minimal 5 Kasus)
Rencana pengujian dirancang sejak awal berdasarkan parameter uji fungsional utama:

| ID | Kategori | Kondisi Input | Hasil yang Diharapkan (Expected Result) |
| :--- | :--- | :--- | :--- |
| **TC01** | Normal | File berisi nilai: `Ali,80`, `Budi,70`, `Cici,90` & KKM = 75 | Rata-rata kelas: 80.0, Max: 90, Min: 70. Siswa Remedial: Budi. |
| **TC02** | Batas Bawah | Input nilai siswa tepat berada pada angka `0` | Nilai diterima sebagai entitas valid, rata-rata kelas menurun secara matematis. |
| **TC03** | Batas Atas | Input nilai siswa tepat berada pada angka `100` | Nilai diterima sebagai entitas valid, masuk kategori nilai tertinggi. |
| **TC04** | Invalid Nilai | Baris file mengandung nilai di luar batas objektif: `Dodo,105` | Sistem menolak baris data tersebut, mengeluarkan log *Warning*, dan lanjut memproses baris berikutnya. |
| **TC05** | Invalid File | Sistem membaca berkas yang tidak ada di direktori (`data/tidak_ada.txt`) | *FileNotFoundError* tertangani dengan baik, sistem keluar dengan pesan peringatan yang aman bagi guru. |

## 11. Pembagian Tugas Kelompok (PIC)
*(Catatan: Untuk pengerjaan individu, seluruh peran dipegang mandiri oleh Anda selaku pemilik repositori).*
*   **Koordinator & Dokumentasi (PIC: Anda):** Menyusun proposal proyek, merancang berkas `README.md`, dan mengatur integrasi berkas repositori.
*   **Programmer Data I/O (PIC: Anda):** Mengimplementasikan kode baca tulis file pada `src/data_io.py`.
*   **Programmer Logika & Tester (PIC: Anda):** Mengimplementasikan mesin kalkulasi statistik pada `src/analisis.py` dan mengeksekusi rencana pengujian berkas `tests/test_case.md`.

## 12. Jadwal Milestone Kerja
*   **Pertemuan 14 (Hari Ini):** Penyelesaian proposal, inisialisasi repositori Git lokal, pembentukan struktur folder proyek, dan *push* cetak biru ke GitHub.
*   **Mandiri (Interval P14–P15):** Implementasi penulisan kode modular Python (`data_io.py`, `analisis.py`, `main.py`).
*   **Pertemuan 15:** Uji coba fungsional 5 test case, pengerjaan *debugging* logika, penyelesaian dokumentasi panduan penggunaan, dan *final push* produk jadi.

## 13. URL Repository GitHub Group
*   **Link Repository:** `https://github.com`
*