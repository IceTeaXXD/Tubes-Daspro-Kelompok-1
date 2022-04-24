from .Functions import*

def menu(role):
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
        print('==========BONUS==========')
        print('11. Magic Conch Shell')
        print('12. Tic Tac Toe')

    elif role == 'admin':
        print('1. Register')
        print('2. Login')
        print('3. Tambah Game')
        print('4. Ubah Game')
        print('5. Ubah Stok')
        print('6. Listing Game Toko')
        print('7. Cari Game Toko')
        print('8. Top Up')
        print('9. Help')
        print('10. Save')
        print('11. Exit')
        print('==========BONUS==========')
        print('12. Magic Conch Shell')
        print('13. Tic Tac Toe')
    else:
        print('1. Login')
        print('2. Help')