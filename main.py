##### Main Module #####

##### KAMUS #####
# userData, gameData, kepemilikanData, riwayatData : 2D Matrix of String
# userid,username,nama,password,role,saldo : String

import Algo
userData, gameData, kepemilikanData, riwayatData = Algo.load()

### Data csv akan diubah menjadi sebuah matriks

### Bentuk data userData
# userData[x][0] = id user
# userData[x][1] = username
# userData[x][2] = nama pengguna
# userData[x][3] = password
# userData[x][4] = role
# userData[x][5] = saldo

### Bentuk data gameData
# gameData[x][0] = id game
# gameData[x][1] = nama game
# gameData[x][2] = kategori
# gameData[x][3] = tahun rilis
# gameData[x][4] = harga
# gameData[x][5] = stok awal

### Bentuk data kepemilikanData
# kepemilikanData[x][0] = id user
# kepemilikanData[x][1] = id game
# kepemilikanData[x][2] = jumlah

### Bentuk data riwayatData
# riwayatData[x][0] = id user
# riwayatData[x][1] = id game
# riwayatData[x][2] = jumlah

##### LOOPING MENU UTAMA #####
role = ''
saved = False

while True:
    Algo.clear()
    Algo.help(role)
    Algo.batas()
    pilih = input('Pilih nomor menu: ')
    Algo.batas()
    Algo.clear()
    if role == '':
        if pilih == '1':
            userid,username,nama,password,role,saldo = Algo.login(userData)
        elif pilih == '2':
            Algo.help(role)

    elif role == 'admin':
        if pilih == '1':
            Algo.register(userData,role)
        elif pilih == '2':
            userid,username,nama,password,role,saldo = Algo.login(userData)
        elif pilih == '3':
            Algo.tambah_game(gameData,role)
        elif pilih == '4':
            Algo.ubah_game(gameData,role)
        elif pilih == '5':
            Algo.ubah_stok(gameData,role)
        elif pilih == '6':
            Algo.list_game_toko(gameData)
        elif pilih == '7':
            Algo.search_game_at_store(gameData)
        elif pilih == '8':
            Algo.topup(userData,role)
        elif pilih == '9':
            Algo.help(role)
        elif pilih == '10':
            saved = Algo.save(userData,gameData,kepemilikanData,riwayatData)
        elif pilih == '11':
            Algo.Exit(userData,gameData,kepemilikanData,riwayatData,saved)
            break
        elif pilih == '12':
            Algo.kerangajaib()
        elif pilih == '13':
            Algo.TicTacToe()
    
    elif role == 'user':
        if pilih == '1':
            userid,username,nama,password,role,saldo = Algo.login(userData)
        elif pilih == '2':
            Algo.list_game_toko(gameData)
        elif pilih == '3':
            Algo.buy_game(userData,gameData,kepemilikanData,riwayatData,userid,role,saldo)
        elif pilih == '4':
            Algo.list_game(gameData,riwayatData,userid,role)
        elif pilih == '5':
            Algo.search_my_game(gameData,riwayatData,userid,role)
        elif pilih == '6':
            Algo.search_game_at_store(gameData)
        elif pilih == '7':
            Algo.riwayat(gameData,riwayatData,userid,role)
        elif pilih == '8':
            Algo.help(role)
        elif pilih == '9':
            saved = Algo.save(userData,gameData,kepemilikanData,riwayatData)
        elif pilih == '10':
            Algo.Exit(userData,gameData,kepemilikanData,riwayatData,saved)
            break
        elif pilih == '11':
            Algo.kerangajaib()
        elif pilih == '12':
            Algo.TicTacToe()
    Algo.batas()
    input('Press Enter To Continue >>>  ')