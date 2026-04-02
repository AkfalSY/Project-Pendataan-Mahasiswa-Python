from . import Database
from . import Utility
import time

def create_first():
    nama = input("Nama\t: ")
    jurusan = input("Jurusan\t: ")
    nim = input("NIM\t: ")
    angkatan = input("Angkatan\t: ")
    jalur_masuk = input("Jalur Masuk\t: ")

    data = Database.TEMPLATE.copy()

    data["pk"]= Utility.string_random(6)
    data["date_add"]= time.strftime("%Y-%m_%d-%H-%M-%S%z", time.gmtime())
    data["nama"] = nama + Database.TEMPLATE["nama"] [len(nama):]
    data["jurusan"] = jurusan + Database.TEMPLATE["jurusan"] [len(jurusan):]
    data["nim"] = nim + Database.TEMPLATE["nim"] [len(nim):]
    data["angkatan"] = angkatan + Database.TEMPLATE["angkatan"] [len(angkatan):]
    data["jalur_masuk"] = jalur_masuk + Database.TEMPLATE["jalur_masuk"] [len(jalur_masuk):]

    data_str= f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["jurusan"]},{data["nim"]},{data["angkatan"]},{data["jalur_masuk"]}\n'

    try: 
        with open(Database.DB_name, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil di buat")

def read():
    try:
        with open(Database.DB_name, "r") as file:
            content = file.readlines()
            return content
    except:
        print("Data tidak dapat dibaca, silahkan coba lagi")

def create(nama,jurusan,nim,angkatan,jalur_masuk):
    data = Database.TEMPLATE.copy()

    data["pk"]= Utility.string_random(6)
    data["date_add"]= time.strftime("%Y-%m_%d-%H-%M-%S%z", time.gmtime())
    data["nama"] = nama + Database.TEMPLATE["nama"] [len(nama):]
    data["jurusan"] = jurusan + Database.TEMPLATE["jurusan"] [len(jurusan):]
    data["nim"] = nim + Database.TEMPLATE["nim"] [len(nim):]
    data["angkatan"] = angkatan + Database.TEMPLATE["angkatan"] [len(angkatan):]
    data["jalur_masuk"] = jalur_masuk + Database.TEMPLATE["jalur_masuk"] [len(jalur_masuk):]

    data_str= f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["jurusan"]},{data["nim"]},{data["angkatan"]},{data["jalur_masuk"]}\n'

    try: 
        with open(Database.DB_name, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil di buat")