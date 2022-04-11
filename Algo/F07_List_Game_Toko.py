from .Functions import*

def list_game_toko(gameData):
    skema = input('Masukan skema pencarian (tahun-/harga-/tahun+/harga+) : ')
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
    quicksort(gameData,0,'ascending')