from .Functions import*

def ubah_game(gameData,role):
    if length_of_obj(gameData) == 0:
        print('Maaf, tidak ada data game yang tersimpan.')
    else:  
        if role == "admin":
            sudahUbah = False
            while not(sudahUbah):
                idGame = input('Masukan id game yang akan diubah: ')
                for i in range(length_of_obj(gameData)):
                    if idGame == gameData[i][0]:
                        indeks = i
                        sudahUbah = True 
                        break

                if sudahUbah:
                    namaGame = input('Masukan nama game: ')
                    kategori = input('Masukan kategori: ')
                    tahunRilis = input('Masukan tahun rilis: ')
                    harga = input('Masukan harga game: ')
                    if namaGame != '':
                        gameData[indeks][1] = namaGame
                    if kategori != '':
                        gameData[indeks][2] = kategori
                    if tahunRilis != '':
                        gameData[indeks][3] = tahunRilis
                    if harga != '':
                        gameData[indeks][4] = harga

                    print(f'Selamat! Berhasil mengubah game {idGame}')
                    break
                else:
                    print('Maaf, id game tidak ditemukan. Ulangi input idGame!')
        else:
            print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')