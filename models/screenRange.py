import tkinter
from lib.rangeSelect import RangeSelect
class ScreenRange:
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def changeRange(self):
        rangeSelect = RangeSelect()
        self.startX, self.startY, self.endX, self.endY = rangeSelect.rangeSelect()