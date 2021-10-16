from models.path import Path
from tkinter import Entry
from tkinter import filedialog
from models.screenRange import ScreenRange
class Controller:
    def __init__(self):
        self.path = Path()
    def onClickFolderRef(self , pathEntry: Entry):
        self.path.changeFolderPath()
        pathEntry.configure(state="normal")
        pathEntry.delete(0, "end")
        pathEntry.insert(0, self.path.folderPath)
        pathEntry.configure(state="readonly")

    def onClickRangeBtn(self):
        screenRange = ScreenRange()
        screenRange.changeRange()
