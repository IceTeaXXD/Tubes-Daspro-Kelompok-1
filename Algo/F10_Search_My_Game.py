##### Modul Search My Game #####
# Fungsi untuk melakukan pencarian game yang dimiliki berdasarkan id dan tahun dan disajikan dalam bentuk tabel

##### KAMUS ARGUMENT #####
# gameData : 2D Matrix of String
# riwayatData : 2D Matrix of String
# userid : String
# role : String

##### KAMUS LOKAL #####
# idGame : String
# tahunRilis : String
# arr_search : 2D Matrix of String
# arr_idGame : 2D Matrix of String
# arr_tahunRilis : 2D Matrix of String
# arr_my_game : 2D Matrix of String

from .Functions import*

def search_my_game(gameData,riwayatData,userid,role):
    if role == "user":
        # Inisiasi variabel
        idGame = input('Masukan id game: ')
        tahunRilis = input('Masukan tahun rilis: ')
        arr_search = []
        arr_idGame = []
        arr_tahunRilis = []

        arr_my_game = list_game_dimiliki(gameData,riwayatData,userid) # Mencari game yang telah dimiliki
        
        # Melakukan pengolahan data pada argument yang diberikan
        if idGame != '':
            arr_idGame += [idGame]
        else:
            for i in range(length_of_obj(gameData)):
                arr_idGame += [gameData[i][0]]        

        if tahunRilis != '':
            arr_tahunRilis += [tahunRilis]
        else:
            for i in range(length_of_obj(gameData)):
                arr_tahunRilis += [gameData[i][3]]

        for i in range(length_of_obj(arr_my_game)):
            if arr_my_game[i][0] in arr_idGame and arr_my_game[i][3] in arr_tahunRilis:
                arr_search += [arr_my_game[i]]

        if length_of_obj(arr_search) != 0:
            bikinTabel(arr_search,'owned')

        else:
            print('Daftar game pada toko yang memenuhi kriteria:')
            print('Tidak ada game pada toko yang memenuhi kriteria')