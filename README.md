# TouchDesignerにfitsファイルを読み込む機能

## 環境構築


#### TouchDesignerの環境内にPillowライブラリをインストール
```
> & "C:\Program Files\Derivative\TouchDesigner\bin\python.exe" -m pip install Pillow
```

## 1. fitsファイルをPythonで読み込み＆OSC通信

#### 1.IPアドレスとポート番号を設定
```
# OSCクライアントの設定
client = udp_client.SimpleUDPClient("000.00.000.00", 8000) 
```
<br>

#### 2.fitsファイルの読み込み
fitsファイルの場所を以下のコードに記述
```
# FITSファイルの読み込み
file_name = "your-fits-file.fits" # アップロードしたファイル名に合わせて変更
```
<br>

#### 3.send_touchdesigner.pyをローカル環境で実行


## 2. TouchDesignerでfitsファイルを画像化

#### 1.TouchDesignerでOSC通信の設定

参考リンク：
https://qiita.com/iwaken71/items/f4c9e1c3b789d19657ae

#### 2.Text DATにget_touchdesigner.pyを記入

#### 3.null DATにOSC in DATを接続

#### 4.画像出力用のmovie file in CHOPを配置

#### 5.Text DATのget_touchdesigner.pyを実行