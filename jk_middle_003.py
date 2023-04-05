import pyautogui as pgui
import time

pgui.FAILSAFE = True

#エクスプローラーの処理に使う変数
index1 = 0
y_pos = ["190", "220", "250"]

#エクセルの処理に使う変数
index2 = 0
value1 = ["1000", "2000", "3000"]
value2 = ["100", "200", "300"]
sell_x1 = "50"
sell_x2 = "180"
sell_x3 = "260"
sell_pos_y = ["185", "205", "220"]
sell_a = ["a1", "a2", "a3"]
sell_b = ["b1", "b2", "b3"]

#エクスプローラー上
def open_explorer(y_position):
    pgui.press("win")
    pgui.click(x=720, y=340, duration=1)
    pgui.write("explorer", 0.3)
    time.sleep(1)
    pgui.press("enter")
    pgui.click(x=70, y=255, duration=0.5)
    pgui.doubleClick(x=310, y=215, duration=0.5)
    pgui.doubleClick(x=300, y=y_position, duration=0.5)

#エクセル上
def activate_xlsx(sell_y , sella, sellb, value_1, value_2):
    pgui.doubleClick(x=50, y=sell_y, duration=1)
    pgui.write(value_1, 0.3)
    pgui.doubleClick(x=180, y=sell_y, duration=1)
    pgui.write(value_2, 0.3)
    pgui.doubleClick(x=260, y=sell_y, duration=1)
    pgui.write("=sum(" + sella + "," + sellb + ")", 1)
    pgui.press("enter")
    pgui.hotkey("Ctrl", "s")
    pgui.click(x=930, y=590, duration=0.5)
    pgui.hotkey("Ctrl", "q")

time.sleep(3)


while index1 < 3:
    y_position = y_pos[index1]
    open_explorer(y_position)
    index1 = index1 + 1
    sell_y = sell_pos_y[index2]
    sella = sell_a[index2]
    sellb = sell_b[index2]
    value_1 = value1[index2]
    value_2 = value2[index2]
    activate_xlsx(sell_y , sella, sellb, value_1, value_2)
    index2 = index2 + 1














