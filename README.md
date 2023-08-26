# PKSFZ

![](https://github.com/FII14/pksfz/blob/main/gambar.jpg)

PKSFZ adalah program yang mencoba mengekstrak isi berkas zip yang dienkripsi dengan mencoba berbagai kata sandi dari sebuah wordlist. Program ini dikembangkan oleh Rofi ([FII14](https://github.com/FII14)).

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Berkontribusi](#berkontribusi)
- [Lisensi](#lisensi)

## Pendahuluan

Program ini adalah program yang mencoba mengekstrak isi berkas zip yang dienkripsi dengan mencoba berbagai kata sandi dari sebuah wordlist. Program ini menggunakan perpustakaan `zipfile` dan memberikan umpan balik tentang keberhasilan atau kegagalan setiap percobaan kata sandi.

## Persyaratan

- Python3
- Perpustakaan `colorama` (instal dengan `pip install colorama`)

## Instalasi

1. Klon repositori ini: `git clone https://github.com/FII14/pksfz.git`
2. Masuk ke direktori: `cd pksfz`
3. Instal perpustakaan yang dibutuhkan: `pip install colorama`

## Penggunaan

1. Pastikan Anda memiliki berkas zip dan berkas wordlist yang sudah disiapkan.
2. Jalankan program dengan perintah: `python3 pksfz.py`
3. Ikuti petunjuk untuk memberikan jalur berkas zip dan berkas wordlist.
4. Program akan mulai mencoba membuka kata sandi menggunakan wordlist yang diberikan.
5. Jika kata sandi yang benar ditemukan, program akan menampilkan pesan sukses dan isi yang diekstrak akan tersedia.

## Berkontribusi

Kontribusi sangat dialu-alukan! Jika Anda menemukan bug atau memiliki saran perbaikan, silakan buat masalah (issue) atau permintaan tarik (pull request) di repositori ini.

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).

