# ライブラリのインポート
from astropy.io import fits
import numpy as np
from pythonosc import udp_client
 
# OSCクライアントの設定
client = udp_client.SimpleUDPClient("000.00.000.00", 8000) # 送信先のIPアドレスとポート番号を指定

# FITSファイルの読み込み
file_name = "your-fits-file.fits" # アップロードしたファイル名に合わせて変更
hdul = fits.open(file_name)
data = hdul
# ファイルを閉じる
hdul.close()


client.send_message("/header", data[0].header)
client.send_message("/data", data[0].data.tolist())


