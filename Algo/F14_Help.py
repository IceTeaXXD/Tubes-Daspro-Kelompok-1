##### MODUL HELP #####
# Memberi penjelasan atas menu yang ada

##### KAMUS ARGUMENT #####
# role : String

from .Functions import*

def help(role):
    print('==========H E L P==========')
    if role == 'user':
        print('1. Login - Untuk login ke akun')
        print('2. Listing Game Toko 0 - Untuk menampilkan daftar game yang tersedia di toko')
        print('3. Beli Game - Untuk membeli game')
        print('4. Lihat Game Saya - Untuk melihat daftar game yang telah dibeli')
        print('5. Cari Game Saya - Untuk mencari game yang telah dibeli')
        print('6. Cari Game Toko - Untuk mencari game yang tersedia di toko')
        print('7. Riwayat Pembelian - Untuk melihat daftar game yang telah dibeli')
        print('8. Help - Untuk melihat daftar menu')
        print('9. Save - Untuk menyimpan data ke dalam file')
        print('10. Exit - Untuk keluar dari program')
        print('11. Magic Conch Shell - Minigame yang dapat menjawab pertanyaan kita')
        print('12. Tic Tac Toe - Minigame yang Tic Tac Toe')

    elif role == 'admin':
        print('1. Register - Untuk mendaftar akun')
        print('2. Login - Untuk login ke akun')
        print('3. Tambah Game - Untuk menambah game ke dalam toko')
        print('4. Ubah Game - Untuk mengubah game yang telah ditambahkan')
        print('5. Ubah Stok - Untuk mengubah stok game yang telah ditambahkan')
        print('6. Listing Game Toko - Untuk menampilkan daftar game yang tersedia di toko')
        print('7. Cari Game Toko - Untuk mencari game yang tersedia di toko')
        print('8. Top Up - Untuk menambah saldo')
        print('9. Help - Untuk melihat daftar menu')
        print('10. Save - Untuk menyimpan data ke dalam file')
        print('11. Exit - Untuk keluar dari program')
        print('12. Magic Conch Shell - Minigame yang dapat menjawab pertanyaan kita')
        print('13. Tic Tac Toe - Minigame yang Tic Tac Toe')
    else:
        print('1. Login - Untuk login ke akun')
        print('2. Help - Untuk melihat daftar menu')