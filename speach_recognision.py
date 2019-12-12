########################################################################################################################
# Speech recognition and searching in wolfram and wiki.                                                                #
# Created by Jarosław Drząszcz(s16136).                                                                                #
########################################################################################################################

import speech_recognition as sr
from wolfram_wiki import search

if __name__ == '__main__':
    mic_list = sr.Microphone.list_microphone_names()
    sample_rate = 44100
    chunk_size = 2048
    r = sr.Recognizer()

    with sr.Microphone(device_index=0, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        # listens for the user's input
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("you said: " + text)
            search(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

