def gambarPapan(arr):
    print(arr[0] + '|' +arr[1] + '|' + arr[2])
    print('-'*3 + '+' + '-'*3 + '+' + '-'*3)
    print(arr[3] + '|' +arr[4] + '|' + arr[5])
    print('-'*3 + '+' + '-'*3 + '+' + '-'*3)
    print(arr[6] + '|' +arr[7] + '|' + arr[8])

arr = ['   ' for i in range(9)]

turn = 0
while True:
    gambarPapan(arr)
    turn += 1
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
    elif turn == 9:
        print('Tidak ada pemenang')
        break
    
    if turn % 2 == 0:
        print('Giliran ' + 'X')
        char = ' X '
    else:
        print('Giliran ' + 'O')
        char = ' O '
    
    pos = input('Pilih posisi: ')
    if pos == '1':
        arr[0] = char
    elif pos == '2':
        arr[1] = char
    elif pos == '3':
        arr[2] = char
    elif pos == '4':
        arr[3] = char
    elif pos == '5':
        arr[4] = char
    elif pos == '6':
        arr[5] = char
    elif pos == '7':
        arr[6] = char
    elif pos == '8':
        arr[7] = char
    elif pos == '9':
        arr[8] = char
    else:
        print('Pilihan tidak valid')
        continue

    # if pos == '1' and arr[0] == '   ':
    #     arr[0] = char
    #     break
    # elif pos == '2' and arr[1] == '   ':
    #     arr[1] = char
    #     break
    # elif pos == '3' and arr[2] == '   ':
    #     arr[2] = char
    #     break
    # elif pos == '4' and arr[3] == '   ':
    #     arr[3] = char
    #     break
    # elif pos == '5' and arr[4] == '   ':
    #     arr[4] = char
    #     break
    # elif pos == '6' and arr[5] == '   ':
    #     arr[5] = char
    #     break
    # elif pos == '7' and arr[6] == '   ':
    #     arr[6] = char
    #     break
    # elif pos == '8' and arr[7] == '   ':
    #     arr[7] = char
    #     break
    # elif pos == '9' and arr[8] == '   ':
    #     arr[8] = char
    #     break