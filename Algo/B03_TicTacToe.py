from .Functions import*

##### KAMUS LOKAL #####
# arr = Array of String
# turn = Integer
# pos = Integer
# char = String

def gambarPapan(arr): # Fungsi untuk menggambar papan permainan
    print(arr[0] + '|' + arr[1] + '|' + arr[2])
    print(kaliString('-',3) + '+' + kaliString('-',3) + '+' + kaliString('-',3))
    print(arr[3] + '|' + arr[4] + '|' + arr[5])
    print(kaliString('-',3) + '+' + kaliString('-',3) + '+' + kaliString('-',3))
    print(arr[6] + '|' + arr[7] + '|' + arr[8])

def TicTacToe():
    arr = ['   ' for i in range(9)] # Inisiasi matriks arr kosong
    turn = 0
    while True: # Looping permainan
        clear()
        gambarPapan(arr)
        turn += 1

        # Kondisi Pemenang
        if arr[0] == arr[1] == arr[2] != '   ':
            print('Pemenangnya adalah ' + arr[0])
            break
        elif arr[3] == arr[4] == arr[5] != '   ':
            print('Pemenangnya adalah ' + arr[3])
            break
        elif arr[6] == arr[7] == arr[8] != '   ':
            print('Pemenangnya adalah ' + arr[6])
            break
        elif arr[0] == arr[3] == arr[6] != '   ':
            print('Pemenangnya adalah ' + arr[0])
            break
        elif arr[1] == arr[4] == arr[7] != '   ':
            print('Pemenangnya adalah ' + arr[1])
            break
        elif arr[2] == arr[5] == arr[8] != '   ':
            print('Pemenangnya adalah ' + arr[2])
            break
        elif arr[0] == arr[4] == arr[8] != '   ':
            print('Pemenangnya adalah ' + arr[0])
            break
        elif arr[2] == arr[4] == arr[6] != '   ':
            print('Pemenangnya adalah ' + arr[2])
            break
        elif turn == 10:
            print('Tidak ada pemenang')
            break
        
        # Kondisi Giliran pemain
        if turn % 2 == 0:
            print('Giliran ' + 'X')
            char = ' X '
        else:
            print('Giliran ' + 'O')
            char = ' O '
        
        # Validasi input tempat
        while True:
            try:
                pos = int(input('Pilih posisi: '))
                if arr[pos-1] == '   ':
                    arr[pos-1] = char
                    break
                elif pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9:
                    print('Posisi sudah terisi')
                else:
                    print('Input tidak valid!')
            except:
                print('Input tidak valid')