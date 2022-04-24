##### Modul List Game pada Toko #####
# Fungsi untuk melakukan pencarian game berdasarkan kategori dan disajikan dalam bentuk tabel

##### KAMUS ARGUMEN #####
# gameData : 2D Matrix of String

##### KAMUS LOKAL #####
# skema : String
# list_sorted : 2D Matrix of String

from .Functions import*

def list_game_toko(gameData):
    skema = input('Masukan skema pencarian (tahun-/harga-/tahun+/harga+) : ')

    # Perkondisian untuk melakukan pemanggilan fungsi quicksort
    if skema == 'tahun-':
        list_sorted = quicksort(gameData,3,'descending')
        bikinTabel(list_sorted,'game')
    elif skema == 'harga-':
        list_sorted = quicksort(gameData,4,'descending')
        bikinTabel(list_sorted,'game')
    elif skema == 'tahun+':
        list_sorted = quicksort(gameData,3,'ascending')
        bikinTabel(list_sorted,'game')
    elif skema == 'harga+':
        list_sorted = quicksort(gameData,4,'ascending')
        bikinTabel(list_sorted,'game')
    elif skema == '':
        list_sorted = quicksort(gameData,0,'ascending')
        bikinTabel(list_sorted,'game')
    else:
        print('Skema sorting tidak valid')

    quicksort(gameData,0,'ascending') # Melakukan sorting gameData ke bentuk semula setelah terjadi manipulasi