from pytube import *
from tkinter import *
def youtube():
    link=var.get()
    video=YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download("D:\youtube")
    print("Video Succesfully Downloaded")
    
root=Tk()
root.geometry('500x500')
root.title("YouTube Video Downloading GUI")
root.configure(bg="cyan")
l=Label(text="YouTube Video Downloader",fg="VioletRed4",font='50')
l.place(x=100,y=100)
var=StringVar()
e=Entry(root,textvariable=var)
e.place(x=60,y=130,width='400')
b=Button(text="DOWNLOAD",fg="Black",bg="Green",command=youtube)
b.place(x=140,y=160)








root.mainloop()
