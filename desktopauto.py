import os
import webbrowser
import tkinter as tk
from tkinter import messagebox

# -------- FUNCTIONS -------- #

def open_chrome():
    try:
        os.startfile("Path to chrome.exe") #Example:"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    except:
        messagebox.showerror("Error", "Chrome not found")

def open_vscode():
    try:
        os.startfile("Path to code.exe(VS CODE)") #Example:"C:\\Users\\YOUR USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    except:
        messagebox.showerror("Error", "VS Code not found")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_documents():
    webbrowser.open("Path to your Documents folder") #Example:"C:\\Users\\YOUR USERNAME\\Documents"

def study_mode():
    webbrowser.open("https://www.youtube.com")
    webbrowser.open("https://web.whatsapp.com/")
    webbrowser.open("Path to your Documents folder") #Example:"C:\\Users\\YOUR USERNAME\\Documents"

def coding_mode():
    try:
        os.startfile("https://www.chatgpt.com")
        os.startfile("Path to code.exe(VS CODE)") #Example:"C:\\Users\\YOUR USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    except:
        messagebox.showerror("Error", "Application path incorrect")

def entertainment_mode():
    webbrowser.open("https://www.youtube.com")
    webbrowser.open("https://www.netflix.com")

# -------- GUI -------- #

root = tk.Tk()
root.title("Desktop Automation Tool")
root.geometry("460x600")
root.configure(bg="#4D98CA")

# Title
title = tk.Label(
    root,
    text="Desktop Automation Tool",
    font=("Segoe UI", 20, "bold"),
    bg="#4D98CA",
    fg="#0d186f"
)
title.pack(pady=20)

# Frame for main buttons
frame = tk.Frame(root, bg="#4D98CA")
frame.pack()

# Button style (3D look)
btn_style = {
    "width": 18,
    "height": 2,
    "font": ("Segoe UI", 11,"bold"),
    "bg": "#DDCB72",
    "fg": "#1b2a49",
    "relief": "raised",
    "bd": 4,
    "activebackground": "#bcd3ff"
}

btn1 = tk.Button(frame, text="Open Chrome", command=open_chrome, **btn_style)
btn1.grid(row=0, column=0, padx=12, pady=10)

btn2 = tk.Button(frame, text="Open VS Code", command=open_vscode, **btn_style)
btn2.grid(row=0, column=1, padx=12, pady=10)

btn3 = tk.Button(frame, text="Open Files", command=open_documents, **btn_style)
btn3.grid(row=1, column=0, padx=12, pady=10)

btn4 = tk.Button(frame, text="Open YouTube", command=open_youtube, **btn_style)
btn4.grid(row=1, column=1, padx=12, pady=10)

# Modes Label
mode_label = tk.Label(
    root,
    text="Modes",
    font=("Segoe UI", 16, "bold"),
    bg="#4D98CA",
    fg="#0d186f"
)
mode_label.pack(pady=15)

mode_frame = tk.Frame(root, bg="#4D98CA")
mode_frame.pack()

mode_style = {
    "width": 22,
    "height": 2,
    "font": ("Segoe UI", 11,"bold"),
    "bg": "#38df5c",
    "fg": "#194231",
    "relief": "raised",
    "bd": 4,
    "activebackground": "#a6f4c9"
}

btn5 = tk.Button(mode_frame, text="Study Mode", command=study_mode, **mode_style)
btn5.grid(row=0, column=0, pady=8)

btn6 = tk.Button(mode_frame, text="Coding Mode", command=coding_mode, **mode_style)
btn6.grid(row=1, column=0, pady=8)

btn7 = tk.Button(mode_frame, text="Entertainment Mode", command=entertainment_mode, **mode_style)
btn7.grid(row=2, column=0, pady=8)

root.mainloop()