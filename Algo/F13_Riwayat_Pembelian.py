from .Functions import*

def riwayat(gameData,riwayatData,userid,role):
    if role== 'user':
        game_dimiliki = list_game_dimiliki(gameData,riwayatData,userid)
        
        if length_of_obj(game_dimiliki) != 0:
            print('Riwayat transaksi:')
            bikinTabel(game_dimiliki,'riwayat')

        else:
            print('Riwayat transaksi:')
            print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')

    else:
        print('Akses hanya untuk role user!')