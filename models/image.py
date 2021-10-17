import re
from tkinter import messagebox
from models.screenRange import ScreenRange
from PIL import ImageGrab
# キャプチャー画像モデル
class Image:
    def __init__(self):
        self.fileNameFormat = "" #ファイル名フォーマット文字列
        self.fileNumber = 1 #ファイルナンバー
        self.image = None #画像実態

    #ファイル名フォーマットを変更
    def saveFileNameFormat(self, fileNameFormat: str):
        patternNum = "^.*\\{n+\\}" #{n…n}正規表現
        patternSuffix = "^.+\\.png$" #.png正規表現
        stripFileNameFormat = fileNameFormat.strip()

        rp1 = re.compile(patternNum)
        # ファイル名中に{n…n}が含まれない場合はエラー
        if(rp1.match(stripFileNameFormat) == None):
            messagebox.showerror('エラー', 'ファイル名中には「{n...n}」が必須です。')
            return
        
        rp2 = re.compile(patternSuffix)
        # ファイル名末尾が.pngでない場合はエラー
        if(rp2.match(stripFileNameFormat) == None):
            messagebox.showerror('エラー', 'ファイル名の末尾は「.png」にしてください。')
            return
        
        self.fileNameFormat = stripFileNameFormat
    
    def screenShot(self, range: ScreenRange):
        
        im = ImageGrab.grab(all_screens=True, bbox=(range.startX, range.startY, range.endX, range.endY))
        im.save("aaa" + str(self.fileNumber) + ".png")
        self.fileNumber += 1
        
