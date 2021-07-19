
from tkinter import *
from tkinter import messagebox
import requests
import subprocess


def b1_event(event):
    #messagebox.showinfo("Pop up1", "Hello")
    r = requests.get('http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=5&PanSpeed=6&TiltSpeed=6', auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b2_event(event):
    #messagebox.showinfo("Pop up2", "Hello")
    r = requests.get('http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=1&PanSpeed=6&TiltSpeed=6', auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)


def b3_event(event):
    r = requests.get('http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=7&PanSpeed=6&TiltSpeed=6', auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b4_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=3&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b5_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b6_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=4&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b7_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=6&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b8_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=2&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b9_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Direction=8&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)
    #r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b10_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Zoom=0", auth=('admin', 'admin'), stream=True)
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b11_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Zoom=1", auth=('admin', 'admin'), stream=True)
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)

def b12_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Focus=0", auth=('admin', 'admin'), stream=True)
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)


def b13_event(event):
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Focus=1", auth=('admin', 'admin'), stream=True)
    r = requests.get("http://192.168.100.253/cgi/ptz_set?Channel=1&Group=PTZCtrlInfo&Stop=0&PanSpeed=6&TiltSpeed=6", auth=('admin', 'admin'), stream=True)



root=Tk()
root.title("CSF IP Cam Control Panel")#控制面板名稱
root.geometry("600x1000")

p1=PhotoImage(file = r"D:/jacob_liang/Desktop/lu.png")
lab1=Label(root,image=p1)
lab1.place(x=0,y=0,width=180,height=180)
lab1.bind('<Button-1>', b1_event)


p2=PhotoImage(file = r"D:/jacob_liang/Desktop/u.png")
lab2=Label(root,image=p2)
lab2.place(x=205,y=0,width=180,height=180)
lab2.bind('<Button-1>', b2_event)

p3=PhotoImage(file = r"D:/jacob_liang/Desktop/ru.png")
lab3=Label(root,image=p3)
lab3.place(x=410,y=0,width=180,height=180)
lab3.bind('<Button-1>', b3_event)

p4=PhotoImage(file = r"D:/jacob_liang/Desktop/l.png")
lab4=Label(root,image=p4)
lab4.place(x=0,y=205,width=180,height=180)
lab4.bind('<Button-1>', b4_event)

p5=PhotoImage(file = r"D:/jacob_liang/Desktop/stop.png")
lab5=Label(root,image=p5)
lab5.place(x=205,y=205,width=180,height=180)
lab5.bind('<Button-1>', b5_event)


p6=PhotoImage(file = r"D:/jacob_liang/Desktop/r.png")
lab6=Label(root,image=p6)
lab6.place(x=410,y=205,width=180,height=180)
lab6.bind('<Button-1>', b6_event)


p7=PhotoImage(file = r"D:/jacob_liang/Desktop/ld.png")
lab7=Label(root,image=p7)
lab7.place(x=0,y=410,width=180,height=180)
lab7.bind('<Button-1>', b7_event)


p8=PhotoImage(file = r"D:/jacob_liang/Desktop/d.png")
lab8=Label(root,image=p8)
lab8.place(x=205,y=410,width=180,height=180)
lab8.bind('<Button-1>', b8_event)


p9=PhotoImage(file = r"D:/jacob_liang/Desktop/rd.png")
lab9=Label(root,image=p9)
lab9.place(x=410,y=410,width=180,height=180)
lab9.bind('<Button-1>', b9_event)


p10=PhotoImage(file = r"D:/jacob_liang/Desktop/zoomout.png")
lab10=Label(root,image=p10)
lab10.place(x=0,y=615,width=180,height=180)
lab10.bind('<Button-1>', b10_event)


p11=PhotoImage(file = r"D:/jacob_liang/Desktop/zoomin.png")
lab11=Label(root,image=p11)
lab11.place(x=205,y=615,width=180,height=180)
lab11.bind('<Button-1>', b11_event)


p12=PhotoImage(file = r"D:/jacob_liang/Desktop/forcusout.png")
lab12=Label(root,image=p12)
lab12.place(x=0,y=820,width=180,height=180)
lab12.bind('<Button-1>', b12_event)

p13=PhotoImage(file = r"D:/jacob_liang/Desktop/forcusin.png")
lab13=Label(root,image=p13)
lab13.place(x=205,y=820,width=180,height=180)
lab13.bind('<Button-1>', b13_event)




root.mainloop()
