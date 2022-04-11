from .Functions import*

def tambah_game(gameData,role):
    if role == 'admin':
        while True:
            namaGame = input('Masukan nama game: ')
            kategori = input('Masukan kategori: ')
            tahunRilis = input('Masukan tahun rilis: ')
            harga = input('Masukan harga game: ')
            stokAwal = input('Masukan stok awal: ') 

            jumlah_game = hitungGame(gameData)
            if jumlah_game < 9: 
                idGame = 'G00' + str(hitungGame(gameData)+1)
            elif jumlah_game < 99:
                idGame = 'G0' + str(hitungGame(gameData)+1)
            elif jumlah_game >= 99:
                idGame = 'G' + str(hitungGame(gameData)+1)

            if namaGame != '' and kategori != '' and tahunRilis != '' and harga != '' and stokAwal != '':
                data = [idGame,namaGame, kategori, tahunRilis, harga, stokAwal]
                gameData += [data]
                print(f'Selamat! Berhasil menambahkan game {namaGame}')
                break

            else:
                print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
    else:
        print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')