# Dokumentasi Rencana Pengujian Aplikasi (Test Case)

| ID | Kategori | Kondisi Input | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC01** | Normal | Data nilai valid: 85.5, 58.0, 92.0, 60.0 & KKM = 75 | Rata-rata terhitung benar, siswa di bawah 75 masuk remedial. |
| **TC02** | Batas Bawah | Input nilai siswa tepat 0 | Nilai sukses diolah tanpa memicu crash program. |
| **TC03** | Batas Atas | Input nilai siswa tepat 100 | Nilai sukses diolah dan tercatat sebagai nilai tertinggi. |
| **TC04** | Invalid Nilai | Baris file bernilai 105 atau negatif | Sistem mengabaikan baris tersebut dengan aman. |
| **TC05** | Invalid File | Membaca path file data salah | Exception diantisipasi dan keluar dengan aman. |