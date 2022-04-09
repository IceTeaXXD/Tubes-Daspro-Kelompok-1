import Algo

userData, gameData, kepemilikanData, riwayatData = Algo.load()
role = ''

while True:
    Algo.clear()
    Algo.help(role)
    Algo.batas()
    pilih = input('Pilih nomor menu: ')
    Algo.batas()
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
            Algo.help(role)
        elif pilih == '9':
            Algo.save(userData,gameData,kepemilikanData,riwayatData)
        elif pilih == '10':
            Algo.Exit()
            break
    
    elif role == 'user':
        if pilih == '1':
            userid,username,nama,password,role,saldo = Algo.login(userData)
        elif pilih == '2':
            Algo.list_game_toko(gameData)
        elif pilih == '3':
            Algo.buy_game(userData,gameData,kepemilikanData,riwayatData,userid,nama,role,saldo)
        elif pilih == '4':
            Algo.list_game(gameData,riwayatData,nama,role)
        elif pilih == '5':
            Algo.search_my_game(gameData,riwayatData,nama,role)
        elif pilih == '6':
            Algo.search_game_at_store(gameData)
        elif pilih == '7':
            Algo.riwayat(riwayatData,nama,role)
        elif pilih == '8':
            Algo.help(role)
        elif pilih == '9':
            Algo.save(userData,gameData,kepemilikanData,riwayatData)
        elif pilih == '10':
            Algo.Exit()
            break
        
    Algo.batas()
    input('Press Enter To Continue >>>  ')