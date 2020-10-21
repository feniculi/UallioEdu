#problema audio potrebbe essere dovuto dal sistema operativo
import pygame as pg
from gtts import gTTS
from playsound import playsound

freq = 25000    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
 
class sound_out:
    def di(self,testo):
        tts = gTTS(text=testo, lang="it")
        tts.save("./data/sound/riproduzione.mp3")
        self.play_music("./data/sound/riproduzione.mp3")
        print("dico " + testo)    


    def play_music(self,music_file):
        clock = pg.time.Clock()
        try:
            pg.mixer.music.set_volume(1.0)
            pg.mixer.music.load(music_file)
            #print("Music file {} loaded!".format(music_file))
        except pygame.error:
            print("File {} not found! {}".format(music_file, pg.get_error()))
            return
    
        pg.mixer.music.play()
        #print("eseguo " + format(music_file))    
        # If you want to fade in the audio...
        # for x in range(0,100):
        #     pg.mixer.music.set_volume(float(x)/100.0)
        #     time.sleep(.0075)
        # # check if playback has finished
        while pg.mixer.music.get_busy():
            clock.tick(50)

