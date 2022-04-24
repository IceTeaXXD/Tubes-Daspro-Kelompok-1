##### Modul Login #####
# Fungsi untuk melakukan login user

##### KAMUS ARGUMEN #####
# userData : 2D Matrix of String

##### KAMUS LOKAL ##### 
# userid,username,nama,password,role,saldo : String
# indeks : Integer

from .Functions import*
from .B01_Cipher import*

def login(userData):
    print("Login")

    # Looping untuk memasukkan username dan password
    loginValid = False
    while not (loginValid):
    # Input username and password
        username = input("Masukan username: ")
        password = input("Masukan password: ")

        # Check apakah username dan password valid dengan membandingkan data yang ada pada array userData
        for i in range(length_of_obj(userData)):
            if username == userData[i][1] and password == deCipher(userData[i][3]):
                print(f"Halo {username} selamat datang di BNMO!")
                loginValid = True
                indeks = i
                break
        else:
            print("Username atau password salah, silakan ulangi input!")

    userid = userData[indeks][0]
    nama = userData[indeks][2]
    role = userData[indeks][4]
    saldo = userData[indeks][5]

    # Membalikkan userid, nama, role, dan saldo sesuai data login

    return userid,username,nama,password,role,saldo
