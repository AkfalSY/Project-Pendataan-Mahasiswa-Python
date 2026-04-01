from . import Operasi

DB_name = "database.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm_dd-HH-MM-SS+zzzz",
    "nama" : " "*100,
    "jurusan" : " "*100,
    "nim" : " "*7,
    "angkatan" : "yyyy",
    "jalur_masuk" : " "*7,
}

def init_console():
    try: 
        with open(DB_name, 'r') as file:
            print("Database tersedia, init berhasil!!!")
    except:
        print("Database tidak tersedia, silahkan coba buat database baru")
        Operasi.create_first()