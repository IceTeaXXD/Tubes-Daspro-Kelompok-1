from .Functions import*

def list_game(gameData,riwayatData,userid,role):
    if role == 'user':
        list_game_arr = list_game_dimiliki(gameData,riwayatData,userid)
        if length_of_obj(list_game_arr) != 0:
            bikinTabel(list_game_arr,'owned')
        else:
            print('Anda belum memiliki game!')
    else:
        print('Akses hanya untuk role user!')