from astropy.io import fits
import numpy as np
from pythonosc import udp_client
import json
 
# OSCクライアントの設定
client = udp_client.SimpleUDPClient("000.00.000.00", 8000) # 送信先のIPアドレスとポート番号を指定

# FITSファイルの読み込み
file_name = "your-fits-file.fits" # アップロードしたファイル名に合わせて変更
hdul = fits.open(file_name)

client.send_message("/header", hdul[0].header)

data = hdul[0].data

#データを1次元に変換
flat_data = data.flatten()

chunk_size = 2000  # 送信するデータのチャンクサイズ

for i in range(0, len(flat_data), chunk_size):
    # データのチャンクを取得
    chunk = flat_data[i:i + chunk_size].tolist()
        
    # チャンクをJSON形式に変換して送信
    client.send_message("/data_chunk", json.dumps(chunk))


# ファイルを閉じる
hdul.close()