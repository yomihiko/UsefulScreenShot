from tkinter import Tk, filedialog
import tkinter
from tkinter import Entry

class Path:
    def __init__(self):
        self.folderPath = ""

    def changeFolderPath(self):
        self.folderPath = filedialog.askdirectory()
