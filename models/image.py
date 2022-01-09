import re
import glob
import os
from tkinter import messagebox
from models.path import Path
from models.screenRange import ScreenRange
from PIL import ImageGrab
# キャプチャー画像モデル
class Image:
    def __init__(self):
        self.fileNameFormat = "" #ファイル名フォーマット文字列
        self.fileNumber = 1 #ファイルナンバー
        self.image = None #画像実態

    #ファイル名を変更
    def saveFileNameFormat(self, fileNameFormat: str):
        stripFileNameFormat = fileNameFormat.strip()
        self.fileNameFormat = stripFileNameFormat

    #スクリーンショットを撮影する
    def screenShot(self, range: ScreenRange, path: Path):
        
        im = ImageGrab.grab(all_screens=True, bbox=(range.startX, range.startY, range.endX, range.endY))
        patternNum = "\\{n+\\}" #{n…n}正規表現
        stripPath = path.folderPath.strip()
        stripFileName = self.fileNameFormat.strip()
        # エラー処理
        # ファイル出力先が空文字の場合など
        if not stripPath:
            messagebox.showerror('エラー', 'ファイル出力先が指定されていません。')
            return
        #ファイル種強く先がフォルダが存在しない場合など
        if not os.path.exists(stripPath):
            messagebox.showerror('エラー', 'ファイル出力先が存在しません。')
        #ファイル名が空文字の場合など
        if not stripFileName:
            messagebox.showerror('エラー', 'ファイル名が指定されていません。')

        #ファイルナンバーから出力ファイル名を生成
        tmpFileNumber = str(self.fileNumber).rjust(4, '0')
        tmpFileName = stripFileName + tmpFileNumber + '.png'
        print(stripPath + '/' + tmpFileName)

        #すでにファイルが存在する場合はファイルナンバーを適切に設定する
        while os.path.isfile(tmpFileName):
            self.fileNumber += 1
            tmpFileNumber = str(self.fileNumber).rjust(4, '0')
            tmpFileName = stripFileName + tmpFileNumber + '.png'

        if self.fileNumber >= 10000:
            messagebox.showerror('エラー', 'これ以上このフォルダにファイルを保存できません。')

        im.save(stripPath + '/' + tmpFileName)
        self.fileNumber += 1
        
