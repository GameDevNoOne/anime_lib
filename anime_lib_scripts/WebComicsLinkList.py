import os

class WebComics():

    def __init__(self, name, link, desc, author, date_Of_Release, rating):
        self.name = name
        self.link = link
        self.desc = desc
        self.author = author
        self.release = date_Of_Release
        self.rating = rating

    def __repr__(self):
        return self.name

webcomic_link_list = []