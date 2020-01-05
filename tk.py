from musicDownloader  import downloadTheSong
import tkinter
import tkinter.messagebox
window = tkinter.Tk()

window.title("Song Downloader")

tkinter.Label(window, text = "Song Name : ").grid(row = 0)
song = tkinter.StringVar()

tkinter.Entry(window, textvariable = song).grid(row = 0, column = 1)

tkinter.Label(window, text = "(Optional)Artist").grid(row = 1) 
by = tkinter.StringVar()
tkinter.Entry(window, textvariable= by).grid(row = 1, column = 1) 
pic  = tkinter.IntVar()
tkinter.Checkbutton(window, text = "Add thumbnail(Takes 15 seconds per song)", variable = pic).grid(columnspan = 2)
def callTheBiggerFunc():
	downloadTheSong(window,(song.get() + by.get()), pic.get())
submit = tkinter.Button(window,text = "Download", command = lambda:  callTheBiggerFunc())
# quit = tkinter.Button(window,text = "quit", comman)
submit.grid(row = 3)
window.mainloop()
