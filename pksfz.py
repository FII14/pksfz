#!/usr/bin/env python3

import time
import zipfile
import os
import sys
from colorama import Fore
from datetime import datetime

h = Fore.GREEN
p = Fore.RESET
m = Fore.LIGHTRED_EX

def berakhir():
    waktu = datetime.now()
    print(f"\n{h}[!] Berakhir pada: {waktu.strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"\n{h}{'-' * 56}{p}\n")

def ekstrak_zip(file_zip, kata_sandi):
    try:
        with zipfile.ZipFile(file_zip, "r") as z:
            z.extractall(pwd=kata_sandi.encode("utf-8"))
            print(f"""{h}
    [+] File zip: {file_zip}
    [+] Kata sandi: {kata_sandi}

    [+] Isi file zip:{p}""")
            
            for info in z.infolist():
                print(f"{h}        [+] {info.filename}{p}")

            if not os.path.exists("hasil"):
                os.makedirs("hasil")
                
            os.rename(info.filename, os.path.join("hasil", info.filename))
            print(f"\n    {h}File zip berhasil diekstrak dan disimpan di dalam folder 'hasil'.{p}")
            
            berakhir()
            sys.exit(0)
            
    except Exception as e:
        pass

def utama():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(f"""{h}
{'-' * 56}
    _______  ___  ____   ______   ________  ________  
   |_   __ \|_  ||_  _|.' ____ \ |_   __  ||  __   _| 
     | |__) | | |_/ /  | (___ \_|  | |_ \_||_/  / /   
     |  ___/  |  __'.   _.____`.   |  _|      .'.' _  
    _| |_    _| |  \ \_| \____) | _| |_     _/ /__/ | 
   |_____|  |____||____|\______.'|_____|   |________| 
{'-' * 56}
    [+] Program     : Pemecah Kata Sandi File Zip
    [+] Dibuat oleh : FII14
    [+] Github      : https://github.com/FII14/pksfz    
{'-' * 56}
{p}""")
    
    try:
        file_zip = input(f"{h}[PKSFZ] Masukkan nama file zip {m}$ {h}")
        if not os.path.exists(file_zip):
            print(f"{h}\nFile zip '{file_zip}' tidak ditemukan.{p}")
            berakhir()
            sys.exit(1)

        if not zipfile.is_zipfile(file_zip):
            print(f"{h}\nFile '{file_zip}' bukan file zip yang valid.{p}")
            berakhir()
            sys.exit(1)

        file_wordlist = input(f"{h}[PKSFZ] Masukkan nama file wordlist {m}$ {h}")
        if not os.path.exists(file_wordlist):
            print(f"{h}\nFile wordlist '{file_wordlist}' tidak ditemukan.{p}")
            berakhir()
            sys.exit(1)

        waktu = datetime.now()
        print(f"\n{h}{'-' * 56}")
        print(f"{h}[!] Dimulai pada: {waktu.strftime('%d-%m-%Y %H:%M:%S')}{p}")

        try:
            with open(file_wordlist, "r", encoding="utf-8", errors="ignore") as w:
                for kata_sandi in w:
                    kata_sandi = kata_sandi.strip()
                    ekstrak_zip(file_zip, kata_sandi)
            print(f"\n{h}Kata sandi tidak ditemukan dalam file wordlist.{p}")
            berakhir()
            sys.exit(1)
        except Exception as e:
            print(f"\n{h}Terjadi kesalahan: {e}{p}")
            berakhir()
            sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n\n{h}Proses dihentikan oleh pengguna.{p}")
        berakhir()
        sys.exit(1)

if __name__ == "__main__":
    utama()
