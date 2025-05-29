"""
Author: Fortune Meya
Date:05/29/2025

This module defines the TTSService class which provides text-to-speech functionality using pyttsx3.
It allows converting text to speech and saving it as an audio file compatible across different operating systems.
"""

import os
import pyttsx3
import platform


class TTSService:
    def __init__(self):
        """
        Initializes the pyttsx3 text-to-speech engine. If initialization fails, prints an error message.
        """
        self.engine =pyttsx3.init()
        if not self.engine:
            print('Error with text to speech')

    def text_to_speech(self,text:str):
        """
        Converts the given text to speech and plays it.
        :param text: The book description to convert into audible speech.
        :type text: string
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def save_audio(self, text: str, filename: str = "audiobook.wav"):
        """
        Saves the given text as an audio file and plays it based on the user's operating system.
        :param text: The book description to convert into speech or audio file.
        :type: string
        :param filename: The name of the filename that the user chooses(default as audiobook.wav file)
        :type: string
        :return:
        """
        print(f"Saving the text to the audio file: {filename}")
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        print(f"Audio is saved to {filename}")

        system = platform.system()
        if system == "Darwin":  # macOS
            os.system(f"afplay {filename}")
        elif system == "Windows":
            os.system(f"start {filename}")
        elif system == "Linux":
            os.system(f"aplay {filename}")
        else:
            print("Audio playback not supported on this OS.")




