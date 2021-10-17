import tkinter
from lib.rangeSelect import RangeSelect
from threading import Lock
class ScreenRange:
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def changeRange(self):
        rangeSelect = RangeSelect()
        rangeSelect.rangeSelect(self.callbackRange)

    def callbackRange(self, sx, sy, ex, ey):
        self.startX, self.startY, self.endX, self.endY = sx, sy, ex, ey