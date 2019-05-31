from tkinter import *
import os
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog

root = Tk()
mixer.init()

# Create menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create Submenu
subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo(
        "About Melody", " This is a music player built using Python by Piyush")


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)


root.title("Melody Music Player")

# root.geometry("300x300")
if "nt" == os.name:
    root.iconbitmap(bitmap=r"melody.ico")
else:
    root.iconbitmap(bitmap=r"@music-player.xbm")

text = Label(root, text="Lets make some noise")
text.pack(pady=10)


# labelphoto = Label(root, image=photo)
# labelphoto.pack()


def play_music():
    try:
        paused  # Check if Pause is declared or not
    except NameError as e:
        print(e)
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing music" + \
                os.path.basename(filename)
            print("Play btn works fine")
        except:
            tkinter.messagebox.showerror(
                "File not found.", "Melody could not find the file. Please check again.")
    else:
        mixer.music.unpause()
        statusbar['text'] = "Music resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music stopped"


def set_vol(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music rewinded"


middleFRame = Frame(root)
middleFRame.pack(padx=30, pady=30)

playPhoto = PhotoImage(file=r"images/play.png")
playBtn = Button(middleFRame, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

stopPhoto = PhotoImage(file=r"images/stop.png")
stopBtn = Button(middleFRame, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file=r"images/pause.png")
pauseBtn = Button(middleFRame, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

bottomFrame = Frame(root)
bottomFrame.pack()

rewindPhoto = PhotoImage(file=r"images/rewind.png")
rewindBtn = Button(bottomFrame, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0, column=0)

scale = Scale(bottomFrame, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0, column=1, padx=30)

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
root.mainloop()
