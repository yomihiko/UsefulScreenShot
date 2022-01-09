import tkinter
from models.path import Path
from tkinter import Entry
from models.screenRange import ScreenRange
from models.image import Image
import threading


class Controller:
    def __init__(self):
        self.path = Path()
        self.image = Image()
        self.screenRange = ScreenRange()

        self.image.saveFileNameFormat(fileNameFormat='scr')
        self.daemon = WaitScreenShotThread(self.image, self.screenRange, self.path)
        self.daemon.start()


    def onClickFolderRef(self , pathEntry: Entry):
        self.path.changeFolderPath()
        pathEntry.configure(state="normal")
        pathEntry.delete(0, "end")
        pathEntry.insert(0, self.path.folderPath)
        pathEntry.configure(state="readonly")

    def onClickRangeBtn(self):
        self.screenRange.changeRange()

    def saveFileNameFormat(self, event, fileNameEntry: Entry):
        self.image.saveFileNameFormat(fileNameEntry.get())
        fileNameEntry.delete(0, "end")
        fileNameEntry.insert(0, self.image.fileNameFormat)

    def shutDown(self, root: tkinter.Tk):
        root.destroy()

class WaitScreenShotThread(threading.Thread):
    def __init__(self, im: Image, sr: ScreenRange, path: Path):
        super(WaitScreenShotThread, self).__init__(target=self, daemon=True)
        self.im = im
        self.sr = sr
        self.path = path

    def run(self):
        f = open('screentime', 'r')
        text = f.read()
        f.close()
        while True:
            f = open('screentime', 'r')
            text2 = f.read()
            f.close()
            if(text2 != "" and  text != text2):
                self.im.screenShot(self.sr, self.path)
                text = text2
                