# Setup UallioEdu
-> Scaricata immagine Ubuntu Mate 32 bit per Raspberry https://ubuntu-mate.org/download/
-> Copiala su SD con il programma https://www.raspberrypi.org/downloads/

login: pi
password:raspberry

```
sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade -y

sudo apt install python3-pip
sudo pip3 install tts
sudo pip3 install gtts
sudo pip3 install playsound
sudo apt-get install python-pygame
sudo pip3 install speechrecognition
sudo pip3 install azure-cognitiveservices-vision-face
sudo apt-get install portaudio19-dev
sudo pip3 install PyAudio
sudo pip3 install telepot
sudo apt-get install flac
sudo apt-get install python3-rpi.gpio
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev

sudo pip3 install pygame

```

per abilitare l'avvio automatico:


```
sudo nano /etc/rc.local
#copia e incolla il seguente testo
#-------------------------------
#!/bin/sh -e
cd /home/pi/Scrivania/Uallio_learning/
sudo python3 main_learning.py &
python3 ualliobot_learning.py &
exit 0
#------------------------

#poi esegui
sudo chmod +x /etc/rc.local
sudo systemctl enable rc-local
sudo systemctl start rc-local.service
sudo systemctl status rc-local.service
--------------------------------------------------------
```
```
sudo apt-get instal geany

segui questo link:
https://makingstuffwork.net/technology/lightweight-desktop-raspberry-pi-with-xfce4/

sudo reboot

sudo apt install xfce4 
sudo apt install xfce4-goodies 
sudo apt install chromium 

sudo nano /etc/X11/Xwrapper.config

Change the allowed_users=console to be allowed_users=anybody
Press CTRL + x, y to save, and overwrite the file.

sudo raspi-config

Select Boot Options, Desktop/CLI, and select Desktop or Desktop Autologin.

Select Finish, and Yes to Reboot.


Rinomina la raspberry come il proprietario
sudo apt-get install wicd

//librerie per il programma
```

? sudo apt-get install libsdl-ttf2.0-0

Abilita SSH e VNC Server
imposta account su VNC SErver
con mail:tuamail@gmail.com
pass: tuapass

Crea una rete di base alla quale si collega sempre il wifi

per far riavviare il sistema esegui il comando


Testa telegram per vedere se funzione
sudo pkill python

per fare supporto da remoto devo installare un ssh sul pc di leo così può entrare sulla raspberry e cambiare le impostazioni
