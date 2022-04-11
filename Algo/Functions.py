import os
import argparse
import sys
import math
import time
from datetime import date

def csv_to_arr(folder,filename):
    if filename == 'user' or filename == 'game':
        kolom = 6
    elif filename == 'kepemilikan':
        kolom = 2
    elif filename == 'riwayat':
        kolom = 5

    arr = []
    csv = open(f'./{folder}/{filename}.csv')
    next(csv)
    for row in csv:
        ch = ';'
        tmp = ''
        for c in row:
            if c == ch or c == '\n':
                arr += [tmp]
                tmp = ''
            else:
                tmp += c
        if tmp:
            arr += [tmp]
            
    # create matrix
    new_arr=[["" for j in range(kolom)] for i in range(length_of_obj(arr)//kolom)]
    count = 0
    for i in range(length_of_obj(arr)//kolom):
        for j in range(kolom):
            new_arr[i][j] = arr[count]
            count += 1
        if count == length_of_obj(arr):
            break
    return new_arr

def length_of_obj(obj):
    counter = 0
    for i in obj:
        counter += 1
    return counter

def saving(data,namaFolder,filename):
    f = open(f'./{namaFolder}/{filename}.csv','w')
    for i in range(length_of_obj(data)):
        for j in range (length_of_obj(data[i])):
            f.write(str(data[i][j]))
            if j == len(data[i])-1:
                f.write('\n')
            else:
                f.write(';')

def quicksort(arr,indeks,sortType):
    if indeks == 0:
        for i in range(length_of_obj(arr)):
            for j in range(i+1,length_of_obj(arr)):
                if arr[i][indeks] > arr[j][indeks]:
                    arr[i],arr[j] = arr[j],arr[i]        

    elif sortType == 'ascending':
        for i in range(length_of_obj(arr)):
            for j in range(i+1,length_of_obj(arr)):
                if int(arr[i][indeks]) > int(arr[j][indeks]):
                    arr[i],arr[j] = arr[j],arr[i] 
                    
    elif sortType == 'descending':
        for i in range(length_of_obj(arr)):
            for j in range(i+1,length_of_obj(arr)):
                if int(arr[i][indeks]) < int(arr[j][indeks]):
                    arr[i],arr[j] = arr[j],arr[i]    
    return arr

def kaliString(string,kali):
    hasil = ''
    for i in range(kali):
        hasil += string
    return hasil

def bikinTabel(list,jenisTabel):
    if jenisTabel == 'game':
        kolom0 = ' ID Game '
        kolom1 = ' Nama Game '
        kolom2 = ' Kategori '
        kolom3 = ' Tahun Rilis '
        kolom4 = ' Harga '
        kolom5 = ' Stok '

        longest0 = length_of_obj(kolom0)
        longest1 = length_of_obj(kolom1)
        longest2 = length_of_obj(kolom2)
        longest3 = length_of_obj(kolom3)
        longest4 = length_of_obj(kolom4)
        longest5 = length_of_obj(kolom5)

        for item in list:
            if length_of_obj(str(item[0])) > longest0:
                longest0 = length_of_obj(str(item[0]))

        for item in list:
            if length_of_obj(str(item[1])) > longest1:
                longest1 = length_of_obj(str(item[1]))

        for item in list:
            if length_of_obj(str(item[2])) > longest2:
                longest2 = length_of_obj(str(item[2]))

        for item in list:
            if length_of_obj(str(item[3])) > longest3:
                longest3 = length_of_obj(str(item[3]))
        
        for item in list:
            if length_of_obj(str(item[4])) > longest4:
                longest4 = length_of_obj(str(item[4]))
        
        for item in list:
            if length_of_obj(str(item[5])) > longest5:
                longest5 = length_of_obj(str(item[5]))

        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+longest5+25))
        print('|',kolom0,kaliString(' ',(longest0-length_of_obj(kolom0))),'|',kolom1,kaliString(' ',(longest1-length_of_obj(kolom1)+1))+'|',kolom2,kaliString(' ',(longest2-length_of_obj(kolom2)+1))+'|',kolom3,kaliString(' ',(longest3-length_of_obj(kolom3)+1))+'|',kolom4,kaliString(' ',(longest4-length_of_obj(kolom4)+1))+'|',kolom5,kaliString(' ',(longest5-length_of_obj(kolom5)+1))+'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+longest5+25))
        for item in list:
            print('|',item[0],kaliString(' ',(longest0-length_of_obj(str(item[0])))),'|',item[1],kaliString(' ',(longest1-length_of_obj(str(item[1])))),'|',item[2],kaliString(' ',(longest2-length_of_obj(str(item[2])))),'|',item[3],kaliString(' ',(longest3-length_of_obj(str(item[3])))),'|',item[4],kaliString(' ',(longest4-length_of_obj(str(str(item[4]))))),'|',item[5],kaliString(' ',(longest5-length_of_obj(str(item[5])))),'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+longest5+25))
    
    elif jenisTabel == 'owned':
        kolom0 = ' ID Game '
        kolom1 = ' Nama Game '
        kolom2 = ' Kategori  '
        kolom3 = ' Tahun Rilis '
        kolom4 = ' Harga '

        longest0 = length_of_obj(kolom0)
        longest1 = length_of_obj(kolom1)
        longest2 = length_of_obj(kolom2)
        longest3 = length_of_obj(kolom3)
        longest4 = length_of_obj(kolom4)

        for item in list:
            if length_of_obj(str(item[0])) > longest0:
                longest0 = length_of_obj(str(item[0]))

        for item in list:
            if length_of_obj(str(item[1])) > longest1:
                longest1 = length_of_obj(str(item[1]))

        for item in list:
            if length_of_obj(str(item[2])) > longest2:
                longest2 = length_of_obj(str(item[2]))

        for item in list:
            if length_of_obj(str(item[3])) > longest3:
                longest3 = length_of_obj(str(item[3]))

        for item in list:
            if length_of_obj(str(item[4])) > longest4:
                longest4 = length_of_obj(str(item[4]))
        
        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+25))
        print('|',kolom0,kaliString(' ',(longest0-length_of_obj(kolom0))),'|',kolom1,kaliString(' ',(longest1-length_of_obj(kolom1)+1))+'|',kolom2,kaliString(' ',(longest2-length_of_obj(kolom2)+1))+'|',kolom3,kaliString(' ',(longest3-length_of_obj(kolom3)+1))+'|',kolom4,kaliString(' ',(longest4-length_of_obj(kolom4)+1))+'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+25))
        for item in list:
            print('|',item[0],kaliString(' ',(longest0-length_of_obj(str(item[0])))),'|',item[1],kaliString(' ',(longest1-length_of_obj(str(item[1])))),'|',item[2],kaliString(' ',(longest2-length_of_obj(str(item[2])))),'|',item[3],kaliString(' ',(longest3-length_of_obj(str(item[3])))),'|',item[4],kaliString(' ',(longest4-length_of_obj(str(item[4])))),'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+longest4+25))

    elif jenisTabel == 'riwayat':
        kolom0 = ' ID Game '
        kolom1 = ' Nama Game '
        kolom2 = ' Harga Game '
        kolom3 = ' Tahun Beli '

        longest0 = length_of_obj(kolom0)
        longest1 = length_of_obj(kolom1)
        longest2 = length_of_obj(kolom2)
        longest3 = length_of_obj(kolom3)

        for item in list:
            if length_of_obj(str(item[0])) > longest0:
                longest0 = length_of_obj(str(item[0]))

        for item in list:
            if length_of_obj(str(item[1])) > longest1:
                longest1 = length_of_obj(str(item[1]))

        for item in list:
            if length_of_obj(str(item[4])) > longest2:
                longest2 = length_of_obj(str(item[2]))

        for item in list:
            if length_of_obj(str(item[5])) > longest3:
                longest3 = length_of_obj(str(item[5]))

        print(kaliString('=',longest0+longest1+longest2+longest3+17))
        print('|',kolom0,kaliString(' ',(longest0-length_of_obj(kolom0))),'|',kolom1,kaliString(' ',(longest1-length_of_obj(kolom1)+1))+'|',kolom2,kaliString(' ',(longest2-length_of_obj(kolom2)+1))+'|',kolom3,kaliString(' ',(longest3-length_of_obj(kolom3)+1))+'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+17))

        for item in list:
            print('|',item[0],kaliString(' ',(longest0-length_of_obj(str(item[0])))),'|',item[1],kaliString(' ',(longest1-length_of_obj(str(item[1])))),'|',item[4],kaliString(' ',(longest2-length_of_obj(item[4]))),'|',item[5],kaliString(' ',(longest3-length_of_obj(str(item[5])))),'|')
        print(kaliString('=',longest0+longest1+longest2+longest3+17))

def longestString(string,kali):
    hasil = ''
    for i in range(kali):
        hasil += string
    return hasil

def hitungGame(gameData):
    jumlahGame = 0
    for i in range (length_of_obj(gameData)):
        jumlahGame += 1
    return jumlahGame

def isOwned(kepemilikanData,idGame,userid):
    for i in range(length_of_obj(kepemilikanData)):
        if kepemilikanData[i][0] == idGame and kepemilikanData[i][1] == userid:
            return True
    return False

def list_game_dimiliki(gameData,riwayatData,userid):
    list_game_dimiliki = []
    for i in range(length_of_obj(riwayatData)):
        if riwayatData[i][3] == userid:
            idGame = riwayatData[i][0]
            for j in range(length_of_obj(gameData)):
                if idGame == gameData[j][0]:
                    namaGame = gameData[j][1]
                    kategoriGame = gameData[j][2]
                    tahunRilis = gameData[j][3]
                    hargaGame = gameData[j][4]
                    tahunBeli = riwayatData[i][4]
            list_game_dimiliki += [[idGame, namaGame, kategoriGame, tahunRilis, hargaGame, tahunBeli]]    
    return list_game_dimiliki

def clear():
    os.system('cls')

def batas():
    print('=========================================================')