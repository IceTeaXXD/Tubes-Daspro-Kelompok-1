from .Functions import*

def topup(userData,role):
    if role == 'admin':
        userName = input('Masukan username: ')
        indeks = 0
        for i in range(length_of_obj(userData)):
            if userData[i][1] == userName:
                indeks = i
                break
        if indeks != 0:
            saldo = int(input('Masukan jumlah saldo yang ingin ditambahkan: '))
            if saldo + int(userData[i][5]) >= 0 :
                userData[indeks][5] = str(int(userData[indeks][5]) + saldo)
                print(f'Top up berhasil! Saldo {userName} menjadi {userData[indeks][5]}')
            else:
                print('Maaf, jumlah saldo tidak valid!')
        else:
            print('Maaf, username tidak ditemukan!')
    else:
        print('Akses hanya untuk role admin!')