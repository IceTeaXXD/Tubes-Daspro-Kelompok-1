from .Functions import*

def save(userData,gameData,kepemilikanData,riwayatData):
    path = './'
    os.chdir(path)

    namaFolder = input('Masukan nama folder penyimpanan: ')

    while length_of_obj(namaFolder) == 0:
        print('Nama folder tidak boleh kosong!')
        namaFolder = input('Masukan nama folder penyimpanan: ')

    if not os.path.exists(namaFolder):
        os.mkdir(namaFolder)

    userData = [['id','username','nama','password','role','saldo']] + userData
    gameData = [['id','nama_game','kategori','tahun_rilis','harga','stok']] + gameData
    kepemilikanData = [['game_id','user_id']] + kepemilikanData
    riwayatData = [['game_id','nama_game','harga','user_id','tahun_beli']] + riwayatData

    saving(userData,namaFolder,'user')
    saving(gameData,namaFolder,'game')
    saving(kepemilikanData,namaFolder,'kepemilikan')
    saving(riwayatData,namaFolder,'riwayat')

    return True