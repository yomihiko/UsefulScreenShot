from tkinter.constants import X
from screeninfo import get_monitors
import tkinter

ADJUST_DISPLAY = 5 #表示調整定数

class RangeSelect:
    def __init__(self):
        self.__startX = 0 #開始X
        self.__startY = 0 #開始Y
        self.__endX = 0 #終了X
        self.__endY = 0 #終了Y

        monitors = get_monitors()
        #最も右にあるモニター
        rightMostMoniter = max(monitors, key=lambda m: m.x + m.width)
        #最も下にあるモニター
        bottomMoniter = max(monitors, key=lambda m: m.y + m.height)


        self.__width = rightMostMoniter.x + rightMostMoniter.width + ADJUST_DISPLAY #画面幅
        self.__height = bottomMoniter.y + bottomMoniter.height + ADJUST_DISPLAY #画面高さ

    #画面範囲選択メイン処理
    #返り値：開始x, 開始y, 終了x, 終了y
    def rangeSelect(self):


        # 表示画面全体を半透明の黒色にする
        root = tkinter.Tk()
        root.geometry(str(self.__width) + "x" + str(self.__height) + "+-"+str(ADJUST_DISPLAY) + "+-" + str(ADJUST_DISPLAY))
        root.overrideredirect(1)
        root.attributes("-alpha", 0.5)
        root.configure(background="black")
        root.bind('<Escape>',lambda e: self.pressEsc(root))


        # 赤枠の描画
        canvas = tkinter.Canvas(root, bg="black", width=self.__width, height=self.__height)
        canvas.place(relx=0, rely=0)

        canvas.bind("<ButtonPress-1>", lambda e: self.start_point_get(e, canvas))
        canvas.bind("<Button1-Motion>", lambda e: self.rect_drawing(e, canvas))
        canvas.bind("<ButtonRelease-1>", lambda e: self.release_action(e, root, canvas))

        root.mainloop()

        return self.__startX, self.__startY, self.__endX, self.__endY

    # クリック開始時
    def start_point_get(self, event, canvas):

        canvas.delete("range")  # 赤枠があれば削除

        # 赤枠を描画（rectangleは矩形の意味）
        canvas.create_rectangle(event.x,event.y, event.x + 1, event.y + 1, outline="red", tag="range")

        self.__startX, self.__startY = event.x, event.y

    # ドラッグ中のイベント - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def rect_drawing(self, event, canvas):

        # ドラッグ中のマウスポインタが領域外に出た時の処理
        if event.x < 0:
            self.__endX = 0
        else:
            self.__endX = min(self.__width, event.x)
        if event.y < 0:
            self.__endY = 0
        else:
            self.__endY = min(self.__height, event.y)

        # 赤枠を再描画
        canvas.coords("range", self.__startX, self.__startY, self.__endX, self.__endY)

    # ドラッグを離したときのイベント - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def release_action(self, event, root, canvas):

        self.__startX, self.__startY, self.__endX, self.__endY = [
            round(n - ADJUST_DISPLAY) for n in canvas.coords("range")
        ]
        root.destroy()
    
    #Escキーが押された時の処理
    def pressEsc(self, root):
        self.__startX, self.__startY, self.__endX, self.__endY = 0, 0, 0, 0 #Esc押下時は未選択として扱う
        root.destroy()
    