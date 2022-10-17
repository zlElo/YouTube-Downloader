from tkinter import *
from pytube import YouTube
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import ttk
import os
import webbrowser

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput

def check():
    the_list = comboOneTwoPunch.get()
    if the_list == ('Video (.mp4)'):
        # Call definition for Video download
        download_video()
    if the_list == ('Audio (.mp3)'):
        # Call definition for Audio download
        download_only_audio()

# this is the function called when the button is clicked
def btnClickFunction():
	check()


def download_only_audio():
    name = 'Audio'
    yt = YouTube(tInput.get())
    items = list(range(0, 57))
    l = len(items)
    ys = yt.streams.get_audio_only()
    # Path for download
    file = filedialog.askdirectory()
    pig = ys.download(file)
    os.rename(pig, f'{file}/downloaded-audio--by_YouTube-Downloader.mp3')
    done(name)

def download_video():
    name = 'Video'
    yt = YouTube(tInput.get())
    items = list(range(0, 57))
    l = len(items)
    ys = yt.streams.get_highest_resolution()

    # Path for download
    file = filedialog.askdirectory()
    ys.download(file)
    done(name)

def done(name):
    root = Tk()
    root.geometry('290x90')
    root.title('Downloaded')

    Label(root, text=f'The {name} has been successfully downloaded!').place(x=20, y=20)
    Button(root, text='Developer', command=Dev).place(x=20, y=40)

    root.mainloop()

def Dev():
    webbrowser.open_new_tab('https://zlelo.github.io')

# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return comboOneTwoPunch.get()


root = Tk()


# This is the section of code which creates the main window
root.geometry('450x80')
root.title('YouTube-Downloader')


# This is the section of code which creates the a label
Label(root, text='Link:').place(x=20, y=24)


# This is the section of code which creates a text input box
tInput=Entry(root, width=25)
tInput.place(x=69, y=23)


# This is the section of code which creates a button
Button(root, text='Download', command=btnClickFunction).place(x=350, y=21.47)

# This is the section of code which creates a combo box
comboOneTwoPunch= ttk.Combobox(root, values=['Audio (.mp3)', 'Video (.mp4)'], font=('arial', 10, 'normal'), width=10)
comboOneTwoPunch.place(x=234, y=23)
comboOneTwoPunch.current(1)


root.mainloop()