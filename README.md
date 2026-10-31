# Aplikasi Rekapitulasi & Analisis Statistik Deskriptif Nilai Matematika

Aplikasi berbasis *console terminal* ini dirancang menggunakan Python untuk membantu guru matematika mengotomatiskan rekapitulasi nilai ujian. Program ini mampu memvalidasi rentang nilai, menghitung statistik deskriptif dasar (*Mean*, *Max*, *Min*), serta mengelompokkan siswa yang memerlukan program remedial secara cepat dan konsisten.

Proyek ini disusun untuk memenuhi tugas besar mata kuliah **Algoritma dan Pemrograman** (Pertemuan 14 & 15), Program Studi S1 Pendidikan Matematika, Universitas Sultan Ageng Tirtayasa.

## 🚀 Fitur Utama
*   **F01:** Membaca basis data nilai dari file teks eksternal (`data/nilai_contoh.txt`).
*   **F02:** Validasi batas objektif nilai matematika (rentang nilai 0–100).
*   **F03:** Perhitungan statistik otomatis (Rata-rata kelas, Nilai Tertinggi, Nilai Terendah).
*   **F04:** Klasifikasi otomatis status ketuntasan siswa berdasarkan standar batas nilai KKM.
*   **F05:** Ekspor hasil analisis secara rapi ke file eksternal (`output/laporan_akhir.txt`).

## 📂 Struktur Repositori Modular
Sesuai prinsip pemrograman modular, arsitektur kode dibagi berdasarkan tanggung jawab fungsinya:
*   `src/data_io.py`: Menangani fungsi pembacaan file mentah dan penulisan laporan akhir.
*   `src/analisis.py`: Menangani mesin logika kalkulasi statistik matematika dan evaluasi KKM.
*   `src/utilitas.py`: Menangani filter validasi angka input data.
*   `src/main.py`: Kontroler utama alur interaksi aplikasi.

## ⚙️ Cara Menjalankan Program
1. Pastikan Anda telah mengaktifkan interpreter Python 3 di VS Code.
2. Buka terminal integrasi di folder utama proyek, lalu jalankan perintah:
   ```bash
   python src/main.py
   ```
3. Masukkan nilai KKM yang diinginkan saat diminta oleh sistem (Contoh: `75`).
4. Periksa terminal untuk melihat laporan visual dan buka folder `output/laporan_akhir.txt` untuk melihat file hasil ekspor.

## 🧪 Hasil Pengujian (Test Case)
Pengujian dilakukan menggunakan pendekatan nilai batas (*boundary values*) dan data tidak valid:
1. **TC01 (Normal):** Membaca data valid di file -> **PASS** (Kalkulasi statistik dan pembagian status 100% akurat).
2. **TC02 (Batas Bawah):** Memproses nilai tepat `0` -> **PASS** (Sistem menerima sebagai nilai sah).
3. **TC03 (Batas Atas):** Memproses nilai tepat `100` -> **PASS** (Sistem menerima sebagai pencapaian puncak).
4. **TC04 (Invalid Nilai):** Baris data bernilai `105` -> **PASS** (Sistem otomatis mengabaikan dengan aman).
5. **TC05 (Invalid File):** File database tidak sengaja terhapus -> **PASS** (*Exception handling* berjalan tanpa membuat program *crash*).
6.