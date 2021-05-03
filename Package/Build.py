from MyQR import myqr
import requests
kirito = myqr
def QRcode(img,url):
    imgfolder='D:/雜物/程式設計/Python/discord bot/demo'
    imageURL=img
    img_data = requests.get(imageURL).content
    with open('%s/%s.png' % (imgfolder, 'QRcodeIMG'), 'wb') as f:
        f.write(img_data)
    version, level, qr_name = kirito.run(
        words=url,                                                         # 網址
        version=1,                                                         # 通關率
        level='H',                                                         # 調整圖片方位
        picture='D:/雜物/程式設計/Python/discord bot/demo/QRcodeIMG.png',   # 設定背景
        colorized=True,                                                    # 是否為彩色
        contrast=2.0,                                                      # 對比
        brightness=1.0,                                                    # 亮度
        save_name='QRcode.png',                                            # 檔案名稱
        save_dir="D:/雜物/程式設計/Python/discord bot/demo/"                # 儲存在當前路徑
    )