from .Functions import*

def load():
    clear()
    # Loading Argument
    parser = argparse.ArgumentParser(description='Masukkan Nama Folder!')
    parser.add_argument('NamaFolder', type=str, help='Nama folder tempat penyimpanan file csv')

    # Error Handling jika nama folder tidak diberikan
    if length_of_obj(sys.argv) == 1:
        print('Tidak ada nama folder yang diberikan!') 

    # Parsing Argument
    args = parser.parse_args()
    folder = args.NamaFolder

    # Error Handling jika nama folder tidak ditemukan
    if not os.path.exists(folder):
        print(f'Folder {folder} tidak ditemukan!')
        sys.exit()

    # Loading Data from CSV
    userData = csv_to_arr(folder,'user')
    gameData = csv_to_arr(folder,'game')
    kepemilikanData = csv_to_arr(folder,'kepemilikan')
    riwayatData = csv_to_arr(folder,'riwayat')

    return userData, gameData, kepemilikanData, riwayatData