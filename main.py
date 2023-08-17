#!/usr/bin/env python3

import time
import zipfile
import os
import sys
from colorama import Fore
from datetime import datetime

m = Fore.RED
h = Fore.GREEN
p = Fore.RESET
k = Fore.YELLOW
c = Fore.CYAN

def berakhir():
    waktu = datetime.now()
    print(f"\n{p}[{k}!{p}] Berakhir pada: {waktu.strftime('%d-%m-%Y %H:%M:%S')}\n")

def ekstrak_zip(file_zip, kata_sandi):
    try:
        with zipfile.ZipFile(file_zip, "r") as z:
            z.extractall(pwd=kata_sandi.encode("utf-8"))
            print(f"""
{p}[{h}+{p}] {h}File zip: {file_zip}
{p}[{h}+{p}] {h}Kata sandi: {kata_sandi}
{p}[{h}+{p}] {h}Status: Benar{p}""")
            berakhir()
            sys.exit(0)
            
    except Exception as e:
        print(f"""
{p}[{m}-{p}] {m}File zip: {file_zip}
{p}[{m}-{p}] {m}Kata sandi: {kata_sandi}
{p}[{m}-{p}] {m}Status: Salah{p}""")
        time.sleep(1)

def utama():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(f"""
{c}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  {p}
{c}@ {p}Program : Pemecah kata sandi file zip     {c}@
{c}@ {p}Pembuat : Rofi [FII14]                    {c}@
{c}@ {p}GitHub  : https://github.com/FII14/pksfz  {c}@
{c}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  {p}
""")
    
    
    try:
        file_zip = input("Masukkan nama file zip: ")
        if not os.path.exists(file_zip):
            print(f"{m}\nKesalahan: File zip '{file_zip}' tidak ditemukan.{p}")
            berakhir()
            sys.exit(1)

        if not zipfile.is_zipfile(file_zip):
            print(f"{m}\nKesalahan: File '{file_zip}' bukan file zip yang valid.{p}")
            berakhir()
            sys.exit(1)

        file_wordlist = input("Masukkan nama file wordlist: ")
        if not os.path.exists(file_wordlist):
            print(f"{m}\nKesalahan: File wordlist '{file_wordlist}' tidak ditemukan.{p}")
            berakhir()
            sys.exit(1)

        waktu = datetime.now()
        print(f"\n{p}[{k}!{p}] Dimulai pada: {waktu.strftime('%d-%m-%Y %H:%M:%S')}")

        try:
            with open(file_wordlist, "r", encoding="utf-8", errors="ignore") as w:
                for kata_sandi in w:
                    kata_sandi = kata_sandi.strip()
                    ekstrak_zip(file_zip, kata_sandi)
            print(f"\n{k}Kata sandi tidak ditemukan dalam file wordlist.{p}")
            berakhir()
            sys.exit(1)
        except Exception as e:
            print(f"\n{k}Terjadi kesalahan: {e}{p}")
            berakhir()
            sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n\n{m}Proses dihentikan oleh pengguna.{p}")
        berakhir()
        sys.exit(1)

if __name__ == "__main__":
    utama()
