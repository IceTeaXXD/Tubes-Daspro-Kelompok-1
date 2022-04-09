from .Functions import*

def load():
    # Loading Argument
    parser = argparse.ArgumentParser(description='argument')
    parser.add_argument('NamaFolder', type=str, help='Folder Name Harus Diisi!')
    args = parser.parse_args()
    folder = args.NamaFolder

    # Loading Data from CSV
    userData = csv_to_arr(folder,'user')
    gameData = csv_to_arr(folder,'game')
    kepemilikanData = csv_to_arr(folder,'kepemilikan')
    riwayatData = csv_to_arr(folder,'riwayat')

    return userData, gameData, kepemilikanData, riwayatData