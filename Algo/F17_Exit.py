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