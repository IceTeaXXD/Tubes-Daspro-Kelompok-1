from .Functions import*

def list_game(gameData,riwayatData,nama,role):
    if role == 'user':
        list_game_arr = list_game_dimiliki(gameData,riwayatData,nama)
        list_game_arr.sort(key=lambda id: id[0])
        bikinTabel(list_game_arr,'owned')
    else:
        print('Akses hanya untuk role user!')