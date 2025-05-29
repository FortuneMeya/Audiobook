"""
Author: Fortune Meya
Date:05/29/2025

This module defines the AudiobookAppp class, which allows users to search for a book, retrieve its metadata from
the Open Library API, and convert the description to speech using a TTS service. Users can either play the audio
directly or save it to a file.
"""
from book_meta_data import BookMetaData
from tts_service import TTSService
from playsound import playsound

class AudiobookAppp:

    def __init__(self):
        """
        Initializes the AudiobookApp by creating instances of BookMetaData and TTSService.
        """
        self.books = BookMetaData(title="", author="")
        self.tts=TTSService()
    def run(self):
        """
        Asked the user for what book they would like to search for. The fetch_from_api() method uses that information to
        fetch the information for the book.The user is given the option to either listen to the book description or save
        it as an audio file.
        :return:
        """
        print('Hello! Welcome To The Audiobook')
        title = input('What book would you like to hear:')
        self.books.title= title
        self.books.fetch_from_api()
        if not self.books.desc:
            print('No description available at the moment')
            return
        self.books.display_info()

        audio_choice= input("Would you like to \n1.Hear the descriptions\n2.Save it as audio?:")
        if audio_choice=='1':
            self.tts.text_to_speech(self.books.desc)
        elif audio_choice=='2':
            filenamee=input('What would you like to save your filename as (ex.book.mp3)')
            self.tts.save_audio(self.books.desc,filenamee)
            playsound(f'{filenamee}')
        else:
            print('Invalid choice')