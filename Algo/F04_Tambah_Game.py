##### Modul Tambah Game #####
# Fungsi untuk melakukan penambahan data game pada database

##### KAMUS ARGUMEN #####
# gameData : 2D Matrix of String
# role : String

##### KAMUS LOKAL #####
# idGame,namaGame,kategori,tahunRilis,harga,stokAwal : String
# jumlah_game : Integer

from .Functions import*

def tambah_game(gameData,role): # Menerima gameData dan role user sebagai parameter
    if role == 'admin': # Validasi apakah role yang menjalankan adalah admin
        while True:
            # Menerima inputan dari user
            namaGame = input('Masukan nama game: ')
            kategori = input('Masukan kategori: ')
            tahunRilis = input('Masukan tahun rilis: ')
            harga = input('Masukan harga game: ')
            stokAwal = input('Masukan stok awal: ') 
            jumlah_game = hitungGame(gameData)  # Menghitung jumlah game yang ada untuk menentukan id game baru

            if jumlah_game < 9: 
                idGame = 'GAME00' + str(jumlah_game+1)
            elif jumlah_game < 99:
                idGame = 'GAME0' + str(jumlah_game+1)
            elif jumlah_game >= 99:
                idGame = 'GAME' + str(jumlah_game+1)

            # Memasukkan data ke dalam gameData dengan syarat tidak ada data yang kosong
            if namaGame != '' and kategori != '' and tahunRilis != '' and harga != '' and stokAwal != '':
                data = [idGame,namaGame, kategori, tahunRilis, harga, stokAwal]
                gameData += [data]
                print(f'Selamat! Berhasil menambahkan game {namaGame}')
                break

            else:
                print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
    else:
        print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')