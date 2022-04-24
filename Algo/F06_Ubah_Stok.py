##### Modul Ubah Stok #####
# Fungsi untuk melakukan pengubahan stok game pada database game yang ada

##### KAMUS ARGUMEN #####
# gameData : 2D Matrix of String
# role : String

##### KAMUS LOKAL #####
# idGame,namaGame,kategori,tahunRilis,harga,stokAwal : String
# stok, stokNow, indeks : Integer
# sudahUbah : Boolean

from .Functions import*

def ubah_stok(gameData,role):
    # Mengecek Apakah ada game yang tersimpan atau tidak
    if length_of_obj(gameData) == 0:
        print('Maaf, tidak ada data game yang tersimpan.')
    else:
        if role == "admin":
            # Looping untuk mencari indeks game yang akan diubah sesuai dengan idGame yang diinput
            sudahUbah = False
            while not(sudahUbah):
                idGame = input('Masukan id game yang akan diubah: ')
                for i in range(length_of_obj(gameData)):
                    if idGame == gameData[i][0]:
                        indeks = i
                        sudahUbah = True 
                        break

                if sudahUbah:
                    # Perkondisian untuk melakukan manipulasi data stok
                    stok = int(input('Masukan stok baru: '))
                    if stok >= 0:
                        stokNow = int(gameData[indeks][5])
                        stokNow += stok
                        gameData[indeks][5] = str(stokNow)
                        print(f'Stok game {gameData[indeks][1]} berhasil ditambahkan. Stok sekarang: {gameData[i][5]}')
                        break
                    elif stok < 0 and int(gameData[i][5]) >= abs(stok):
                        stokNow = int(gameData[indeks][5])
                        stokNow += stok
                        gameData[indeks][5] = str(stokNow)
                        print(f'Stok game {gameData[indeks][1]} berhasil dikurangi. Stok sekarang: {gameData[i][5]}')
                        break
                    else:
                        print(f'Stok game {gameData[indeks][1]} gagal dikurangi karena stok kurang. Stok sekarang: {gameData[i][5]}')
                        break
                else:
                    print('Tidak ada game dengan ID tersebut! Ulangi input idGame!')
        else:
            print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')