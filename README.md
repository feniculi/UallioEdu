# Setup UallioEdu
-> Scaricata immagine Ubuntu Mate 64 bit per Raspberry https://ubuntu-mate.org/download/
-> Copiala su SD con il programma https://www.raspberrypi.org/downloads/
login: pi
password:raspberry
collega ad internet network options

setup tastiera
localization option italian

segui questo link:
https://makingstuffwork.net/technology/lightweight-desktop-raspberry-pi-with-xfce4/

sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade -y
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

sudo apt install python3-pip
sudo pip3 install pygame
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
sudo apt-get instal geany
sudo apt-get install python-rpi.gpio

? sudo apt-get install libsdl-ttf2.0-0

Abilita SSH e VNC Server
imposta account su VNC SErver
con mail:cesare.pec@gmail.com
Feniculi2019Cesare


Crea una rete di base alla quale si collega sempre il wifi

per far riavviare il sistema esegui il comando

sudo nano /etc/rc.local


cd /home/pi/Desktop/raspberry/
python3 main_paolo.py &
python3 uallio_bot_paolo.py &

Testa telegram per vedere se funzione
sudo pkill python

per fare supporto da remoto devo installare un ssh sul pc di leo così può entrare sulla raspberry e cambiare le impostazioni
