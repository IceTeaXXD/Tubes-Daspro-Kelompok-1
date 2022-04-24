##### MODUL RIWAYAT PEMBELIAN #####
# Mencari riwayat pembelian game

##### KAMUS ARGUMENT #####
# gameData : 2D Matrix of String
# riwayatData : 2D Matrix of String
# userid : String
# role : String

##### KAMUS LOKAL #####
# game_dimiliki : 2D Matrix of String

from .Functions import*

def riwayat(gameData,riwayatData,userid,role):
    if role== 'user':
        game_dimiliki = list_game_dimiliki(gameData,riwayatData,userid) # Mencari game yang telah dimiliki
        
        # Perkonidisian jika data game telah didapat dan melakukan output tabel
        if length_of_obj(game_dimiliki) != 0:
            print('Riwayat transaksi:')
            bikinTabel(game_dimiliki,'riwayat')

        else:
            print('Riwayat transaksi:')
            print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')

    else:
        print('Akses hanya untuk role user!')