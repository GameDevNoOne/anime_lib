import os

class Manga():
    
    def __init__(self, name, link, desc, author, date_Of_Release):
        self.name = name
        self.link = link
        self.descripion = desc
        self.author = author
        self.release = date_Of_Release
    
    def __repr__(self):
        return self.name

mangaList = []