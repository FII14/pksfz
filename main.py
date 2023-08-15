#!/usr/bin/env python3

import time
import zipfile
import os
import sys

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Pemecah Kata Sandi File Zip     @
@ Pembuat : Rofi [FII14]                    @
@ GitHub  : https://github.com/FII14/PKSFZ  @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

file_zip = input("Masukkan path ke file zip: ")

if not os.path.exists(file_zip):
    print(f"Kesalahan: File zip '{file_zip}' tidak ditemukan.")
    sys.exit(1)
  
file_wordlist = input("Masukkan path ke file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.")
    sys.exit(1)

try:
    with open(file_wordlist, "r", encoding="utf-8", errors="ignore") as w:

        for kata_sandi in w:
            kata_sandi = kata_sandi.strip()

            try:
                with zipfile.ZipFile(file_zip, "r") as z:
                    z.extractall(pwd=kata_sandi.encode("utf-8"))
                print(f"\n[*] File zip: {file_zip}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Benar\n")
                sys.exit(0)

            except Exception as e:
                print(f"\n[*] File zip: {file_zip}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Salah")
                time.sleep(1)

    print("\nKata sandi tidak ditemukan dalam wordlist.")
    sys.exit(1)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    sys.exit(1)
