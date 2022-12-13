from tkinter import *
# from tkinter import filedialog
from pygame import mixer
import os
import musicjam
os.chdir('/Users/petitmi/UBCO-MDS/533/project')
class MusicPlayer:
    def __init__(self, window):
        window.geometry('800x200'); window.title('Music Player'); window.resizable(0,0)
        Load = Button(window, text = 'Generate Music',  width = 52, height= 2, font = ('Times', 20), command = self.Generate)
        Play = Button(window, text = 'Play',  width = 20, height= 5,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 20, height= 5, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 20, height= 5, font = ('Times', 10), command = self.stop)
        Load.place(x=100,y=20);Play.place(x=100,y=100);Pause.place(x=300,y=100);Stop.place(x=500,y=100) 
        self.music_file = False
        self.playing_state = False
    def Generate(self):
        # self.music_file = 'filedialog.askopenfilename()'
        jam = musicjam.MusicGenerator()
        jam.generateMusic()
        self.music_file ='filename.mid'  #
    def play(self):
        if self.music_file:
            mixer.init()
            # mixer.music.load('self.music_file')
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
