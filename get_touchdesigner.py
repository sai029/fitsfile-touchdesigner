import numpy as np
from PIL import Image
import json
import re

#fitsデータの受け取り
data = [[cell.val for cell in row] for row in op('null1').rows()]

# 正規表現で /data_chunk の後の文字列だけ抽出
extracted = ""
for row in data:
    for item in row:
        match = re.match(r'^/data_chunk "(.*)"$', item)
        if match:
            extracted += match.group(1)

# データをNumPy配列に変換
data = np.array(json.loads(extracted))
# NaN除去
data = np.nan_to_num(data)


#データの数だけフレームを表示
for i in range(len(data[0])):
    frame = data[0, i, :, :]

    # 画像スケーリング（0〜255に正規化）
    data_min = np.min(frame)
    data_max = np.max(frame)
    scaled_data = 255 * (frame - data_min) / (data_max - data_min)
    scaled_data = scaled_data.astype(np.uint8)

    # 画像の表示
    image = Image.fromarray(scaled_data)
    image.save('/tmp/fits_img.png')
    op('moviefilein1').par.file = '/tmp/fits_img.png'
