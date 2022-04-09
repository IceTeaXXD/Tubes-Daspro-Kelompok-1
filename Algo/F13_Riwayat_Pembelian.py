from .Functions import*

def riwayat(riwayatData,nama,role):
    if role== 'user':
        arr_riwayat = []
        for i in range(length_of_obj(riwayatData)):
            if riwayatData[i][1] == nama:
                arr_riwayat.append(riwayatData[i])
        if length_of_obj(arr_riwayat) != 0:
            print('Riwayat transaksi:')
            print(tabulate(arr_riwayat, headers=["ID", "Nama", "Harga", "User ID", "Tahun Beli",], tablefmt="fancy_grid"))
        else:
            print('Riwayat transaksi:')
            print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')
    else:
        print('Akses hanya untuk role user!')