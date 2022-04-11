from .Functions import*
from .B01_Cipher import*

def register(userData,role):
    if role == 'admin': # Validasi Role
        print("Register")
        # Input Data
        nama = input("Masukan nama: ")

        validasi_user = False
        while not (validasi_user):  # Looping untuk melakukan validasi username
            username = input("Masukan username: ")

            # Sistem Validasi Username
            count = 0   # Inisialisasi variabel counter
            char = ['-','_']    # Char yang diperbolehkan

            for i in range (length_of_obj(username)):   # Looping untuk mengecek tiap karakter username valid atau tidak
                if username[i].isupper() or username[i].islower() or username[i] in char or username[i].isdigit():
                    count += 1  # Counter akan ditambahkan terus jika valid.
                                # Counter akan bernilai sama dengan panjang username input jika semua karakter valid

            if count == length_of_obj(username):
                for i in range(length_of_obj(userData)):    # Algoritma untuk mengecek apakah username sudah terpakai
                    if username == userData[i][1]:
                        print("Username sudah terpakai, silakan masukkan username lain.")
                        validasi_user = False   
                        break
                    elif i == length_of_obj(userData)-1:
                        validasi_user = True    # Username tervalidasi
                        break
            else:
                print("Username tidak valid, silakan ulangi input!")

        # Looping untuk membuat dan melakukan validasi password
        while True: 
            password = input("Masukan password: ")
            # Syarat password pada algoritma ini:
            # 1. Password harus terdiri >= 8 karakter
            # 2. Password harus teridiri atas minimal 1 huruf besar, 1 huruf kecil, dan 1 angka
            if length_of_obj(password) < 8: 
                print("Password minimal terdiri atas 8 karakter, silakan ulangi input!")
            elif not any(char.isdigit() for char in password):
                print("Password harus memiliki minimal 1 angka, silakan ulangi input!")
            elif not any(char.isupper() for char in password):
                print("Password harus memiliki minimal 1 huruf besar, silakan ulangi input!")
            elif not any(char.islower() for char in password):
                print("Password harus memiliki minimal 1 huruf kecil, silakan ulangi input!")
            # password tidak boleh memiliki spasi
            elif ' ' in password:
                print("Password tidak boleh memiliki spasi, silakan ulangi input!")
            else:
                break

        password = Cipher(password) # Melakukan enkripsi password
        
        # Memasukkan data yang telah diinput ke dalam array semua data user
        data_user = [str(length_of_obj(userData)+1),username,nama,password,'user','0']
        userData += [data_user]
        print("Registrasi Berhasil!")
    else:
        print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')