from .Functions import*

##### KAMUS LOKAL #####
# tanya = String
# x = Integer
# a = Integer
# c = Integer
# m = Integer
# LCG = Integer
# n = Integer
# jawaban = Array of String

def kerangajaib():
    while True:
        tanya = input('Apa pertanyaanmu? ')
        if tanya =='':
            break
        else:
            # Fungsi LCG untuk mendapatkan random integer
            x = int(time.time()) 
            a = x % 10
            c = int(time.process_time_ns())
            m = 19
            LCG = ((a*x)+c) % m 
            n = abs((LCG % 6))

            jawaban = ['Ya', 'Tidak','Bisa Jadi','Mungkin','Tentunya','Tidak mungkin']
            print(jawaban[n])