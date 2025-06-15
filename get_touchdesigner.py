import numpy as np
from PIL import Image

#fitsデータの受け取り
data = hdul[0].data

# 画像スケーリング（0〜255に正規化）
data = np.nan_to_num(data)  # NaN除去
data_min = np.min(data)
data_max = np.max(data)
scaled_data = 255 * (data - data_min) / (data_max - data_min)
scaled_data = scaled_data.astype(np.uint8)

# 画像の表示
image = Image.fromarray(scaled_data)
image.show()