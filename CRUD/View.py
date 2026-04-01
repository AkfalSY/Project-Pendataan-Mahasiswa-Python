from . import Database
from . import Operasi

def read_console():
    data_file = Operasi.read()

    index = "No"
    nama = "Nama"
    jurusan = "Jurusan"
    nim = "NIM"
    angkatan = "Angkatan"
    jalur_masuk = "Jalur Masuk"

    print("\n"+"="*128)    
    print(f"{index:4} | {nama:40} | {jurusan:40} | {nim:7} | {angkatan:8} | {jalur_masuk:7}")    
    print("-"*128)    

    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        nama = data_break[2]
        jurusan = data_break[3]
        nim = data_break[4]
        angkatan = data_break[5]
        jalur_masuk = data_break[6]
        print(f"{index+1:4} | {nama:.40} | {jurusan:.40} | {nim:.7} | {angkatan:8} | {jalur_masuk:7}", end="") 

    print("\n"+"="*128+"\n")   