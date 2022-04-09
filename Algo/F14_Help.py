from .Functions import*

def help(role):
    print('==========MENU==========')
    if role == 'user':
        print('1. Login')
        print('2. Listing Game Toko')
        print('3. Beli Game')
        print('4. Lihat Game Saya')
        print('5. Cari Game Saya')
        print('6. Cari Game Toko')
        print('7. Riwayat Pembelian')
        print('8. Help')
        print('9. Save')
        print('10. Exit')

    elif role == 'admin':
        print('1. Register')
        print('2. Login')
        print('3. Tambah Game')
        print('4. Ubah Game')
        print('5. Ubah Stok')
        print('6. Listing Game Toko')
        print('7. Cari Game Toko')
        print('8. Help')
        print('9. Save')
        print('10. Exit')
    else:
        print('1. Login')
        print('2. Help')