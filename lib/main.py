#!/usr/bin/env python3

import os
import tkinter as tk
import requests as rq
import subprocess as sp
from tkinter import messagebox
import minecraft_launcher_lib as ml

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


def start():
    email = str(mailInp.get())
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

    version = "1.16.3"
    print(version)

    directory = ml.utils.get_minecraft_directory()

    login_data = ml.account.login_user(email, password)

    options = {
    "username": login_data["selectedProfile"]["name"],
    "uuid": login_data["selectedProfile"]["id"],
    "token": login_data["accessToken"],
    "jvmArguments": ["-Xmx1G", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseG1GC", "-XX:G1NewSizePercent=20", "-XX:G1ReservePercent=20", "-XX:MaxGCPauseMillis=50", "-XX:G1HeapRegionSize=32M"],
    "launcherName": "StyxCraft",
    "launcherVersion": "1.0",
    "enableLoggingConfig": False,
    }
    minecraft_command = ml.command.get_minecraft_command(version, directory, options)
    print(minecraft_command)
    sp.call(minecraft_command)

titleTxt = tk.Label(win, text="Styx", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

inputFrame1 = tk.Frame(win)
inputFrame1.pack()

inputFrame2 = tk.Frame(win)
inputFrame2.pack()

mailTxt = tk.Label(inputFrame1, text="E-Mail", font=('Calibri Light', 20, "bold"), bg=bgColor, fg=fgColor)
mailTxt.pack(side="left")

mailInp = tk.Entry(inputFrame1, font=('Calibri Light', 20), bg=bgColor, fg=fgColor)
mailInp.pack(side="right")

pwTxt = tk.Label(inputFrame2, text="Password", font=('Calibri Light', 20, "bold"), bg=bgColor, fg=fgColor)
pwTxt.pack(side="left")

pwInp = tk.Entry(inputFrame2, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, show="*")
pwInp.pack(side="right")

startBtn = tk.Button(win, text="Start", command=start, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
startBtn.pack()

win.mainloop()
