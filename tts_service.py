import os
import pyttsx3

class TTSService:
    def __init__(self):
        self.engine =pyttsx3.init()

    def text_to_speech(self,text:str):
        self.engine.say(text)
        self.engine.runAndWait()


    def save_audio(self, text: str, filename: str = "audiobook.wav"):
        print(f"Saving the text to the audio file: {filename}")
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        print(f"Audio is saved to {filename}")
        os.system(f"afplay {filename}")



