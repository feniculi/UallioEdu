#!/usr/bin/python3
# -*- coding: utf-8 -*-
#configurazione
led="si"
mic_name = "Bus 001 Device 006: ID 0d8c:0134 C-Media Electronics, Inc. "
if led=="si":
    from led_base import ledc
from tts_base import sound_out
import random
import time
import speech_recognition as sr

riproduci=sound_out()

class vocale_in:
    def riconosci(self,first):
        device_id=0
        sample_rate = 48000
        chunk_size = 2048
        recognizer = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        for i, microphone_name in enumerate(mic_list): 
            if microphone_name == mic_name: 
                device_id = i 

        """Transcribe speech from recorded from `microphone`.
    
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occured, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
    
        # check that recognizer and microphone arguments are appropriate type
    
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError('`recognizer` must be `Recognizer` instance')
    
         # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
    
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source:
            print("***************************\n\nAttendi")
            recognizer.adjust_for_ambient_noise(source)
            if led=="si":
                ledc.WHITE()
            print("\nParla pure... sono in ascolto...")
            audio = recognizer.listen(source)
            print("\nRicevuto. Attendi.")
            if led=="si":
                ledc.RED()


        # set up the response object
    
        response = {'success': True, 'error': None, 'transcription': None}
    
        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
    
        try:
            response['transcription'] = recognizer.recognize_google(audio,language='it-IT')
            print ("\n"+ "Ho capito questo: " + str(response['transcription']) +"\n")
        except sr.RequestError:
            # API was unreachable or unresponsive
            response['success'] = False
            response['error'] = 'API unavailable'
            response['transcription'] = ""
            print ("API unavailable")
            if led=="si":
                ledc.YELLOW()
            time.sleep(5)

        except sr.UnknownValueError:
            # speech was unintelligible 
            response['error'] = 'Unable to recognize speech'
            print ("I didn't catch that. What did you say?\n")
            response['transcription'] = ""
 
        if response['error']:
            print ('ERROR: {}'.format(response['error']))
            response['transcription'] = ""
                        
        return response['transcription'].lower()
