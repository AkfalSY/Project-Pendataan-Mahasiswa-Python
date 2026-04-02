import os 
import CRUD as CRUD
from CRUD import init_console, read_console, create_console, update_console

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt":os.system("cls")

    print("SELAMAT DATANG DIPOGRAM")
    print("PENCATATAN MAHASISWA")
    print("=======================")

    #check apakah database ada 
    init_console()

    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt":os.system("cls")

        print("SELAMAT DATANG DIPOGRAM")
        print("PENCATATAN MAHASISWA")
        print("=======================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_option = input("Masukan Opsi : ")

        match user_option:
            case "1": read_console()
            case "2": create_console()
            case "3": update_console()
            case "4": print("Delete Data")

        is_done = input("Apakah anda mau mencoba lagi (y/n) ? ")
        if is_done == "n" or is_done == "N":
            break
        
        print("Terimakasih sudah mencoba!!!")