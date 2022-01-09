#import pyautogui
from PIL import ImageGrab
from rangeSelect import RangeSelect

r = RangeSelect()
a, b, c, d = r.rangeSelect()

im = ImageGrab.grab(all_screens=True, bbox=(a, b, c, d))
im.save("aaa.png")
#screenshot = pyautogui.screenshot(region = (a, b, c, d))
#screenshot.save('スクリーンショット.png')
