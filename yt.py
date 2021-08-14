from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube
from PIL import Image,ImageTk
import io
import base64
from urllib.request import urlopen

def progress_function(chunk, file_handle, bytes_remaining):
    filesize=file_size.get()
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    print(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))


def browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    destination.set(download_Directory)
    

def download():
    download_folder=destination.get()
    link=vid_link.get()
    yt=YouTube(link,on_progress_callback=progress_function)
    ym=yt.streams.get_highest_resolution()
    file_size.set(ym.filesize)
    ym.download(download_folder)
    messagebox.showinfo("SUCCESSFULL","Downloaded and Saved in\n"+ download_folder)
    for widget in window.winfo_children():
        widget.destroy()
    img=Image.open("happy.png")
    resize_image = img.resize((200, 200))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(image=img)
    label1.image = img
    label1.pack(pady=30)
    text=Label(text="Thank you for downloading!",font=("Arial",18),fg="#696969")
    text.pack(pady=20)


def foo():
    vid_link.set(ent_link.get())
    link=ent_link.get()    
    for widget in window.winfo_children():
        widget.destroy()  
    yt=YouTube(link)
    ym=yt.streams.get_highest_resolution()
    print(yt.streams)
    vtitle=Label(text=yt.title,wraplength=300,justify=CENTER,font=("Arial",12))
    vtitle.pack(pady=20) 
    raw_data = urlopen(yt.thumbnail_url).read()
    im = Image.open(io.BytesIO(raw_data))
    resize_image = im.resize((240,135))
    img = ImageTk.PhotoImage(resize_image) 
    label1 = Label(image=img)
    label1.image = img
    label1.pack(pady=10)
    vid_det=Frame()
    vid_det.pack(pady=2)
    duration=yt.length
    mins=duration//60
    secs=duration%60
    if secs<10:
        secs=str(secs)
        seconds="0"
        seconds=seconds+secs
    else:
        seconds=str(secs)
    dur=Label(vid_det,text=f"Duration: {mins}:"+seconds,font=("Calibri",11))
    dur.pack(side=LEFT,padx=10)
    size=ym.filesize
    size=size/(1024**2)
    size=round(size,2)
    vid_siz=Label(vid_det,text=f"Size of file: {size} MB",font=("Calibri",11))
    vid_siz.pack(side=RIGHT,padx=10)
    f=Frame()
    f.pack(pady=20)
    dest=Label(f,text="Destination Folder :",font=("Arial",10))
    dest.pack(side=LEFT)
    brow=Button(f,text="Browse",font=("Arial",10),command=browse)
    brow.pack(side=RIGHT)
    dest_ent=Entry(f,textvariable=destination,width=30)
    dest_ent.pack(side=RIGHT,padx=5)
    down=Button(text="Download",command=download,font=("Calibri",13),bg="#ed1c24",fg="white")
    down.pack(ipadx=5,ipady=2)

window=Tk()
window.geometry("400x400")
window.title('Youtube Downloader')
window.resizable(False,False)
img=Image.open("logo.png")
resize_image = img.resize((280, 210))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.pack(pady=10)
head=Label(text="Enter link of the video",font=("Arial",13),fg="#28282B")
head.pack(padx=10,pady=10)
ent_link=Entry(width=40)
ent_link.pack()
destination=StringVar()
vid_link=StringVar()
file_size=IntVar()
btn=Button(text="Proceed",font=("Calibri",13),bg="#ed1c24",fg="white",command=foo)
btn.pack(pady=20,ipadx=6)
window.mainloop()

