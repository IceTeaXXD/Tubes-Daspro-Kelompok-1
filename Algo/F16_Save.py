from .Functions import*

def save(userData,gameData,kepemilikanData,riwayatData):
    path = './'
    os.chdir(path)
    namaFolder = input('Masukan nama folder penyimpanan: ')
    if not os.path.exists(namaFolder):
        os.mkdir(namaFolder)

    userData = [['id','username','nama','password','role','saldo']] + userData
    gameData = [['id','nama','kategori','tahun_rilis','harga','stok']] + gameData
    kepemilikanData = [['game_id','user_id']] + kepemilikanData
    riwayatData = [['game_id','nama','harga','user_id','tahun_beli']] + riwayatData

    saving(userData,namaFolder,'user')
    saving(gameData,namaFolder,'game')
    saving(kepemilikanData,namaFolder,'kepemilikan')
    saving(riwayatData,namaFolder,'riwayat')
