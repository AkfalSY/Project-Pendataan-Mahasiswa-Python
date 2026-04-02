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

def create_console():
    print("\n\n"+"="*128)
    print("Silahkan tambah data mahasiswa\n")

    nama = input("Nama\t: ")
    jurusan = input("Jurusan\t: ")
    nim = input("NIM\t: ")
    angkatan = input("Angkatan\t: ")
    jalur_masuk = input("Jalur Masuk\t: ")

    Operasi.create(nama,jurusan,nim,angkatan,jalur_masuk)

def update_console():
    read_console()
    while True:
        try: 
            print("Silahkan pilih nomor data yang ingin diubah")
            nomor = int(input("Nomor\t: "))
            data_mahasiswa = Operasi.read(index=nomor)
            break

        except:
            print("Inputan salah, silahkan coba lagi!!!")

    data_break = data_mahasiswa.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    nama = data_break[2]
    jurusan = data_break[3]
    nim = data_break[4]
    angkatan = data_break[5]
    jalur_masuk = data_break[6][:-1]

    while True:
        print("\n"+"="*128)
        print("Silahkan pilih data apa yang ingin anda rubah")
        print(f"1. Nama\t : {nama:.40}")
        print(f"2. Jurusan\t : {jurusan:.40}")
        print(f"3. NIM\t : {nim:.40}")
        print(f"4. Angkatan\t : {angkatan:.40}")
        print(f"5. Jalur Masuk\t : {jalur_masuk:.40}")

        input_user = input("pilih data [1,2,3,4,5] : ")
        match input_user:
            case "1": nama = input("Nama\t: ")
            case "2": jurusan = input("Jurusan\t: ")
            case "3": nim = input("NIM\t: ")
            case "4": angkatan = input("Angkatan\t: ")
            case "5": jalur_masuk = input("Jalur Masuk\t: ")
            case _: print("inputan yang anda masukan salah, silahkan coba lagi!!!")
        
        print("Data baru yang anda ubah")
        print(f"1. Nama\t : {nama:.40}")
        print(f"2. Jurusan\t : {jurusan:.40}")
        print(f"3. NIM\t : {nim:.40}")
        print(f"4. Angkatan\t : {angkatan:.40}")
        print(f"5. Jalur Masuk\t : {jalur_masuk:.40}")

        is_done = input("Apakah sudah selesai (y/n) ? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(nomor,pk,date_add,nama,jurusan,nim,angkatan,jalur_masuk)

