from .Functions import*

def list_game(gameData,riwayatData,userid,role):
    if role == 'user':
        list_game_arr = list_game_dimiliki(gameData,riwayatData,userid)
        bikinTabel(list_game_arr,'owned')
    else:
        print('Akses hanya untuk role user!')