from .Functions import*

def search_game_at_store(gameData):
    idGame = input('Masukan id game: ')
    namaGame = input('Masukan nama game: ')
    hargaGame = input('Masukan harga game: ')
    kategoriGame = input('Masukan kategori game: ')
    tahunRilis = input('Masukan tahun rilis: ')
    
    arr_search = []
    arr_idGame = []
    arr_namaGame = []
    arr_hargaGame = []
    arr_kategoriGame = []
    arr_tahunRilis = []

    if idGame == '' and namaGame == '' and hargaGame == '' and kategoriGame == '' and tahunRilis == '':
        print('Maaf, id game, nama game, harga game, kategori game, dan tahun rilis tidak boleh kosong!')
        return

    if length_of_obj(idGame) > 0:
        arr_idGame += [idGame]
    else:
        for i in range(length_of_obj(gameData)):
            arr_idGame += [gameData[i][0]]
    
    if length_of_obj(namaGame) > 0:
        arr_namaGame += [namaGame]
    else:
        for i in range(length_of_obj(gameData)):
            arr_namaGame += [gameData[i][1]]

    if length_of_obj(hargaGame) > 0:
        arr_hargaGame += [hargaGame]
    else:
        for i in range(length_of_obj(gameData)):
            arr_hargaGame += [gameData[i][4]]

    if length_of_obj(kategoriGame) > 0:
        arr_kategoriGame += [kategoriGame]
    else:
        for i in range(length_of_obj(gameData)):
            arr_kategoriGame += [gameData[i][2]]

    if length_of_obj(tahunRilis) > 0:
        arr_tahunRilis += [tahunRilis]
    else:
        for i in range(length_of_obj(gameData)):
            arr_tahunRilis += [gameData[i][3]]

    for i in range(length_of_obj(gameData)):
        if gameData[i][0] in arr_idGame and gameData[i][1] in arr_namaGame and gameData[i][4] in arr_hargaGame and gameData[i][2] in arr_kategoriGame and gameData[i][3] in arr_tahunRilis:
            arr_search += [gameData[i]]

    if length_of_obj(arr_search) != 0:
        print('Daftar game pada toko yang memenuhi kriteria:')
        bikinTabel(arr_search,'game')

    else:
        print('Daftar game pada toko yang memenuhi kriteria:')
        print('Tidak ada game pada toko yang memenuhi kriteria')