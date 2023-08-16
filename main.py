#!/usr/bin/env python3

import time
import zipfile
import os
import sys
from colorama import Fore

m = Fore.RED
h = Fore.GREEN
p = Fore.RESET
k = Fore.YELLOW
c = Fore.CYAN

print(f"""
{c}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
{c}@ {p}Program : Pemecah Kata Sandi File Zip {c}    @
{c}@ {p}Pembuat : Rofi [FII14]  {c}                  @
{c}@ {p}GitHub  : https://github.com/FII14/PKSFZ {c} @
{c}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
{p}""")

file_zip = input("Masukkan path ke file zip: ")

if not os.path.exists(file_zip):
    print(f"{m}Kesalahan: File zip '{file_zip}' tidak ditemukan.{p}")
    sys.exit(1)
  
file_wordlist = input("Masukkan path ke file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"{m}Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.{p}")
    sys.exit(1)

try:
    with open(file_wordlist, "r", encoding="utf-8", errors="ignore") as w:

        for kata_sandi in w:
            kata_sandi = kata_sandi.strip()

            try:
                with zipfile.ZipFile(file_zip, "r") as z:
                    z.extractall(pwd=kata_sandi.encode("utf-8"))
                print(f"\n{h}[*] File zip: {file_zip}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Benar\n{p}")
                sys.exit(0)

            except Exception as e:
                print(f"\n{m}[*] File zip: {file_zip}\n[*] Kata sandi: {kata_sandi}\n[*] Status: Salah{p}")
                time.sleep(1)

    print(f"\n{k}Kata sandi tidak ditemukan dalam wordlist.{p}")
    sys.exit(1)

except Exception as e:
    print(f"{k}Terjadi kesalahan: {e}{p}")
    sys.exit(1)
