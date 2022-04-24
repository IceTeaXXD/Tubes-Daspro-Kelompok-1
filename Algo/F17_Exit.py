##### MODUL EXIT #####
# Fungsi untuk keluar dari program

##### KAMUS ARGUEMTN #####
# userData : 2D Matrix of String
# gameData : 2D Matrix of String
# kepemilikanData : 2D Matrix of String
# riwayatData : 2D Matrix of String
# saved : Boolean

from .Functions import*
from .F16_Save import*

def Exit(userData,gameData,kepemilikanData,riwayatData,saved):
    if saved:
        os.system('cls')
        print('Terima kasih telah menggunakan aplikasi ini.')
        print('Sampai jumpa lagi!')
    else:
        pilih = input('Apakah anda ingin melakukan save terlebih dahulu (y/n) ? ')
        if pilih == 'y':
            save(userData,gameData,kepemilikanData,riwayatData)
            os.system('cls')
            print('Terima kasih telah menggunakan aplikasi ini.')
            print('Sampai jumpa lagi!')
        elif pilih == 'n':
            os.system('cls')
            print('Terima kasih telah menggunakan aplikasi ini.')
            print('Sampai jumpa lagi!')
        else:
            print('Pilihan tidak valid!')