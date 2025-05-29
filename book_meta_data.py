"""
Author: Fortune Meya
Date:05/29/2025

This module defines the BookMetaData class which interacts with the Open Library API to fetch book information
based on a user-provided title. It stores metadata such as title, author, description, narrator, and estimated
duration of the audiobook description.
"""

import requests
from urllib.parse import quote_plus #Allows for use of + when it comes to the url
class BookMetaData:
    def __init__(self,title: str,author:str, desc:str= "", narrator: str= "", duration:float=0.0 ):
        """
        Initializes a BookMetaData object with given or default values.

        :param title: The title of the book
        :type title: string
        :param author: The author of the book
        :type author: string
        :param desc: The description of the book(defaults as an empty string)
        :type desc: string
        :param narrator: The narrator of the book(defaults as an empty string)
        :type narrator: string
        :param duration: The duration of the book description(defaults to 0)
        :type duration: float
        """
        self.title= title
        self.author = author
        self.desc = desc
        self.narrator = narrator
        self.duration = duration

    def fetch_from_api(self):
            """
            Fetches book metadata from the Open Library API using the title.
            Updates the title, author, and description based on API results.
            If no data is found, prints appropriate messages.
            """
            encoded_title = quote_plus(self.title)
            url = f"https://openlibrary.org/search.json?title={encoded_title}"
            response = requests.get(url)
            status_code= response.status_code


            if status_code !=200:
                print(f'There is a {status_code} error')
                return
            data= response.json()

            if not data['docs']:
                print('There was no results founds')
                return
            book= data['docs'][0]
            self.title =book.get('title','Unknown Title')
            self.author = data['docs'][0].get('author_name', ['Unknown'])[0]
            description_data = book.get('description', 'No description available')
            work_key = data['docs'][0]['key']
            work_url = f"https://openlibrary.org{work_key}.json"
            work_response = requests.get(work_url)
            if work_response.status_code == 200:
                work_data = work_response.json()
                description_data = work_data.get("description", "No description available")

            if isinstance(description_data, dict):
                self.desc = description_data.get('value', 'No description available')
            elif isinstance(description_data, str):
                self.desc = description_data
            else:
                self.desc = "No description available"


            self.duration = round(len(self.desc.split()) / 130, 2)

    def display_info(self):
        """
        Displays the fetched metadata information for the book.
        """
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Descriptions:{self.desc}")
        print(f"Narrator:{self.narrator}")
        print(f"Duration:{self.duration} hours")