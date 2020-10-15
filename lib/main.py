#!/usr/bin/env python3

import os
import requests as rq
import tkinter as tk
from tkinter import messagebox

# Theme
fgColor = "white"
bgColor = "#212121"
lightColor = "#3e7fef"
activeColor = "#3f3f3f"
errorColor = "#f4494f"
reliefStyle = "flat"

# Window
win = tk.Tk()
win.title("SML")
win.config(bg=bgColor)

# Check Java Path
os.system('where java > javapath.txt')
with open (os.getcwd() + '\\javapath.txt') as outlog:
    outdata = outlog.readlines()
javapath =outdata[0]

def start():
    username = str(userInp.get())
    password = str(pwInp.get())

    try:
        statuscheck = rq.get(f"https://authserver.mojang.com/")
    except:
        titleTxt["fg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="No connection to the internet")
        return

    if str(statuscheck) != "<Response [200]>":
        titleTxt["fg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="Bad or no connection to mojang auth server")
        return
    else:
        titleTxt["fg"] = lightColor

    usercheck = rq.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")

    if usercheck.text == "":
        userInp["fg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="Name incorrect")
        return
    else:
        userInp["fg"] = lightColor


    # rqout = rq.get(f"https://login.minecraft.net?user={username}&password={password}&version=13")


    javacommand = f'cd "C:/Program Files (x86)/Common Files/Oracle/Java/javapath/"'
    startcommand = f'java.exe -Xms512m -Xmx1g -Djava.library.path=natives/ -cp "minecraft.jar;lwjgl.jar;lwjgl_util.jar" net.minecraft.client.Minecraft {username} {sessionid}'
    os.system(javacommand)
    os.system(startcommand)


titleTxt = tk.Label(win, text="Styx", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

inputFrame1 = tk.Frame(win)
inputFrame1.pack()

inputFrame2 = tk.Frame(win)
inputFrame2.pack()

userTxt = tk.Label(inputFrame1, text="Username", font=('Calibri Light', 20, "bold"), bg=bgColor, fg=fgColor)
userTxt.pack(side="left")

userInp = tk.Entry(inputFrame1, font=('Calibri Light', 20), bg=bgColor, fg=fgColor)
userInp.pack(side="right")

pwTxt = tk.Label(inputFrame2, text="Password", font=('Calibri Light', 20, "bold"), bg=bgColor, fg=fgColor)
pwTxt.pack(side="left")

pwInp = tk.Entry(inputFrame2, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, show="*")
pwInp.pack(side="right")

startBtn = tk.Button(win, text="Start", command=start, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
startBtn.pack()

win.mainloop()
