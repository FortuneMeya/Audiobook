
from book_meta_data import BookMetaData
from tts_service import TTSService

class AudiobookAppp:

    def __init__(self):
        self.books = BookMetaData(title="", author="")

        self.tts=TTSService()
    def run(self):
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
        else:
            print('Invalid choice')












