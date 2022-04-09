from .Functions import*

def login(userData):
    print("Login")
    loginValid = False
    while not (loginValid):
    # Input username and password
        username = input("Masukan username: ")
        password = input("Masukan password: ")

        # Check whether the username and password is valid
        for i in range(length_of_obj(userData)):
            if username == userData[i][1] and password == userData[i][3]:
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

    return userid,username,nama,password,role,saldo