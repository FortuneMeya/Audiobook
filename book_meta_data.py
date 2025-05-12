import requests
from urllib.parse import quote_plus #Allows for use of + when it comes to the url
class BookMetaData:
    def __init__(self,title: str,author:str, desc:str= "", narrator: str= "", duration:float=0.0 ):
        self.title= title
        self.author = author
        self.desc = desc
        self.narrator = narrator
        self.duration = duration

    def fetch_from_api(self):
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


            if isinstance(description_data,dict):
                self.desc=description_data.get('value','No description available ')
            else:
                self.desc = "No description available"
                self.display_info()
            self.narrator='The Best Narrator'
            self.duration=round(len(self.desc.split())/130,2)

    def display_info(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Descriptions:{self.desc}")
        print(f"Narrator:{self.narrator}")
        print(f"Duration:{self.duration} hours")






























