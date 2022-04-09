from .Functions import*

def buy_game(userData,gameData,kepemilikanData,riwayatData,userid,role,saldo):
    if role == "user":
        saldo_ = int(saldo)
        indeks = 0
        found = False
        # Mencari indeks game yang akan dibeli
        idGame = input('Masukan id game yang ingin dibeli: ')
        for i in range(length_of_obj(gameData)):
            if idGame == gameData[i][0]:
                indeks = i
                found = True
                break
        
        hargaGame = int(gameData[indeks][4])
        stokGame = int(gameData[indeks][5])
        namaGame = gameData[indeks][1]

        if isOwned(kepemilikanData,idGame,userid):
            print('Anda sudah memiliki game tersebut!')
                
        elif not(found):
            print('Maaf, id game tidak ditemukan. Ulangi input idGame!')

        elif found and saldo_ >= hargaGame and stokGame > 0:
            # Mengurangi Stok Game
            gameData[indeks][5] = str(int(gameData[indeks][5]) - 1)

            # Mengurangi Saldo User
            saldo_ -= hargaGame
            for i in range(length_of_obj(userData)):  # Looping mencari saldo sesuai dengan userID
                if userData[i][0] == userid:
                    userData[i][5] = str(saldo_)
                    break
            
            # Menambahkan data pembelian ke dalam data kepemilikan
            temp_kepemilikan = [idGame, userid]
            kepemilikanData += [temp_kepemilikan]

            # Menambahkan data pembelian ke riwayat data pembelian
            tahun = str(date.today().year)
            riwayatData += [[idGame,namaGame,str(hargaGame),userid,tahun]]

            print(f'Selamat! Anda telah membeli game {gameData[indeks][1]}')

        else:
            print('Maaf, stok game tidak mencukupi atau saldo anda tidak mencukupi untuk membeli game tersebut!')
        
    else:
        print('Akses hanya untuk role user!')