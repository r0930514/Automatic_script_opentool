import os
import tkinter as tk 
import tkinter.messagebox as tm
from functools import partial
import time


#初始設定
path = './所有SH' #存取位置
dirs = os.listdir(path) #將路徑中的資料存入一個陣列中 （資料0、 資料1)
dirs_t = os.listdir(path)
dirs_count = len(dirs) #這個資料夾中有多少個文件
print (dirs)
print(dirs_t)
os.chdir(path) #移動到指定的資料夾

#主視窗設定
win = tk.Tk()
win.title("整合指令集GUI")
win.config(background = "white")
win.geometry("400x600")
win.resizable(0,0)

#Command函數設定
def com_funtion (t):
    information.config(fg="black",text="執行開始，請前往終端機")
    com = dirs_t[t] 
    os.system("./%s" %(com))
    exit()

#按鈕
for i in range(0,dirs_count,1):
    dirs[i] = tk.Button(text=dirs[i]) #按鈕顯示文字設定
    dirs[i].config(background="white") #按鈕背景
    dirs[i].pack() #包裝按鈕

#按鈕指令設定
for q in range(0,dirs_count,1):
    dirs[q].config(command = partial(com_funtion,q))

#退出按鈕
exitbtn = tk.Button(text="EXIT")
exitbtn.config(background = "white")
def COM():
    exit()
exitbtn.config(command = COM)
exitbtn.pack()

#文字提示
information = tk.Label(fg="black",text="請選擇要執行的項目")
information.pack()

#視窗常駐（需要在最底下）
win.mainloop()

