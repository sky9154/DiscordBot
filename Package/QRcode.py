from MyQR import myqr
import requests
import os
def build(img, url, fileType):
    kirito = myqr
    if "https" in img or "http" in img:   # 使用in運算子檢查
        imgURL = img
        img_data = requests.get(imgURL).content
        if fileType == "GIF" or fileType == "gif":
            img = "./picData.gif"
            name = "QRcode.gif"
        else:
            img = "./picData.png"
            name = "QRcode.png"
        with open(img, "wb") as f:
            f.write(img_data)
        f.close()
    version, level, qr_name = kirito.run(
        words = url,                  # 網址
        version = 1,                  # 二維碼的邊長
        picture = img,                # 二維碼的背景圖片
        colorized = True,             # 背景圖片是否採用彩色
        save_name = name    # 檔案名稱
    )
    os.remove(img)