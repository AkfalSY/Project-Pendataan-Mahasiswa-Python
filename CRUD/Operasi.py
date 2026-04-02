from . import Database
from . import Utility
import time
import os

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
    data["angkatan"] = angkatan 
    data["jalur_masuk"] = jalur_masuk + Database.TEMPLATE["jalur_masuk"] [len(jalur_masuk):]

    data_str= f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["jurusan"]},{data["nim"]},{data["angkatan"]},{data["jalur_masuk"]}\n'

    try: 
        with open(Database.DB_name, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil di buat")

def read(**kwargs):
    try:
        with open(Database.DB_name, "r") as file:
            content = file.readlines()
            jumlah_mahasiswa = len(content)
            if "index" in kwargs:
                index_mahasiswa = kwargs["index"]-1
                if index_mahasiswa < 0 or index_mahasiswa > jumlah_mahasiswa:
                    return False
                else:
                    return content[index_mahasiswa]
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
    data["angkatan"] = str(angkatan)
    data["jalur_masuk"] = jalur_masuk + Database.TEMPLATE["jalur_masuk"] [len(jalur_masuk):]

    data_str= f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["jurusan"]},{data["nim"]},{data["angkatan"]},{data["jalur_masuk"]}\n'

    try: 
        with open(Database.DB_name, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak berhasil di buat")

def update(nomor,pk,date_add,nama,jurusan,nim,angkatan,jalur_masuk):
    
    data = Database.TEMPLATE.copy()
    
    data["pk"]= pk
    data["date_add"]= date_add
    data["nama"] = nama + Database.TEMPLATE["nama"] [len(nama):]
    data["jurusan"] = jurusan + Database.TEMPLATE["jurusan"] [len(jurusan):]
    data["nim"] = nim + Database.TEMPLATE["nim"] [len(nim):]
    data["angkatan"] = str(angkatan)
    data["jalur_masuk"] = jalur_masuk + Database.TEMPLATE["jalur_masuk"] [len(jalur_masuk):]

    data_str= f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["jurusan"]},{data["nim"]},{data["angkatan"]},{data["jalur_masuk"]}\n'

    try:
        with open(Database.DB_name, "r") as file:
            data_sementara = file.readlines()

        data_sementara[nomor - 1] = data_str

        with open(Database.DB_name, "w", encoding="utf-8") as file:
            file.writelines(data_sementara)

        print("Data berhasil di update!!!")

    except:
        print("Data tidak berhasil di update, silahkan coba lagi!!!")


def delete(nomor): 
    try:
        with open(Database.DB_name, "r") as file:
            counter = 0 
            while True:
                content = file.readline()
                if len(content) == 0 :
                    break 
                elif counter == nomor-1:
                    pass 
                else: 
                    with open("data_tempt.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1

        os.replace("data_tempt.txt", Database.DB_name)

    except:
        print("Database Error")