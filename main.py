#!/usr/bin/env python3

import time
import zipfile
import os
import sys
from colorama import Fore
from datetime import datetime  # Impor modul datetime

m = Fore.RED
h = Fore.GREEN
p = Fore.RESET
k = Fore.YELLOW
c = Fore.CYAN

def berakhir():
    waktu = datetime.now()
    print(f"\n{p}[{k}!{p}] Berakhir pada: {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n")
    

os.system("clear")

file_zip = input("\nMasukkan path ke file zip: ")

if not os.path.exists(file_zip):
    print(f"{m}Kesalahan: File zip '{file_zip}' tidak ditemukan.{p}")
    sys.exit(1)

file_wordlist = input("Masukkan path ke file wordlist: ")

if not os.path.exists(file_wordlist):
    print(f"{m}Kesalahan: File wordlist '{file_wordlist}' tidak ditemukan.{p}")
    sys.exit(1)

waktu = datetime.now()
print(f"\n{p}[{k}!{p}] Dimulai pada: {waktu.strftime('%Y-%m-%d %H:%M:%S')}")

try:
    with open(file_wordlist, "r", encoding="utf-8", errors="ignore") as w:
        for kata_sandi in w:
            kata_sandi = kata_sandi.strip()

            try:
                with zipfile.ZipFile(file_zip, "r") as z:
                    z.extractall(pwd=kata_sandi.encode("utf-8"))
                print(f"\n{p}[{h}*{p}] {h}File zip: {file_zip}\n{p}[{h}*{p}] {h}Kata sandi: {kata_sandi}\n{p}[{h}*{p}] {h}Status: Benar")
                berakhir()
                sys.exit(0)

            except Exception as e:
                print(f"\n{p}[{m}*{p}] {m}File zip: {file_zip}\n{p}[{m}*{p}] {m}Kata sandi: {kata_sandi}\n{p}[{m}*{p}] {m}Status: Salah{p}")
                time.sleep(1)

    print(f"\n{k}Kata sandi tidak ditemukan dalam wordlist.{p}")
    berakhir()
    sys.exit(1)

except Exception as e:
    print(f"{k}Terjadi kesalahan: {e}{p}")
    sys.exit(1)
