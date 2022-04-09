from .Functions import*

def register(userData,role):
    if role == 'admin':
        print("Register")
        nama = input("Masukan nama: ")
        validasi_user = False
        while not (validasi_user):
            username = input("Masukan username: ")

            # Sistem Validasi Username
            count = 0
            char = ['-','_']
            for i in range (length_of_obj(username)):
                if username[i].isupper() or username[i].islower() or username[i] in char or username[i].isdigit():
                    count += 1

            # Cek Username valid atau tidak
            if count == length_of_obj(username):
                # Algoritma untuk mengecek apakah username sudah terpakai
                for i in range(length_of_obj(userData)):
                    if username == userData[i][1]:
                        print("Username sudah terpakai, silakan masukkan username lain.")
                        validasi_user = False
                        break
                    elif i == length_of_obj(userData)-1:
                        validasi_user = True
                        break
            else:
                print("Username tidak valid, silakan ulangi input!")

        # Create password and check whether the password is valid
        while True:
            password = input("Masukan password: ")
            if length_of_obj(password) < 8:
                print("Password minimal terdiri atas 8 karakter, silakan ulangi input!")
            elif not any(char.isdigit() for char in password):
                print("Password harus memiliki minimal 1 angka, silakan ulangi input!")
            elif not any(char.isupper() for char in password):
                print("Password harus memiliki minimal 1 huruf besar, silakan ulangi input!")
            elif not any(char.islower() for char in password):
                print("Password harus memiliki minimal 1 huruf kecil, silakan ulangi input!")
            else:
                break

        data_user = [str(length_of_obj(userData)+1), username,nama,password,'user','0']
        userData += [data_user]
        print("Registrasi Berhasil!")
    else:
        print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')
